import json

from ..core.qt_server import QtServer
from .data_helper import MdbDataHelper
from typing import Union, List

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
        try:
            # s = "*NODE\r\n" + "\r\n".join(",".join(f"{x:g}" for x in row) for row in node_data) + "\r\n"
            # if QtServer.QT_MERGE :
            #     QtServer.MERGE_STR += s
            # else:
            #     QtServer.post_command(s,"QDAT")
            # print(s)
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "node_data": node_data,
                "intersected": intersected,
                "is_merged": is_merged,
                "merge_error": merge_error,
                "numbering_type": numbering_type,
                "start_id": start_id
            }
            json_string = json.dumps(params, indent=2)
            QtServer.get_command(header="ADD-NODES", command=json_string)
        except Exception as ex:
            raise Exception(ex)

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
            sec_id:截面编号
            initial_type:索单元初始参数类型 1-初始拉力 2-初始水平力 3-无应力长度
            initial_value:索单元初始始参数值
            plate_type:板单元类型  0-薄板 1-厚板
        Example:
            mdb.add_element(index=1,ele_type=1,node_ids=[1,2],beta_angle=1,mat_id=1,sec_id=1)
        Returns: 无
        """
        try:
            if node_ids is None and ele_type != 4:
                raise Exception("操作错误,请输入此单元所需节点列表,[i,j]")
            if node_ids is None and ele_type == 4:
                raise Exception("操作错误,请输入此板单元所需节点列表,[i,j,k,l]")
            s = "*ELEMENT\r\n"
            if ele_type in (1,2):   # 1-梁 2-杆
                s += f"{index},{ele_type},{mat_id},{sec_id},{beta_angle},{node_ids[0]},{node_ids[1]}" + "\r\n"
            elif ele_type == 3: # 3-索
                s += f"{index},{ele_type},{mat_id},{sec_id},{beta_angle},{node_ids[0]},{node_ids[1]},{initial_type},{initial_value:g}" + "\r\n"
            elif ele_type == 4: # 4-板
                s += f"{index},{ele_type},{mat_id},{sec_id},{beta_angle},{node_ids[0]},{node_ids[1]},{node_ids[2]},{node_ids[3]},{plate_type}" + "\r\n"
            print(s)
            if QtServer.QT_MERGE:
                QtServer.MERGE_STR += s  # 开启合并发送时需要调用update_model生效
            else:
                QtServer.post_command(s,"QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_elements(ele_data: list = None):
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
        try:
            s = "*ELEMENT\r\n" + "\r\n".join(",".join(str(x) for x in row) for row in ele_data) + "\r\n"
            print(s)
            QtServer.post_command(s,"QDAT")
        except Exception as ex:
            raise Exception(ex)

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
        try:
            if node_ids is None:
                node_str = ""
            elif isinstance(node_ids, list):    # 列表转化为XtoYbyN
                node_str = MdbDataHelper.parse_int_list_to_str(node_ids)
            else:  # 已经是XtoYbyN
                node_str = str(node_ids)

            if element_ids is None:
                elem_str = ""
            elif isinstance(element_ids, list):
                elem_str = MdbDataHelper.parse_int_list_to_str(element_ids)
            else:
                elem_str = str(element_ids)

            s = "*STRGROUP\r\n" + f"{name},{node_str},{elem_str}" + "\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

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
        try:
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "name": name,
                "new_name": new_name
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.get_command(header="UPDATE-STRUCTURE-GROUP-NAME", command=json_string)
        except Exception as ex:
            raise Exception(ex)

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
        try:
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "name": name,
                "new_name": new_name,
                "node_ids": MdbDataHelper.id_to_list(node_ids),
                "element_ids": MdbDataHelper.id_to_list(element_ids)
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.get_command(header="UPDATE-STRUCTURE-GROUP", command=json_string)
        except Exception as ex:
            raise Exception(ex)

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
        try:
            if name != "":
                params = {
                    "version": QtServer.QT_VERSION,  # 版本控制
                    "name": name
                }
                json_string = json.dumps(params, indent=2, ensure_ascii=False)
                QtServer.get_command(header="REMOVE-STRUCTURE-GROUP", command=json_string)
            else:
                QtServer.post_command(header="REMOVE-ALL-STRUCTURE-GROUP")

        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_structure_to_group(name: str = "", node_ids: Union[str, list[int]] = None, element_ids: Union[str, list[int]] = None):
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
        try:
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "name": name,
                "node_ids": MdbDataHelper.id_to_list(node_ids),
                "element_ids": MdbDataHelper.id_to_list(element_ids)
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.get_command(header="ADD-STRUCTURE-TO-GROUP", command=json_string)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_structure_from_group(name: str = "", node_ids: Union[str, list[int]] = None, element_ids=None):
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
        try:
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "name": name,
                "node_ids": MdbDataHelper.id_to_list(node_ids),
                "element_ids": MdbDataHelper.id_to_list(element_ids)
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.get_command(header="REMOVE-STRUCTURE-FROM-GROUP", command=json_string)
        except Exception as ex:
            raise Exception(ex)

    # endregion