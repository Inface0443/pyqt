using System;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace QtModel.Core;

public static class QtServer
{
    private static readonly HttpClient Client = new();

    public static string Url { get; set; } = "http://localhost:55125/pythonForQt/";
    public static string MergeString { get; set; } = string.Empty;
    public static bool QtMerge { get; set; }
    public static string QtVersion { get; set; } = "1.2.3";

    public static string? SendCommand(string command = "", string header = "")
        => SendCommandAsync(command, header).GetAwaiter().GetResult();

    public static async Task<string?> SendCommandAsync(string command = "", string header = "")
    {
        using var request = new HttpRequestMessage(HttpMethod.Post, Url)
        {
            Content = new StringContent(command, Encoding.UTF8)
        };
        if (!string.IsNullOrEmpty(header))
        {
            request.Content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue(header);
        }

        var response = await Client.SendAsync(request).ConfigureAwait(false);
        var text = await response.Content.ReadAsStringAsync().ConfigureAwait(false);
        return response.StatusCode switch
        {
            System.Net.HttpStatusCode.OK => text,
            System.Net.HttpStatusCode.BadRequest => throw new InvalidOperationException(text),
            System.Net.HttpStatusCode.RequestEntityTooLarge =>
                throw new InvalidOperationException("请求体过大，请拆分请求或调整服务端限制"),
            System.Net.HttpStatusCode.GatewayTimeout =>
                throw new InvalidOperationException("服务端或反向代理超时，请增加最大等待时间"),
            _ => throw new InvalidOperationException("连接错误，请重新尝试")
        };
    }

    public static Task<string?> SendDictAsync(string header, object? payload = null)
    {
        if (payload is null)
        {
            return SendCommandAsync(string.Empty, header);
        }

        var dictionary = JsonSerializer.Serialize(payload, new JsonSerializerOptions
        {
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
            Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping
        });

        return SendCommandAsync(dictionary, header);
    }

    public static string? SendDict(string header, object? payload = null)
        => SendDictAsync(header, payload).GetAwaiter().GetResult();
}
