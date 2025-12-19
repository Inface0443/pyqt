from qtmodel.core.qt_server import QtServer


class OdbModelBoundary:
    """
    用于获取边界信息
    """

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
        return QtServer.send_dict("GET-BOUNDARY-GROUP-NAMES", None)

    @staticmethod
    def get_general_support_data():
        """
        获取一般支承信息
        Args: 无
        Example:
            odb.get_general_support_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-GENERAL-SUPPORT-DATA")

    @staticmethod
    def get_elastic_link_data():
        """
        获取弹性连接信息
        Args: 无
        Example:
            odb.get_elastic_link_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-ELASTIC-LINK-DATA")

    @staticmethod
    def get_elastic_support_data():
        """
        获取弹性支承信息
        Args: 无
        Example:
            odb.get_elastic_support_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-ELASTIC-SUPPORT-DATA")

    @staticmethod
    def get_master_slave_link_data():
        """
        获取主从连接信息
        Args: 无
        Example:
            odb.get_master_slave_link_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-MASTER-SLAVE-LINK-DATA")

    @staticmethod
    def get_node_local_axis_data():
        """
        获取节点坐标信息
        Args:无
        Example:
            odb.get_node_local_axis_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-NODE-LOCAL-AXIS-DATA")

    @staticmethod
    def get_beam_constraint_data():
        """
        获取节点坐标信息
        Args: 无
        Example:
           odb.get_beam_constraint_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-BEAM-CONSTRAINT-DATA")

    @staticmethod
    def get_constraint_equation_data():
        """
        获取约束方程信息
        Args: 无
        Example:
            odb.get_constraint_equation_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-CONSTRAINT-EQUATION-DATA")

    @staticmethod
    def get_effective_width_data():
        """
        获取有效宽度数据
        Args: 无
        Example:
            odb.get_effective_width_data()
        Returns:  list[dict]
        """
        return QtServer.send_dict("GET-EFFECTIVE-WIDTH-DATA")

# endregion
