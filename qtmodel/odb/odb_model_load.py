from qtmodel.core.qt_server import QtServer


class OdbModelLoad:
    """获取模型数据"""

    # region 钢束信息
    @staticmethod
    def get_tendon_property_data():
        """
        获取所有钢束特性信息
        Args: 无
        Example:
            odb.get_tendon_property_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-TENDON-PROPERTY-DATA")

    @staticmethod
    def get_tendon_data():
        """
        获取所有钢塑和信息
        Args: 无
        Example:
            odb.get_tendon_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-TENDON-DATA")
    # endregion

    # region 荷载信息
    @staticmethod
    def get_load_case_names():
        """
        获取荷载工况名
        Args: 无
        Example:
            odb.get_load_case_names()
        Returns: 包含信息为list[str]
        """
        return QtServer.send_dict("GET-LOAD-CASE-NAMES", None)

    @staticmethod
    def get_pre_stress_load_data():
        """
        获取预应力荷载
        Args: 无
        Example:
            odb.get_pre_stress_load()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-PRE-STRESS-LOAD-DATA")

    @staticmethod
    def get_node_mass_data():
        """
        获取节点质量
        Args: 无
        Example:
            odb.get_node_mass_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-NODE-MASS-DATA", None)

    @staticmethod
    def get_nodal_force_load_data():
        """
        获取节点力荷载
        Args: 无
        Example:
            odb.get_nodal_force_load()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-NODAL-FORCE-LOAD-DATA")

    @staticmethod
    def get_nodal_displacement_load_data():
        """
        获取节点位移荷载
        Args: 无
        Example:
            odb.get_nodal_displacement_load_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-NODAL-DISPLACEMENT-LOAD-DATA")

    @staticmethod
    def get_beam_element_load_data():
        """
        获取梁单元荷载
        Args: 无
        Example:
            odb.get_beam_element_load_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-BEAM-ELEMENT-LOAD-DATA")

    @staticmethod
    def get_plate_element_load_data():
        """
        获取梁单元荷载
        Args: 无
        Example:
            odb.get_plate_element_load_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-PLATE-ELEMENT-LOAD-DATA")

    @staticmethod
    def get_initial_tension_load_data():
        """
        获取初拉力荷载数据
        Args: 无
        Example:
            odb.get_initial_tension_load_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-INITIAL-TENSION-LOAD-DATA")

    @staticmethod
    def get_cable_length_load_data():
        """
        获取指定荷载工况的初拉力荷载数据
        Args: 无
        Example:
            odb.get_cable_length_load()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-CABLE-LENGTH-LOAD-DATA")

    @staticmethod
    def get_deviation_parameters():
        """
        获取制造偏差参数
        Args: 无
        Example:
            odb.get_deviation_parameters()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-DEVIATION-PARAMETERS", None)

    @staticmethod
    def get_deviation_load_data():
        """
        获取指定荷载工况的制造偏差荷载
        Args: 无
        Example:
            odb.get_deviation_load_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-DEVIATION-LOAD-DATA")
    # endregion
