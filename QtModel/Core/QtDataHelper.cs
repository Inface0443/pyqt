using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;

namespace QtModel.Core;

public static class QtDataHelper
{
    public static string StrConcreteBoxBeam(bool symmetry = true, IReadOnlyList<double>? secInfo = null,
        int boxNum = 3, double boxHeight = 2, IReadOnlyList<string>? charmInfo = null,
        IReadOnlyList<double>? secRight = null, IReadOnlyList<string>? charmRight = null,
        IReadOnlyDictionary<string, IReadOnlyList<double>>? boxOtherInfo = null,
        IReadOnlyDictionary<string, IReadOnlyList<double>>? boxOtherRight = null)
    {
        if (secInfo is null)
        {
            throw new ArgumentNullException(nameof(secInfo));
        }

        var builder = new StringBuilder();
        var bridgeWidth = symmetry
            ? 2 * secInfo[10]
            : secInfo[10] + (secRight is null ? 0 : secRight[10]);
        builder.AppendFormat(CultureInfo.InvariantCulture, "{0:g},{1},{2},{3}\r\n",
            bridgeWidth, boxNum, boxHeight, symmetry ? "YES" : "NO");
        builder.AppendLine(string.Join(",", secInfo.Select(x => x.ToString("g", CultureInfo.InvariantCulture))));

        if (charmInfo is not null)
        {
            builder.AppendLine(string.Join(",",
                charmInfo.Select(item =>
                {
                    var segments = item.Split(',').SelectMany(term => term.Split('*'));
                    return $"({string.Join(',', segments)})";
                })));
        }

        AppendBoxOther(builder, boxOtherInfo, "L");

        if (!symmetry)
        {
            if (secRight is not null)
            {
                builder.AppendLine(string.Join(",", secRight.Select(x => x.ToString("g", CultureInfo.InvariantCulture))));
            }

            if (charmRight is not null)
            {
                builder.AppendLine(string.Join(",",
                    charmRight.Select(item =>
                    {
                        var segments = item.Split(',').SelectMany(term => term.Split('*'));
                        return $"({string.Join(',', segments)})";
                    })));
            }

            AppendBoxOther(builder, boxOtherRight, "R");
        }

        return builder.ToString();
    }

    public static string StrSteelBeam(IReadOnlyList<double>? secInfo = null,
        IReadOnlyDictionary<string, IReadOnlyList<double>>? ribInfo = null,
        IReadOnlyList<(int Start, int End, double Offset, string Position, int Count, string Name)>? ribPlace = null)
    {
        if (secInfo is null)
        {
            throw new ArgumentNullException(nameof(secInfo));
        }

        var builder = new StringBuilder();
        builder.AppendLine(string.Join(",", secInfo.Select(x => x.ToString("g", CultureInfo.InvariantCulture))));

        if (ribInfo is not null)
        {
            foreach (var kvp in ribInfo)
            {
                builder.Append("RIB=");
                builder.Append(kvp.Key);
                builder.Append(',');
                builder.AppendLine(string.Join(",", kvp.Value.Select(v => v.ToString("g", CultureInfo.InvariantCulture))));
            }
        }

        if (ribPlace is not null)
        {
            foreach (var row in ribPlace)
            {
                builder.Append("PLACE=");
                builder.AppendLine(string.Join(',', new[]
                {
                    row.Start.ToString(CultureInfo.InvariantCulture),
                    row.End.ToString(CultureInfo.InvariantCulture),
                    row.Offset.ToString("g", CultureInfo.InvariantCulture),
                    row.Position,
                    row.Count.ToString(CultureInfo.InvariantCulture),
                    row.Name
                }));
            }
        }

        return builder.ToString();
    }

    public static string StrCustomCompoundBeam(IReadOnlyList<double>? matCombine = null,
        IReadOnlyList<IReadOnlyDictionary<string, IReadOnlyList<(double X, double Y)>>>? loopSegments = null,
        IReadOnlyList<IReadOnlyDictionary<string, IReadOnlyList<(double X, double Y)>>>? secondaryLoopSegments = null)
    {
        if (matCombine is null)
        {
            throw new ArgumentNullException(nameof(matCombine));
        }

        var builder = new StringBuilder();
        builder.AppendLine(string.Join(",", matCombine.Select(x => x.ToString("g", CultureInfo.InvariantCulture))));
        builder.AppendLine("M=");

        AppendLoopSegments(builder, loopSegments);

        builder.AppendLine("S=");
        AppendLoopSegments(builder, secondaryLoopSegments);

        return builder.ToString();
    }

