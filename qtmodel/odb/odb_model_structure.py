from qtmodel.core.qt_server import QtServer
from qtmodel.core.data_helper import QtDataHelper
from qtmodel.core.model_db import Node


class OdbModelStructure:
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
        return QtServer.send_dict("GET-OVERLAP-NODES", payload)

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
        return QtServer.send_dict("GET-NODE-ID", payload)

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
        return QtServer.send_dict("GET-GROUP-NODES", payload)

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
        json_str = QtServer.send_dict("GET-NODE-DATA", payload)
        nodes = Node.from_json(json_str)
        return Node.to_json(nodes)

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
        return QtServer.send_dict("GET-ELEMENTS-BY-POINT", payload)

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
        return QtServer.send_dict("GET-ELEMENTS-BY-MATERIAL", payload)

    @staticmethod
    def get_element_by_section(index: int = 1):
        """
        获取某一截面相应的单元
        Args:
            index:截面编号
        Example:
            odb.get_element_by_section(index=1)
        Returns: 包含信息为list[int]
        """
        payload = {"index": index}
        return QtServer.send_dict("GET-ELEMENTS-BY-SECTION", payload)

    @staticmethod
    def get_overlap_elements():
        """
        获取重合节点
        Args:无
        Example:
            odb.get_overlap_elements()
        Returns:  包含信息为list[list[int]]
        """
        return QtServer.send_dict("GET-OVERLAP-ELEMENTS", None)

    @staticmethod
    def get_structure_group_names():
        """
        获取结构组名称
        Args:无
        Example:
            odb.get_structure_group_names()
        Returns: 包含信息为list[str]
        """
        return QtServer.send_dict("GET-STRUCTURE-GROUP-NAMES", None)

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
        return QtServer.send_dict("GET-ELEMENT-DATA", payload)

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
        return QtServer.send_dict("GET-ELEMENT-TYPE", payload)

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
        return QtServer.send_dict("GET-GROUP-ELEMENTS", payload)

    @staticmethod
    def get_element_weight(ids=None):
        """
        根据单元编号获取单元重量
        Args:
            ids: 单元编号支持整数或整数列表且支持XtoYbyN形式字符串，默认获取所有单元重量
        Example:
            odb.get_element_weight(ids=1)
        Returns: dict<int,double>类型的json格式字符串
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)}
        return QtServer.send_dict("GET-ELEMENT-WEIGHT", payload)
    # endregion

    # region 跨度信息
    @staticmethod
    def get_span_supports(span_info_name: str = ""):
        """
        获取跨度信息的支承节点号
        Args:
            span_info_name: 跨度信息名
        Example:
            odb.get_span_supports(span_info_name="跨度")
        Returns: list[int]
        """
        payload = {"span_info_name": span_info_name}
        return QtServer.send_dict("GET-SPAN-SUPPORTS", payload)

    @staticmethod
    def get_span_elements(span_info_name: str = ""):
        """
        获取跨度信息的支承节点号
        Args:
            span_info_name: 跨度信息名
        Example:
            odb.get_span_elements(span_info_name="跨度")
        Returns: list[int]
        """
        payload = {"span_name": span_info_name}
        return QtServer.send_dict("GET-SPAN-ELEMENTS", payload)
    # endregion