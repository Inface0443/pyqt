import time
from qtmodel.core.qt_server import QtServer
from typing import List


class MdbProject:
    """
    用于项目管理，如打开保存运行分析等操作
    """

    # region 项目管理
    @staticmethod
    def set_url(url: str):
        QtServer.URL = url

    @staticmethod
    def set_version(version: str = QtServer.QT_VERSION):
        """
        控制第三方库版本
        Args:无
        Example:
            mdb.set_version()
        Returns: 无
        """
        QtServer.QT_VERSION = version

    @staticmethod
    def undo_model():
        """
        撤销模型上次操作
        Args:无
        Example:
            mdb.undo_model()
        Returns: 无
        """
        QtServer.send_dict(header="UNDO")

    @staticmethod
    def redo_model():
        """
        重做上次撤销
        Args:无
        Example:
            mdb.redo_model()
        Returns: 无
        """
        QtServer.send_dict(header="REDO")

    @staticmethod
    def update_model():
        """
        刷新模型信息
        Args: 无
        Example:
            mdb.update_model()
        Returns: 无
        """
        QtServer.send_dict(header="UPDATE")

    @staticmethod
    def update_to_pre():
        """
        切换到前处理
        Args: 无
        Example:
            mdb.update_to_pre()
        Returns: 无
        """
        QtServer.send_dict(header="UPDATE-TO-PRE")

    @staticmethod
    def update_to_post():
        """
        切换到后处理
        Args:  无
        Example:
            mdb.update_to_post()
        Returns: 无
        """
        QtServer.send_dict(header="UPDATE-TO-POST")

    @staticmethod
    def do_solve():
        """
        运行分析
        Args: 无
        Example:
            mdb.do_solve()
        Returns: 无
        """
        QtServer.send_dict(header="DO-SOLVE")
        # 设置缓冲时间
        time.sleep(3)

    @staticmethod
    def initial():
        """
        初始化模型,新建模型
        Args: 无
        Example:
            mdb.initial()
        Returns: 无
        """
        QtServer.send_dict(header="INITIAL")

    @staticmethod
    def open_file(file_path: str):
        """
        打开bfmd文件
        Args:
            file_path: 文件全路径
        Example:
            mdb.open_file(file_path="a.bfmd")
        Returns: 无
        """
        if not file_path.endswith(".bfmd"):
            raise Exception("操作错误，仅支持bfmd文件")
        QtServer.send_command(header="OPEN-FILE", command=file_path)

    @staticmethod
    def close_project():
        """
        关闭项目
        Args: 无
        Example:
            mdb.close_project()
        Returns: 无
        """
        QtServer.send_dict(header="CLOSE-PROJECT")

    @staticmethod
    def save_file(file_path: str = ""):
        """
        保存bfmd文件，默认保存为当前路径
        Args:
            file_path: 文件全路径
        Example:
            mdb.save_file(file_path="a.bfmd")
        Returns: 无
        """
        QtServer.send_command(header="SAVE-FILE", command=file_path)

    @staticmethod
    def import_command(command: str, command_type: int = 1):
        """
        导入命令
        Args:
            command:命令字符
            command_type:命令类型,默认桥通命令 1-桥通命令 2-mct命令
        Example:
            mdb.import_command(command="*SEC-INFO")
            mdb.import_command(command="*SECTION",command_type=2)
        Returns: 无
        """
        if command_type < 1 or command_type > 2:
            raise Exception("仅支持command_type(1-桥通命令 2-mct命令 )")
        # 创建参数字典
        params = {
            "command": command,
            "command_type": command_type,
        }
        result = QtServer.send_dict(header="INP-COMMAND", payload=params)
        return result

    @staticmethod
    def import_file(file_path: str):
        """
        导入文件,导入文件为桥通所在主机文件
        Args:
            file_path:导入文件(.mct/.qdat/.dxf/.3dx)
        Example:
            mdb.import_file(file_path="a.mct")
        Returns: 无
        """
        QtServer.send_command(header="INP-FILE", command=file_path)

    @staticmethod
    def export_file(file_path: str, convert_sec_group: bool = False, type_kind: int = 2, group_name: List[str] = None):
        """
        导出命令为导出到本机所在地址,默认输出截面特性和截面信息
        Args:
            file_path:导出文件全路径，支持格式(.mct/.qdat/.obj/.txt/.py)
            convert_sec_group:是否将变截面组转换为变截面
            type_kind:输出文件类型 0-仅输出截面特性和材料特性(仅供qdat输出) 1-仅输出模型文件  2-输出截面特性和截面信息
            group_name:obj与 APDL导出时指定结构组导出
        Example:
            mdb.export_file(file_path="a.mct")
        Returns: 无
        """
        # 创建参数字典
        params = {
            "file_path": file_path,
            "convert_sec_group": convert_sec_group,
            "type_kind": type_kind,
            "group_name": group_name,
        }
        content = QtServer.send_dict(header="EXP-FILE", payload=params)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def export_qt_helper(file_path: str):
        """
        输出桥通qdat命令帮助文档,仅支持最新帮助文档,保存路径为调用主机下
        Args:
            file_path:导出文件全路径，支持格式(.txt/.qdat)
        Example:
            mdb.export_qt_helper(file_path="a.qdat")
        Returns: 无
        """
        # 创建参数字典
        content = QtServer.send_dict(header="EXP-QT-HELPER")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    # endregion
