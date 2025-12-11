from qtmodel.core.qt_server import QtServer
from qtmodel.core.data_helper import QtDataHelper
from typing import Optional


class MdbStructure:
    """
    用于节点单元结构操作
    """

    # region 节点操作
    @staticmethod
    def add_nodes(node_data: list[list[float]], intersected: bool = False,
                  is_merged: bool = False, merge_error: float = 1e-3,
                  numbering_type: int = 0, start_id: int = 1):
        """
        根据坐标信息和节点编号添加一组节点，可指定节点号，或不指定节点号
        Args:
             node_data: [[id,x,y,z]...]  或[[x,y,z]...]  指定节点编号时不进行交叉分割、合并、编号等操作
             intersected: 是否交叉分割
             is_merged: 是否忽略位置重复节点
             merge_error: 合并容许误差
             numbering_type:编号方式 0-未使用的最小号码 1-最大号码加1 2-用户定义号码
             start_id:自定义节点起始编号(用户定义号码时使用)
        Example:
            mdb.add_nodes(node_data=[[1,1,2,3],[2,1,2,3]])
        Returns: 无
        """
        params = {
            "node_data": node_data,
            "intersected": intersected,
            "is_merged": is_merged,
            "merge_error": merge_error,
            "numbering_type": numbering_type,
            "start_id": start_id
        }
        QtServer.send_dict(header="ADD-NODES", payload=params)

    @staticmethod
    def update_node(node_id: int, new_id: int = -1, x: float = 1, y: float = 1, z: float = 1):
        """
        根据节点号修改节点坐标
        Args:
             node_id: 旧节点编号
             new_id: 新节点编号,默认为-1时不改变节点编号
             x: 更新后x坐标
             y: 更新后y坐标
             z: 更新后z坐标
        Example:
            mdb.update_node(node_id=1,new_id=2,x=2,y=2,z=2)
        Returns: 无
        """
        payload = {
            "node_id": node_id,
            "new_id": new_id,
            "x": x,
            "y": y,
            "z": z,
        }
        return QtServer.send_dict("UPDATE-NODE", payload)

    @staticmethod
    def update_node_id(node_id: int, new_id: int):
        """
        修改节点Id
        Args:
             node_id: 节点编号
             new_id: 新节点编号
        Example:
            mdb.update_node_id(node_id=1,new_id=2)
        Returns: 无
        """
        payload = {
            "node_id": node_id,
            "new_id": new_id,
        }
        return QtServer.send_dict("UPDATE-NODE-ID", payload)

    @staticmethod
    def merge_nodes(ids=None, tolerance: float = 1e-4):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        Args:
             ids: 合并节点集合,默认全部节点,支持列表和XtoYbyN形式字符串
             tolerance: 合并容许误差
        Example:
            mdb.merge_nodes()
        Returns: 无
        """
        if ids is None:
            # merge all nodes
            return QtServer.send_dict("MERGE-NODES")
        payload = {
            "tolerance": tolerance,
            "ids": QtDataHelper.parse_ids_to_array(ids)
        }
        return QtServer.send_dict("MERGE-NODES", payload)

    @staticmethod
    def move_nodes(ids=None, offset_x: float = 0, offset_y: float = 0, offset_z: float = 0):
        """
        移动节点坐标，默认移动所有节点
        Args:
            ids:节点号
            offset_x:X轴偏移量
            offset_y:Y轴偏移量
            offset_z:Z轴偏移量
        Example:
            mdb.move_nodes(ids=1,offset_x=1.5,offset_y=1.5,offset_z=1.5)
        Returns: 无
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "offsets": [offset_x, offset_y, offset_z]
        }
        return QtServer.send_dict("MOVE-NODES", payload)

    @staticmethod
    def remove_nodes(ids=None):
        """
        删除指定节点,默认删除所有节点
        Args:
            ids:节点编号,支持多种类型
        Example:
            mdb.remove_nodes()
            mdb.remove_nodes(ids=1)
            mdb.remove_nodes(ids=[1,2,3])
        Returns: 无
        """
        if ids is None:
            return QtServer.send_dict("REMOVE-NODES")
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)}
        return QtServer.send_dict("REMOVE-NODES", payload)

    @staticmethod
    def renumber_nodes(ids: Optional[list[int]] = None, new_ids: Optional[list[int]] = None):
        """
        节点编号重排序，默认按1升序重排所有节点
        Args:
            ids:原修改节点号
            new_ids:新节点号
        Example:
            mdb.renumber_nodes()
            mdb.renumber_nodes([7,9,22],[1,2,3])
        Returns: 无
        """
        payload = {}
        if ids is None or new_ids is None:
            return QtServer.send_dict("RENUMBER-NODES")
        if len(ids) != len(new_ids):
            raise Exception("原节点和新节点编号数据无法对应")
        payload["node_ids"] = ids
        payload["new_ids"] = new_ids
        return QtServer.send_dict("RENUMBER-NODES", payload if payload else None)

    # endregion

    # region 单元操作
    @staticmethod
    def add_element(index: int = 1, ele_type: int = 1, node_ids: list[int] = None, beta_angle: float = 0,
                    mat_id: int = -1, sec_id: int = -1, initial_type: int = 1, initial_value: float = 0, plate_type: int = 0):
        """
        根据单元编号和单元类型添加单元
        Args:
            index:单元编号
            ele_type:单元类型 1-梁 2-杆 3-索 4-板
            node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]
            beta_angle:贝塔角
            mat_id:材料编号
            sec_id:截面编号或者板厚
            initial_type:索单元初始参数类型 1-初始拉力 2-初始水平力 3-无应力长度
            initial_value:索单元初始始参数值
            plate_type:板单元类型  0-薄板 1-厚板
        Example:
            mdb.add_element(index=1,ele_type=1,node_ids=[1,2],beta_angle=1,mat_id=1,sec_id=1)
        Returns: 无
        """
        payload = {
            "index": index,
            "ele_type": ele_type,
            "node_ids": QtDataHelper.parse_ids_to_array(node_ids),
            "beta_angle": beta_angle,
            "mat_id": mat_id,
            "sec_id": sec_id,
            "initial_type": initial_type,
            "initial_value": initial_value,
            "plate_type": plate_type,
        }
        return QtServer.send_dict("ADD-ELEMENT", payload)

    @staticmethod
    def add_elements(ele_data: list[list[float]] = None):
        """
        根据单元编号和单元类型添加单元
        Args:
            ele_data:单元信息
                [编号,类型(1-梁 2-杆),materialId,sectionId,betaAngle,nodeI,nodeJ]
                [编号,类型(3-索),materialId,sectionId,betaAngle,nodeI,nodeJ,张拉类型(1-初拉力 2-初始水平力 3-无应力长度),张拉值]
                [编号,类型(4-板),materialId,thicknessId,betaAngle,nodeI,nodeJ,nodeK,nodeL,plate_type(0-薄板 1-厚板)]
        Example:
            mdb.add_elements(ele_data=[
                [1,1,1,1,0,1,2],
                [2,2,1,1,0,1,2],
                [3,3,1,1,0,1,2,1,100],
                [4,4,1,1,0,1,2,3,4,0]])
        Returns: 无
        """
        payload = {
            "ele_data": ele_data,
        }
        return QtServer.send_dict("ADD-ELEMENTS", payload)

    @staticmethod
    def revert_local_orientation(ids=None):
        """
        反转杆系单元局部方向
        Args:
            ids: 杆系单元编号,支持整形、列表、XtoYbyZ形式字符串
        Example:
            mdb.revert_local_orientation(1)
        Returns: 无
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)}
        return QtServer.send_dict("REVERT-LOCAL-ORIENTATION", payload)

    @staticmethod
    def update_element_id(old_id: int, new_id: int):
        """
        更改单元编号
        Args:
            old_id: 单元编号
            new_id: 新单元编号
        Example:
            mdb.update_element_id(1,2)
        Returns: 无
        """
        payload = {"old_id": old_id, "new_id": new_id}
        return QtServer.send_dict("UPDATE-ELEMENT-ID", payload)

    @staticmethod
    def update_element(old_id: int, new_id: int = -1, ele_type: int = 1, node_ids: list[int] = None, beta_angle: float = 0,
                       mat_id: int = -1, sec_id: int = -1, initial_type: int = 1, initial_value: float = 0, plate_type: int = 0):
        """
        根据单元编号和单元类型添加单元
        Args:
            old_id:原单元编号
            new_id:现单元编号，默认不修改原单元Id
            ele_type:单元类型 1-梁 2-杆 3-索 4-板
            node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]
            beta_angle:贝塔角
            mat_id:材料编号
            sec_id:截面编号
            initial_type:索单元初始参数类型 1-初始拉力 2-初始水平力 3-无应力长度
            initial_value:索单元初始始参数值
            plate_type:板单元类型  0-薄板 1-厚板
        Example:
            mdb.update_element(old_id=1,ele_type=1,node_ids=[1,2],beta_angle=1,mat_id=1,sec_id=1)
        Returns: 无
        """
        payload = {
            "old_id": old_id,
            "new_id": new_id,
            "ele_type": ele_type,
            "node_ids": node_ids,
            "beta_angle": beta_angle,
            "mat_id": mat_id,
            "sec_id": sec_id,
            "initial_type": initial_type,
            "initial_value": initial_value,
            "plate_type": plate_type,
        }
        return QtServer.send_dict("UPDATE-ELEMENT", payload)

    @staticmethod
    def update_element_material(ids=None, mat_id: int = 1):
        """
        更新指定单元的材料号
        Args:
            ids: 单元编号,支持整形、列表、XtoYbyZ形式字符串
            mat_id: 材料编号
        Example:
            mdb.update_element_material(ids=1,mat_id=2)
        Returns: 无
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids), "mat_id": mat_id}
        return QtServer.send_dict("UPDATE-ELEMENT-MATERIAL", payload)

    @staticmethod
    def update_element_beta(ids=None, beta: float = 0):
        """
        更新指定单元的贝塔角
        Args:
            ids: 单元编号,支持整形、列表、XtoYbyZ形式字符串
            beta: 贝塔角度数
        Example:
            mdb.update_element_beta(ids=1,beta=90)
        Returns: 无
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids), "beta_angle": beta}
        return QtServer.send_dict("UPDATE-ELEMENT-BETA", payload)

    @staticmethod
    def update_frame_section(ids, sec_id: int = 1):
        """
        更新杆系单元截面
        Args:
            ids: 单元编号,支持整形、列表、XtoYbyZ形式字符串
            sec_id: 截面号
        Example:
            mdb.update_frame_section(ids=1,sec_id=2)
        Returns: 无
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids), "sec_id": sec_id}
        return QtServer.send_dict("UPDATE-FRAME-SECTION", payload)

    @staticmethod
    def update_plate_thick(ids, thick_id: int = 1):
        """
        更新杆系单元截面
        Args:
            ids: 单元编号,支持整形、列表、XtoYbyZ形式字符串
            thick_id: 板厚号
        Example:
            mdb.update_plate_thick(ids=1,thick_id=2)
        Returns: 无
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids), "thick_id": thick_id}
        return QtServer.send_dict("UPDATE-PLATE-THICK", payload)

    @staticmethod
    def update_element_node(element_id: int, node_ids: list[int]):
        """
        更新单元节点
        Args:
            element_id: 单元编号
            node_ids: 杆系单元时为[i,j] 板单元[i,j,k,l]
        Example:
            mdb.update_element_node(1,[1,2])
            mdb.update_element_node(2,[1,2,3,4])
        Returns: 无
        """
        payload = {"element_id": element_id, "node_ids": node_ids}
        return QtServer.send_dict("UPDATE-ELEMENT-NODE", payload)

    @staticmethod
    def remove_elements(ids=None, remove_free: bool = False):
        """
        删除指定编号的单元,默认则删除所有单元
        Args:
            ids: 单元编号,支持整形、列表、XtoYbyZ形式字符串
            remove_free: 是否删除自由节点
        Example:
            mdb.remove_elements()
            mdb.remove_elements(ids=1)
        Returns: 无
        """
        if ids is None:
            # remove all elements
            return QtServer.send_dict("REMOVE-ELEMENTS")
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids), "remove_free": remove_free}
        return QtServer.send_dict("REMOVE-ELEMENTS", payload)

    @staticmethod
    def renumber_elements(element_ids: Optional[list[int]] = None, new_ids: Optional[list[int]] = None):
        """
        单元编号重排序，默认按1升序重排所有节点
        Args:
            element_ids:被修改单元号
            new_ids:新单元号
        Example:
            mdb.renumber_elements()
            mdb.renumber_elements([7,9,22],[1,2,3])
        Returns: 无
        """
        payload = {}
        if element_ids is None or new_ids is None:
            # renumber all elements
            return QtServer.send_dict("RENUMBER-ELEMENTS")
        payload["element_ids"] = element_ids
        payload["new_ids"] = new_ids
        return QtServer.send_dict("RENUMBER-ELEMENTS", payload if payload else None)

    # endregion

    # region 结构组操作
    @staticmethod
    def add_structure_group(name: str = "", node_ids=None, element_ids=None):
        """
        添加结构组
        Args:
            name: 结构组名
            node_ids: 节点编号列表,支持XtoYbyN类型字符串(可选参数)
            element_ids: 单元编号列表,支持XtoYbyN类型字符串(可选参数)
        Example:
            mdb.add_structure_group(name="新建结构组1")
            mdb.add_structure_group(name="新建结构组2",node_ids=[1,2,3,4],element_ids=[1,2])
            mdb.add_structure_group(name="新建结构组2",node_ids="1to10 11to21by2",element_ids=[1,2])
        Returns: 无
        """
        payload = {
            "name": name,
            "node_ids": QtDataHelper.parse_ids_to_array(node_ids),
            "element_ids": QtDataHelper.parse_ids_to_array(element_ids),
        }
        return QtServer.send_dict("ADD-STRUCTURE-GROUP", payload)

    @staticmethod
    def update_structure_group_name(name: str = "", new_name: str = ""):
        """
        更新结构组名
        Args:
            name: 结构组名
            new_name: 新结构组名(可选参数)
        Example:
            mdb.update_structure_group_name(name="结构组1",new_name="新结构组")
        Returns: 无
        """
        params = {
            "version": QtServer.QT_VERSION,  # 版本控制
            "name": name,
            "new_name": new_name
        }
        QtServer.send_dict("UPDATE-STRUCTURE-GROUP-NAME", params)

    @staticmethod
    def update_structure_group(name: str = "", new_name: str = "", node_ids=None, element_ids=None):
        """
        更新结构组信息
        Args:
            name: 结构组名
            new_name: 新结构组名
            node_ids: 节点编号列表,支持XtoYbyN类型字符串(可选参数)
            element_ids: 单元编号列表,支持XtoYbyN类型字符串(可选参数)
        Example:
            mdb.update_structure_group(name="结构组",new_name="新建结构组",node_ids=[1,2,3,4],element_ids=[1,2])
        Returns: 无
        """
        params = {
            "name": name,
            "new_name": new_name,
            "node_ids": QtDataHelper.parse_ids_to_array(node_ids),
            "element_ids": QtDataHelper.parse_ids_to_array(element_ids)
        }
        QtServer.send_dict("UPDATE-STRUCTURE-GROUP", params)

    @staticmethod
    def remove_structure_group(name: str = ""):
        """
        可根据结构与组名删除结构组，当组名为默认则删除所有结构组
        Args:
            name:结构组名称
        Example:
            mdb.remove_structure_group(name="新建结构组1")
            mdb.remove_structure_group()
        Returns: 无
        """
        params = {
            "version": QtServer.QT_VERSION,  # 版本控制
            "name": name
        }
        QtServer.send_dict(header="REMOVE-STRUCTURE-GROUP", payload=params)


    @staticmethod
    def add_structure_to_group(name: str = "", node_ids=None, element_ids=None):
        """
        为结构组添加节点和/或单元
        Args:
            name: 结构组名
            node_ids: 节点编号列表(可选参数)
            element_ids: 单元编号列表(可选参数)
        Example:
            mdb.add_structure_to_group(name="现有结构组1",node_ids=[1,2,3,4],element_ids=[1,2])
        Returns: 无
        """
        params = {
            "name": name,
            "node_ids": QtDataHelper.parse_ids_to_array(node_ids),
            "element_ids": QtDataHelper.parse_ids_to_array(element_ids)
        }
        QtServer.send_dict("ADD-STRUCTURE-TO-GROUP", params)

    @staticmethod
    def remove_structure_from_group(name: str = "", node_ids=None, element_ids=None):
        """
        为结构组删除节点、单元
        Args:
            name: 结构组名
            node_ids: 节点编号列表(可选参数)
            element_ids: 单元编号列表(可选参数)
        Example:
            mdb.remove_structure_from_group(name="现有结构组1",node_ids=[1,2,3,4],element_ids=[1,2])
        Returns: 无
        """
        params = {
            "name": name,
            "node_ids": QtDataHelper.parse_ids_to_array(node_ids),
            "element_ids": QtDataHelper.parse_ids_to_array(element_ids)
        }
        QtServer.send_dict("REMOVE-STRUCTURE-FROM-GROUP", params)

    # endregion
