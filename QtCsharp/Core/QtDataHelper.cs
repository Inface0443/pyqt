using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;

namespace QtCsharp.Core;

/// <summary>
/// 与 Python 版 QtDataHelper 功能保持一致的工具类。
/// </summary>
public static class QtDataHelper
{
    private static readonly CultureInfo Invariant = CultureInfo.InvariantCulture;

    public static string StrConcreteBoxBeam(
        bool symmetry = true,
        IList<double>? secInfo = null,
        int boxNum = 3,
        double boxHeight = 2,
        IList<string>? charmInfo = null,
        IList<double>? secRight = null,
        IList<string>? charmRight = null,
        IDictionary<string, IList<double>>? boxOtherInfo = null,
        IDictionary<string, IList<double>>? boxOtherRight = null)
    {
        if (secInfo == null)
        {
            secInfo = Array.Empty<double>();
        }

        double bridgeWidth = symmetry
            ? 2 * secInfo.ElementAtOrDefault(10)
            : secInfo.ElementAtOrDefault(10) + (secRight?.ElementAtOrDefault(10) ?? 0);

        var builder = new StringBuilder();
        builder.AppendFormat(Invariant, "{0:G},{1},{2},{3}\r\n",
            bridgeWidth,
            boxNum,
            boxHeight,
            symmetry ? "YES" : "NO");

        builder.AppendLine(string.Join(",", secInfo.Select(FormatNumber)));

        if (charmInfo != null && charmInfo.Count >= 4)
        {
            builder.AppendLine(string.Join(",",
                new[] { charmInfo[0], charmInfo[2], charmInfo[1], charmInfo[3] }
                    .Select(item => "(" + string.Join(",", ExpandCharmTerm(item)) + ")")));
        }

        if (boxOtherInfo != null && boxOtherInfo.Keys.Any(k => k is "i1" or "B0" or "B4" or "T4"))
        {
            foreach (var key in new[] { "i1", "B0", "B4", "T4" })
            {
                if (boxOtherInfo.TryGetValue(key, out var values))
                {
                    builder.Append("L").Append(key).Append("=");
                    builder.AppendLine(string.Join(",", values.Select(FormatNumber)));
                }
            }
        }

        if (!symmetry && secRight != null)
        {
            builder.AppendLine(string.Join(",", secRight.Select(FormatNumber)));

            if (charmRight != null && charmRight.Count >= 4)
            {
                builder.AppendLine(string.Join(",",
                    new[] { charmRight[0], charmRight[2], charmRight[1], charmRight[3] }
                        .Select(item => "(" + string.Join(",", ExpandCharmTerm(item)) + ")")));
            }

            if (boxOtherRight != null && boxOtherRight.Keys.Any(k => k is "i1" or "B0" or "B4" or "T4"))
            {
                foreach (var key in new[] { "i1", "B0", "B4", "T4" })
                {
                    if (boxOtherRight.TryGetValue(key, out var values))
                    {
                        builder.Append("R").Append(key).Append("=");
                        builder.AppendLine(string.Join(",", values.Select(FormatNumber)));
                    }
                }
            }
        }

        return builder.ToString();
    }

    public static string StrSteelBeam(
        IList<double>? secInfo = null,
        IDictionary<string, IList<double>>? ribInfo = null,
        IEnumerable<IEnumerable<object>>? ribPlace = null)
    {
        var builder = new StringBuilder();

        if (secInfo != null)
        {
            builder.AppendLine(string.Join(",", secInfo.Select(FormatNumber)));
        }

        if (ribInfo != null && ribInfo.Count > 0)
        {
            foreach (var kvp in ribInfo)
            {
                builder.Append("RIB=").Append(kvp.Key).Append(",");
                builder.AppendLine(string.Join(",", kvp.Value.Select(FormatNumber)));
            }
        }

        if (ribPlace != null)
        {
            foreach (var row in ribPlace)
            {
                builder.Append("PLACE=");
                builder.AppendLine(string.Join(",", row.Select(FormatObject)));
            }
        }

        return builder.ToString();
    }