    public static string StrCompoundSection(IReadOnlyList<double>? secInfo = null,
        IReadOnlyList<double>? matCombine = null)
    {
        if (secInfo is null || matCombine is null)
        {
            throw new ArgumentNullException(secInfo is null ? nameof(secInfo) : nameof(matCombine));
        }

        var builder = new StringBuilder();
        builder.AppendLine(string.Join(",", secInfo.Select(x => x.ToString("g", CultureInfo.InvariantCulture))));
        builder.AppendLine(string.Join(",", matCombine.Select(x => x.ToString("g", CultureInfo.InvariantCulture))));
        return builder.ToString();
    }

    public static string StrCustomSection(
        IReadOnlyList<IReadOnlyDictionary<string, IReadOnlyList<(double X, double Y)>>>? loopSegments = null,
        IReadOnlyList<(double X1, double Y1, double X2, double Y2, double Thickness)>? secLines = null)
    {
        var builder = new StringBuilder();

        AppendLoopSegments(builder, loopSegments);

        if (secLines is not null && secLines.Count > 0)
        {
            builder.AppendLine(string.Join("\r\n",
                secLines.Select(row =>
                    "LINE=" + string.Join(',', new[]
                    {
                        row.X1.ToString("g", CultureInfo.InvariantCulture),
                        row.Y1.ToString("g", CultureInfo.InvariantCulture),
                        row.X2.ToString("g", CultureInfo.InvariantCulture),
                        row.Y2.ToString("g", CultureInfo.InvariantCulture),
                        row.Thickness.ToString("g", CultureInfo.InvariantCulture)
                    }))));
        }

        return builder.ToString();
    }

    public static string GetStrByData(string secType, IReadOnlyDictionary<string, object?> secData)
    {
        secType ??= string.Empty;
        secData ??= new Dictionary<string, object?>();

        T? Get<T>(string key)
        {
            if (!secData.TryGetValue(key, out var value) || value is null)
            {
                return default;
            }

            if (value is T tValue)
            {
                return tValue;
            }

            return (T?)Convert.ChangeType(value, typeof(T));
        }

        return StrSection(
            secType,
            Get<IReadOnlyList<double>>("sec_info"),
            Get<bool?>("symmetry") ?? true,
            Get<IReadOnlyList<string>>("charm_info"),
            Get<IReadOnlyList<double>>("sec_right"),
            Get<IReadOnlyList<string>>("charm_right"),
            Get<int?>("box_num") ?? 3,
            Get<double?>("box_height") ?? 2,
            Get<IReadOnlyDictionary<string, IReadOnlyList<double>>>("box_other_info"),
            Get<IReadOnlyDictionary<string, IReadOnlyList<double>>>("box_other_right"),
            Get<IReadOnlyList<double>>("mat_combine"),
            Get<IReadOnlyDictionary<string, IReadOnlyList<double>>>("rib_info"),
            Get<IReadOnlyList<(int, int, double, string, int, string)>>("rib_place"),
            Get<IReadOnlyList<IReadOnlyDictionary<string, IReadOnlyList<(double, double)>>>>("loop_segments"),
            Get<IReadOnlyList<(double, double, double, double, double)>>("sec_lines"),
            Get<IReadOnlyList<IReadOnlyDictionary<string, IReadOnlyList<(double, double)>>>>("secondary_loop_segments")
        );
    }

