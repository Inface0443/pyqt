from __main__ import qt_model
from .qt_keyword import *


class Mdb:
    """
    Mdb类负责建模相关操作
    """

    def __int__(self):
        self.initial()

    # region 初始化模型
    @staticmethod
    def initial():
        """
        初始化模型
        Returns: 无
        """
        qt_model.Initial()

    # region 节点单元操作
    @staticmethod
    def add_structure_group(name="", index=-1):
        """
        添加结构组
        Args:
            name: 结构组名
            index: 结构组编号(非必须参数)，默认自动识别当前编号
        Returns: 无
        """
        qt_model.AddStructureGroup(name=name, id=index)

    @staticmethod
    def remove_structure_group(name="", index=-1):
        """
        可根据结构与组名或结构组编号删除结构组，当组名和组编号均为默认则删除所有结构组
        Args:
            name:结构组名称
            index:结构组编号
        Returns: 无
        """
        if index != -1:
            qt_model.RemoveStructureGroup(id=index)
        elif name != "":
            qt_model.RemoveStructureGroup(name=name)
        else:
            qt_model.RemoveAllStructureGroup()

    @staticmethod
    def add_structure_to_group(name="", node_ids=None, element_ids=None):
        """
        为结构组添加节点和/或单元
        Args:
             name: 结构组名
             node_ids: 节点编号列表(可选参数)
             element_ids: 单元编号列表(可选参数)
        Returns: 无
        """
        if node_ids is None:
            node_ids = []
        if element_ids is None:
            element_ids = []
        qt_model.AddStructureToGroup(name=name, nodeIds=node_ids, elementIds=element_ids)

    @staticmethod
    def remove_structure_in_group(name="", node_ids=None, element_ids=None):
        """
        为结构组删除节点和/或单元
        Args:
             name: 结构组名
             node_ids: 节点编号列表(可选参数)
             element_ids: 单元编号列表(可选参数)
        Returns: 无
        """
        if node_ids is None:
            node_ids = []
        if element_ids is None:
            element_ids = []
        qt_model.RemoveStructureOnGroup(name=name, nodeIds=node_ids, elementIds=element_ids)

    @staticmethod
    def add_node(x=1, y=1, z=1, index=-1):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        Args:
             x: 节点坐标x
             y: 节点坐标y
             z: 节点坐标z
             index: 节点编号，默认自动识别编号 (可选参数)
        Returns:无
        """
        if index != -1:
            qt_model.AddNode(id=index, x=x, y=y, z=z)
        else:
            qt_model.AddNode(x=x, y=y, z=z)

    @staticmethod
    def add_nodes(node_list):
        """
        添加多个节点，可以选择指定节点编号
        Args:
             node_list:节点坐标信息 [[x1,y1,z1],...]或 [[id1,x1,y1,z1]...]
        Returns: 无
        """
        qt_model.AddNodes(dataList=node_list)

    @staticmethod
    def remove_node(index=None):
        """
        删除指定节点
        Args:
            index:节点编号
        Returns: 无
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
        Args:
            index:单元编号
            ele_type:单元类型 1-梁 2-索 3-杆 4-板
            node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]
            beta_angle:贝塔角
            mat_id:材料编号
            sec_id:截面编号
        Returns: 无
        """
        if node_ids is None and ele_type != 4:
            raise OperationFailedException("操作错误,请输入此单元所需节点列表,[i,j]")
        if node_ids is None and ele_type == 4:
            raise OperationFailedException("操作错误,请输入此板单元所需节点列表,[i,j,k,l]")
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
        Args:
            index: 单元编号,默认时删除所有单元
        Returns: 无
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
        Args:
            index:材料编号,默认自动识别 (可选参数)
            name:材料名称
            material_type: 材料类型
            standard_name:规范名称
            database:数据库
            construct_factor:构造系数
            modified:是否修改默认材料参数,默认不修改 (可选参数)
            modify_info:材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (可选参数)
        Returns: 无
        """
        if modified and len(modify_info) != 4:
            raise OperationFailedException("操作错误,modify_info数据无效!")
        if not modified:
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
        Args:
            index: 指定收缩徐变编号,默认则自动识别 (可选参数)
            name: 收缩徐变名
            code_index: 收缩徐变规范索引
            time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)
        Returns:无
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
        Args:
            index: 材料编号
            creep_id: 收缩徐变编号
            f_cuk: 材料标准抗压强度,仅自定义材料是需要输入
        Returns: 无
        """

        qt_model.UpdateMaterialCreep(materialId=index, timePatameterId=creep_id, fcuk=f_cuk)

    @staticmethod
    def remove_material(index=-1):
        """
        删除指定材料
        Args:
            index:指定材料编号，默认则删除所有材料
        Returns: 无
        """
        if index == -1:
            qt_model.RemoveAllMaterial()
        else:
            qt_model.RemoveMaterial(id=index)

    # endregion

    # region 截面和板厚操作
    @staticmethod
    def add_parameter_section(index=-1, name="", section_type="矩形", section_info=None,
                              charm_info=None, section_right=None, charm_right=None, box_number=3, height=2, material_info=None,
                              bias_type="中心", center_type="质心", shear_consider=True, bias_x=0, bias_y=0):
        """
        添加截面信息
        Args:
             index: 截面编号,默认自动识别
             name:截面名称
             section_type:截面类型
             section_info:截面信息 (必要参数)
             charm_info:混凝土截面倒角信息 (仅混凝土箱梁截面需要)str[4]
             section_right:混凝土截面右半信息 (对称时可忽略，仅混凝土箱梁截面需要) str[19]
             charm_right:混凝土截面右半倒角信息 (对称时可忽略，仅混凝土箱梁截面需要) str[4]
             box_number: 混凝土箱室数 (仅混凝土箱梁截面需要)
             height: 混凝土箱梁梁高 (仅混凝土箱梁截面需要)
             material_info: 组合截面材料信息 [弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c] (仅组合材料需要)
             bias_type:偏心类型
             center_type:中心类型
             shear_consider:考虑剪切 bool
             bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要)
             bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要)

        Returns: 无
        """
        if section_info is None:
            raise OperationFailedException("操作错误,请输入此截面的截面信息，参数列表可参考截面定义窗口!")
        elif section_type == "混凝土箱梁":
            if len(section_info) != 19 or len(charm_info) != 4:
                raise OperationFailedException("操作错误，混凝土箱梁参数错误，参数列表可参考截面定义窗口！")
            qt_model.AddParameterSection(id=index, name=name, secType=section_type, secInfo=section_info, charmInfo=charm_info,
                                         N=box_number, H=height, charmInfoR=charm_right, secInfoR=section_right,
                                         biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                         horizontalPos=bias_x, verticalPos=bias_y)
        elif section_type == "钢管砼" or section_type == "钢箱砼":
            if len(material_info) != 5:
                raise OperationFailedException("操作错误，材料比错误，参数列表：[弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c] ！")
            if len(section_info) != 2 or len(section_info) != 6:
                raise OperationFailedException("操作错误，截面参数列表：[D,t]-钢管砼  [W,H,dw,tw,tt,tb]-钢箱砼")
            qt_model.AddParameterSection(id=index, name=name, secType=section_type, secInfo=section_info,
                                         elasticModulusRatio=material_info[0], densityRatio=material_info[1], steelPoisson=material_info[2],
                                         concretePoisson=material_info[3], temperatureRatio=material_info[4],
                                         biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                         horizontalPos=bias_x, verticalPos=bias_y)
        else:
            qt_model.AddParameterSection(id=index, name=name, secType=section_type, secInfo=section_info,
                                         biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                         horizontalPos=bias_x, verticalPos=bias_y)

    @staticmethod
    def add_steel_section(index=-1, name="", section_type=SEC_GGL, section_info=None, rib_info=None, rib_place=None,
                          bias_type="中心", center_type="质心", shear_consider=True, bias_x=0, bias_y=0):
        """
        添加钢梁截面,包括参数型钢梁截面和自定义带肋钢梁截面
        Args:
             index:
             name:
             section_type:截面类型
             section_info:截面信息
             rib_info:肋板信息
             rib_place:肋板位置
             bias_type:偏心类型
             center_type:中心类型
             shear_consider:考虑剪切
             bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要,相对形心)
             bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要)
        Returns: 无
        """
        if section_info is None:
            raise OperationFailedException("操作错误,请输入此截面的截面信息，参数列表可参考截面定义窗口")
        qt_model.AddSteelSection(id=index, name=name, type=section_type, sectionInfoList=section_info, ribInfoList=rib_info,
                                 ribPlaceList=rib_place, baisType=bias_type, centerType=center_type,
                                 shearConsider=shear_consider, horizontalPos=bias_x, verticalPos=bias_y)

    @staticmethod
    def add_user_section(index=-1, name="", section_type="特性截面", property_info=None):
        """
        添加自定义截面,目前仅支持特性截面
        Args:
             index:截面编号
             name:截面名称
             section_type:截面类型
             property_info:截面特性列表
        Returns: 无
        """
        if property_info is None:
            raise OperationFailedException("操作错误,请输入此截面的截面特性，特性列表可参考截面定义窗口")
        qt_model.AddUserSection(id=index, name=name, type=section_type, propertyInfo=property_info)

    @staticmethod
    def add_tapper_section(index=-1, name="", begin_id=1, end_id=1, vary_info=None):
        """
        添加变截面,需先建立单一截面
        Args:
             index:截面编号
             name:截面名称
             begin_id:截面始端编号
             end_id:截面末端编号
             vary_info:截面变化信息
        Returns: 无
        """
        if vary_info is not None:
            if len(vary_info) != 2:
                raise OperationFailedException("操作错误,vary_info数据无效!")
            qt_model.AddTapperSection(id=index, name=name, beginId=begin_id, endId=end_id,
                                      varyParameterWidth=vary_info[0], varyParameterHeight=vary_info[1])
        else:
            qt_model.AddTapperSection(id=index, name=name, beginId=begin_id, endId=end_id)

    @staticmethod
    def remove_section(index=-1):
        """
        删除截面信息
        Args:
             index: 截面编号,参数为默认时删除全部截面
        Returns: 无
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
        Args:
             index: 板厚id
             name: 板厚名称
             t:   板厚度
             thick_type: 板厚类型 0-普通板 1-加劲肋板
             bias_info:  默认不偏心,偏心时输入列表[type,value] type:0-厚度比 1-数值
             rib_pos:肋板位置
             dist_v:纵向截面肋板间距
             dist_l:横向截面肋板间距
             rib_v:纵向肋板信息
             rib_l:横向肋板信息
        Returns: 无
        """
        if rib_v is None:
            rib_v = []
        if rib_l is None:
            rib_l = []
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
        Args:
             index:板厚编号,默认时删除所有板厚信息
        Returns: 无
        """
        if index == -1:
            qt_model.RemoveAllThickness()
        else:
            qt_model.RemoveThickness(id=index)

    @staticmethod
    def add_tapper_section_group(ids=None, name="", factor_w=1.0, factor_h=1.0, ref_w=0, ref_h=0, dis_w=0, dis_h=0):
        """
        添加变截面组
        Args:
             ids:变截面组编号
             name: 变截面组名
             factor_w: 宽度方向变化阶数 线性(1.0) 非线性(!=1.0)
             factor_h: 高度方向变化阶数 线性(1.0) 非线性(!=1.0)
             ref_w: 宽度方向参考点 0-i 1-j
             ref_h: 高度方向参考点 0-i 1-j
             dis_w: 宽度方向间距
             dis_h: 高度方向间距
        Returns: 无
        """
        qt_model.AddTapperSectionGroup(ids=ids, name=name, factorW=factor_w, factorH=factor_h, w=ref_w, h=ref_h, disW=dis_w, disH=dis_h)

    @staticmethod
    def update_section_bias(index=1, bias_type="中心", center_type="质心", shear_consider=True, bias_point=None):
        """
        更新截面偏心
        Args:
             index:截面编号
             bias_type:偏心类型
             center_type:中心类型
             shear_consider:考虑剪切
             bias_point:自定义偏心点(仅自定义类型偏心需要)
        Returns: 无
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
    def add_boundary_group(name="", index=-1):
        """
        新建边界组
        Args:
             name:边界组名
             index:边界组编号，默认自动识别当前编号 (可选参数)
        Returns: 无
        """
        qt_model.AddBoundaryGroup(name=name, id=index)

    @staticmethod
    def remove_boundary_group(name=""):
        """
        按照名称删除边界组
        Args:
            name: 边界组名称，默认删除所有边界组 (非必须参数)
        Returns: 无
        """
        if name != "":
            qt_model.RemoveBoundaryGroup(name)
        else:
            qt_model.RemoveAllBoundaryGroup()

    @staticmethod
    def remove_boundary(group_name="", boundary_type=-1, index=1):
        """
        根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息
        Args:
            group_name: 边界组名
            boundary_type: 边界类型
            index: 边界编号
        Returns: 无
        """
        if group_name == "":
            qt_model.RemoveAllBoundary()

    @staticmethod
    def add_general_support(index=-1, node_id=1, boundary_info=None, group_name="默认边界组"):
        """
        添加一般支承
        Args:
             index:边界编号
             node_id:节点编号
             boundary_info:边界信息，例如[X,Y,Z,Rx,Ry,Rz] 1-固定 0-自由
             group_name:边界组名
        Returns: 无
        """
        if boundary_info is None or len(boundary_info) != 6:
            raise OperationFailedException("操作错误，要求输入一般支承列表长度为6")
        qt_model.AddGeneralSupport(id=index, nodeId=node_id, boundaryInfo=boundary_info, groupName=group_name)

    @staticmethod
    def add_elastic_support(index=-1, node_id=1, support_type=1, boundary_info=None, group_name="默认边界组"):
        """
        添加弹性支承
        Args:
             index:编号
             node_id:节点编号
             support_type:支承类型
             boundary_info:边界信息
             group_name:边界组
        Returns: 无
        """
        qt_model.AddElasticSupport(id=index, nodeId=node_id, supportType=support_type, boundaryInfo=boundary_info,
                                   groupName=group_name)

    @staticmethod
    def add_master_slave_link(index=-1, master_id=1, slave_id=2, boundary_info=None, group_name="默认边界组"):
        """
        添加主从约束
        Args:
             index:编号
             master_id:主节点号
             slave_id:从节点号
             boundary_info:边界信息
             group_name:边界组名
        Returns: 无
        """
        qt_model.AddMasterSlaveLink(id=index, masterId=master_id, slaveId=slave_id, boundaryInfo=boundary_info, groupName=group_name)

    @staticmethod
    def add_elastic_link(index=-1, link_type=1, start_id=1, end_id=2, beta_angle=0, boundary_info=None,
                         group_name="默认边界组", dis_ratio=0.5, kx=0):
        """
        添加弹性连接
        Args:
             index:节点编号
             link_type:节点类型
             start_id:起始节点号
             end_id:终节点号
             beta_angle:贝塔角
             boundary_info:边界信息
             group_name:边界组名
             dis_ratio:距离比
             kx:刚度
        Returns: 无
        """
        qt_model.AddElasticLink(id=index, linkType=link_type, startId=start_id, endId=end_id, beta=beta_angle,
                                boundaryInfo=boundary_info, groupName=group_name, disRatio=dis_ratio, kDx=kx)

    @staticmethod
    def add_beam_constraint(index=-1, beam_id=2, info_i=None, info_j=None, group_name="默认边界组"):
        """
        添加梁端约束
        Args:
             index:约束编号,默认自动识别
             beam_id:梁号
             info_i:i端约束信息 [IsFreedX,IsFreedY,IsFreedZ,IsFreedRX,IsFreedRY,IsFreedRZ]
             info_j:j端约束信息 [IsFreedX,IsFreedY,IsFreedZ,IsFreedRX,IsFreedRY,IsFreedRZ]
             group_name:边界组名
        Returns: 无
        """
        if info_i is None or len(info_i) != 6:
            raise OperationFailedException("操作错误，要求输入I端约束列表长度为6")
        if info_j is None or len(info_j) != 6:
            raise OperationFailedException("操作错误，要求输入J端约束列表长度为6")
        qt_model.AddBeamConstraint(id=index, beamId=beam_id, nodeInfoI=info_i, nodeInfo2=info_j, groupName=group_name)

    @staticmethod
    def add_node_axis(index=-1, input_type=1, node_id=1, coord_info=None):
        """
        添加节点坐标
        Args:
             index:默认自动识别
             input_type:输入方式
             node_id:节点号
             coord_info:局部坐标信息 -List<float>(角)  -List<List<float>>(三点/向量)
        Returns: 无
        """
        if coord_info is None:
            raise OperationFailedException("操作错误，输入坐标系信息不能为空")
        qt_model.AddNodalAxises(id=index, input_type=input_type, nodeId=node_id, nodeInfo=coord_info)

    # endregion

    # region 移动荷载
    @staticmethod
    def add_standard_vehicle(name="", standard_code=1, load_type="高速铁路", load_length=0, n=6):
        """
        添加标准车辆
        Args:
             name:车辆荷载名称
             standard_code:荷载规范
             load_type:荷载类型
             load_length:荷载长度
             n:车厢数
        Returns: 无
        """
        qt_model.AddStandardVehicle(name=name, standardIndex=standard_code, loadType=load_type, loadLength=load_length, N=n)

    @staticmethod
    def add_node_tandem(name="", start_id=-1, node_ids=None):
        """
        添加节点纵列
        Args:
             name:节点纵列名
             start_id:起始节点号
             node_ids:节点列表
        Returns: 无
        """
        if node_ids is None:
            raise OperationFailedException("操作错误，输入节点列表不能为空")
        qt_model.AddNodeTandem(name=name, startId=start_id, nodeIds=node_ids)

    @staticmethod
    def add_influence_plane(name="", tandem_names=None):
        """
        添加影响面
        Args:
             name:影响面名称
             tandem_names:节点纵列名称组
        Returns: 无
        """
        qt_model.AddInfluencePlane(name=name, tandemNames=tandem_names)

    @staticmethod
    def add_lane_line(name="", influence_name="", tandem_name="", offset=0, direction=0):
        """
        添加车道线
        Args:
             name:车道线名称
             influence_name:影响面名称
             tandem_name:节点纵列名
             offset:偏移
             direction:方向
        Returns: 无
        """
        qt_model.AddLaneLine(name, influenceName=influence_name, tandemName=tandem_name, offset=offset, direction=direction)

    @staticmethod
    def add_live_load_case(name="", influence_plane="", span=0, sub_case=None):
        """
        添加移动荷载工况
        Args:
             name:荷载工况名
             influence_plane:影响线名
             span:跨度
             sub_case:子工况信息 List<string[]>
        Returns: 无
        """
        if sub_case is None:
            raise OperationFailedException("操作错误，子工况信息列表不能为空")
        qt_model.AddLiveLoadCase(name=name, influencePlane=influence_plane, span=span, subCase=sub_case)

    @staticmethod
    def remove_vehicle(index=-1):
        """
        删除车辆信息
        Args:
             index:车辆荷载编号
        Returns: 无
        """
        qt_model.RemoveVehicle(id=index)

    @staticmethod
    def remove_node_tandem(index=-1, name=""):
        """
        按照 节点纵列编号/节点纵列名 删除节点纵列
        Args:
             index:节点纵列编号
             name:节点纵列名
        Returns: 无
        """
        if index != -1:
            qt_model.RemoveNodeTandem(id=index)
        elif name != "":
            qt_model.RemoveNodeTandem(name=name)

    @staticmethod
    def remove_influence_plane(index=-1, name=""):
        """
        按照 影响面编号/影响面名称 删除影响面
        Args:
             index:影响面编号
             name:影响面名称
        Returns: 无
        """
        if index != -1:
            qt_model.RemoveInfluencePlane(id=index)
        elif name != "":
            qt_model.RemoveInfluencePlane(name=name)

    @staticmethod
    def remove_lane_line(name="", index=-1):
        """
        按照 车道线编号/车道线名称 删除车道线
        Args:
             name:车道线名称
             index:车道线编号
        Returns: 无
        """
        if index != -1:
            qt_model.RemoveLaneLine(id=index)
        elif name != "":
            qt_model.RemoveLaneLine(name=name)

    @staticmethod
    def remove_live_load_case(name=""):
        """
        删除移动荷载工况
        Args:
             name:移动荷载工况名
        Returns: 无
        """
        qt_model.RemoveLiveLoadCase(name=name)

    # endregion

    # region 钢束操作
    @staticmethod
    def add_tendon_group(name="", index=-1):
        """
        按照名称添加钢束组，添加时可指定钢束组id
        Args:
            name: 钢束组名称
            index: 钢束组编号(非必须参数)，默认自动识别
        Returns: 无
        """
        qt_model.AddTendonGroup(name=name, id=index)

    @staticmethod
    def remove_tendon_group(name="", index=-1):
        """
        按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组
        Args:
             name:钢束组名称,默认自动识别 (可选参数)
             index:钢束组编号,默认自动识别 (可选参数)
        Returns: 无
        """
        if name != "":
            qt_model.RemoveTendonGroup(name=name)
        elif index != -1:
            qt_model.RemoveTendonGroup(id=index)
        else:
            qt_model.RemoveAllStructureGroup()

    @staticmethod
    def add_tendon_property(name="", index=-1, tendon_type=TYP_PRE, material_id=1, duct_type=1,
                            steel_type=1, steel_detail=None, loos_detail=None, slip_info=None):
        """
        添加钢束特性
        Args:
             name:钢束特性名
             index:钢束编号,默认自动识别 (可选参数)
             tendon_type: 0-PRE 1-POST
             material_id: 钢材材料编号
             duct_type: 1-金属波纹管  2-塑料波纹管  3-铁皮管  4-钢管  5-抽芯成型
             steel_type: 1-钢绞线  2-螺纹钢筋
             steel_detail: 钢绞线[钢束面积,孔道直径,摩阻系数,偏差系数]  螺纹钢筋[钢筋直径,钢束面积,孔道直径,摩阻系数,偏差系数,张拉方式(1-一次张拉\2-超张拉)]
             loos_detail: 松弛信息[规范(1-公规 2-铁规),张拉(1-一次张拉 2-超张拉),松弛(1-一般松弛 2-低松弛)] (仅钢绞线需要)
             slip_info: 滑移信息[始端距离,末端距离]
        Returns: 无
        """
        if steel_detail is None:
            raise OperationFailedException("操作错误，钢束特性信息不能为空")
        if loos_detail is None:
            loos_detail = []
        if slip_info is None:
            slip_info = [0.006, 0.006]
        qt_model.AddTendonProperty(name=name, id=index, tendonType=tendon_type, materialId=material_id,
                                   ductType=duct_type, steelType=steel_type, steelDetail=steel_detail,
                                   loosDetail=loos_detail, slipInfo=slip_info)

    @staticmethod
    def add_tendon_3d(name="", property_name="", group_name="默认钢束组", num=1, line_type=1, position_type=TYP_STRAIGHT,
                      control_info=None, point_insert=None, tendon_direction=None,
                      rotation_angle=0, track_group="默认结构组"):
        """
        添加三维钢束
        Args:
             name:钢束名称
             property_name:钢束特性名称
             group_name:默认钢束组
             num:根数
             line_type:1-导线点  2-折线点
             position_type: 定位方式 1-直线  2-轨迹线
             control_info: 控制点信息[[x1,y1,z1,r1],[x2,y2,z2,r2]....]
             point_insert: 定位方式为直线时为插入点坐标[x,y,z], 轨迹线时为 [插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id]
             tendon_direction:直线钢束方向向量 x轴-[1,0,0] y轴-[0,1,0] (轨迹线时不用赋值)
             rotation_angle:绕钢束旋转角度
             track_group:轨迹线结构组名  (直线时不用赋值)
        Returns: 无
        """
        if tendon_direction is None:
            tendon_direction = []
        if control_info is None:
            raise OperationFailedException("操作错误，钢束形状控制点不能为空")
        if point_insert is None or len(point_insert) != 3:
            raise OperationFailedException("操作错误，钢束插入点信息不能为空且长度必须为3")
        qt_model.AddTendon3D(name=name, propertyName=property_name, groupName=group_name, num=num, lineType=line_type,
                             positionType=position_type, controlPoints=control_info,
                             pointInsert=point_insert, tendonDirection=tendon_direction,
                             rotationAngle=rotation_angle, trackGroup=track_group)

    @staticmethod
    def remove_tendon(name="", index=-1):
        """
        按照名称或编号删除钢束,默认时删除所有钢束
        Args:
             name:钢束名称
             index:钢束编号
        Returns: 无
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
        Args:
             name:钢束组名称
             index:钢束组编号
        Returns: 无
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
        Args:
             node_id:节点编号
             mass_info:[m,rmX,rmY,rmZ]
        Returns: 无
        """
        if mass_info is None:
            raise OperationFailedException("操作错误，节点质量信息列表不能为空")
        qt_model.AddNodalMass(nodeId=node_id, massInfo=mass_info)

    @staticmethod
    def remove_nodal_mass(node_id=-1):
        """
        删除节点质量
        Args:
             node_id:节点号
        Returns: 无
        """
        qt_model.RemoveNodalMass(nodeId=node_id)

    @staticmethod
    def add_pre_stress(index=-1, case_name="", tendon_name="", pre_type=2, force=1395000, group_name="默认荷载组"):
        """
        添加预应力
        Args:
             index:编号
             case_name:荷载工况名
             tendon_name:钢束名
             pre_type:预应力类型
             force:预应力
             group_name:边界组
        Returns: 无
        """
        qt_model.AddPreStress(caseName=case_name, tendonName=tendon_name, preType=pre_type, force=force, id=index, groupName=group_name)

    @staticmethod
    def remove_pre_stress(case_name="", tendon_name="", group_name="默认荷载组"):
        """
        删除预应力
        Args:
             case_name:荷载工况
             tendon_name:钢束组
             group_name:边界组名
        Returns: 无
        """
        qt_model.RemovePreStress(caseName=case_name, tendonName=tendon_name, groupName=group_name)

    # endregion

    # region 荷载操作
    @staticmethod
    def add_load_group(name="", index=-1):
        """
        根据荷载组名称添加荷载组
        Args:
             name: 荷载组名称
             index: 荷载组编号，默认自动识别 (可选参数)
        Returns: 无
        """
        if name != "":
            qt_model.AddLoadGroup(name=name, id=index)

    @staticmethod
    def remove_load_group(name="", index=-1):
        """
        根据荷载组名称或荷载组id删除荷载组,参数为默认时删除所有荷载组
        Args:
             name: 荷载组名称
             index: 荷载组编号
        Returns: 无
        """
        if name != "":
            qt_model.RemoveLoadGroup(name=name)
        elif index != -1:
            qt_model.RemoveLoadGroup(id=index)
        else:
            qt_model.RemoveAllLoadGroup()

    @staticmethod
    def add_nodal_force(case_name="", node_id=1, load_info=None, group_name="默认荷载组"):
        """
        添加节点荷载
             case_name:荷载工况名
             node_id:节点编号
             load_info:[Fx,Fy,Fz,Mx,My,Mz]
             group_name:荷载组名
        Returns: 无
        """
        if load_info is None or len(load_info) != 6:
            raise OperationFailedException("操作错误，节点荷载列表信息不能为空，且其长度必须为6")
        qt_model.AddNodalForce(caseName=case_name, nodeId=node_id, loadInfo=load_info, groupName=group_name)

    @staticmethod
    def remove_nodal_force(case_name="", node_id=-1):
        """
        删除节点荷载
        Args:
             case_name:荷载工况名
             node_id:节点编号
        Returns: 无
        """
        qt_model.RemoveNodalForce(caseName=case_name, nodeId=node_id)

    @staticmethod
    def add_node_displacement(case_name="", node_id=1, load_info=None, group_name="默认荷载组"):
        """
        添加节点位移
        Args:
             case_name:荷载工况名
             node_id:节点编号
             load_info:[Dx,Dy,Dz,Rx,Ry,Rz]
             group_name:荷载组名
        Returns: 无
        """
        if load_info is None or len(load_info) != 6:
            raise OperationFailedException("操作错误，节点位移列表信息不能为空，且其长度必须为6")
        qt_model.AddNodeDisplacement(caseName=case_name, nodeId=node_id, loadInfo=load_info, groupName=group_name)

    @staticmethod
    def remove_nodal_displacement(case_name="", node_id=-1):
        """
        删除节点位移
        Args:
             case_name:荷载工况名
             node_id:节点编号
        Returns: 无
        """
        qt_model.RemoveNodalDisplacement(caseName=case_name, nodeId=-node_id)

    @staticmethod
    def add_beam_load(case_name="", beam_id=1, load_type=1, coord_system=3, load_info=None, group_name="默认荷载组"):
        """
        添加梁单元荷载
        Args:
             case_name:荷载工况名
             beam_id:单元编号
             load_type:荷载类型
             coord_system:坐标系
             load_info:荷载信息
             group_name:荷载组名
        Returns: 无
        """
        qt_model.AddBeamLoad(caseName=case_name, beamId=beam_id, loadType=load_type,
                             coordinateSystem=coord_system, loadInfo=load_info, groupName=group_name)

    @staticmethod
    def remove_beam_load(case_name="", element_id=1, load_type=1, group_name="默认荷载组"):
        """
        删除梁单元荷载
        Args:
             case_name:荷载工况名
             element_id:单元号
             load_type:荷载类型
             group_name:边界组名
        Returns: 无
        """
        qt_model.RemoveBeamLoad(caseName=case_name, elementId=element_id, loadType=load_type, groupName=group_name)

    @staticmethod
    def add_initial_tension(element_id=1, case_name="", group_name="默认荷载组", tension=0, tension_type=1):
        """
        添加初始拉力
        Args:
             element_id:单元编号
             case_name:荷载工况名
             group_name:荷载组名
             tension:初始拉力
             tension_type:张拉类型
        Returns: 无
        """
        qt_model.AddInitialTension(elementId=element_id, caseName=case_name, groupName=group_name, tension=tension, tensionType=tension_type)

    @staticmethod
    def add_cable_length_load(element_id=1, case_name="", group_name="默认荷载组", length=0, tension_type=1):
        """
        添加索长张拉
        Args:
             element_id:单元类型
             case_name:荷载工况名
             group_name:荷载组名
             length:长度
             tension_type:张拉类型
        Returns: 无
        """
        qt_model.AddCableLenghtLoad(elementId=element_id, caseName=case_name, groupName=group_name, length=length, tensionType=tension_type)

    @staticmethod
    def add_plate_element_load(element_id=1, case_name="", load_type=1, load_place=1, coord_system=1, group_name="默认荷载组", load_info=None):
        """
        添加版单元荷载
        Args:
             element_id:单元id
             case_name:荷载工况名
             load_type:荷载类型
             load_place:荷载位置
             coord_system:坐标系
             group_name:荷载组名
             load_info:荷载信息
        Returns: 无
        """
        qt_model.AddPlateElementLoad(elementId=element_id, caseName=case_name, loadType=load_type, loadPlace=load_place,
                                     coordSystem=coord_system, groupName=group_name, loadInfo=load_info)

    @staticmethod
    def add_deviation_parameter(name="", element_type=1, parameter_info=None):
        """
        添加制造误差
        Args:
             name:名称
             element_type:单元类型
             parameter_info:参数列表
        Returns: 无
        """
        if parameter_info is None:
            raise OperationFailedException("操作错误，制造误差信息不能为空")
        qt_model.AddDeviationParameter(name=name, elementType=element_type, parameterInfo=parameter_info)

    @staticmethod
    def add_deviation_load(element_id=1, case_name="", parameter_name=None, group_name="默认荷载组"):
        """
        添加制造误差荷载
        Args:
             element_id:单元编号
             case_name:荷载工况名
             parameter_name:参数名
             group_name:荷载组名
        Returns: 无
        """
        if parameter_name is None:
            raise OperationFailedException("操作错误，制造误差名称信息不能为空")
        qt_model.AddDeviationLoad(elementId=element_id, caseName=case_name, parameterName=parameter_name, groupName=group_name)

    @staticmethod
    def add_element_temperature(element_id=1, case_name="", temperature=1, group_name="默认荷载组"):
        """
        添加单元温度
        Args:
             element_id:单元编号
             case_name:荷载工况名
             temperature:温度
             group_name:荷载组名
        Returns: 无
        """
        qt_model.AddElementTemperature(elementId=element_id, caseName=case_name, temperature=temperature, groupName=group_name)

    @staticmethod
    def add_gradient_temperature(element_id=1, case_name="", temperature=1, section_oriental=1, element_type=1, group_name=""):
        """
        添加梯度温度
             element_id:单元编号
             case_name:荷载工况名
             temperature:温度
             section_oriental:截面方向
             element_type:单元类型
             group_name:荷载组名
        Returns: 无
        """
        qt_model.AddGradientTemperature(elementId=element_id, caseName=case_name, temperature=temperature,
                                        sectionOriental=section_oriental, elementType=element_type, groupNmae=group_name)

    @staticmethod
    def add_beam_section_temperature(element_id=1, case_name="", paving_thick=0, temperature_type=1, paving_type=1, group_name="默认荷载组"):
        """
        添加梁截面温度
        Args:
             element_id:单元编号
             case_name:荷载工况名
             paving_thick:铺设厚度
             temperature_type:温度类型
             paving_type:铺设类型
             group_name:荷载组名
        Returns: 无
        """
        qt_model.AddBeamSectionTemperature(elementId=element_id, caseName=case_name, pavingThickness=paving_thick,
                                           temperatureType=temperature_type, pavingType=paving_type, groupName=group_name)

    @staticmethod
    def add_index_temperature(element_id=1, case_name="", temperature=0, index=1, group_name="默认荷载组"):
        """
        添加指数温度
        Args:
             element_id:单元编号
             case_name:荷载工况名
             temperature:单元类型
             index:指数
             group_name:荷载组名
        Returns: 无
        """
        qt_model.AddIndexTemperature(elementId=element_id, caseName=case_name, temperature=temperature, index=index, groupName=group_name)

    @staticmethod
    def add_plate_temperature(element_id=1, case_name="", temperature=0, group_name="默认荷载组"):
        """
        添加顶板温度
        Args:
             element_id:单元编号
             case_name:荷载
             temperature:温度
             group_name:荷载组名
        Returns: 无
        """
        qt_model.AddTopPlateTemperature(elementId=element_id, caseName=case_name, temperature=temperature, groupName=group_name)

    # endregion

    # region 沉降操作
    @staticmethod
    def add_sink_group(name="", sink=0.1, node_ids=None):
        """
        添加沉降组
        Args:
             name: 沉降组名
             sink: 沉降值
             node_ids: 节点编号
        Returns: 无
        """
        if node_ids is None:
            raise OperationFailedException("操作错误，沉降定义中节点信息不能为空")
        qt_model.AddSinkGroup(name=name, sinkValue=sink, nodeIds=node_ids)

    @staticmethod
    def remove_sink_group(name=""):
        """
        按照名称删除沉降组
        Args:
             name:沉降组名,默认删除所有沉降组
        Returns: 无
        """
        if name == "":
            qt_model.RemoveAllSinkGroup()
        else:
            qt_model.RemoveSinkGroup(name=name)

    @staticmethod
    def add_sink_case(name="", sink_groups=None):
        """
        添加沉降工况
        Args:
             name:荷载工况名
             sink_groups:沉降组名
        Returns: 无
        """
        if sink_groups is None:
            raise OperationFailedException("操作错误，沉降工况定义中沉降组信息不能为空")
        qt_model.AddSinkCase(name=name, sinkGroups=sink_groups)

    @staticmethod
    def remove_sink_case(name=""):
        """
        按照名称删除沉降工况,不输入名称时默认删除所有沉降工况
        Args:
             name:沉降工况名
        Returns: 无
        """
        if name == "":
            qt_model.RemoveAllSinkCase()
        else:
            qt_model.RemoveSinkCase()

    @staticmethod
    def add_concurrent_reaction(names=None):
        """
        添加并发反力组
        Args:
             names: 结构组名称集合
        Returns: 无
        """
        if names is None:
            raise OperationFailedException("操作错误，添加并发反力组时结构组名称不能为空")
        qt_model.AddConcurrentReaction(names=names)

    @staticmethod
    def remove_concurrent_reaction():
        """
        删除并发反力组
        Returns: 无
        """
        qt_model.RemoveConcurrentRection()

    @staticmethod
    def add_concurrent_force():
        """
        添加并发内力
        Returns: 无
        """
        qt_model.AddConcurrentForce()

    @staticmethod
    def remove_concurrent_force():
        """
        删除并发内力
        Returns: 无
        """
        qt_model.RemoveConcurrentForce()

    @staticmethod
    def add_load_case(index=-1, name="", load_case_type=LD_CS):
        """
        添加荷载工况
        Args:
            index:沉降工况编号
            name:沉降名
            load_case_type:荷载工况类型
        Returns: 无
        """
        qt_model.AddLoadCase(id=index, name=name, loadCaseType=load_case_type)

    @staticmethod
    def remove_load_case(index=-1, name=""):
        """
        删除荷载工况,参数均为默认时删除全部荷载工况
        Args:
            index:荷载编号
            name:荷载名
        Returns: 无
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
        Returns: 无
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
        Args:
            name:施工阶段信息
            duration:时长
            active_structures:激活结构组信息 [[结构组名，(int)龄期，施工阶段名，(int)1-变形法 2-接线法 3-无应力法],...]
            delete_structures:钝化结构组信息 [结构组1，结构组2,...]
            active_boundaries:激活边界组信息 [[边界组1，(int)0-变形前 1-变形后],...]
            delete_boundaries:钝化边界组信息 [边界组1，结构组2,...]
            active_loads:激活荷载组信息 [[荷载组1,(int)0-开始 1-结束],...]
            delete_loads:钝化荷载组信息 [[荷载组1,(int)0-开始 1-结束],...]
            temp_loads:临时荷载信息 [荷载组1，荷载组2,..]
            index:施工阶段编号，默认自动添加
        Returns: 无
        """
        if temp_loads is None:
            temp_loads = []
        if delete_loads is None:
            delete_loads = []
        if active_loads is None:
            active_loads = []
        if delete_boundaries is None:
            delete_boundaries = []
        if active_structures is None:
            active_structures = []
        if delete_structures is None:
            delete_structures = []
        if active_boundaries is None:
            active_boundaries = []
        qt_model.AddConstructionStage(name=name, duration=duration, activeStructures=active_structures, inActiveStructures=delete_structures
                                      , activeBoundaries=active_boundaries, inActiveBoundaries=delete_boundaries, activeLoads=active_loads,
                                      inActiveLoads=delete_loads, tempLoads=temp_loads, id=index)

    @staticmethod
    def remove_construction_stage(name=""):
        """
        按照施工阶段名删除施工阶段
        Args:
            name:所删除施工阶段名称
        Returns: 无
        """
        qt_model.RemoveConstructionStage(name=name)

    @staticmethod
    def remove_all_construction_stage():
        """
        删除所有施工阶段
        Returns: 无
        """
        qt_model.RemoveAllConstructionStage()

    @staticmethod
    def add_load_combine(name="", combine_type=1, describe="", combine_info=None):
        """
        添加荷载组合
        Args:
            name:荷载组合名
            combine_type:荷载组合类型
            describe:描述
            combine_info:荷载组合信息
        Returns: 无
        """
        if combine_info is None:
            combine_info = []
        qt_model.AddLoadCombine(name=name, loadCombineType=combine_type, describe=describe, caseAndFactor=combine_info)

    @staticmethod
    def remove_load_combine(name=""):
        """
        删除荷载组合
        Args:
             name:指定删除荷载组合名，默认时则删除所有荷载组合
        Returns: 无
        """
        if name != "":
            qt_model.DeleteLoadCombine(name=name)
        else:
            qt_model.DeleteAllLoadCombine()
    # endregion


class OperationFailedException(Exception):
    """用户操作失败时抛出的异常"""
    pass

    """
                添加截面信息
                Args:
                     index: 截面编号,默认自动识别
                     name:截面名称
                     section_type:截面类型
                     section_info:截面信息 (必要参数)
                     bias_type:偏心类型
                     center_type:中心类型
                     shear_consider:考虑剪切
                     bias_point:自定义偏心点(仅自定义类型偏心需要)
                Returns: 无
                """
