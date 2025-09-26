from ..core.qt_server import QtServer
from ..core.data_helper import QtDataHelper


class OdbModel:
    """
    用于获取模型信息
    """

    # region 获取节点信息
    @staticmethod
    def get_overlap_nodes(round_num: int = 4):
        """
        获取重合节点
        Args:
            round_num: 判断精度，默认小数点后四位
        Example:
            odb.get_overlap_nodes()
        Returns: 包含信息为list[list[int]]
        """
        payload = {"round_num": round_num}
        return QtServer.send_get("GET-OVERLAP-NODES", payload)

    @staticmethod
    def get_node_id(x: float = 0, y: float = 0, z: float = 0, tolerance: float = 1e-4):
        """
        获取节点编号,结果为-1时则表示未找到该坐标节点
        Args:
            x: 目标点X轴坐标
            y: 目标点Y轴坐标
            z: 目标点Z轴坐标
            tolerance: 距离容许误差
        Example:
            odb.get_node_id(x=1,y=1,z=1)
        Returns: int
        """
        payload = {"x": x, "y": y, "z": z, "tolerance": tolerance}
        return QtServer.send_get("GET-NODE-ID", payload)

    @staticmethod
    def get_group_nodes(group_name: str = "默认结构组"):
        """
        获取结构组节点编号
        Args:
            group_name: 结构组名
        Example:
            odb.get_group_nodes(group_name="默认结构组")
        Returns: list[int]
        """
        payload = {"group_name": group_name}
        return QtServer.send_get("GET-GROUP-NODES", payload)

    @staticmethod
    def get_node_data(ids=None):
        """
        获取节点信息 默认获取所有节点信息
        Args:
            ids:节点号集合支持XtoYbyN形式字符串
        Example:
            odb.get_node_data()     # 获取所有节点信息
            odb.get_node_data(ids=1)    # 获取单个节点信息
            odb.get_node_data(ids=[1,2])    # 获取多个节点信息
        Returns:  包含信息为list[dict] or dict
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_get("GET-NODE-DATA", payload)

    # endregion

    # region 获取单元信息
    @staticmethod
    def get_element_by_point(x: float = 0, y: float = 0, z: float = 0, tolerance: float = 1):
        """
        获取某一点指定范围内单元集合,单元中心点为节点平均值
        Args:
            x: 坐标x
            y: 坐标y
            z: 坐标z
            tolerance:容许范围,默认为1
        Example:
            odb.get_element_by_point(0.5,0.5,0.5,tolerance=1)
        Returns: 包含信息为list[int]
        """
        payload = {"x": x, "y": y, "z": z, "tolerance": tolerance}
        return QtServer.send_get("GET-ELEMENTS-BY-POINT", payload)

    @staticmethod
    def get_element_by_material(name: str = ""):
        """
        获取某一材料相应的单元
        Args:
            name:材料名称
        Example:
            odb.get_element_by_material("材料1")
        Returns: 包含信息为list[int]
        """
        payload = {"name": name}
        return QtServer.send_get("GET-ELEMENTS-BY-MATERIAL", payload)

    @staticmethod
    def get_overlap_elements():
        """
        获取重合节点
        Args:无
        Example:
            odb.get_overlap_elements()
        Returns:  包含信息为list[list[int]]
        """
        return QtServer.send_get("GET-OVERLAP-ELEMENTS", None)

    @staticmethod
    def get_structure_group_names():
        """
        获取结构组名称
        Args:无
        Example:
            odb.get_structure_group_names()
        Returns: 包含信息为list[str]
        """
        return QtServer.send_get("GET-STRUCTURE-GROUP-NAMES", None)




    @staticmethod
    def get_element_data(ids=None):
        """
        获取单元信息
        Args:
            ids:单元号,支持整数或整数型列表且支持XtoYbyN形式字符串,默认为None时获取所有单元信息
        Example:
            odb.get_element_data() # 获取所有单元结果
            odb.get_element_data(ids=1) # 获取指定编号单元信息
        Returns:  包含信息为list[dict] or dict
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_get("GET-ELEMENT-DATA", payload)

    @staticmethod
    def get_element_type(element_id: int) -> str:
        """
        获取单元类型
        Args:
            element_id: 单元号
        Example:
            odb.get_element_type(element_id=1) # 获取1号单元类型
        Returns: str
        """
        payload = {"element_id": element_id}
        return QtServer.send_get("GET-ELEMENT-TYPE", payload)

    @staticmethod
    def get_group_elements(group_name: str = "默认结构组"):
        """
        获取结构组单元编号
        Args:
            group_name: 结构组名
        Example:
            odb.get_group_elements(group_name="默认结构组")
        Returns: list[int]
        """
        payload = {"group_name": group_name}
        return QtServer.send_get("GET-GROUP-ELEMENTS", payload)





    # endregion

    # region 获取材料
    @staticmethod
    def get_concrete_material(ids=None):
        """
        获取混凝土材料信息
        Args:
            ids: 材料号支持XtoYbyN形式字符串,默认时输出全部材料
        Example:
            odb.get_concrete_material() # 获取所有材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_get("GET-CONCRETE-MATERIAL", payload)

    @staticmethod
    def get_steel_plate_material(ids=None):
        """
        获取钢材材料信息
        Args:
            ids: 材料号支持XtoYbyN形式字符串,默认时输出全部材料
        Example:
            odb.get_steel_plate_material() # 获取所有钢材材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_get("GET-STEEL-PLATE-MATERIAL", payload)

    @staticmethod
    def get_pre_stress_bar_material(ids=None):
        """
        获取钢材材料信息
        Args:
            ids: 材料号,默认时输出全部材料
        Example:
            odb.get_pre_stress_bar_material() # 获取所有预应力材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_get("GET-PRE-STRESS-BAR-MATERIAL", payload)

    @staticmethod
    def get_steel_bar_material(ids=None):
        """
        获取钢筋材料信息
        Args:
            ids: 材料号,默认None时输出全部材料
        Example:
            odb.get_steel_bar_material() # 获取所有钢筋材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_get("GET-STEEL-BAR-MATERIAL", payload)

    @staticmethod
    def get_user_define_material(ids=None):
        """
        获取自定义材料信息
        Args:
            ids: 材料号支持XtoYbyN形式字符串,默认None时输出全部材料
        Example:
            odb.get_user_define_material() # 获取所有自定义材料信息
            odb.get_user_define_material("1to10") # 获取所有自定义材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_get("GET-USER-DEFINE-MATERIAL", payload)

    @staticmethod
    def get_material_data():
        """
        获取材料信息
        Args: 无
        Example:
            odb.get_material_data() # 获取所有材料信息
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_get("GET-MATERIAL-DATA", None)

    @staticmethod
    def get_thickness_data(thick_id: int):
        """
        获取所有板厚信息
        Args:
        Example:
            odb.get_thickness_data(1)
        Returns:
            包含信息为dict
        """
        payload = {"thick_id": thick_id}
        return QtServer.send_get("GET-THICKNESS-DATA", payload)

    @staticmethod
    def get_all_thickness_data():
        """
        获取所有板厚信息
        Args:
        Example:
            odb.get_all_thickness_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_get("GET-ALL-THICKNESS-DATA", None)
    # endregion


    # region 获取施工阶段信息
    @staticmethod
    def get_stage_name():
        """
        获取所有施工阶段名称
        Args: 无
        Example:
            odb.get_stage_name()
        Returns: 包含信息为list[int]
        """
        return QtServer.send_get("GET-STAGE-NAMES", None)

    @staticmethod
    def get_elements_of_stage(stage_id: int):
        """
        获取指定施工阶段单元编号信息
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_elements_of_stage(stage_id=1)
        Returns: 包含信息为list[int]
        """
        payload = {"stage_id": stage_id}
        return QtServer.send_get("GET-ELEMENTS-OF-STAGE", payload)

    @staticmethod
    def get_nodes_of_stage(stage_id: int):
        """
        获取指定施工阶段节点编号信息
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_nodes_of_stage(stage_id=1)
        Returns: 包含信息为list[int]
        """
        payload = {"stage_id": stage_id}
        return QtServer.send_get("GET-NODES-OF-STAGE", payload)

    @staticmethod
    def get_groups_of_stage(stage_id: int):
        """
        获取施工阶段结构组、边界组、荷载组名集合
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_groups_of_stage(stage_id=1)
        Returns: 包含信息为dict
        """
        payload = {"stage_id": stage_id}
        return QtServer.send_get("GET-GROUPS-OF-STAGE", payload)
    # endregion