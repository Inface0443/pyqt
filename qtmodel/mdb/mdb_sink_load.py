from ..core.qt_server import QtServer
from typing import Union, List
from qtmodel.core.data_helper import QtDataHelper


class MdbSinkLoad:
    """
    用于支座沉降荷载添加
    """

    # region 支座沉降操作
    @staticmethod
    def add_sink_group(name: str = "", sink: float = 0.1, node_ids: (Union[int, List[int], str]) = None):
        """
        添加沉降组
        Args:
             name: 沉降组名
             sink: 沉降值
             node_ids: 节点编号，支持数或列表
        Example:
            mdb.add_sink_group(name="沉降1",sink=0.1,node_ids=[1,2,3])
        Returns: 无
        """
        try:
            if isinstance(node_ids, int):
                node_ids = [node_ids]
            if node_ids is None:
                id_str = ""
            elif isinstance(node_ids, list):
                id_str = QtDataHelper.parse_int_list_to_str(node_ids)
            else:
                id_str = str(node_ids)
            s = "*SINK-GROUP\r\n" + f"{name},{sink:g},{id_str}\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(f"添加沉降组:{name}错误,{ex}")

    @staticmethod
    def add_sink_case(name: str, sink_groups: (Union[str, List[str]]) = None):
        """
        添加沉降工况
        Args:
            name:荷载工况名
            sink_groups:沉降组名，支持字符串或列表
        Example:
            mdb.add_sink_case(name="沉降工况1",sink_groups=["沉降1","沉降2"])
        Returns: 无
        """
        try:
            if isinstance(sink_groups, str):
                sink_groups = [sink_groups]
            s = "*SINK-CASE\r\n" + f"{name},{','.join(sink_groups)}\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(f"添加沉降工况:{name}错误,{ex}")

    @staticmethod
    def add_concurrent_reaction(names: (Union[str, List[str]])):
        """
        添加并发反力组
        Args:
             names: 结构组名称集合
        Example:
            mdb.add_concurrent_reaction(names=["默认结构组"])
        Returns: 无
        """
        try:
            if names is None:
                raise Exception("操作错误，添加并发反力组时结构组名称不能为空")
            if isinstance(names, str):
                names = [names]
            s = "*CCT-REACT\r\n" + ",".join(names) + "\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(f"添加并发反力组错误,{ex}")

    @staticmethod
    def add_concurrent_force(names: (Union[str, List[str]])):
        """
        创建并发内力组
        Args:
            names: 结构组名称集合
        Example:
            mdb.add_concurrent_force(names=["默认结构组"])
        Returns: 无
        """
        try:
            if isinstance(names, str):
                names = [names]
            s = "*CCT-FORCE\r\n" + ",".join(names) + "\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(f"添加并发内力组错误,{ex}")



    @staticmethod
    def update_sink_case(name: str, new_name: str = "", sink_groups: (Union[str, List[str]]) = None):
        """
        todo 更新沉降工况
        Args:
            name:荷载工况名
            new_name: 新沉降组名,默认不修改
            sink_groups:沉降组名，支持字符串或列表
        Example:
            mdb.update_sink_case(name="沉降工况1",sink_groups=["沉降1","沉降2"])
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "sink_groups": sink_groups,
        }
        return QtServer.send_dict("UPDATE-SINK-CASE", payload)



    @staticmethod
    def remove_sink_group(name: str = ""):
        """
        todo 按照名称删除沉降组
        Args:
             name:沉降组名,默认删除所有沉降组
        Example:
            mdb.remove_sink_group()
            mdb.remove_sink_group(name="沉降1")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        return QtServer.send_dict("REMOVE-SINK-GROUP", payload)

    @staticmethod
    def remove_sink_case(name=""):
        """
        todo 按照名称删除沉降工况,不输入名称时默认删除所有沉降工况
        Args:
            name:沉降工况名
        Example:
            mdb.remove_sink_case()
            mdb.remove_sink_case(name="沉降1")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        return QtServer.send_dict("REMOVE-SINK-CASE", payload)



    @staticmethod
    def remove_concurrent_reaction():
        """
        todo 删除所有并发反力组
        Args:无
        Example:
            mdb.remove_concurrent_reaction()
        Returns: 无
        """
        payload = {}
        return QtServer.send_dict("REMOVE-CONCURRENT-REACTION", payload)

    @staticmethod
    def remove_concurrent_force():
        """
        todo 删除所有并发内力组
        Args: 无
        Example:
            mdb.remove_concurrent_force()
        Returns: 无
        """
        payload = {}
        return QtServer.send_dict("REMOVE-CONCURRENT-FORCE", payload)


    # endregion