    public static string StrCustomCompoundBeam(
        IEnumerable<double>? matCombine = null,
        IEnumerable<IDictionary<string, IEnumerable<IEnumerable<double>>>>? loopSegments = null,
        IEnumerable<IDictionary<string, IEnumerable<IEnumerable<double>>>>? secondaryLoopSegments = null)
    {
        var builder = new StringBuilder();
        if (matCombine != null)
        {
            builder.AppendLine(string.Join(",", matCombine.Select(FormatNumber)));
        }
        else
        {
            builder.AppendLine(string.Empty);
        }

        builder.AppendLine("M=");
        builder.Append(FormatLoopSegments(loopSegments));

        builder.AppendLine("S=");
        builder.Append(FormatLoopSegments(secondaryLoopSegments));

        return builder.ToString();
    }

    public static string StrCompoundSection(
        IEnumerable<double>? secInfo = null,
        IEnumerable<double>? matCombine = null)
    {
        var builder = new StringBuilder();
        if (secInfo != null)
        {
            builder.AppendLine(string.Join(",", secInfo.Select(FormatNumber)));
        }
        if (matCombine != null)
        {
            builder.AppendLine(string.Join(",", matCombine.Select(FormatNumber)));
        }
        return builder.ToString();
    }

    public static string StrCustomSection(
        IEnumerable<IDictionary<string, IEnumerable<IEnumerable<double>>>>? loopSegments = null,
        IEnumerable<IEnumerable<double>>? secLines = null)
    {
        var builder = new StringBuilder();
        builder.Append(FormatLoopSegments(loopSegments));

        if (secLines != null)
        {
            foreach (var line in secLines)
            {
                builder.Append("LINE=");
                builder.AppendLine(string.Join(",", line.Select(FormatNumber)));
            }
        }

        return builder.ToString();
    }

    public static string GetStrByData(string secType, IDictionary<string, object?> secData)
    {
        var secInfo = ToDoubleList(GetValue(secData, "sec_info")) ?? new List<double>();
        bool symmetry = ToBool(GetValue(secData, "symmetry"), true);
        var charmInfo = ToStringList(GetValue(secData, "charm_info"));
        var secRight = ToDoubleList(GetValue(secData, "sec_right"));
        var charmRight = ToStringList(GetValue(secData, "charm_right"));
        int boxNum = ToInt(GetValue(secData, "box_num"), 3);
        double boxHeight = ToDouble(GetValue(secData, "box_height"), 2.0);
        var boxOtherInfo = ToDictionaryOfDoubleLists(GetValue(secData, "box_other_info"));
        var boxOtherRight = ToDictionaryOfDoubleLists(GetValue(secData, "box_other_right"));
        var matCombine = ToDoubleList(GetValue(secData, "mat_combine"));
        var ribInfo = ToDictionaryOfDoubleLists(GetValue(secData, "rib_info"));
        var ribPlace = ToEnumerableOfEnumerable(GetValue(secData, "rib_place"));
        var loopSegments = ToLoopSegments(GetValue(secData, "loop_segments"));
        var secLines = ToEnumerableOfDoubles(GetValue(secData, "sec_lines"));
        var secondaryLoopSegments = ToLoopSegments(GetValue(secData, "secondary_loop_segments"));

        return StrSection(
            secType,
            secInfo,
            symmetry,
            charmInfo,
            secRight,
            charmRight,
            boxNum,
            boxHeight,
            boxOtherInfo,
            boxOtherRight,
            matCombine,
            ribInfo,
            ribPlace,
            loopSegments,
            secLines,
            secondaryLoopSegments);
    }