    public static string StrSection(
        string secType = "矩形",
        IReadOnlyList<double>? secInfo = null,
        bool symmetry = true,
        IReadOnlyList<string>? charmInfo = null,
        IReadOnlyList<double>? secRight = null,
        IReadOnlyList<string>? charmRight = null,
        int boxNum = 3,
        double boxHeight = 2,
        IReadOnlyDictionary<string, IReadOnlyList<double>>? boxOtherInfo = null,
        IReadOnlyDictionary<string, IReadOnlyList<double>>? boxOtherRight = null,
        IReadOnlyList<double>? matCombine = null,
        IReadOnlyDictionary<string, IReadOnlyList<double>>? ribInfo = null,
        IReadOnlyList<(int Start, int End, double Offset, string Position, int Count, string Name)>? ribPlace = null,
        IReadOnlyList<IReadOnlyDictionary<string, IReadOnlyList<(double X, double Y)>>>? loopSegments = null,
        IReadOnlyList<(double X1, double Y1, double X2, double Y2, double Thickness)>? secLines = null,
        IReadOnlyList<IReadOnlyDictionary<string, IReadOnlyList<(double X, double Y)>>>? secondaryLoopSegments = null)
    {
        return secType switch
        {
            "混凝土箱梁" => StrConcreteBoxBeam(symmetry, secInfo, boxNum, boxHeight, charmInfo, secRight,
                charmRight, boxOtherInfo, boxOtherRight),
            "工字钢梁" or "箱型钢梁" => StrSteelBeam(secInfo, ribInfo, ribPlace),
            "特性截面" => secInfo is null
                ? string.Empty
                : string.Join(",", secInfo.Select(x => x.ToString("g", CultureInfo.InvariantCulture))) + "\r\n",
            _ when secType.StartsWith("自定义组合", StringComparison.Ordinal) =>
                StrCustomCompoundBeam(matCombine, loopSegments, secondaryLoopSegments),
            _ when secType.EndsWith("组合梁", StringComparison.Ordinal) ||
                   new[] { "钢管砼", "钢箱砼", "哑铃型钢管混凝土", "哑铃型钢管混凝土竖向" }.Contains(secType) =>
                StrCompoundSection(secInfo, matCombine),
            _ when secType.StartsWith("自定义", StringComparison.Ordinal) =>
                StrCustomSection(loopSegments, secLines),
            _ => secInfo is null
                ? string.Empty
                : string.Join(",", secInfo.Select(x => x.ToString("g", CultureInfo.InvariantCulture))) + "\r\n"
        };
    }

    public static string ParseIntListToStr(object? ids)
    {
        if (ids is null)
        {
            return string.Empty;
        }

        if (ids is string s)
        {
            return s;
        }

        if (ids is int single)
        {
            return single.ToString(CultureInfo.InvariantCulture);
        }

        var numbers = ids switch
        {
            IEnumerable<int> enumerable => enumerable.ToList(),
            IEnumerable<object> objEnumerable => objEnumerable.Select(Convert.ToInt32).ToList(),
            _ => throw new ArgumentException("Unsupported id type", nameof(ids))
        };

        if (numbers.Count == 0)
        {
            return string.Empty;
        }

        numbers = numbers.Distinct().OrderBy(x => x).ToList();

        if (numbers.Count == 1)
        {
            return numbers[0].ToString(CultureInfo.InvariantCulture);
        }

        if (numbers.Count == 2)
        {
            return string.Join(" ", numbers.Select(n => n.ToString(CultureInfo.InvariantCulture)));
        }

        string CreateIdExpression(int from, int to, int increment)
            => increment == 1
                ? $"{from} to {to}"
                : $"{from} to {to} by {increment}";

        var ranges = new List<string>();
        var start = numbers[0];
        var previous = numbers[0];
        var currentIncrement = numbers[1] - numbers[0];

        for (var i = 1; i < numbers.Count; i++)
        {
            var expected = previous + currentIncrement;
            var actual = numbers[i];
            if (actual != expected)
            {
                ranges.Add(CreateIdExpression(start, previous, currentIncrement));
                start = actual;
                currentIncrement = i + 1 < numbers.Count ? numbers[i + 1] - numbers[i] : 1;
            }

            previous = actual;
        }

        ranges.Add(CreateIdExpression(start, previous, currentIncrement));
        return string.Join(",", ranges);
    }

    public static IReadOnlyList<int> ParseIdsToArray(object? ids, bool allowEmpty = true)
    {
        if (ids is null)
        {
            return allowEmpty ? Array.Empty<int>() : throw new ArgumentNullException(nameof(ids));
        }

        if (ids is int single)
        {
            return new[] { single };
        }

        if (ids is IEnumerable<int> enumerable)
        {
            return enumerable.ToArray();
        }

        if (ids is string s)
        {
            var parsed = ParseNumberString(s);
            if (parsed is null)
            {
                throw new ArgumentException("无法解析的编号字符串", nameof(ids));
            }

            return parsed;
        }

        if (ids is IEnumerable<object> objEnumerable)
        {
            return objEnumerable.Select(Convert.ToInt32).ToArray();
        }

        throw new ArgumentException("Unsupported id type", nameof(ids));
    }

