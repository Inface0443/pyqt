from qtmodel.core.qt_server import QtServer


class OdbModelLoad:
    """获取模型数据"""

    # region 钢束信息
    @staticmethod
    def get_tendon_property(name:str):
        """
        获取预应力荷载
        Args:
            name: 根据钢束特性名获取钢束特性
        Example:
            odb.get_tendon_property(name="钢束特性1")
        Returns: 包含信息为list[dict]
        """
        payload = {"name": name}
        return QtServer.send_dict("GET-TENDON-PROPERTY", payload)

    @staticmethod
    def get_tendon_data(name:str):
        """
        获取预应力荷载
        Args:
            name: 根据钢束名获取钢束信息
        Example:
            odb.get_tendon_data(name="钢束1")
        Returns: 包含信息为list[dict]
        """
        payload = {"name": name}
        return QtServer.send_dict("GET-TENDON-DATA", payload)
    # endregion

    # region 荷载信息
    @staticmethod
    def get_case_names():
        """
        获取荷载工况名
        Args: 无
        Example:
            odb.get_case_names()
        Returns: 包含信息为list[str]
        """
        return QtServer.send_dict("GET-CASE-NAMES", None)

    @staticmethod
    def get_pre_stress_load(case_name: str):
        """
        获取预应力荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_pre_stress_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        payload = {"case_name": case_name}
        return QtServer.send_dict("GET-PRESTRESS-LOAD", payload)

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
    def get_nodal_force_load(case_name: str):
        """
        获取节点力荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_nodal_force_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        payload = {"case_name": case_name}
        return QtServer.send_dict("GET-NODAL-FORCE-LOAD", payload)

    @staticmethod
    def get_nodal_displacement_load(case_name: str):
        """
        获取节点位移荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_nodal_displacement_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        payload = {"case_name": case_name}
        return QtServer.send_dict("GET-NODAL-DISPLACEMENT-LOAD", payload)

    @staticmethod
    def get_beam_element_load(case_name: str):
        """
        获取梁单元荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_beam_element_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        payload = {"case_name": case_name}
        return QtServer.send_dict("GET-BEAM-ELEMENT-LOAD", payload)

    @staticmethod
    def get_plate_element_load(case_name: str):
        """
        获取梁单元荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_beam_element_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        payload = {"case_name": case_name}
        return QtServer.send_dict("GET-PLATE-ELEMENT-LOAD", payload)

    @staticmethod
    def get_initial_tension_load(case_name: str):
        """
        获取初拉力荷载数据
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_initial_tension_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        payload = {"case_name": case_name}
        return QtServer.send_dict("GET-INITIAL-TENSION-LOAD", payload)

    @staticmethod
    def get_cable_length_load(case_name: str):
        """
        获取指定荷载工况的初拉力荷载数据
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_cable_length_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        payload = {"case_name": case_name}
        return QtServer.send_dict("GET-CABLE-LENGTH-LOAD", payload)

    @staticmethod
    def get_deviation_parameter():
        """
        获取制造偏差参数
        Args: 无
        Example:
            odb.get_deviation_parameter()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-DEVIATION-PARAMETER", None)

    @staticmethod
    def get_deviation_load(case_name: str):
        """
        获取指定荷载工况的制造偏差荷载
        Args:
            case_name:荷载工况名
        Example:
            odb.get_deviation_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        payload = {"case_name": case_name}
        return QtServer.send_dict("GET-DEVIATION-LOAD", payload)
    # endregion
