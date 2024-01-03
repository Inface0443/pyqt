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

    @staticmethod
    def add_material(material_id=-1, name="", material_type="混凝土", standard_name="公路18规范", database="C50", construct_factor=1,
                     modified=False, modify_info=None):
        if modified and len(modify_info) != 4:
            raise OperationFailedException("操作错误,modify_info数据无效!")
        if modified:
            mdb.AddMaterial(id=material_id, name=name, materialType=material_type, standardName=standard_name,
                            database=database, constructFactor=construct_factor, isModified=modified)
        else:
            mdb.AddMaterial(id=material_id, name=name, materialType=material_type, standardName=standard_name,
                            database=database, constructFactor=construct_factor, isModified=modified,
                            elasticModulus=modify_info[0], unitWeight=modify_info[1],
                            posiRatio=modify_info[2], tempratureCoefficient=modify_info[3])

    @staticmethod
    def add_time_material(creep_id=-1, name="", code_index=1, time_parameter=None):
        if time_parameter is None:  # 默认不修改收缩徐变相关参数
            mdb.AddTimeParameter(id=creep_id, name=name, codeId=code_index)
        elif code_index == 1:  # 公规 JTG 3362-2018
            if len(time_parameter) != 4:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            mdb.AddTimeParameter(id=creep_id, name=name, codeId=code_index, rh=time_parameter[0], bsc=time_parameter[1],
                                 timeStart=time_parameter[2], flyashCotent=time_parameter[3])
        elif code_index == 2:  # 公规 JTG D62-2004
            if len(time_parameter) != 3:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            mdb.AddTimeParameter(id=creep_id, name=name, codeId=code_index, rh=time_parameter[0], bsc=time_parameter[1],
                                 timeStart=time_parameter[2])
        elif code_index == 3:  # 公规 JTJ 023-85
            if len(time_parameter) != 4:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            mdb.AddTimeParameter(id=creep_id, name=name, codeId=code_index, creepBaseF1=time_parameter[0], creepNamda=time_parameter[1],
                                 shrinkSpeek=time_parameter[2], shrinkEnd=time_parameter[3])
        elif code_index == 4:  # 铁规 TB 10092-2017
            if len(time_parameter) != 5:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            mdb.AddTimeParameter(id=creep_id, name=name, codeId=code_index, rh=time_parameter[0], creepBaseF1=time_parameter[1],
                                 creepNamda=time_parameter[2], shrinkSpeek=time_parameter[3], shrinkEnd=time_parameter[4])
        elif code_index == 5:  # 地铁 GB 50157-2013
            if len(time_parameter) != 3:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            mdb.AddTimeParameter(id=creep_id, name=name, codeId=code_index, rh=time_parameter[0], shrinkSpeek=time_parameter[1],
                                 shrinkEnd=time_parameter[2])
        elif code_index == 6:  # 老化理论
            if len(time_parameter) != 4:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            mdb.AddTimeParameter(id=creep_id, name=name, codeId=code_index, creepEnd=time_parameter[0], creepSpeek=time_parameter[1],
                                 shrinkSpeek=time_parameter[2], shrinkEnd=time_parameter[3])

    @staticmethod
    def update_material_creep(material_id=1, creep_id=1, f_cuk=0):
        mdb.UpdateMaterialCreep(materialId=material_id, timePatameterId=creep_id, fcuk=f_cuk)

    @staticmethod
    def remove_material(material_id=-1):
        if material_id == -1:
            mdb.RemoveAllMaterial()
        else:
            mdb.RemoveMaterial(id=material_id)

    @staticmethod
    def add_section(section_id=-1, name="", section_type=JX, sec_info=None,
                    bias_type="中心", center_type="质心", shear_consider=True, bias_point=None):
        if center_type == "自定义":
            if len(bias_point) != 2:
                raise OperationFailedException("操作错误,bias_point数据无效!")
            mdb.AddSection(id=section_id, name=name, secType=section_type, secInfo=sec_info, biasType=bias_type, centerType=center_type,
                           shearConsider=shear_consider, horizontalPos=bias_point[0], verticalPos=bias_point[1])
        else:
            mdb.AddSection(id=section_id, name=name, secType=section_type, secInfo=sec_info, biasType=bias_type, centerType=center_type,
                           shearConsider=shear_consider)

    @staticmethod
    def add_single_box(section_id=-1, name="", n=1, h=4, section_info=None, charm_info=None, section_info2=None, charm_info2=None,
                       bias_type="中心", center_type="质心", shear_consider=True, bias_point=None):
        if center_type == "自定义":
            if len(bias_point) != 2:
                raise OperationFailedException("操作错误,bias_point数据无效!")
            mdb.AddSingleBoxSection(id=section_id, name=name, N=n, H=h, secInfo=section_info, charmInfo=charm_info,
                                    secInfoR=section_info2, charmInfoR=charm_info2, biasType=bias_type, centerType=center_type,
                                    shearConsider=shear_consider)
        else:
            mdb.AddSingleBoxSection(id=section_id, name=name, N=n, H=h, secInfo=section_info, charmInfo=charm_info,
                                    secInfoR=section_info2, charmInfoR=charm_info2, biasType=bias_type, centerType=center_type,
                                    shearConsider=shear_consider, horizontalPos=bias_point[0], verticalPos=bias_point[1])

    @staticmethod
    def add_user_section(section_id=-1, name="", section_type="特性截面", property_info=None):
        mdb.AddUserSection(id=section_id, name=name, type=section_type, propertyInfo=property_info)

    @staticmethod
    def add_tapper_section(section_id=-1, name="", begin_id=1, end_id=1, vary_info=None):
        if vary_info is not None:
            if len(vary_info) != 2:
                raise OperationFailedException("操作错误,vary_info数据无效!")
            mdb.AddTaperSection(id=section_id, name=name, beginId=begin_id, endId=end_id,
                                varyParameterWidth=vary_info[0], varyParameterHeight=vary_info[1])
        else:
            mdb.AddTaperSection(id=section_id, name=name, beginId=begin_id, endId=end_id)

    @staticmethod
    def remove_section(section_id=-1):
        if section_id == -1:
            mdb.RemoveAllSection()
        else:
            mdb.RemoveSection(id=section_id)


class OperationFailedException(Exception):
    """用户操作失败时抛出的异常"""
    pass
