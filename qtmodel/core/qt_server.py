import json
from typing import Optional

import requests


class QtServer:
    URL: str = "http://localhost:55125/pythonForQt/"
    MERGE_STR: str = ""
    QT_MERGE: bool = False  # 是否合并发送
    QT_VERSION: str = "1.2.3"

    @staticmethod
    def send_command(command: str = "", header: str = ""):
        """
        用于单次数据传输，数据传输完成但不刷新UI
        :param command:建议输入json对象(单行)
        :param header: 数据块标识符
        :return:
        """
        response = requests.post(QtServer.URL,
                                 headers={'Content-Type': f'{header}'},
                                 data=command.encode('utf-8'))
        if response.status_code == 200:
            return response.text
        elif response.status_code == 400:
            raise Exception(response.text)
        elif response.status_code == 413:
            raise Exception("请求体过大，请拆分请求或调整服务端或反向代理（Nginx/网关/负载均衡）请求限制")
        elif response.status_code == 504:
            raise Exception("服务端或反向代理（Nginx/网关/负载均衡）超时，请增加最大等待时间")
        else:
            raise Exception("连接错误，请重新尝试")

    @staticmethod
    def send_dict(header: str, payload: Optional[dict] = None):
        """
        统一发送：有参数 -> JSON；无参数 -> 不带 command 的 post
        """
        try:
            if not payload:  # None 或 空字典
                return QtServer.send_command(header=header, command="")
            if "version" not in payload:
                payload["version"] = QtServer.QT_VERSION
            json_string = json.dumps(payload, ensure_ascii=False)
            return QtServer.send_command(header=header, command=json_string)
        except Exception as ex:
            raise Exception(ex)
