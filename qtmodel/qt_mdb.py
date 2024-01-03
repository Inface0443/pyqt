from __main__ import mdb
from .model_keyword import *


class Mdb:
    @staticmethod
    def initial_model():
        """
        初始化模型
        :return: None
        """
        mdb.Initial()

    @staticmethod
    def add_structure_group(name="", group_id=-1):
        """
        添加结构组
        :param name: 结构组名
        :param group_id: 结构组编号(非必须参数)，默认自动识别当前编号(即max_id+1)
        :return: None
        """
        mdb.AddStructureGroup(name, group_id)

    @staticmethod
    def remove_structure_group(name="", group_id=-1):
        """
        可根据结构与组名或结构组编号删除结构组，如组名和组编号均为默认则删除所有结构组
        :param name: 结构组名(非必须参数)
        :param group_id: 结构组编号(非必须参数)
        :return:
        """
        if group_id != -1:
            mdb.RemoveStructureGroup(group_id)
        elif name != "":
            mdb.RemoveStructureGroup(name)
        else:
            mdb.RemoveAllStructureGroup()

    @staticmethod
    def add_group_structure(name="", node_ids=None, element_ids=None):
        """
        为结构组添加节点和/或单元
        :param name: 结构组名
        :param node_ids: 节点编号列表(非必选参数)
        :param element_ids: 单元编号列表(非必选参数)
        :return:
        """
        mdb.AddStructureToGroup(name, node_ids, element_ids)

    @staticmethod
    def remove_group_structure(name="", node_ids=None, element_ids=None):
        """
        为结构组删除节点和/或单元
        :param name: 结构组名
        :param node_ids: 节点编号列表(非必选参数)
        :param element_ids: 单元编号列表(非必选参数)
        :return:
        """
        mdb.RemoveStructureOnGroup(name, node_ids, element_ids)

    @staticmethod
    def add_boundary_group(name="", group_id=-1):
        """
        新建边界组
        :param name:边界组名
        :param group_id:边界组编号(非必选参数)，默认自动识别当前编号(即max_id+1)
        :return:
        """
        mdb.AddBoundaryGroup(name, group_id)

    @staticmethod
    def remove_boundary_group(name=""):
        """
        按照名称删除边界组
        :param name: 边界组名称(非必须参数)，默认删除所有边界组
        :return:
        """
        if name != "":
            mdb.RemoveBoundaryGroup(name)
        else:
            mdb.RemoveAllBoundaryGroup()

    @staticmethod
    def remove_boundary(group_name="", boundary_type=-1, boundary_id=1):
        """
        根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息
        :param group_name: 边界组名
        :param boundary_type: 边界类型
        :param boundary_id: 边界编号
        :return:
        """
        if group_name == "":
            mdb.RemoveAllBoundary()

    @staticmethod
    def add_tendon_group(name="", group_id=-1):
        """
        按照名称添加钢束组，添加时可指定钢束组id
        :param name: 钢束组名称
        :param group_id: 钢束组编号(非必须参数)，默认自动识别(即max_id+1)
        :return:
        """
        mdb.AddTendonGroup(name, group_id)

    @staticmethod
    def remove_tendon_group(name="", group_id=-1):
        """
        按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组
        :param name:钢束组名称(非必须参数)
        :param group_id:钢束组编号(非必须参数)
        :return:
        """
        if name != "":
            mdb.RemoveTendonGroup(name)
        elif group_id != -1:
            mdb.RemoveTendonGroup(group_id)
        else:
            mdb.RemoveAllStructureGroup()

    @staticmethod
    def add_load_group(name="", group_id=-1):
        """
        根据荷载组名称添加荷载组
        :param name: 荷载组名称
        :param group_id: 荷载组编号(非必须参数)，默认自动识别(即max_id+1)
        :return:
        """
        if name != "":
            mdb.AddLoadGroup(name, group_id)

    @staticmethod
    def remove_load_group(name="", group_id=-1):
        """
        根据荷载组名称或荷载组id删除荷载组,参数为默认时删除所有荷载组
        :param name: 荷载组名称
        :param group_id: 荷载组编号
        :return:
        """
        if name != "":
            mdb.RemoveLoadGroup(name)
        elif group_id != -1:
            mdb.RemoveLoadGroup(group_id)
        else:
            mdb.RemoveAllLoadGroup()

    @staticmethod
    def add_node(x=1, y=1, z=1, node_id=-1):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        :param x: 节点坐标x
        :param y: 节点坐标y
        :param z: 节点坐标z
        :param node_id: 节点编号，默认自动识别编号
        :return:
        """
        if node_id != -1:
            mdb.AddNode(node_id, x, y, z)
        else:
            mdb.AddNode(x, y, z)

    @staticmethod
    def add_nodes(node_list):
        """
        添加多个节点，可以选择指定节点编号
        :param node_list:节点坐标信息 [[x1,y1,z1],...]或 [[id1,x1,y1,z1]...]
        :return:
        """
        mdb.AddNodes(node_list)

    @staticmethod
    def add_element(ele_id=1, ele_type=1, node_ids=None, beta_angle=0, mat_id=-1, sec_id=-1):
        """
        根据单元编号和单元类型添加单元
        :param ele_id:单元编号
        :param ele_type:单元类型 1-梁 2-索 3-杆 4-板
        :param node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]
        :param beta_angle:贝塔角
        :param mat_id:材料编号
        :param sec_id:截面编号
        :return:
        """
        if ele_type == 1:
            mdb.AddBeam(ele_id, node_ids[0], node_ids[1], beta_angle, mat_id, sec_id)
        elif ele_id == 2:
            mdb.AddCable(ele_id, node_ids[0], node_ids[1], beta_angle, mat_id, sec_id)
        elif sec_id == 3:
            mdb.AddLink(ele_id, node_ids[0], node_ids[1], beta_angle, mat_id, sec_id)
        else:
            mdb.AddPlate(ele_id, node_ids[0], node_ids[1], node_ids[2], node_ids[3], beta_angle, mat_id, sec_id)


    # @staticmethod
    #     # def update_ele_material():