from __main__ import qt_model
from .model_keyword import *


class Mdb:
    def __int__(self):
        self.initial_model()

    @staticmethod
    def initial_model():
        """
        初始化模型
        :return: None
        """
        qt_model.Initial()

    @staticmethod
    def add_structure_group(name="", index=-1):
        """
        添加结构组
        :param name: 结构组名
        :param index: 结构组编号(非必须参数)，默认自动识别当前编号(即max_id+1)
        :return: None
        """
        qt_model.AddStructureGroup(name=name, id=index)

    @staticmethod
    def remove_structure_group(name="", index=-1):
        """
        可根据结构与组名或结构组编号删除结构组，如组名和组编号均为默认则删除所有结构组
        :param name: 结构组名(非必须参数)
        :param index: 结构组编号(非必须参数)
        :return:
        """
        if index != -1:
            qt_model.RemoveStructureGroup(id=index)
        elif name != "":
            qt_model.RemoveStructureGroup(name=name)
        else:
            qt_model.RemoveAllStructureGroup()

    @staticmethod
    def add_group_structure(name="", node_ids=None, element_ids=None):
        """
        为结构组添加节点和/或单元
        :param name: 结构组名
        :param node_ids: 节点编号列表(非必选参数)
        :param element_ids: 单元编号列表(非必选参数)
        :return:
        """
        qt_model.AddStructureToGroup(name=name, nodeIds=node_ids, elementIds=element_ids)

    @staticmethod
    def remove_group_structure(name="", node_ids=None, element_ids=None):
        """
        为结构组删除节点和/或单元
        :param name: 结构组名
        :param node_ids: 节点编号列表(非必选参数)
        :param element_ids: 单元编号列表(非必选参数)
        :return:
        """
        qt_model.RemoveStructureOnGroup(name=name, nodeIds=node_ids, elementIds=element_ids)

    @staticmethod
    def add_boundary_group(name="", index=-1):
        """
        新建边界组
        :param name:边界组名
        :param index:边界组编号，默认自动识别当前编号 (非必选参数)
        :return:
        """
        qt_model.AddBoundaryGroup(name=name, id=index)

    @staticmethod
    def remove_boundary_group(name=""):
        """
        按照名称删除边界组
        :param name: 边界组名称，默认删除所有边界组 (非必须参数)
        :return:
        """
        if name != "":
            qt_model.RemoveBoundaryGroup(name)
        else:
            qt_model.RemoveAllBoundaryGroup()

    @staticmethod
    def remove_boundary(group_name="", boundary_type=-1, index=1):
        """
        根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息
        :param group_name: 边界组名
        :param boundary_type: 边界类型
        :param index: 边界编号
        :return:
        """
        if group_name == "":
            qt_model.RemoveAllBoundary()

    @staticmethod
    def add_tendon_group(name="", index=-1):
        """
        按照名称添加钢束组，添加时可指定钢束组id
        :param name: 钢束组名称
        :param index: 钢束组编号(非必须参数)，默认自动识别(即max_id+1)
        :return:
        """
        qt_model.AddTendonGroup(name=name, id=index)

    @staticmethod
    def remove_tendon_group(name="", index=-1):
        """
        按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组
        :param name:钢束组名称,默认自动识别 (可选参数)
        :param index:钢束组编号,默认自动识别 (可选参数)
        :return:
        """
        if name != "":
            qt_model.RemoveTendonGroup(name=name)
        elif index != -1:
            qt_model.RemoveTendonGroup(id=index)
        else:
            qt_model.RemoveAllStructureGroup()

    @staticmethod
    def add_load_group(name="", index=-1):
        """
        根据荷载组名称添加荷载组
        :param name: 荷载组名称
        :param index: 荷载组编号，默认自动识别 (可选参数)
        :return:
        """
        if name != "":
            qt_model.AddLoadGroup(name=name, id=index)

    @staticmethod
    def remove_load_group(name="", index=-1):
        """
        根据荷载组名称或荷载组id删除荷载组,参数为默认时删除所有荷载组
        :param name: 荷载组名称
        :param index: 荷载组编号
        :return:
        """
        if name != "":
            qt_model.RemoveLoadGroup(name=name)
        elif index != -1:
            qt_model.RemoveLoadGroup(id=index)
        else:
            qt_model.RemoveAllLoadGroup()

    @staticmethod
    def add_node(x=1, y=1, z=1, index=-1):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        :param x: 节点坐标x
        :param y: 节点坐标y
        :param z: 节点坐标z
        :param index: 节点编号，默认自动识别编号 (可选参数)
        :return:
        """
        if index != -1:
            qt_model.AddNode(id=index, x=x, y=y, z=z)
        else:
            qt_model.AddNode(x=x, y=y, z=z)

    @staticmethod
    def add_nodes(node_list):
        """
        添加多个节点，可以选择指定节点编号
        :param node_list:节点坐标信息 [[x1,y1,z1],...]或 [[id1,x1,y1,z1]...]
        :return:
        """
        qt_model.AddNodes(dataList=node_list)

    @staticmethod
    def add_element(index=1, ele_type=1, node_ids=None, beta_angle=0, mat_id=-1, sec_id=-1):
        """
        根据单元编号和单元类型添加单元
        :param index:单元编号
        :param ele_type:单元类型 1-梁 2-索 3-杆 4-板
        :param node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]
        :param beta_angle:贝塔角
        :param mat_id:材料编号
        :param sec_id:截面编号
        :return:
        """
        if ele_type == 1:
            qt_model.AddBeam(id=index, idI=node_ids[0], idJ=node_ids[1], betaAngle=beta_angle, materialId=mat_id, sectionId=sec_id)
        elif index == 2:
            qt_model.AddCable(id=index, idI=node_ids[0], idJ=node_ids[1], betaAngle=beta_angle, materialId=mat_id, sectionId=sec_id)
        elif sec_id == 3:
            qt_model.AddLink(id=index, idI=node_ids[0], idJ=node_ids[1], betaAngle=beta_angle, materialId=mat_id, sectionId=sec_id)
        else:
            qt_model.AddPlate(id=index, idI=node_ids[0], idJ=node_ids[1], idK=node_ids[2], idL=node_ids[3], betaAngle=beta_angle,
                              materialId=mat_id,
                              sectionId=sec_id)

    @staticmethod
    def add_material(index=-1, name="", material_type="混凝土", standard_name="公路18规范", database="C50", construct_factor=1,
                     modified=False, modify_info=None):
        """
        添加材料
        :param index:材料编号,默认自动识别 (可选参数)
        :param name:材料名称
        :param material_type: 材料类型
        :param standard_name:规范名称
        :param database:数据库
        :param construct_factor:构造系数
        :param modified:是否修改默认材料参数,默认不修改 (可选参数)
        :param modify_info:材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (可选参数)
        :return:
        """
        if modified and len(modify_info) != 4:
            raise OperationFailedException("操作错误,modify_info数据无效!")
        if modified:
            qt_model.AddMaterial(id=index, name=name, materialType=material_type, standardName=standard_name,
                                 database=database, constructFactor=construct_factor, isModified=modified)
        else:
            qt_model.AddMaterial(id=index, name=name, materialType=material_type, standardName=standard_name,
                                 database=database, constructFactor=construct_factor, isModified=modified,
                                 elasticModulus=modify_info[0], unitWeight=modify_info[1],
                                 posiRatio=modify_info[2], tempratureCoefficient=modify_info[3])

    @staticmethod
    def add_time_material(index=-1, name="", code_index=1, time_parameter=None):
        """
        添加收缩徐变材料
        :param index:收缩徐变编号,默认自动识别 (可选参数)
        :param name:收缩徐变名
        :param code_index:收缩徐变规范索引
        :param time_parameter:对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)
        :return:
        """
        if time_parameter is None:  # 默认不修改收缩徐变相关参数
            qt_model.AddTimeParameter(id=index, name=name, codeId=code_index)
        elif code_index == 1:  # 公规 JTG 3362-2018
            if len(time_parameter) != 4:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, rh=time_parameter[0], bsc=time_parameter[1],
                                      timeStart=time_parameter[2], flyashCotent=time_parameter[3])
        elif code_index == 2:  # 公规 JTG D62-2004
            if len(time_parameter) != 3:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, rh=time_parameter[0], bsc=time_parameter[1],
                                      timeStart=time_parameter[2])
        elif code_index == 3:  # 公规 JTJ 023-85
            if len(time_parameter) != 4:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, creepBaseF1=time_parameter[0], creepNamda=time_parameter[1],
                                      shrinkSpeek=time_parameter[2], shrinkEnd=time_parameter[3])
        elif code_index == 4:  # 铁规 TB 10092-2017
            if len(time_parameter) != 5:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, rh=time_parameter[0], creepBaseF1=time_parameter[1],
                                      creepNamda=time_parameter[2], shrinkSpeek=time_parameter[3], shrinkEnd=time_parameter[4])
        elif code_index == 5:  # 地铁 GB 50157-2013
            if len(time_parameter) != 3:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, rh=time_parameter[0], shrinkSpeek=time_parameter[1],
                                      shrinkEnd=time_parameter[2])
        elif code_index == 6:  # 老化理论
            if len(time_parameter) != 4:
                raise OperationFailedException("操作错误,time_parameter数据无效!")
            qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, creepEnd=time_parameter[0], creepSpeek=time_parameter[1],
                                      shrinkSpeek=time_parameter[2], shrinkEnd=time_parameter[3])

    @staticmethod
    def update_material_creep(index=1, creep_id=1, f_cuk=0):
        """
        将收缩徐变参数连接到材料
        :param index: 材料编号
        :param creep_id: 收缩徐变编号
        :param f_cuk: 材料标准抗压强度,仅自定义材料是需要输入
        :return:
        """
        qt_model.UpdateMaterialCreep(materialId=index, timePatameterId=creep_id, fcuk=f_cuk)

    @staticmethod
    def remove_material(index=-1):
        if index == -1:
            qt_model.RemoveAllMaterial()
        else:
            qt_model.RemoveMaterial(id=index)

    @staticmethod
    def add_section(index=-1, name="", section_type=JX, sec_info=None,
                    bias_type="中心", center_type="质心", shear_consider=True, bias_point=None):
        """
        添加截面信息
        :param index: 截面编号,默认自动识别
        :param name:
        :param section_type:
        :param sec_info:
        :param bias_type:
        :param center_type:
        :param shear_consider:
        :param bias_point:
        :return:
        """
        if center_type == "自定义":
            if len(bias_point) != 2:
                raise OperationFailedException("操作错误,bias_point数据无效!")
            qt_model.AddSection(id=index, name=name, secType=section_type, secInfo=sec_info, biasType=bias_type, centerType=center_type,
                                shearConsider=shear_consider, horizontalPos=bias_point[0], verticalPos=bias_point[1])
        else:
            qt_model.AddSection(id=index, name=name, secType=section_type, secInfo=sec_info, biasType=bias_type, centerType=center_type,
                                shearConsider=shear_consider)

    @staticmethod
    def add_single_box(index=-1, name="", n=1, h=4, section_info=None, charm_info=None, section_info2=None, charm_info2=None,
                       bias_type="中心", center_type="质心", shear_consider=True, bias_point=None):
        """
        添加单项多室混凝土截面
        :param index:
        :param name:
        :param n:
        :param h:
        :param section_info:
        :param charm_info:
        :param section_info2:
        :param charm_info2:
        :param bias_type:
        :param center_type:
        :param shear_consider:
        :param bias_point:
        :return:
        """
        if center_type == "自定义":
            if len(bias_point) != 2:
                raise OperationFailedException("操作错误,bias_point数据无效!")
            qt_model.AddSingleBoxSection(id=index, name=name, N=n, H=h, secInfo=section_info, charmInfo=charm_info,
                                         secInfoR=section_info2, charmInfoR=charm_info2, biasType=bias_type, centerType=center_type,
                                         shearConsider=shear_consider, horizontalPos=bias_point[0], verticalPos=bias_point[1])
        else:
            qt_model.AddSingleBoxSection(id=index, name=name, N=n, H=h, secInfo=section_info, charmInfo=charm_info,
                                         secInfoR=section_info2, charmInfoR=charm_info2, biasType=bias_type, centerType=center_type,
                                         shearConsider=shear_consider)

    @staticmethod
    def add_steel_section(index=-1, name="", section_type=GGL, section_info=None, rib_info=None, rib_place=None,
                          bias_type="中心", center_type="质心", shear_consider=True, bias_point=None):
        """
        添加钢梁截面,包括参数型钢梁截面和自定义带肋钢梁截面
        :param index:
        :param name:
        :param section_type:
        :param section_info:
        :param rib_info:
        :param rib_place:
        :param bias_type:
        :param center_type:
        :param shear_consider:
        :param bias_point:
        :return:
        """
        if center_type == "自定义":
            if len(bias_point) != 2:
                raise OperationFailedException("操作错误,bias_point数据无效!")
            qt_model.AddSteelSection(id=index, name=name, type=section_type, sectionInfoList=section_info, ribInfoList=rib_info,
                                     ribPlaceList=rib_place, baisType=bias_type, centerType=center_type,
                                     shearConsider=shear_consider, horizontalPos=bias_point[0], verticalPos=bias_point[1])
        else:
            qt_model.AddSteelSection(id=index, name=name, type=section_type, sectionInfoList=section_info, ribInfoList=rib_info,
                                     ribPlaceList=rib_place, baisType=bias_type, centerType=center_type,
                                     shearConsider=shear_consider)

    @staticmethod
    def add_user_section(index=-1, name="", section_type="特性截面", property_info=None):
        """
        添加自定义截面,目前仅支持特性截面
        :param index:
        :param name:
        :param section_type:
        :param property_info:
        :return:
        """
        qt_model.AddUserSection(id=index, name=name, type=section_type, propertyInfo=property_info)

    @staticmethod
    def add_tapper_section(index=-1, name="", begin_id=1, end_id=1, vary_info=None):
        """
        添加变截面,需先建立单一截面
        :param index:
        :param name:
        :param begin_id:
        :param end_id:
        :param vary_info:
        :return:
        """
        if vary_info is not None:
            if len(vary_info) != 2:
                raise OperationFailedException("操作错误,vary_info数据无效!")
            qt_model.AddTaperSection(id=index, name=name, beginId=begin_id, endId=end_id,
                                     varyParameterWidth=vary_info[0], varyParameterHeight=vary_info[1])
        else:
            qt_model.AddTaperSection(id=index, name=name, beginId=begin_id, endId=end_id)

    @staticmethod
    def remove_section(index=-1):
        """
        删除截面信息
        :param index: 截面编号,参数为默认时删除全部截面
        :return:
        """
        if index == -1:
            qt_model.RemoveAllSection()
        else:
            qt_model.RemoveSection(id=index)

    @staticmethod
    def add_thickness(index=-1, name="", t=0, thick_type=0, bias_info=None,
                      rib_pos=0, dist_v=0, dist_l=0, rib_v=None, rib_l=None):
        """
        添加板厚
        :param index: 板厚id
        :param name: 板厚名称
        :param t:   板厚度
        :param thick_type: 板厚类型 0-普通板 1-加劲肋板
        :param bias_info:  默认不偏心,偏心时输入列表[type,value] type:0-厚度比 1-数值
        :param rib_pos:肋板位置
        :param dist_v:纵向截面肋板间距
        :param dist_l:横向截面肋板间距
        :param rib_v:纵向肋板信息
        :param rib_l:横向肋板信息
        :return:
        """
        if bias_info is None:
            qt_model.AddThickness(id=index, name=name, t=t, type=thick_type, isBiased=False, ribPos=rib_pos,
                                  verticalDis=dist_v, lateralDis=dist_l, verticalRib=rib_v, lateralRib=rib_l)
        else:
            qt_model.AddThickness(id=index, name=name, t=t, type=thick_type, isBiased=False, ribPos=rib_pos,
                                  offSetType=bias_info[0], offSetValue=bias_info[1],
                                  verticalDis=dist_v, lateralDis=dist_l, verticalRib=rib_v, lateralRib=rib_l)

    @staticmethod
    def remove_thickness(index=-1):
        """
        删除板厚
        :param index:板厚编号,默认时删除所有板厚信息
        :return:
        """
        if index == -1:
            qt_model.RemoveAllThickness()
        else:
            qt_model.RemoveThickness(id=index)

    @staticmethod
    def add_tapper_section_group(ids=None, name="", factor_w=1.0, factor_h=1.0, ref_w=0, ref_h=0, dis_w=0, dis_h=0):
        """
        添加变截面组
        :param ids:变截面组编号
        :param name: 变截面组名
        :param factor_w: 宽度方向变化阶数 线性(1.0) 非线性(!=1.0)
        :param factor_h: 高度方向变化阶数 线性(1.0) 非线性(!=1.0)
        :param ref_w: 宽度方向参考点 0-i 1-j
        :param ref_h: 高度方向参考点 0-i 1-j
        :param dis_w: 宽度方向间距
        :param dis_h: 高度方向间距
        :return:
        """
        qt_model.AddTapperSectionGroup(ids=ids, name=name, factorW=factor_w, factorH=factor_h, w=ref_w, h=ref_h, disW=dis_w, disH=dis_h)

    @staticmethod
    def update_section_bias(index=1, bias_type="中心", center_type="质心", shear_consider=True, bias_point=None):
        """
        更新截面偏心
        :param index:
        :param bias_type:
        :param center_type:
        :param shear_consider:
        :param bias_point:
        :return:
        """
        if center_type == "自定义":
            if len(bias_point) != 2:
                raise OperationFailedException("操作错误,bias_point数据无效!")
            qt_model.UpdateSectionBias(id=index, biasType=bias_type, centerType=center_type,
                                       shearConsider=shear_consider, horizontalPos=bias_point[0], verticalPos=bias_point[1])
        else:
            qt_model.UpdateSectionBias(id=index, biasType=bias_type, centerType=center_type,
                                       shearConsider=shear_consider)

    @staticmethod
    def add_general_support(index=-1, node_id=1, boundary_info=None, group_name="默认边界组", node_system=0):
        pass

    @staticmethod
    def test_print():
        print(1)


class OperationFailedException(Exception):
    """用户操作失败时抛出的异常"""
    pass