    public static string StrSection(
        string secType = "矩形",
        IEnumerable<double>? secInfo = null,
        bool symmetry = true,
        IList<string>? charmInfo = null,
        IEnumerable<double>? secRight = null,
        IList<string>? charmRight = null,
        int boxNum = 3,
        double boxHeight = 2,
        IDictionary<string, IList<double>>? boxOtherInfo = null,
        IDictionary<string, IList<double>>? boxOtherRight = null,
        IEnumerable<double>? matCombine = null,
        IDictionary<string, IList<double>>? ribInfo = null,
        IEnumerable<IEnumerable<object>>? ribPlace = null,
        IEnumerable<IDictionary<string, IEnumerable<IEnumerable<double>>>>? loopSegments = null,
        IEnumerable<IEnumerable<double>>? secLines = null,
        IEnumerable<IDictionary<string, IEnumerable<IEnumerable<double>>>>? secondaryLoopSegments = null)
    {
        return secType switch
        {
            "混凝土箱梁" => StrConcreteBoxBeam(symmetry, secInfo?.ToList() ?? new List<double>(), boxNum, boxHeight,
                charmInfo, secRight?.ToList(), charmRight, boxOtherInfo, boxOtherRight),
            "工字钢梁" or "箱型钢梁" => StrSteelBeam(secInfo?.ToList(), ribInfo, ribPlace),
            "特性截面" => string.Join(",", (secInfo ?? Array.Empty<double>()).Select(FormatNumber)) + "\r\n",
            var type when type.StartsWith("自定义组合", StringComparison.Ordinal) =>
                StrCustomCompoundBeam(matCombine, loopSegments, secondaryLoopSegments),
            var type when type.EndsWith("组合梁", StringComparison.Ordinal) ||
                          type is "钢管砼" or "钢箱砼" or "哑铃型钢管混凝土" or "哑铃型钢管混凝土竖向" =>
                StrCompoundSection(secInfo, matCombine),
            var type when type.StartsWith("自定义", StringComparison.Ordinal) =>
                StrCustomSection(loopSegments, secLines),
            _ => string.Join(",", (secInfo ?? Array.Empty<double>()).Select(FormatNumber)) + "\r\n"
        };
    }

    public static string ParseIntListToStr(object? ids)
    {
        if (ids == null)
        {
            return string.Empty;
        }

        if (ids is string str)
        {
            return str;
        }

        if (ids is int single)
        {
            return single.ToString(Invariant);
        }

        var set = new SortedSet<int>(ToIntList(ids));
        if (set.Count == 0)
        {
            return string.Empty;
        }

        if (set.Count == 1)
        {
            return set.Min.ToString(Invariant);
        }

        if (set.Count == 2)
        {
            return string.Join(" ", set.Select(v => v.ToString(Invariant)));
        }

        var sorted = set.ToList();
        var result = new List<string>();
        int startIndex = 0;
        int currentIndex = 2;
        int idIncrement = sorted[1] - sorted[0];

        string CreateIdExpression(int from, int to, int increment) =>
            increment == 1
                ? $"{from}to{to}"
                : $"{from}to{to}by{increment}";

        while (true)
        {
            int currentIncrement = sorted[currentIndex] - sorted[currentIndex - 1];
            if (currentIncrement == idIncrement)
            {
                if (currentIndex >= sorted.Count - 1)
                {
                    result.Add(CreateIdExpression(sorted[startIndex], sorted[currentIndex], idIncrement));
                    break;
                }
                currentIndex += 1;
                continue;
            }

            int prevCount = (sorted[currentIndex - 1] - sorted[startIndex]) / idIncrement + 1;
            if (prevCount <= 2)
            {
                result.Add(sorted[startIndex].ToString(Invariant));
                if (currentIndex >= sorted.Count - 1)
                {
                    result.Add($"{sorted[currentIndex - 1]} {sorted[currentIndex]}");
                    break;
                }
                startIndex = currentIndex - 1;
                idIncrement = sorted[startIndex + 1] - sorted[startIndex];
                currentIndex = startIndex + 2;
            }
            else
            {
                result.Add(CreateIdExpression(sorted[startIndex], sorted[currentIndex - 1], idIncrement));
                if (currentIndex >= sorted.Count - 1)
                {
                    result.Add(sorted[currentIndex].ToString(Invariant));
                    break;
                }
                if (currentIndex == sorted.Count - 2)
                {
                    result.Add($"{sorted[currentIndex]} {sorted[currentIndex + 1]}");
                    break;
                }
                startIndex = currentIndex;
                idIncrement = sorted[startIndex + 1] - sorted[startIndex];
                currentIndex = startIndex + 2;
            }
        }

        return string.Join(" ", result);
    }

