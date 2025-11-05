using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Text.Encodings.Web;
using System.Text.Json;
using System.Threading.Tasks;

namespace QtCsharp.Core;

public static class QtServer
{
    private static readonly HttpClient Client = new();
    private static readonly JsonSerializerOptions JsonOptions = new()
    {
        Encoder = JavaScriptEncoder.UnsafeRelaxedJsonEscaping,
        WriteIndented = false
    };

    public static string Url { get; set; } = "http://localhost:55125/pythonForQt/";
    public static string MergeString { get; set; } = string.Empty;
    public static bool QtMerge { get; set; }
    public static string QtVersion { get; set; } = "1.2.3";

    public static Task<string> SendCommandAsync(string command = "", string header = "")
    {
        return SendCommandInternalAsync(command ?? string.Empty, header ?? string.Empty);
    }

    public static string SendCommand(string command = "", string header = "")
    {
        return SendCommandAsync(command, header).GetAwaiter().GetResult();
    }

    public static async Task<string> SendDictAsync(string header, IDictionary<string, object?>? payload = null)
    {
        if (header == null)
        {
            throw new ArgumentNullException(nameof(header));
        }

        var commandPayload = payload != null ? new Dictionary<string, object?>(payload) : null;
        if (commandPayload is { Count: > 0 })
        {
            if (!commandPayload.ContainsKey("version"))
            {
                commandPayload["version"] = QtVersion;
            }
            var json = JsonSerializer.Serialize(commandPayload, JsonOptions);
            return await SendCommandInternalAsync(json, header).ConfigureAwait(false);
        }

        return await SendCommandInternalAsync(string.Empty, header).ConfigureAwait(false);
    }

    public static string SendDict(string header, IDictionary<string, object?>? payload = null)
    {
        return SendDictAsync(header, payload).GetAwaiter().GetResult();
    }

    private static async Task<string> SendCommandInternalAsync(string command, string header)
    {
        using var request = new HttpRequestMessage(HttpMethod.Post, Url)
        {
            Content = new StringContent(command, Encoding.UTF8)
        };

        request.Headers.TryAddWithoutValidation("Content-Type", header);

        using var response = await Client.SendAsync(request).ConfigureAwait(false);
        var content = await response.Content.ReadAsStringAsync().ConfigureAwait(false);

        return response.StatusCode switch
        {
            System.Net.HttpStatusCode.OK => content,
            System.Net.HttpStatusCode.BadRequest => throw new InvalidOperationException(content),
            (System.Net.HttpStatusCode)413 => throw new InvalidOperationException("请求体过大，请拆分请求或调整服务端或反向代理（Nginx/网关/负载均衡）请求限制"),
            System.Net.HttpStatusCode.GatewayTimeout => throw new InvalidOperationException("服务端或反向代理（Nginx/网关/负载均衡）超时，请增加最大等待时间"),
            _ => throw new InvalidOperationException("连接错误，请重新尝试")
        };
    }
}
