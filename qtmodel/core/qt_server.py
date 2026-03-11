import json
import threading
from typing import Optional
import requests

class QtServer:
    URL: str = "http://localhost:55125/pythonForQt/"
    QT_VERSION: str = "2.2.3"
    _session = requests.Session()
    _lock = threading.Lock()

    @staticmethod
    def send_command(command: str = "", header: str = ""):
        try:
            with QtServer._lock:
                response = QtServer._session.post(
                    QtServer.URL,
                    headers={'Content-Type': f'{header}'},
                    data=command.encode('utf-8'),
                    timeout=(3, 60)
                )

            if response.status_code == 200:
                return response.text
            elif response.status_code == 400:
                raise Exception(response.text)
            elif response.status_code == 413:
                raise Exception("请求体过大，请拆分请求或调整服务端请求限制")
            elif response.status_code == 504:
                raise Exception("服务端处理超时，请增加最大等待时间")
            else:
                raise Exception(f"连接错误，请重新尝试。HTTP {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as ex:
            raise Exception(f"请求失败: {ex}") from ex

    @staticmethod
    def send_dict(header: str, payload: Optional[dict] = None):
        try:
            if not payload:
                return QtServer.send_command(header=header, command="")
            payload = dict(payload)
            if "version" not in payload:
                payload["version"] = QtServer.QT_VERSION
            json_string = json.dumps(payload, ensure_ascii=False)
            return QtServer.send_command(header=header, command=json_string)
        except Exception as ex:
            raise Exception(str(ex)) from ex