    public static List<List<double>> ConvertThreePointsToVectors(IList<IList<double>> points)
    {
        if (points.Count != 3 || points.Any(p => p.Count != 3))
        {
            throw new ArgumentException("操作错误，需要三个三维坐标点");
        }

        var p1 = points[0];
        var p2 = points[1];
        var p3 = points[2];

        var v1 = new List<double>
        {
            p2[0] - p1[0],
            p2[1] - p1[1],
            p2[2] - p1[2]
        };
        Normalize(v1);

        var v3 = new List<double>
        {
            p3[0] - p1[0],
            p3[1] - p1[1],
            p3[2] - p1[2]
        };

        double dot = v1[0] * v3[0] + v1[1] * v3[1] + v1[2] * v3[2];
        var projection = new[] { v1[0] * dot, v1[1] * dot, v1[2] * dot };

        var v2 = new List<double>
        {
            v3[0] - projection[0],
            v3[1] - projection[1],
            v3[2] - projection[2]
        };
        Normalize(v2);

        return new List<List<double>> { v1, v2 };
    }

    public static List<List<double>> ConvertAngleToVectors(IList<double> angles)
    {
        if (angles.Count != 3 || angles.All(a => Math.Abs(a) < double.Epsilon))
        {
            throw new ArgumentException("操作错误，数据无效");
        }

        double rx = DegreesToRadians(angles[0]);
        double ry = DegreesToRadians(angles[1]);
        double rz = DegreesToRadians(angles[2]);

        double ca = Math.Cos(rx);
        double sa = Math.Sin(rx);
        double cb = Math.Cos(ry);
        double sb = Math.Sin(ry);
        double cg = Math.Cos(rz);
        double sg = Math.Sin(rz);

        double v1x = cb * cg;
        double v1y = sa * sb * cg + ca * sg;
        double v1z = -ca * sb * cg + sa * sg;

        double v2x = -cb * sg;
        double v2y = -sa * sb * sg + ca * cg;
        double v2z = ca * sb * sg + sa * cg;

        var v1 = new List<double> { Round(v1x), Round(v1y), Round(v1z) };
        var v2 = new List<double> { Round(v2x), Round(v2y), Round(v2z) };
        return new List<List<double>> { v1, v2 };
    }

    public static List<int>? ParseNumberString(string? input)
    {
        if (string.IsNullOrWhiteSpace(input))
        {
            return null;
        }

        var tokens = input.Trim().Split((char[]?)null, StringSplitOptions.RemoveEmptyEntries);
        var ids = new List<int>();
        foreach (var token in tokens)
        {
            if (token.Contains("to", StringComparison.Ordinal))
            {
                var parts = token.Split(new[] { "to", "by" }, StringSplitOptions.RemoveEmptyEntries);
                if (parts.Length >= 2 &&
                    int.TryParse(parts[0], NumberStyles.Integer, Invariant, out int start) &&
                    int.TryParse(parts[1], NumberStyles.Integer, Invariant, out int end))
                {
                    int step = 1;
                    if (parts.Length > 2 && !int.TryParse(parts[2], NumberStyles.Integer, Invariant, out step))
                    {
                        step = 1;
                    }

                    if (step > 0 && end >= start)
                    {
                        int count = (end - start) / step + 1;
                        for (int n = 0; n < count; n++)
                        {
                            ids.Add(start + n * step);
                        }
                    }
                }
            }
            else if (int.TryParse(token, NumberStyles.Integer, Invariant, out int value))
            {
                ids.Add(value);
            }
        }

        return ids;
    }

    public static string LiveLoadSetLine(int code, int calcType, IList<string>? groups)
    {
        return groups == null || groups.Count == 0
            ? $"{code},{calcType},\r\n"
            : $"{code},{calcType},{string.Join(",", groups)}\r\n";
    }

    public static List<int> ParseIdsToArray(object? ids, bool allowEmpty = true)
    {
        var result = new List<int>();
        if (ids == null)
        {
            return result;
        }

        switch (ids)
        {
            case int value:
                result.Add(value);
                break;
            case string text:
                var parsed = ParseNumberString(text);
                if (parsed != null)
                {
                    result.AddRange(parsed);
                }
                break;
            default:
                foreach (var item in ToIntList(ids))
                {
                    result.Add(item);
                }
                break;
        }

        if (result.Count == 0 && !allowEmpty)
        {
            throw new InvalidOperationException("集合不可为空，请核查数据");
        }

        return result;
    }

