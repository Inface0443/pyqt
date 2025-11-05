using System;
using System.Text.Json;
using System.Threading.Tasks;
using QtModel.Core;

namespace QtModel.Mdb;

public static class MdbProject
{
    public static void SetUrl(string url) => QtServer.Url = url;

    public static void SetMergeStr(bool isOpen) => QtServer.QtMerge = isOpen;

    public static void SetVersion(string version = "1.2.3")
    {
        QtServer.QtVersion = version;
        QtServer.SendCommand(JsonSerializer.Serialize(new { version }), "QDAT");
    }

    public static void UndoModel() => QtServer.SendCommand(header: "UNDO");

    public static void RedoModel() => QtServer.SendCommand(header: "REDO");

    public static void UpdateModel()
    {
        QtServer.SendCommand(QtServer.MergeString, "UPDATE");
        QtServer.MergeString = string.Empty;
    }

    public static void UpdateToPre() => QtServer.SendCommand(header: "UPDATE-TO-PRE");

    public static void UpdateToPost() => QtServer.SendCommand(header: "UPDATE-TO-POST");

    public static void DoSolve()
    {
        QtServer.SendCommand(header: "DO-SOLVE");
        Task.Delay(TimeSpan.FromSeconds(3)).Wait();
    }

    public static void Initial() => QtServer.SendCommand(header: "INITIAL");

    public static void OpenFile(string filePath)
    {
        if (!filePath.EndsWith(".bfmd", StringComparison.OrdinalIgnoreCase))
        {
            throw new InvalidOperationException("操作错误，仅支持bfmd文件");
        }

        QtServer.SendCommand(filePath, "OPEN-FILE");
    }

    public static void CloseProject() => QtServer.SendCommand(header: "CLOSE-PROJECT");

    public static void SaveFile(string filePath = "")
        => QtServer.SendCommand(filePath, "SAVE-FILE");

    public static void ImportCommand(string command, int commandType = 1)
    {
        var header = commandType == 1 ? "COMMAND" : "MCT";
        QtServer.SendCommand(command, header);
    }

    public static void ImportJson(object payload)
    {
        var json = JsonSerializer.Serialize(payload, new JsonSerializerOptions
        {
            Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping
        });
        QtServer.SendCommand(json, "IMPORT-JSON");
    }

    public static void ImportFile(string filePath) => QtServer.SendCommand(filePath, "IMPORT-FILE");

    public static void ExportFile(string filePath) => QtServer.SendCommand(filePath, "EXPORT-FILE");
}