    public static IReadOnlyList<int>? ParseNumberString(string input)
    {
        if (string.IsNullOrWhiteSpace(input))
        {
            return Array.Empty<int>();
        }

        var tokens = input.Split(new[] { ',', ';' }, StringSplitOptions.RemoveEmptyEntries);
        var result = new List<int>();

        foreach (var token in tokens)
        {
            var trimmed = token.Trim();
            if (Regex.IsMatch(trimmed, "^\\d+$"))
            {
                result.Add(int.Parse(trimmed, CultureInfo.InvariantCulture));
                continue;
            }

            var match = Regex.Match(trimmed, @"^(?<from>\d+)\s+to\s+(?<to>\d+)(?:\s+by\s+(?<by>\d+))?$",
                RegexOptions.IgnoreCase);
            if (!match.Success)
            {
                return null;
            }

            var from = int.Parse(match.Groups["from"].Value, CultureInfo.InvariantCulture);
            var to = int.Parse(match.Groups["to"].Value, CultureInfo.InvariantCulture);
            var step = match.Groups["by"].Success
                ? int.Parse(match.Groups["by"].Value, CultureInfo.InvariantCulture)
                : 1;

            if (step <= 0 || from > to)
            {
                return null;
            }

            for (var value = from; value <= to; value += step)
            {
                result.Add(value);
            }
        }

        return result;
    }

    public static (double X, double Y, double Z)[] ConvertThreePointsToVectors(
        IReadOnlyList<(double X, double Y, double Z)> points)
    {
        if (points.Count != 3)
        {
            throw new ArgumentException("需要三个点来生成向量", nameof(points));
        }

        var origin = points[0];
        return new[]
        {
            (points[1].X - origin.X, points[1].Y - origin.Y, points[1].Z - origin.Z),
            (points[2].X - origin.X, points[2].Y - origin.Y, points[2].Z - origin.Z)
        };
    }

    public static (double X, double Y, double Z)[] ConvertAngleToVectors(IReadOnlyList<double> angles)
    {
        if (angles.Count != 3)
        {
            throw new ArgumentException("角度数量必须为3", nameof(angles));
        }

        double DegreeToRadian(double deg) => Math.PI * deg / 180.0;

        var alpha = DegreeToRadian(angles[0]);
        var beta = DegreeToRadian(angles[1]);
        var gamma = DegreeToRadian(angles[2]);

        return new[]
        {
            (Math.Cos(alpha), Math.Cos(beta), Math.Cos(gamma)),
            (Math.Sin(alpha), Math.Sin(beta), Math.Sin(gamma))
        };
    }

    public static string LiveLoadSetLine(int code, int calcType, IReadOnlyList<string> groups)
    {
        return $"{code},{calcType},{string.Join(',', groups)}";
    }

    private static void AppendLoopSegments(StringBuilder builder,
        IReadOnlyList<IReadOnlyDictionary<string, IReadOnlyList<(double X, double Y)>>>? segments)
    {
        if (segments is null)
        {
            return;
        }

        foreach (var segment in segments)
        {
            foreach (var (key, points) in segment)
            {
                builder.AppendLine($"{NormalizeLoopKey(key)}={string.Join(',', points.Select(p => $"({p.X:g},{p.Y:g})"))}");
            }
        }
    }

    private static void AppendBoxOther(StringBuilder builder,
        IReadOnlyDictionary<string, IReadOnlyList<double>>? values, string prefix)
    {
        if (values is null)
        {
            return;
        }

        foreach (var key in new[] { "i1", "B0", "B4", "T4" })
        {
            if (!values.TryGetValue(key, out var list))
            {
                continue;
            }

            builder.Append(prefix);
            builder.Append(key);
            builder.Append('=');
            builder.AppendLine(string.Join(",", list.Select(v => v.ToString("g", CultureInfo.InvariantCulture))));
        }
    }

    private static string NormalizeLoopKey(string key)
        => string.Equals(key, "main", StringComparison.OrdinalIgnoreCase) ? "MAIN" : "SUB";
}