    private static IEnumerable<string> ExpandCharmTerm(string item)
    {
        return item.Split(',')
            .SelectMany(term => term.Split('*'))
            .Select(term => term.Trim());
    }

    private static string FormatNumber(double value) => value.ToString("G", Invariant);

    private static string FormatObject(object? value)
    {
        return value switch
        {
            null => string.Empty,
            double d => FormatNumber(d),
            float f => FormatNumber(f),
            int i => i.ToString(Invariant),
            long l => l.ToString(Invariant),
            decimal m => m.ToString("G", Invariant),
            _ => value.ToString() ?? string.Empty
        };
    }

    private static string FormatLoopSegments(IEnumerable<IDictionary<string, IEnumerable<IEnumerable<double>>>>? segments)
    {
        if (segments == null)
        {
            return string.Empty;
        }

        var builder = new StringBuilder();
        foreach (var segment in segments)
        {
            foreach (var kvp in segment)
            {
                var key = string.Equals(kvp.Key, "main", StringComparison.OrdinalIgnoreCase) ? "MAIN" : "SUB";
                var points = kvp.Value.Select(pt => "(" + string.Join(",", pt.Select(FormatNumber)) + ")");
                builder.Append(key).Append("=");
                builder.AppendLine(string.Join(",", points));
            }
        }

        return builder.ToString();
    }

    private static object? GetValue(IDictionary<string, object?> data, string key)
    {
        return data.TryGetValue(key, out var value) ? value : null;
    }

    private static IList<string>? ToStringList(object? value)
    {
        if (value == null)
        {
            return null;
        }

        if (value is IList<string> list)
        {
            return list;
        }

        if (value is IEnumerable enumerable && value is not string)
        {
            var result = new List<string>();
            foreach (var item in enumerable)
            {
                if (item != null)
                {
                    result.Add(item.ToString() ?? string.Empty);
                }
            }
            return result;
        }

        if (value is string str)
        {
            return str.Split(new[] { ',', ';' }, StringSplitOptions.RemoveEmptyEntries)
                .Select(s => s.Trim()).ToList();
        }

        return null;
    }

    private static IList<double>? ToDoubleList(object? value)
    {
        if (value == null)
        {
            return null;
        }

        if (value is IList<double> list)
        {
            return list;
        }

        if (value is double d)
        {
            return new List<double> { d };
        }

        if (value is IEnumerable enumerable && value is not string)
        {
            var result = new List<double>();
            foreach (var item in enumerable)
            {
                if (item == null)
                {
                    continue;
                }

                if (item is double doubleValue)
                {
                    result.Add(doubleValue);
                }
                else if (item is IConvertible convertible)
                {
                    try
                    {
                        result.Add(convertible.ToDouble(Invariant));
                    }
                    catch
                    {
                        // Ignore invalid entries
                    }
                }
            }
            return result;
        }

        if (value is string str)
        {
            var items = str.Split(new[] { ',', ' ' }, StringSplitOptions.RemoveEmptyEntries);
            return items.Select(s => double.Parse(s, Invariant)).ToList();
        }

        return null;
    }

    private static IEnumerable<IEnumerable<object>>? ToEnumerableOfEnumerable(object? value)
    {
        if (value is IEnumerable<IEnumerable<object>> typed)
        {
            return typed;
        }

        if (value is IEnumerable outer && value is not string)
        {
            var list = new List<List<object>>();
            foreach (var row in outer)
            {
                if (row is IEnumerable inner && row is not string)
                {
                    var innerList = new List<object>();
                    foreach (var item in inner)
                    {
                        innerList.Add(item ?? string.Empty);
                    }
                    list.Add(innerList);
                }
            }
            return list;
        }

        return null;
    }

    private static IEnumerable<IEnumerable<double>>? ToEnumerableOfDoubles(object? value)
    {
        if (value is IEnumerable<IEnumerable<double>> typed)
        {
            return typed;
        }

        if (value is IEnumerable outer && value is not string)
        {
            var result = new List<List<double>>();
            foreach (var row in outer)
            {
                var list = ToDoubleList(row);
                if (list != null)
                {
                    result.Add(list.ToList());
                }
            }
            return result;
        }

        return null;
    }

