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

    # region 组操作

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

    # endregion

    # region 节点单元操作
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
    def remove_node(index=None):
        """
        删除指定节点
        :param index:
        :return:
        """
        if index is None:
            qt_model.RemoveAllNodes()
        elif type(index) == int:
            qt_model.RemoveNode(id=index)
        else:
            qt_model.RemoveNodes(ids=index)

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
    def remove_element(index=None):
        """
        删除指定编号的单元
        :param index: 单元编号,默认时删除所有单元
        :return:
        """
        if index is None:
            qt_model.RemoveAllElements()
        else:
            qt_model.RemoveElement(index=index)

    # endregion

    # region 材料操作
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

    # endregion

    # region 截面和板厚操作
    @staticmethod
    def add_section(index=-1, name="", section_type=SEC_JX, sec_info=None,
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
    def add_steel_section(index=-1, name="", section_type=SEC_GGL, section_info=None, rib_info=None, rib_place=None,
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

    # endregion

    # region 边界操作
    @staticmethod
    def add_general_support(index=-1, node_id=1, boundary_info=None, group_name="默认边界组", node_system=0):
        """
        添加一般支承
        :param index:
        :param node_id:
        :param boundary_info:
        :param group_name:
        :param node_system:
        :return:
        """
        qt_model.AddGeneralSupport(id=index, nodeId=node_id, boundaryInfo=boundary_info, groupName=group_name, nodeSystem=node_system)

    @staticmethod
    def add_elastic_support(index=-1, node_id=1, support_type=1, boundary_info=None, group_name="默认边界组", node_system=0):
        """
        添加弹性支承
        :param index:
        :param node_id:
        :param support_type:
        :param boundary_info:
        :param group_name:
        :param node_system:
        :return:
        """
        qt_model.AddElasticSupport(id=index, nodeId=node_id, supportType=support_type, boundaryInfo=boundary_info,
                                   groupName=group_name, nodeSystem=node_system)

    @staticmethod
    def add_master_slave_link(index=-1, master_id=1, slave_id=2, boundary_info=None, group_name="默认边界组"):
        """
        添加主从约束
        :param index:
        :param master_id:
        :param slave_id:
        :param boundary_info:
        :param group_name:
        :return:
        """
        qt_model.AddMasterSlaveLink(id=index, masterId=master_id, slaveId=slave_id, boundaryInfo=boundary_info, groupName=group_name)

    @staticmethod
    def add_elastic_link(index=-1, link_type=1, start_id=1, end_id=2, beta_angle=0, boundary_info=None,
                         group_name="默认边界组", dis_ratio=0.5, kx=0):
        """
        添加弹性连接
        :param index:
        :param link_type:
        :param start_id:
        :param end_id:
        :param beta_angle:
        :param boundary_info:
        :param group_name:
        :param dis_ratio:
        :param kx:
        :return:
        """
        qt_model.AddElasticLink(id=index, linkType=link_type, startId=start_id, endId=end_id, beta=beta_angle,
                                boundaryInfo=boundary_info, groupName=group_name, disRatio=dis_ratio, kDx=kx)

    @staticmethod
    def add_beam_constraint(index=-1, beam_id=2, info_i=None, info_j=None, group_name="默认边界组"):
        """
        添加梁端约束
        :param index:约束编号,默认自动识别
        :param beam_id:梁号
        :param info_i:i端约束信息 [IsFreedX,IsFreedY,IsFreedZ,IsFreedRX,IsFreedRY,IsFreedRZ]
        :param info_j:j端约束信息 [IsFreedX,IsFreedY,IsFreedZ,IsFreedRX,IsFreedRY,IsFreedRZ]
        :param group_name:边界组名
        :return:
        """
        qt_model.AddBeamConstraint(id=index, beamId=beam_id, nodeInfoI=info_i, nodeInfo2=info_j, groupName=group_name)

    @staticmethod
    def add_node_axis(index=-1, input_type=1, node_id=1, coord_info=None):
        """
        添加节点坐标
        :param index:默认自动识别
        :param input_type:输入方式
        :param node_id:节点号
        :param coord_info:局部坐标信息 -List<float>(角)  -List<List<float>>(三点/向量)
        :return:
        """
        qt_model.AddNodalAxises(id=index, input_type=input_type, nodeId=node_id, nodeInfo=coord_info)

    # endregion

    # region 移动荷载
    @staticmethod
    def add_standard_vehicle(name="", standard_code=1, load_type="高速铁路", load_length=0, n=6):
        """
        添加标准车辆
        :param name:
        :param standard_code:
        :param load_type:
        :param load_length:
        :param n:
        :return:
        """
        qt_model.AddStandardVehicle(name=name, standardIndex=standard_code, loadType=load_type, loadLength=load_length, N=n)

    @staticmethod
    def add_node_tandem(name="", start_id=-1, node_ids=None):
        """
        添加节点纵列
        :param name:
        :param start_id:
        :param node_ids:
        :return:
        """
        qt_model.AddNodeTandem(name=name, startId=start_id, nodeIds=node_ids)

    @staticmethod
    def add_influence_plane(name="", tandem_names=None):
        """
        添加影响面
        :param name:
        :param tandem_names:
        :return:
        """
        qt_model.AddInfluencePlane(name=name, tandemNames=tandem_names)

    @staticmethod
    def add_lane_line(name="", influence_name="", tandem_name="", offset=0, direction=0):
        """
        添加车道线
        :param name:
        :param influence_name:
        :param tandem_name:
        :param offset:
        :param direction:
        :return:
        """
        qt_model.AddLaneLine(name, influenceName=influence_name, tandemName=tandem_name, offset=offset, direction=direction)

    @staticmethod
    def add_live_load_case(name="", influence_plane="", span=0, sub_case=None):
        """
        添加移动荷载工况
        :param name:
        :param influence_plane:
        :param span:
        :param sub_case:
        :return:
        """
        qt_model.AddLiveLoadCase(name=name, influencePlane=influence_plane, span=span, subCase=sub_case)

    @staticmethod
    def remove_vehicle(index=-1):
        """
        删除车辆信息
        :param index:
        :return:
        """
        qt_model.RemoveVehicle(id=index)

    @staticmethod
    def remove_node_tandem(index=-1, name=""):
        """
        删除节点纵列
        :param index:
        :param name:
        :return:
        """
        if index != -1:
            qt_model.RemoveNodeTandem(id=index)
        elif name != "":
            qt_model.RemoveNodeTandem(name=name)

    @staticmethod
    def remove_influence_plane(index=-1, name=""):
        """
        删除影响线
        :param index:
        :param name:
        :return:
        """
        if index != -1:
            qt_model.RemoveInfluencePlane(id=index)
        elif name != "":
            qt_model.RemoveInfluencePlane(name=name)

    @staticmethod
    def remove_lane_line(name="", index=-1):
        """
        删除车道线
        :param name:
        :param index:
        :return:
        """
        if index != -1:
            qt_model.RemoveLaneLine(id=index)
        elif name != "":
            qt_model.RemoveLaneLine(name=name)

    @staticmethod
    def remove_live_load_case(name=""):
        """
        删除移动荷载工况
        :param name:
        :return:
        """
        qt_model.RemoveLiveLoadCase(name=name)

    # endregion

    # region 钢束操作
    @staticmethod
    def add_tendon_property(name="", index=-1, tendon_type=PRE, material_id=1, duct_type=1,
                            steel_type=1, steel_detail=None, loos_detail=None, slip_info=None):
        """
        添加钢束特性
        :param name:钢束特性名
        :param index:钢束编号,默认自动识别 (可选参数)
        :param tendon_type: 0-PRE 1-POST
        :param material_id: 钢材材料编号
        :param duct_type: 1-金属波纹管  2-塑料波纹管  3-铁皮管  4-钢管  5-抽芯成型
        :param steel_type: 1-钢绞线  2-螺纹钢筋
        :param steel_detail: 钢绞线[钢束面积,孔道直径,摩阻系数,偏差系数]  螺纹钢筋[钢筋直径,钢束面积,孔道直径,摩阻系数,偏差系数,张拉方式(1-一次张拉\2-超张拉)]
        :param loos_detail: 松弛信息[规范(1-公规 2-铁规),张拉(1-一次张拉 2-超张拉),松弛(1-一般松弛 2-低松弛)] (仅钢绞线需要)
        :param slip_info: 滑移信息[始端距离,末端距离]
        :return:
        """
        qt_model.AddTendonProperty(name=name, id=index, tendonType=tendon_type, materialId=material_id,
                                   ductType=duct_type, steelType=steel_type, steelDetail=steel_detail,
                                   loosDetail=loos_detail, slipInfo=slip_info)

    @staticmethod
    def add_tendon_3d(name="", property_name="", group_name="默认钢束组", num=1, line_type=1, position_type=STRAIGHT,
                      control_info=None, point_insert=None, tendon_direction=None,
                      rotation_angle=0, track_group="默认结构组"):
        """
        添加三维钢束
        :param name:钢束名称
        :param property_name:钢束特性名称
        :param group_name:默认钢束组
        :param num:根数
        :param line_type:1-导线点  2-折线点
        :param position_type: 定位方式 1-直线  2-轨迹线
        :param control_info: 控制点信息[[x1,y1,z1,r1],[x2,y2,z2,r2]....]
        :param point_insert: 定位方式为直线时为插入点坐标[x,y,z], 轨迹线时为 [插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id]
        :param tendon_direction:直线钢束方向向量 x轴-[1,0,0] y轴-[0,1,0] (轨迹线时不用赋值)
        :param rotation_angle:绕钢束旋转角度
        :param track_group:轨迹线结构组名  (直线时不用赋值)
        :return:
        """
        qt_model.AddTendon3D(name=name, propertyName=property_name, groupName=group_name, num=num, lineType=line_type,
                             positionType=position_type, controlPoints=control_info,
                             pointInsert=point_insert, tendonDirection=tendon_direction,
                             rotationAngle=rotation_angle, trackGroup=track_group)

    @staticmethod
    def remove_tendon(name="", index=-1):
        """
        按照名称或编号删除钢束,默认时删除所有钢束
        :param name:
        :param index:
        :return:
        """
        if name != "":
            qt_model.RemoveTendon(name=name)
        elif index != -1:
            qt_model.RemoveTendon(id=index)
        else:
            qt_model.RemoveAllTendon()

    @staticmethod
    def remove_tendon_property(name="", index=-1):
        """
        按照名称或编号删除钢束组,默认时删除所有钢束组
        :param name:
        :param index:
        :return:
        """
        if name != "":
            qt_model.RemoveTendonProperty(name=name)
        elif index != -1:
            qt_model.RemoveTendonProperty(id=index)
        else:
            qt_model.RemoveAllTendonGroup()

    @staticmethod
    def add_nodal_mass(node_id=1, mass_info=None):
        """
        添加节点质量
        :param node_id:节点编号
        :param mass_info:[m,rmX,rmY,rmZ]
        :return:
        """
        qt_model.AddNodalMass(nodeId=node_id, massInfo=mass_info)

    @staticmethod
    def remove_nodal_mass(node_id=-1):
        """
        删除节点质量
        :param node_id:
        :return:
        """
        qt_model.RemoveNodalMass(nodeId=node_id)

    @staticmethod
    def add_pre_stress(index=-1, case_name="", tendon_name="", pre_type=2, force=1395000, group_name="默认荷载组"):
        """
        添加预应力
        :param index:
        :param case_name:
        :param tendon_name:
        :param pre_type:
        :param force:
        :param group_name:
        :return:
        """
        qt_model.AddPreStress(caseName=case_name, tendonName=tendon_name, preType=pre_type, force=force, id=index, groupName=group_name)

    @staticmethod
    def remove_pre_stress(case_name="", tendon_name="", group_name="默认荷载组"):
        """
        删除预应力
        :param case_name:
        :param tendon_name:
        :param group_name:
        :return:
        """
        qt_model.RemovePreStress(caseName=case_name, tendonName=tendon_name, groupName=group_name)

    # endregion

    # region 荷载操作
    @staticmethod
    def add_nodal_force(case_name="", node_id=1, load_info=None, group_name="默认荷载组"):
        """
        添加节点荷载
        :param case_name:荷载工况名
        :param node_id:节点编号
        :param load_info:[Fx,Fy,Fz,Mx,My,Mz]
        :param group_name:荷载组名
        :return:
        """
        qt_model.AddNodalForce(caseName=case_name, nodeId=node_id, loadInfo=load_info, groupName=group_name)

    @staticmethod
    def remove_nodal_force(case_name="", node_id=-1):
        """
        删除节点荷载
        :param case_name:荷载工况名
        :param node_id:节点编号
        :return:
        """
        qt_model.RemoveNodalForce(caseName=case_name, nodeId=node_id)

    @staticmethod
    def add_node_displacement(case_name="", node_id=1, load_info=None, group_name="默认荷载组"):
        """
        添加节点位移
        :param case_name:荷载工况名
        :param node_id:节点编号
        :param load_info:[Dx,Dy,Dz,Rx,Ry,Rz]
        :param group_name:荷载组名
        :return:
        """
        qt_model.AddNodeDisplacement(caseName=case_name, nodeId=node_id, loadInfo=load_info, groupName=group_name)

    @staticmethod
    def remove_nodal_displacement(case_name="", node_id=-1):
        """
        删除节点位移
        :param case_name:荷载工况名
        :param node_id:节点编号
        :return:
        """
        qt_model.RemoveNodalDisplacement(caseName=case_name, nodeId=-node_id)

    @staticmethod
    def add_beam_load(case_name="", beam_id=1, load_type=1, coordinate_system=3, load_info=None, group_name="默认荷载组"):
        """
        添加梁单元荷载
        :param case_name:荷载工况名
        :param beam_id:单元编号
        :param load_type:荷载类型
        :param coordinate_system:坐标系
        :param load_info:
        :param group_name:
        :return:
        """
        qt_model.AddBeamLoad(caseName=case_name, beamId=beam_id, loadType=load_type,
                             coordinateSystem=coordinate_system, loadInfo=load_info, groupName=group_name)

    @staticmethod
    def remove_beam_load(case_name="", element_id=1, load_type=1, group_name="默认荷载组"):
        """
        删除梁单元荷载
        :param case_name:
        :param element_id:
        :param load_type:
        :param group_name:
        :return:
        """
        qt_model.RemoveBeamLoad(caseName=case_name, elementId=element_id, loadType=load_type, groupName=group_name)

    @staticmethod
    def add_initial_tension(element_id=1, case_name="", group_name="默认荷载组", tension=0, tension_type=1):
        """
        添加初始拉力
        :param element_id:
        :param case_name:
        :param group_name:
        :param tension:
        :param tension_type:
        :return:
        """
        qt_model.AddInitialTension(elementId=element_id, caseName=case_name, groupName=group_name, tension=tension, tensionType=tension_type)

    @staticmethod
    def add_cable_length_load(element_id=1, case_name="", group_name="默认荷载组", length=0, tension_type=1):
        """
        添加索长张拉
        :param element_id:
        :param case_name:
        :param group_name:
        :param length:
        :param tension_type:
        :return:
        """
        qt_model.AddCableLenghtLoad(elementId=element_id, caseName=case_name, groupName=group_name, length=length, tensionType=tension_type)

    @staticmethod
    def add_plate_element_load(element_id=1, case_name="", load_type=1, load_place=1, coord_system=1, group_name="默认荷载组", load_info=None):
        """
        添加版单元荷载
        :param element_id:
        :param case_name:
        :param load_type:
        :param load_place:
        :param coord_system:
        :param group_name:
        :param load_info:
        :return:
        """
        qt_model.AddPlateElementLoad(elementId=element_id, caseName=case_name, loadType=load_type, loadPlace=load_place,
                                     coordSystem=coord_system, groupName=group_name, loadInfo=load_info)

    @staticmethod
    def add_deviation_parameter(name="", element_type=1, parameter_info=None):
        """
        添加制造误差
        :param name:
        :param element_type:
        :param parameter_info:
        :return:
        """
        qt_model.AddDeviationParameter(name=name, elementType=element_type, parameterInfo=parameter_info)

    @staticmethod
    def add_deviation_load(element_id=1, case_name="", parameter_name=None, group_name="默认荷载组"):
        """
        添加制造误差荷载
        :param element_id:
        :param case_name:
        :param parameter_name:
        :param group_name:
        :return:
        """
        qt_model.AddDeviationLoad(elementId=element_id, caseName=case_name, parameterName=parameter_name, groupName=group_name)

    @staticmethod
    def add_element_temperature(element_id=1, case_name="", temperature=1, group_name="默认荷载组"):
        """
        添加单元温度
        :param element_id:
        :param case_name:
        :param temperature:
        :param group_name:
        :return:
        """
        qt_model.AddElementTemperature(elementId=element_id, caseName=case_name, temperature=temperature, groupName=group_name)

    @staticmethod
    def add_gradient_temperature(element_id=1, case_name="", temperature=1, section_oriental=1, element_type=1, group_name=""):
        """
        添加梯度温度
        :param element_id:
        :param case_name:
        :param temperature:
        :param section_oriental:
        :param element_type:
        :param group_name:
        :return:
        """
        qt_model.AddGradientTemperature(elementId=element_id, caseName=case_name, temperature=temperature,
                                        sectionOriental=section_oriental, elementType=element_type, groupNmae=group_name)

    @staticmethod
    def add_beam_section_temperature(element_id=1, case_name="", paving_thick=0, temperature_type=1, paving_type=1, group_name="默认荷载组"):
        """
        添加梁截面温度
        :param element_id:
        :param case_name:
        :param paving_thick:
        :param temperature_type:
        :param paving_type:
        :param group_name:
        :return:
        """
        qt_model.AddBeamSectionTemperature(elementId=element_id, caseName=case_name, pavingThickness=paving_thick,
                                           temperatureType=temperature_type, pavingType=paving_type, groupName=group_name)

    @staticmethod
    def add_index_temperature(element_id=1, case_name="", temperature=0, index=1, group_name="默认荷载组"):
        """
        添加指数温度
        :param element_id:
        :param case_name:
        :param temperature:
        :param index:
        :param group_name:
        :return:
        """
        qt_model.AddIndexTemperature(elementId=element_id, caseName=case_name, temperature=temperature, index=index, groupName=group_name)

    @staticmethod
    def add_plate_temperature(element_id=1, case_name="", temperature=0, group_name="默认荷载组"):
        """
        添加顶板温度
        :param element_id:
        :param case_name:
        :param temperature:
        :param group_name:
        :return:
        """
        qt_model.AddTopPlateTemperature(elementId=element_id, caseName=case_name, temperature=temperature, groupName=group_name)

    # endregion

    # region 沉降操作
    @staticmethod
    def add_sink_group(name="", sink=0.1, node_ids=None):
        """
        添加沉降组
        :param name: 沉降组名
        :param sink: 沉降值
        :param node_ids: 节点编号
        :return:
        """
        qt_model.AddSinkGroup(name=name, sinkValue=sink, nodeIds=node_ids)

    @staticmethod
    def remove_sink_group(name=""):
        """
        按照名称删除沉降组
        :param name:沉降组名,默认删除所有沉降组
        :return:
        """
        if name == "":
            qt_model.RemoveAllSinkGroup()
        else:
            qt_model.RemoveSinkGroup(name=name)

    @staticmethod
    def add_sink_case(name="", sink_groups=None, n_max=1, n_min=1, factor=1):
        """
        添加沉降工况
        :param name:
        :param sink_groups:
        :param n_max:
        :param n_min:
        :param factor:
        :return:
        """
        qt_model.AddSinkCase(name=name, sinkGroups=sink_groups, nMax=n_max, nMin=n_min, factor=factor)

    @staticmethod
    def remove_sink_case(name=""):
        """
        按照名称删除沉降工况,不输入名称时默认删除所有沉降工况
        :param name:
        :return:
        """
        if name == "":
            qt_model.RemoveAllSinkCase()
        else:
            qt_model.RemoveSinkCase()

    @staticmethod
    def add_concurrent_reaction(names=None):
        """
        添加并发反力组
        :param names: 结构组名称集合
        :return:
        """
        qt_model.AddConcurrentReaction(names=names)

    @staticmethod
    def remove_concurrent_reaction():
        """
        删除并发反力组
        :return:
        """
        qt_model.RemoveConcurrentRection()

    @staticmethod
    def add_concurrent_force():
        """
        添加并发内力
        :return:
        """
        qt_model.AddConcurrentForce()

    @staticmethod
    def remove_concurrent_force():
        """
        删除并发内力
        :return:
        """
        qt_model.RemoveConcurrentForce()

    @staticmethod
    def add_load_case(index=-1, name="", load_case_type=CS):
        """
        添加荷载工况
        :param index:
        :param name:
        :param load_case_type:
        :return:
        """
        qt_model.AddLoadCase(id=index, name=name, loadCaseType=load_case_type)

    @staticmethod
    def remove_load_case(index=-1, name=""):
        """
        删除荷载工况,参数均为默认时删除全部荷载工况
        :param index: 按照荷载工况编号删除
        :param name: 按诈骗荷载工况名删除
        :return:
        """
        if name != "":
            qt_model.DeleteLoadCase(name=name)
        elif index != -1:
            qt_model.DeleteLoadCase(id=index)
        else:
            qt_model.DeleteAllLoadCase()

    @staticmethod
    def test_print():
        """
        测试运行
        :return:
        """
        print(1)
        raise Exception("错误")

    # endregion

    # region 施工阶段和荷载组合
    @staticmethod
    def add_construction_stage(name="", duration=0, active_structures=None, delete_structures=None, active_boundaries=None,
                               delete_boundaries=None, active_loads=None, delete_loads=None, temp_loads=None, index=-1):
        """
        添加施工阶段信息
        :param name:
        :param duration:
        :param active_structures:
        :param delete_structures:
        :param active_boundaries:
        :param delete_boundaries:
        :param active_loads:
        :param delete_loads:
        :param temp_loads:
        :param index:
        :return:
        """
        qt_model.AddConstructionStage(name=name, duration=duration, activeStructures=active_structures, inActiveStructures=delete_structures
                                      , activeBoundaries=active_boundaries, inActiveBoundaries=delete_boundaries, activeLoads=active_loads,
                                      inActiveLoads=delete_loads, tempLoads=temp_loads, id=index)

    @staticmethod
    def remove_construction_stage(name=""):
        """
        按照施工阶段名删除施工阶段
        :param name:
        :return:
        """
        qt_model.RemoveConstructionStage(name=name)

    @staticmethod
    def remove_all_construction_stage():
        """
        删除所有施工阶段
        :return:
        """
        qt_model.RemoveAllConstructionStage()

    @staticmethod
    def add_load_combine(name="", combine_type=1, describe="", combine_info=None):
        """
        添加荷载组合
        :param name:
        :param combine_type:
        :param describe:
        :param combine_info:
        :return:
        """
        qt_model.AddLoadCombine(name=name, loadCombineType=combine_type, describe=describe, caseAndFactor=combine_info)

    @staticmethod
    def remove_load_combine(name=""):
        """
        删除荷载组合,参数默认时删除所有荷载组合
        :param name:
        :return:
        """
        if name != "":
            qt_model.DeleteLoadCombine(name=name)
        else:
            qt_model.DeleteAllLoadCombine()
    # endregion


class OperationFailedException(Exception):
    """用户操作失败时抛出的异常"""
    pass
