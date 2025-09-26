from ..core.qt_server import QtServer


class OdbModelBoundary:
    # region 获取模型边界信息
    @staticmethod
    def get_boundary_group_names():
        """
        获取自边界组名称
        Args:无
        Example:
            odb.get_boundary_group_names()
        Returns: 包含信息为list[str]
        """
        return QtServer.send_get("GET-BOUNDARY-GROUP-NAMES", None)

    @staticmethod
    def get_general_support_data(group_name: str = None):
        """
        获取一般支承信息
        Args:
             group_name:默认输出所有边界组信息
        Example:
            odb.get_general_support_data()
        Returns: 包含信息为list[dict]
        """
        payload = {"group_name": group_name} if group_name is not None else None
        return QtServer.send_get("GET-GENERAL-SUPPORT-DATA", payload)

    @staticmethod
    def get_elastic_link_data(group_name: str = None):
        """
        获取弹性连接信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_elastic_link_data()
        Returns: 包含信息为list[dict]
        """
        payload = {"group_name": group_name} if group_name is not None else None
        return QtServer.send_get("GET-ELASTIC-LINK-DATA", payload)

    @staticmethod
    def get_elastic_support_data(group_name: str = None):
        """
        获取弹性支承信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_elastic_support_data()
        Returns: 包含信息为list[dict]
        """
        payload = {"group_name": group_name} if group_name is not None else None
        return QtServer.send_get("GET-ELASTIC-SUPPORT-DATA", payload)

    @staticmethod
    def get_master_slave_link_data(group_name: str = None):
        """
        获取主从连接信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_master_slave_link_data()
        Returns: 包含信息为list[dict]
        """
        payload = {"group_name": group_name} if group_name is not None else None
        return QtServer.send_get("GET-MASTER-SLAVE-LINK-DATA", payload)

    @staticmethod
    def get_node_local_axis_data():
        """
        获取节点坐标信息
        Args:无
        Example:
            odb.get_node_local_axis_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_get("GET-NODE-LOCAL-AXIS-DATA", None)

    @staticmethod
    def get_beam_constraint_data(group_name: str = None):
        """
           获取节点坐标信息
           Args:
               group_name:默认输出所有边界组信息
           Example:
               odb.get_beam_constraint_data()
           Returns: 包含信息为list[dict]或 dict
        """
        payload = {"group_name": group_name} if group_name is not None else None
        return QtServer.send_get("GET-BEAM-CONSTRAINT-DATA", payload)

    @staticmethod
    def get_constraint_equation_data(group_name: str = None):
        """
         获取约束方程信息
         Args:
             group_name:默认输出所有边界组信息
         Example:
             odb.get_constraint_equation_data()
         Returns: 包含信息为list[dict]
         """
        payload = {"group_name": group_name} if group_name is not None else None
        return QtServer.send_get("GET-CONSTRAINT-EQUATION-DATA", payload)

    @staticmethod
    def get_effective_width(group_name: str = None):
        """
        获取有效宽度数据
        Args:
            group_name:边界组
        Example:
            odb.get_effective_width(group_name="边界组1")
        Returns:  list[dict]
        """
        payload = {"group_name": group_name} if group_name is not None else None
        return QtServer.send_get("GET-EFFECTIVE-WIDTH", payload)

# endregion