    private static IEnumerable<IDictionary<string, IEnumerable<IEnumerable<double>>>>? ToLoopSegments(object? value)
    {
        if (value is IEnumerable<IDictionary<string, IEnumerable<IEnumerable<double>>>> typed)
        {
            return typed;
        }

        if (value is IEnumerable outer && value is not string)
        {
            var result = new List<Dictionary<string, IEnumerable<IEnumerable<double>>>>();
            foreach (var item in outer)
            {
                if (item is IDictionary dict)
                {
                    var entry = new Dictionary<string, IEnumerable<IEnumerable<double>>>();
                    foreach (DictionaryEntry kvp in dict)
                    {
                        var points = ToEnumerableOfDoubles(kvp.Value);
                        if (points != null)
                        {
                            entry[kvp.Key?.ToString() ?? string.Empty] = points.Select(p => p.ToList()).ToList();
                        }
                    }
                    result.Add(entry);
                }
            }
            return result;
        }

        return null;
    }

    private static IDictionary<string, IList<double>>? ToDictionaryOfDoubleLists(object? value)
    {
        if (value is IDictionary<string, IList<double>> typed)
        {
            return typed;
        }

        if (value is IDictionary<string, IEnumerable<double>> dictionary)
        {
            return dictionary.ToDictionary(k => k.Key, k => (IList<double>)k.Value.ToList());
        }

        if (value is IDictionary dict)
        {
            var result = new Dictionary<string, IList<double>>();
            foreach (DictionaryEntry entry in dict)
            {
                var list = ToDoubleList(entry.Value);
                if (list != null)
                {
                    result[entry.Key?.ToString() ?? string.Empty] = list;
                }
            }
            return result;
        }

        return null;
    }

    private static IEnumerable<int> ToIntList(object value)
    {
        if (value is IEnumerable<int> ints)
        {
            return ints;
        }

        if (value is IEnumerable enumerable && value is not string)
        {
            var list = new List<int>();
            foreach (var item in enumerable)
            {
                if (item is int intValue)
                {
                    list.Add(intValue);
                }
                else if (item is IConvertible convertible)
                {
                    try
                    {
                        list.Add(convertible.ToInt32(Invariant));
                    }
                    catch
                    {
                        // Ignore invalid entries
                    }
                }
            }
            return list;
        }

        throw new ArgumentException("不支持的 ids 类型");
    }

    private static double ToDouble(object? value, double defaultValue)
    {
        if (value is null)
        {
            return defaultValue;
        }

        if (value is double d)
        {
            return d;
        }

        if (value is IConvertible convertible)
        {
            try
            {
                return convertible.ToDouble(Invariant);
            }
            catch
            {
                return defaultValue;
            }
        }

        return defaultValue;
    }

    private static int ToInt(object? value, int defaultValue)
    {
        if (value is null)
        {
            return defaultValue;
        }

        if (value is int i)
        {
            return i;
        }

        if (value is IConvertible convertible)
        {
            try
            {
                return convertible.ToInt32(Invariant);
            }
            catch
            {
                return defaultValue;
            }
        }

        return defaultValue;
    }

    private static bool ToBool(object? value, bool defaultValue)
    {
        if (value is null)
        {
            return defaultValue;
        }

        if (value is bool b)
        {
            return b;
        }

        if (value is IConvertible convertible)
        {
            try
            {
                return convertible.ToBoolean(Invariant);
            }
            catch
            {
                return defaultValue;
            }
        }

        if (value is string str)
        {
            if (bool.TryParse(str, out var result))
            {
                return result;
            }
        }

        return defaultValue;
    }

    private static void Normalize(IList<double> vector)
    {
        double length = Math.Sqrt(vector[0] * vector[0] + vector[1] * vector[1] + vector[2] * vector[2]);
        if (length > 0)
        {
            vector[0] /= length;
            vector[1] /= length;
            vector[2] /= length;
        }
    }

    private static double DegreesToRadians(double degrees) => degrees * Math.PI / 180.0;

    private static double Round(double value) => Math.Round(value, 6);
}
