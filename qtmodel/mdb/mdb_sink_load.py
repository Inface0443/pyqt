from qtmodel.core.qt_server import QtServer
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
        """
           添加沉降分组
           """
        payload = {
            "name": name,
            "sink": sink,
            "node_ids": QtDataHelper.parse_ids_to_array(node_ids),
        }
        return QtServer.send_dict("ADD-SINK-GROUP", payload)

    @staticmethod
    def add_sink_case(name: str, sink_groups: (Union[str, List[str]]) = None):
        """
          添加沉降工况
        """
        if isinstance(sink_groups, str):
            groups = [sink_groups] if sink_groups else []
        else:
            groups = sink_groups

        payload = {
            "name": name,
            "sink_groups": groups,
        }
        return QtServer.send_dict("ADD-SINK-CASE", payload)

    @staticmethod
    def add_concurrent_reaction(names: Union[str, List[str]]):
        """
        添加并行反力组合（并行反力工况之类）
        """
        if isinstance(names, str):
            name_list = [names] if names else []
        else:
            name_list = names

        payload = {
            "names": name_list,
        }
        return QtServer.send_dict("ADD-CONCURRENT-REACTION", payload)

    @staticmethod
    def add_concurrent_force(names: Union[str, List[str]]):
        """
           添加并行内力工况
           """
        if isinstance(names, str):
            name_list = [names] if names else []
        else:
            name_list = names

        payload = {
            "names": name_list,
        }
        return QtServer.send_dict("ADD-CONCURRENT-FORCE", payload)

    @staticmethod
    def update_sink_case(name: str, new_name: str = "", sink_groups: (Union[str, List[str]]) = None):
        """
        更新沉降工况
        Args:
            name:荷载工况名
            new_name: 新沉降组名,默认不修改
            sink_groups:沉降组名，支持字符串或列表
        Example:
            mdb.update_sink_case(name="沉降工况1",sink_groups=["沉降1","沉降2"])
        Returns: 无
        """
        if isinstance(sink_groups, str):
            name_list = [sink_groups] if sink_groups else []
        else:
            name_list = sink_groups
        payload = {
            "name": name,
            "new_name": new_name,
            "sink_groups": name_list,
        }
        return QtServer.send_dict("UPDATE-SINK-CASE", payload)

    @staticmethod
    def remove_sink_group(name: str = ""):
        """
        按照名称删除沉降组
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
        按照名称删除沉降工况,不输入名称时默认删除所有沉降工况
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
        删除所有并发反力组
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
        删除所有并发内力组
        Args: 无
        Example:
            mdb.remove_concurrent_force()
        Returns: 无
        """
        payload = {}
        return QtServer.send_dict("REMOVE-CONCURRENT-FORCE", payload)
    # endregion
