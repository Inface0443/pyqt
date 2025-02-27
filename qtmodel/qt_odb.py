from __main__ import qt_model
from .qt_db import *
from typing import Union, List


class Odb:
    """
    获取模型计算结果和模型信息
    """

    # region 视图控制
    @staticmethod
    def display_node_id(show_id: bool = True):
        """
        设置节点号显示
        Args:
            show_id:是否打开节点号显示
        Example:
            odb.display_node_id()
            odb.display_node_id(False)
        Returns: 无
        """
        try:
            qt_model.DisplayNodeId(showId=show_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def display_element_id(show_id: bool = True):
        """
        设置单元号显示
        Args:
            show_id:是否打开单元号显示
        Example:
            odb.display_element_id()
            odb.display_element_id(False)
        Returns: 无
        """
        try:
            qt_model.DisplayElementId(showId=show_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def set_view_camera(camera_point: tuple[float, float, float], focus_point: tuple[float, float, float],
                        camera_rotate: tuple[float, float, float] = (45, 45, 0), scale: float = 0.5):
        """
        更改三维显示相机设置
        Args:
            camera_point: 相机坐标点
            focus_point: 相机焦点
            camera_rotate:相机绕XYZ旋转角度
            scale: 缩放系数
        Example:
           odb.set_view_camera(camera_point=(-100,-100,100),focus_point=(0,0,0))
        Returns: 无
        """
        try:
            qt_model.SetViewCamera(direction=[camera_point[0], camera_point[1], camera_point[2], focus_point[0], focus_point[1], focus_point[2],
                                              camera_rotate[0], camera_rotate[1], camera_rotate[2], scale])
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def set_view_direction(direction: int = 1, horizontal_degree: float = 0, vertical_degree: float = 0, scale: float = 1):
        """
        更改三维显示默认视图
        Args:
            direction: 1-空间视图1 2-前视图 3-三维视图2 4-左视图  5-顶视图 6-右视图 7-空间视图3 8-后视图 9-空间视图4 10-底视图
            horizontal_degree:水平向旋转角度
            vertical_degree:竖向旋转角度
            scale:缩放系数
        Example:
           odb.set_view_direction(direction=1,scale=1.2)
        Returns: 无
        """
        try:
            qt_model.SetViewDirection(direction=direction, horizontalDegree=horizontal_degree, verticalDegree=vertical_degree, scale=scale)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def activate_structure(node_ids: list[int] = None, element_ids: list[int] = None):
        """
        激活指定阶段和单元,默认激活所有
        Args:
            node_ids: 节点集合
            element_ids: 单元集合
        Example:
           odb.activate_structure(node_ids=[1,2,3],element_ids=[1,2,3])
        Returns: 无
        """
        try:
            qt_model.ActivateStructure(nodeIds=node_ids, elementIds=element_ids)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def set_unit(unit_force: str = "KN", unit_length: str = "MM"):
        """
        修改视图显示时单位制,不影响建模
        Args:
            unit_force: 支持 N KN TONF KIPS LBF
            unit_length: 支持 M MM CM IN FT
        Example:
           odb.set_unit(unit_force="N",unit_length="M")
        Returns: 无
        """
        try:
            qt_model.SetUnit(unitForce=unit_force, unit_length=unit_length)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_display():
        """
        删除当前所有显示,包括边界荷载钢束等全部显示
        Args: 无
        Example:
           odb.remove_display()
        Returns: 无
        """
        try:
            qt_model.DisplayReset()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def save_png(file_path: str):
        """
        保存当前模型窗口图形信息
        Args:
            file_path: 文件全路径
        Example:
           odb.save_png(file_path=r"D:\\QT\\aa.png")
        Returns: 无
        """
        try:
            qt_model.SavePng(file_path)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def set_render(flag: bool = True):
        """
        消隐设置开关
        Args:
            flag: 默认设置打开消隐
        Example:
           odb.set_render(flag=True)
        Returns: 无
        """
        try:
            qt_model.SetRender(flag)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def change_construct_stage(stage: int = 0):
        """
        消隐设置开关
        Args:
            stage: 施工阶段名称或施工阶段号  0-基本
        Example:
           odb.change_construct_stage(0)
           odb.change_construct_stage(stage=1)
        Returns: 无
        """
        try:
            qt_model.ChangeConstructStage(stage)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 静力结果查看
    @staticmethod
    def get_element_stress(element_id: (Union[int, List[int]]) = 1, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取单元应力,支持单个单元和单元列表
        Args:
            element_id: 单元编号,支持整数或整数型列表
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        Example:
            odb.get_element_stress(element_id=1,stage_id=1)
            odb.get_element_stress(element_id=[1,2,3],stage_id=1)
            odb.get_element_stress(element_id=1,stage_id=-1,case_name="工况名")
        Returns: json字符串,包含信息为list[dict] or dict
        """
        try:
            bf_list = qt_model.GetElementStress(element_id, stage_id, result_kind, increment_type, case_name)
            list_res = []
            for item in bf_list:
                if item.ElementType == "BEAM":
                    stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4], item.StressI[5],
                                item.StressI[6], item.StressI[7], item.StressI[8]]
                    stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4], item.StressJ[5],
                                item.StressJ[6], item.StressJ[7], item.StressJ[8]]
                    list_res.append(str(BeamElementStress(item.ElementId, stress_i, stress_j)))
                elif item.ElementType == "SHELL" or item.ElementType == "PLATE":
                    stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4]]
                    stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4]]
                    stress_k = [item.StressK[0], item.StressK[1], item.StressK[2], item.StressK[3], item.StressK[4]]
                    stress_l = [item.StressL[0], item.StressL[1], item.StressL[2], item.StressL[3], item.StressL[4]]
                    stress_i2 = [item.StressI2[0], item.StressI2[1], item.StressI2[2], item.StressI2[3], item.StressI2[4]]
                    stress_j2 = [item.StressJ2[0], item.StressJ2[1], item.StressJ2[2], item.StressJ2[3], item.StressJ2[4]]
                    stress_k2 = [item.StressK2[0], item.StressK2[1], item.StressK2[2], item.StressK2[3], item.StressK2[4]]
                    stress_l2 = [item.StressL2[0], item.StressL2[1], item.StressL2[2], item.StressL2[3], item.StressL2[4]]
                    list_res.append(str(ShellElementStress(item.ElementId, stress_i, stress_j, stress_k, stress_l,
                                                           stress_i2, stress_j2, stress_k2, stress_l2)))
                elif item.ElementType == "CABLE" or item.ElementType == "LINK" or item.ElementType == "TRUSS":
                    stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4], item.StressI[5],
                                item.StressI[6], item.StressI[7], item.StressI[8]]
                    stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4], item.StressJ[5],
                                item.StressJ[6], item.StressJ[7], item.StressJ[8]]
                    list_res.append(str(TrussElementStress(item.ElementId, stress_i, stress_j)))
                elif item.ElementType == "COM-BEAM":
                    stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4], item.StressI[5],
                                item.StressI[6], item.StressI[7], item.StressI[8]]
                    stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4], item.StressJ[5],
                                item.StressJ[6], item.StressJ[7], item.StressJ[8]]
                    stress_i2 = [item.StressI2[0], item.StressI2[1], item.StressI2[2], item.StressI2[3], item.StressI2[4], item.StressI2[5],
                                 item.StressI2[6], item.StressI2[7], item.StressI2[8]]
                    stress_j2 = [item.StressJ2[0], item.StressJ2[1], item.StressJ2[2], item.StressJ2[3], item.StressJ2[4], item.StressJ2[5],
                                 item.StressJ2[6], item.StressJ2[7], item.StressJ2[8]]
                    list_res.append(str(CompositeBeamStress(element_id, stress_i, stress_j, stress_i2, stress_j2)))
                else:
                    raise TypeError(f"操作错误,不存在{item.ElementType}类型")
            return json.dumps(list_res) if len(list_res) > 1 else list_res[0]
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_element_force(element_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取单元内力,支持单个单元和单元列表
        Args:
            element_id: 单元编号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        Example:
            odb.get_element_force(element_id=1,stage_id=1)
            odb.get_element_force(element_id=[1,2,3],stage_id=1)
            odb.get_element_force(element_id=1,stage_id=-1,case_name="工况名")
        Returns: json字符串,包含信息为list[dict] or dict
        """
        try:
            if type(element_id) != int and type(element_id) != list:
                raise TypeError("类型错误,element_id仅支持 int和 list[int]")
            bf_list = qt_model.GetElementForce(element_id, stage_id, result_kind, increment_type, case_name)
            list_res = []
            for item in bf_list:
                if item.ElementType == "BEAM":
                    force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                    force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                    list_res.append(str(BeamElementForce(item.ElementId, force_i, force_j)))
                elif item.ElementType == "SHELL" or item.ElementType == "PLATE":
                    force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                    force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                    force_k = [item.ForceK.Fx, item.ForceK.Fy, item.ForceK.Fz, item.ForceK.Mx, item.ForceK.My, item.ForceK.Mz]
                    force_l = [item.ForceL.Fx, item.ForceL.Fy, item.ForceL.Fz, item.ForceL.Mx, item.ForceL.My, item.ForceL.Mz]
                    list_res.append(str(ShellElementForce(item.ElementId, force_i, force_j, force_k, force_l)))
                elif item.ElementType == "CABLE" or item.ElementType == "LINK" or item.ElementType == "TRUSS":
                    force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                    force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                    list_res.append(str(TrussElementForce(item.ElementId, force_i, force_j)))
                elif item.ElementType == "COM-BEAM":
                    all_force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                    all_force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                    main_force_i = [item.MainForceI.Fx, item.MainForceI.Fy, item.MainForceI.Fz, item.MainForceI.Mx, item.MainForceI.My,
                                    item.MainForceI.Mz]
                    main_force_j = [item.MainForceJ.Fx, item.MainForceJ.Fy, item.MainForceJ.Fz, item.MainForceJ.Mx, item.MainForceJ.My,
                                    item.MainForceJ.Mz]
                    sub_force_i = [item.SubForceI.Fx, item.SubForceI.Fy, item.SubForceI.Fz, item.SubForceI.Mx, item.SubForceI.My, item.SubForceI.Mz]
                    sub_force_j = [item.SubForceJ.Fx, item.SubForceJ.Fy, item.SubForceJ.Fz, item.SubForceJ.Mx, item.SubForceJ.My, item.SubForceJ.Mz]
                    is_composite = item.IsComposite
                    shear_force = item.ShearForce
                    list_res.append(str(CompositeElementForce(item.ElementId, all_force_i, all_force_j, shear_force,
                                                              main_force_i, main_force_j, sub_force_i, sub_force_j, is_composite)))

                else:
                    raise TypeError(f"操作错误,不存在{item.ElementType}类型")
            return json.dumps(list_res) if len(list_res) > 1 else list_res[0]
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_reaction(node_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取节点反力
        Args:
            node_id: 节点编号,支持整数或整数型列表
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        Example:
            odb.get_reaction(node_id=1,stage_id=1)
            odb.get_reaction(node_id=[1,2,3],stage_id=1)
            odb.get_reaction(node_id=1,stage_id=-1,case_name="工况名")
        Returns: json字符串,包含信息为list[dict] or dict
        """
        try:
            bs_list = qt_model.GetSupportReaction(node_id, stage_id, result_kind, increment_type, case_name)
            list_res = []
            for item in bs_list:
                force = [item.Force.Fx, item.Force.Fy, item.Force.Fz, item.Force.Mx, item.Force.My, item.Force.Mz]
                list_res.append(str(SupportReaction(item.NodeId, force)))
            return json.dumps(list_res) if len(list_res) > 1 else list_res[0]
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_node_displacement(node_id: (Union[int, List[int]]) = None, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1,
                              case_name=""):
        """
        获取节点,支持单个节点和节点列表
        Args:
            node_id: 节点号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        Example:
            odb.get_node_displacement(node_id=1,stage_id=1)
            odb.get_node_displacement(node_id=[1,2,3],stage_id=1)
            odb.get_node_displacement(node_id=1,stage_id=-1,case_name="工况名")
        Returns: json字符串,包含信息为list[dict] or dict
        """
        try:
            bf_list = qt_model.GetNodeDisplacement(node_id, stage_id, result_kind, increment_type, case_name)
            list_res = []
            for item in bf_list:
                displacements = [item.Displacement.Dx, item.Displacement.Dy, item.Displacement.Dz,
                                 item.Displacement.Rx, item.Displacement.Ry, item.Displacement.Rz]
                list_res.append(str(NodeDisplacement(item.NodeId, displacements)))
            return json.dumps(list_res) if len(list_res) > 1 else list_res[0]
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_self_concurrent_reaction(node_id: int, case_name: str):
        """
        获取自并发反力
        Args:
          node_id:节点号
          case_name:工况号
        Example:
          odb.get_self_concurrent_reaction(node_id=1,case_name="工况1_Fx最大")
        Returns: json字符串,包含信息为dict
        """
        try:
            res_dict = qt_model.GetSelfConcurrentReaction(nodeId=node_id, loadCaseName=case_name)
            return json.dumps(res_dict)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_all_concurrent_reaction(node_id: int, case_name: str):
        """
        获取完全并发反力
        Args:
          node_id:节点号
          case_name:工况号
        Example:
          odb.get_all_concurrent_reaction(node_id=1,case_name="工况1_Fx最大")
        Returns: json字符串,包含信息为dict
        """
        try:
            res_dict = qt_model.GetAllConcurrentReaction(nodeId=node_id, loadCaseName=case_name)
            return json.dumps(res_dict)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_beam_concurrent_force(ele_id: (Union[int, List[int]]) = None, case_name: str = ""):
        """
        获取梁单元并发内力
        Args:
          ele_id:单元号
          case_name:工况号
        Example:
          odb.get_beam_concurrent_force(ele_id=1,case_name="工况1_Fx最大")
        Returns: json字符串,包含信息为dict
        """
        try:
            res_dict = qt_model.GetBeamConcurrentForce(eleId=ele_id, loadCaseName=case_name)
            return json.dumps(res_dict)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_composite_beam_concurrent_force(ele_id: (Union[int, List[int]]) = None, case_name: str = ""):
        """
        获取组合梁单元并发内力
        Args:
          ele_id:单元号
          case_name:工况号
        Example:
          odb.get_composite_beam_concurrent_force(ele_id=1,case_name="工况1_Fx最大")
        Returns: json字符串,包含信息为dict
        """
        try:
            res_dict = qt_model.GetCompositeBeamConcurrentForce(eleId=ele_id, loadCaseName=case_name)
            return json.dumps(res_dict)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 动力结果查看
    @staticmethod
    def get_vibration_node_displacement(node_id: (Union[int, List[int]]) = None, mode: int = 1):
        """
        获取指定节点指定模态的振型向量
        Args:
            node_id: 节点号
            mode: 模态号
        Example:
            odb.get_vibration_node_displacement(node_id=1,mode=1)
        Returns: json字符串,包含信息为list[dict] or dict
        """
        try:
            bf_list = qt_model.GetVibrationNodeDisplacement(nodeIds=node_id, mode=mode)
            list_res = []
            for item in bf_list:
                displacements = [item.Displacement.Dx, item.Displacement.Dy, item.Displacement.Dz,
                                 item.Displacement.Rx, item.Displacement.Ry, item.Displacement.Rz]
                list_res.append(str(NodeDisplacement(item.NodeId, displacements)))
            return json.dumps(list_res) if len(list_res) > 1 else list_res[0]
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_period_and_frequency(mode: int = 1):
        """
        获取周期和频率
        Args:
            mode:模态号
        Example:
            odb.get_period_and_frequency(mode=1)
        Returns: json字符串,包含信息为dict
        """
        try:
            res_dict = qt_model.GetPeriodAndFrequency(mode=mode)
            return json.dumps(res_dict)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_participation_mass(mode: int = 1):
        """
        获取振型参与质量百分比
        Args:
            mode:模态号
        Example:
            odb.get_participation_mass(mode=1)
        Returns: json字符串,包含信息为dict
        """
        try:
            res_dict = qt_model.GetParticipationMass(mode=mode)
            return json.dumps(res_dict)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_participation_factor(mode: int = 1):
        """
        获取振型参与质量系数
        Args:
            mode:模态号
        Example:
            odb.get_participation_factor(mode=1)
        Returns: json字符串,包含信息为dict
        """
        try:
            res_dict = qt_model.GetParticipationFactor(mode=mode)
            return json.dumps(res_dict)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 绘制模型结果
    @staticmethod
    def plot_reaction_result(file_path: str, stage_id: int = 1, load_case_name: str = "", show_increment: bool = False,
                             envelope_type: int = 1, component: int = 1,
                             show_number: bool = True, text_rotation=0, max_min_kind: int = -1,
                             show_legend: bool = True, digital_count=3, show_exponential: bool = True, arrow_scale: float = 1):
        """
        保存结果图片到指定文件甲
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 0-Fx 1-Fy 2-Fz 3-Fxyz 4-Mx 5-My 6-Mz 7-Mxyz
            show_number: 数值选项卡开启
            show_legend: 图例选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            arrow_scale:箭头大小
        Example:
            odb.plot_reaction_result(file_path=r"D:\\图片\\反力图.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotReactionResult(filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                                        envelopeType=envelope_type, component=component,
                                        showNumber=show_number, textRotationAngle=text_rotation, maxMinValueKind=max_min_kind,
                                        showLegend=show_legend, digitalCount=digital_count,
                                        showAsExponential=show_exponential, arrowScale=arrow_scale)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_displacement_result(file_path: str, stage_id: int = 1, load_case_name: str = "", show_increment: bool = False,
                                 envelope_type: int = 1, component: int = 1,
                                 show_deformed: bool = True, deformed_scale: float = 1.0, deformed_actual: bool = False,
                                 show_number: bool = True, text_rotation=0, max_min_kind: int = 1,
                                 show_legend: bool = True, digital_count=3, show_exponential: bool = True, show_pre_deformed: bool = True):
        """
        保存结果图片到指定文件甲
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 0-Dx 1-Dy 2-Dz 3-Rx 4-Ry 5-Rz 6-Dxy 7-Dyz 8-Dxz 9-Dxyz
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            show_legend: 图例选项卡开启
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            show_pre_deformed: 显示变形前
        Example:
            odb.plot_displacement_result(file_path=r"D:\\图片\\变形图.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotDisplacementResult(filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                                            envelopeType=envelope_type, component=component,
                                            showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                                            showNumber=show_number, textRotationAngle=text_rotation, digitalCount=digital_count,
                                            showAsExponential=show_exponential, maxMinValueKind=max_min_kind,
                                            showLegend=show_legend, showUndeformedShape=show_pre_deformed)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_beam_element_force(file_path: str, stage_id: int = 1, load_case_name: str = "合计", show_increment: bool = False,
                                envelope_type: int = 1, component: int = 0,
                                show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 0,
                                show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                                show_pre_deformed: bool = False, position: int = 0):
        """
        绘制梁单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 0-Dx 1-Dy 2-Dz 3-Rx 4-Ry 5-Rz 6-Dxy 7-Dyz 8-Dxz 9-Dxyz
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            show_legend: 图例选项卡开启
            show_pre_deformed: 显示变形前
            position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部
        Example:
            odb.plot_beam_element_force(file_path=r"D:\\图片\\梁内力.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotBeamElementForce(
                filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                envelopeType=envelope_type, component=component,
                showLineChart=show_line_chart, lineScale=line_scale, flipPlot=flip_plot,
                showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                showNumber=show_number, textRotationAngle=text_rotation, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed, position=position)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_truss_element_force(file_path: str, stage_id: int = 1, load_case_name: str = "合计", show_increment: bool = False,
                                 envelope_type: int = 1, component: int = 0,
                                 show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                 show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                 show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 0,
                                 show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                                 show_pre_deformed: bool = False, position: int = 0):
        """
        绘制杆单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 0-N 1-Fx 2-Fy 3-Fz
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            show_legend: 图例选项卡开启
            show_pre_deformed: 显示变形前
            position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部
        Example:
            odb.plot_truss_element_force(file_path=r"D:\\图片\\杆内力.png",load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotTrussElementForce(
                filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                envelopeType=envelope_type, component=component,
                showLineChart=show_line_chart, lineScale=line_scale, flipPlot=flip_plot,
                showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                showNumber=show_number, textRotationAngle=text_rotation, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed, position=position)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_plate_element_force(file_path: str, stage_id: int = 1, load_case_name: str = "合计", show_increment: bool = False,
                                 envelope_type: int = 1, force_kind: int = 0, component: int = 0,
                                 show_number: bool = False, text_rotation_angle: int = 0, max_min_kind: int = 0,
                                 show_deformed: bool = True, deformed_scale: float = 1.0, deformed_actual: bool = False,
                                 show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                                 show_pre_deformed: bool = False, ):
        """
        绘制板单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Fxx 1-Fyy 2-Fxy 3-Mxx 4-Myy 5-Mxy
            force_kind: 力类型
            load_case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelope_type: 包络类型
            show_number: 是否显示数值
            show_deformed: 是否显示变形形状
            show_pre_deformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotation_angle: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment: 是否显示增量结果
        Example:
            odb.plot_plate_element_force(file_path=r"D:\\图片\\板内力.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotPlateElementForce(
                filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                envelopeType=envelope_type, forceKind=force_kind, component=component,
                showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                showNumber=show_number, textRotationAngle=text_rotation_angle, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_composite_beam_force(file_path: str, stage_id: int = 1, load_case_name: str = "合计", show_increment: bool = False,
                                  envelope_type: int = 1, mat_type: int = 0, component: int = 0,
                                  show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                  show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                  show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 0,
                                  show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                                  show_pre_deformed: bool = False, position: int = 0):
        """
        绘制组合梁单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            mat_type: 材料类型 0-主材 1-辅材 2-主材+辅材
            component: 分量编号 0-Fx 1-Fy 2-Fz 3-Mx 4-My 5-Mz
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            show_legend: 图例选项卡开启
            show_pre_deformed: 显示变形前
            position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部
        Example:
            odb.plot_composite_beam_force(file_path=r"D:\\图片\\组合梁内力.png",mat_type=0,component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotCompositeBeamForce(
                filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                envelopeType=envelope_type, matType=mat_type, component=component,
                showLineChart=show_line_chart, lineScale=line_scale, flipPlot=flip_plot,
                showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                showNumber=show_number, textRotationAngle=text_rotation, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed, position=position)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_beam_element_stress(file_path: str, stage_id: int = 1, load_case_name: str = "合计", show_increment: bool = False,
                                 envelope_type: int = 1, component: int = 0,
                                 show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                 show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                 show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 0,
                                 show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                                 show_pre_deformed: bool = False, position: int = 0):
        """
        绘制梁单元应力结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 0-轴力分量 1-Mz分量 2-My分量 3-组合包络 4-左上 5-右上 6-右下 7-左下
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            show_legend: 图例选项卡开启
            show_pre_deformed: 显示变形前
            position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部
        Example:
            odb.plot_beam_element_stress(file_path=r"D:\\图片\\梁应力.png",show_line_chart=False,component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotBeamElementStress(
                filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                envelopeType=envelope_type, component=component,
                showLineChart=show_line_chart, lineScale=line_scale, flipPlot=flip_plot,
                showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                showNumber=show_number, textRotationAngle=text_rotation, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed, position=position)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_truss_element_stress(file_path: str, stage_id: int = 1, load_case_name: str = "合计", show_increment: bool = False, envelope_type: int = 1,
                                  show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                  show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                  show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 0,
                                  show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                                  show_pre_deformed: bool = False, position: int = 0):
        """
        绘制杆单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            show_legend: 图例选项卡开启
            show_pre_deformed: 显示变形前
            position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部
        Example:
            odb.plot_truss_element_stress(file_path=r"D:\\图片\\杆应力.png",load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotTrussElementStress(
                filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment, envelopeType=envelope_type,
                showLineChart=show_line_chart, lineScale=line_scale, flipPlot=flip_plot,
                showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                showNumber=show_number, textRotationAngle=text_rotation, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed, position=position)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_composite_beam_stress(file_path: str, stage_id: int = 1, load_case_name: str = "合计", show_increment: bool = False,
                                   envelope_type: int = 1, mat_type: int = 0, component: int = 0,
                                   show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                   show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                   show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 0,
                                   show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                                   show_pre_deformed: bool = False, position: int = 0):
        """
        绘制组合梁单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            mat_type: 材料类型 0-主材 1-辅材
            component: 分量编号 0-轴力分量 1-Mz分量 2-My分量 3-包络 4-左上 5-右上 6-左下 7-右下
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            show_legend: 图例选项卡开启
            show_pre_deformed: 显示变形前
            position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部
        Example:
            odb.plot_composite_beam_stress(file_path=r"D:\\图片\\组合梁应力.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotCompositeBeamStress(
                filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                envelopeType=envelope_type, matType=mat_type, component=component,
                showLineChart=show_line_chart, lineScale=line_scale, flipPlot=flip_plot,
                showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                showNumber=show_number, textRotationAngle=text_rotation, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed, position=position)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_plate_element_stress(file_path: str, stage_id: int = 1, load_case_name: str = "合计", show_increment: bool = False,
                                  envelope_type: int = 1, stress_kind: int = 0, component: int = 0,
                                  show_number: bool = False, text_rotation_angle: int = 0, max_min_kind: int = 0,
                                  show_deformed: bool = True, deformed_scale: float = 1.0, deformed_actual: bool = False,
                                  show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                                  show_pre_deformed: bool = False, position: int = 0):
        """
        绘制板单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Fxx 1-Fyy 2-Fxy 3-Mxx 4-Myy 5-Mxy
            stress_kind: 力类型 0-单元 1-节点平均
            load_case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelope_type: 包络类型
            show_number: 是否显示数值
            show_deformed: 是否显示变形形状
            show_pre_deformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotation_angle: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment: 是否显示增量结果
            position: 位置 0-板顶 1-板底 2-绝对值最大
        Example:
            odb.plot_plate_element_stress(file_path=r"D:\\图片\\板应力.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotPlateElementStress(
                filePath=file_path, stageId=stage_id, loadCaseName=load_case_name, showIncrementResult=show_increment,
                envelopeType=envelope_type, stressKind=stress_kind, component=component,
                showAsDeformedShape=show_deformed, deformedScale=deformed_scale, deformedActual=deformed_actual,
                showNumber=show_number, textRotationAngle=text_rotation_angle, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed, position=position)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_vibration_mode(file_path: str = "", mode: int = 1, show_number: bool = True, text_rotation_angle: float = 0, max_min_kind: int = 0,
                            show_legend: bool = True, digital_count: int = 3, show_exponential: bool = True,
                            show_pre_deformed: bool = False):
        """
        绘制板单元结果图并保存到指定文件
        Args:
           file_path: 保存路径名
           mode: 模态号
           show_number: 是否显示数值
           show_pre_deformed: 是否显示未变形形状
           show_legend: 是否显示图例
           text_rotation_angle: 数值选项卡内文字旋转角度
           digital_count: 小数点位数
           show_exponential: 是否以指数形式显示
           max_min_kind: 最大最小值显示类型
        Example:
           odb.plot_vibration_mode(file_path=r"D:\\图片\\自振模态.png",mode=1)
        Returns: 无
        """
        try:
            qt_model.PlotVibrationMode(
                filePath=file_path, mode=mode,
                showNumber=show_number, textRotationAngle=text_rotation_angle, maxMinValueKind=max_min_kind,
                showLegend=show_legend, digitalCount=digital_count, showAsExponential=show_exponential,
                showUndeformedShape=show_pre_deformed)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 获取模型信息
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
        Returns: json字符串,包含信息为list[int]
        """
        try:
            qt_result = qt_model.GetElementByPoint(x=x, y=y, z=z, tolerance=tolerance)
            result = list(qt_result)
            return json.dumps(result)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_element_by_material(name: str = ""):
        """
        获取某一材料相应的单元
        Args:
            name:材料名称
        Example:
            odb.get_element_by_material("材料1")
        Returns: json字符串,包含信息为list[int]
        """
        try:
            qt_result = qt_model.GetElementByMaterial(name=name)
            result = list(qt_result)
            return json.dumps(result)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_overlap_nodes(round_num: int = 4):
        """
        获取重合节点
        Args:
            round_num: 判断精度，默认小数点后四位
        Example:
            odb.get_overlap_nodes()
        Returns: json字符串,包含信息为list[list[int]]
        """
        try:
            result = []
            qt_result = qt_model.GetOverlapNodes(mathRound=round_num)
            for i in range(len(qt_result)):
                result.append(list(qt_result[i]))
            return json.dumps(result)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_overlap_elements():
        """
        获取重合节点
        Args:无
        Example:
            odb.get_overlap_elements()
        Returns:  json字符串,包含信息为list[list[int]]
        """
        try:
            result = []
            qt_result = qt_model.GetOverlapElements()
            for i in range(len(qt_result)):
                result.append(list(qt_result[i]))
            return json.dumps(result)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_structure_group_names():
        """
        获取结构组名称
        Args:无
        Example:
            odb.get_structure_group_names()
        Returns: json字符串,包含信息为list[str]
        """
        try:
            res_list = list(qt_model.GetStructureGroupNames())
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_thickness_data(thick_id: int):
        """
        获取所有板厚信息
        Args:
        Example:
            odb.get_thickness_data(1)
        Returns:
            json字符串,包含信息为dict
        """
        try:
            return qt_model.GetThicknessData(thick_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_all_thickness_data():
        """
        获取所有板厚信息
        Args:
        Example:
            odb.get_all_thickness_data()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            sec_ids = qt_model.GetAllThicknessIds()
            res_list = []
            for item in sec_ids:
                res_list.append(qt_model.GetThicknessData(item))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_all_section_shape():
        """
        获取所有截面形状信息
        Args:
        Example:
            odb.get_all_section_shape()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            sec_ids = qt_model.GetAllSectionIds()
            res_list = []
            for item in sec_ids:
                res_list.append(qt_model.GetSectionShape(item))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_section_shape(sec_id: int):
        """
        获取截面形状信息
        Args:
            sec_id: 目标截面编号
        Example:
            odb.get_section_shape(1)
        Returns:
            json字符串,包含信息为dict
        """
        try:
            return qt_model.GetSectionShape(sec_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_all_section_data():
        """
        获取所有截面详细信息,截面特性详见UI自定义特性截面
        Args: 无
        Example:
            odb.get_all_section_data()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            ids = Odb.get_section_ids()
            res_list = []
            for item in ids:
                res_list.append(qt_model.GetSectionInfo(item))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_section_data(sec_id: int):
        """
        获取截面详细信息,截面特性详见UI自定义特性截面
        Args:
            sec_id: 目标截面编号
        Example:
            odb.get_section_data(1)
        Returns: json字符串,包含信息为dict
        """
        try:
            return qt_model.GetSectionInfo(sec_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_section_property(index: int):
        """
        获取指定截面特性
        Args:
            index:截面号
        Example:
            odb.get_section_property(1)
        Returns: dict
        """
        try:
            return qt_model.GetSectionProperty(index)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_section_ids():
        """
        获取模型所有截面号
        Args: 无
        Example:
            odb.get_section_ids()
        Returns: list[int]
        """
        try:
            return list(qt_model.GetAllSectionIds())
        except Exception as ex:
            raise Exception(ex)

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
        try:
            return qt_model.GetNodeId(x=x, y=y, z=z, tolerance=tolerance)
        except Exception as ex:
            raise Exception(ex)

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
        try:
            return list(qt_model.GetStructureGroupElements(group_name))
        except Exception as ex:
            raise Exception(ex)

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
        try:
            return list(qt_model.GetStructureGroupNodes(group_name))
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_node_data(ids=None):
        """
        获取节点信息 默认获取所有节点信息
        Args: 无
        Example:
            odb.get_node_data()     # 获取所有节点信息
            odb.get_node_data(ids=1)    # 获取单个节点信息
            odb.get_node_data(ids=[1,2])    # 获取多个节点信息
        Returns:  json字符串,包含信息为list[dict] or dict
        """
        try:
            if ids is None:
                node_list = qt_model.GetNodeData()
            else:
                node_list = qt_model.GetNodeData(ids)
            res_list = []
            for item in node_list:
                res_list.append(str(Node(item.Id, item.XCoor, item.YCoor, item.ZCoor)))
            return json.dumps(res_list) if len(res_list) > 1 else res_list[0]
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_element_data(ids: (Union[int, List[int]]) = None):
        """
        获取单元信息
        Args:
            ids:单元号,支持整数或整数型列表,默认为None时获取所有单元信息
        Example:
            odb.get_element_data() # 获取所有单元结果
            odb.get_element_data(ids=1) # 获取指定编号单元信息
        Returns:  json字符串,包含信息为list[dict] or dict
        """
        try:
            item_list = []
            target_ids = []
            if ids is None:
                item_list.extend(Odb.get_beam_element())
                item_list.extend(Odb.get_plate_element())
                item_list.extend(Odb.get_cable_element())
                item_list.extend(Odb.get_link_element())
                return json.dumps(item_list)
            if isinstance(ids, int):
                target_ids.append(ids)
            else:
                target_ids.extend(ids)
            for item_id in target_ids:
                ele_type = Odb.get_element_type(item_id)
                if ele_type == "BEAM":
                    item_list.append(Odb.get_beam_element(item_id)[0])
                if ele_type == "PLATE":
                    item_list.append(Odb.get_plate_element(item_id)[0])
                if ele_type == "CABLE":
                    item_list.append(Odb.get_cable_element(item_id)[0])
                if ele_type == "LINK":
                    item_list.append(Odb.get_link_element(item_id)[0])
            return json.dumps(item_list) if len(item_list) > 1 else item_list[0]
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_element_type(ele_id: int) -> str:
        """
        获取单元类型
        Args:
            ele_id: 单元号
        Example:
            odb.get_element_type(ele_id=1) # 获取1号单元类型
        Returns: str
        """
        try:
            return qt_model.GetElementType(ele_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_beam_element(ids=None):
        """
        获取梁单元信息
        Args:
            ids: 梁单元号,默认时获取所有梁单元
        Example:
            odb.get_beam_element() # 获取所有单元信息
        Returns:  list[str] 其中str为json格式
        """
        try:
            res_list = []
            if ids is None:
                item_list = qt_model.GetBeamElementData()
            else:
                item_list = qt_model.GetBeamElementData(ids)
            for item in item_list:
                res_list.append(str(Element(item.Id, "BEAM", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle)))
            return res_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_plate_element(ids=None):
        """
        获取板单元信息
        Args:
            ids: 板单元号,默认时获取所有板单元
        Example:
            odb.get_plate_element() # 获取所有单元信息
        Returns:  list[str] 其中str为json格式
        """
        try:
            res_list = []
            if ids is None:
                item_list = qt_model.GetPlateElementData()
            else:
                item_list = qt_model.GetPlateElementData(ids)
            for item in item_list:
                res_list.append(str(Element(item.Id, "PLATE", [item.NodeI.Id, item.NodeJ.Id, item.NodeK.Id, item.NodeL.Id],
                                            item.MaterialId, item.ThicknessId, item.BetaAngle)))
            return res_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_cable_element(ids=None):
        """
        获取索单元信息
        Args:
            ids: 索单元号,默认时获取所有索单元
        Example:
            odb.get_cable_element() # 获取所有单元信息
        Returns:  list[str] 其中str为json格式
        """
        try:
            res_list = []
            if ids is None:
                item_list = qt_model.GetCableElementData()
            else:
                item_list = qt_model.GetCableElementData(ids)
            for item in item_list:
                res_list.append(str(Element(item.Id, "CABLE", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle,
                                            int(item.InitialParameterType), item.InitialParameter)))
            return res_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_link_element(ids=None):
        """
        获取杆单元信息
        Args:
            ids: 杆单元号,默认时输出全部杆单元
        Example:
            odb.get_link_element() # 获取所有单元信息
        Returns:  list[str] 其中str为json格式
        """
        try:
            res_list = []
            if ids is None:
                item_list = qt_model.GetLinkElementData()
            else:
                item_list = qt_model.GetLinkElementData(ids)
            for item in item_list:
                res_list.append(str(Element(item.Id, "LINK", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle)))
            return res_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_material_data():
        """
        获取材料信息
        Args: 无
        Example:
            odb.get_material_data() # 获取所有材料信息
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            mat_list = []
            mat_list.extend(Odb.get_concrete_material())
            mat_list.extend(Odb.get_steel_plate_material())
            mat_list.extend(Odb.get_pre_stress_bar_material())
            mat_list.extend(Odb.get_steel_bar_material())
            mat_list.extend(Odb.get_user_define_material())
            return json.dumps(mat_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_concrete_material(ids=None):
        """
        获取混凝土材料信息
        Args:
            ids: 材料号,默认时输出全部材料
        Example:
            odb.get_concrete_material() # 获取所有材料信息
        Returns:  list[str] 其中str为json格式
        """
        try:
            res_list = []
            item_list = qt_model.GetConcreteMaterialData(ids)
            for item in item_list:
                creep_id = -1 if item.IsCalShrinkCreep is False else item.ConcreteTimeDependency.Id
                res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="混凝土", standard=item.Standard, database=item.Database,
                                             data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                             modified=item.IsModifiedByUser, construct_factor=item.ConstructionCoefficient,
                                             creep_id=creep_id, f_cuk=item.StrengthCheck.Fcuk)))
            return res_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_steel_plate_material(ids=None):
        """
        获取钢材材料信息
        Args:
            ids: 材料号,默认时输出全部材料
        Example:
            odb.get_steel_plate_material() # 获取所有钢材材料信息
        Returns:  list[str] 其中str为json格式
        """
        try:
            res_list = []
            item_list = qt_model.GetSteelPlateMaterialData(ids)
            for item in item_list:
                res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="钢材", standard=item.Standard,
                                             database=item.StrengthCheck.Database,
                                             data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                             modified=item.IsModifiedByUser, construct_factor=item.ConstructionCoefficient,
                                             creep_id=-1, f_cuk=0)))
            return res_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_pre_stress_bar_material(ids=None):
        """
        获取钢材材料信息
        Args:
            ids: 材料号,默认时输出全部材料
        Example:
            odb.get_pre_stress_bar_material() # 获取所有预应力材料信息
        Returns:  list[str] 其中str为json格式
        """
        try:
            res_list = []
            item_list = qt_model.GetPreStressedBarMaterialData(ids)
            for item in item_list:
                res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="预应力", standard=item.Standard, database=item.Database,
                                             data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                             modified=item.IsModifiedByUser, construct_factor=item.ConstructionCoefficient,
                                             creep_id=-1, f_cuk=0)))
            return res_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_steel_bar_material(ids=None):
        """
        获取钢筋材料信息
        Args:
            ids: 材料号,默认时输出全部材料
        Example:
            odb.get_steel_bar_material() # 获取所有钢筋材料信息
        Returns:  list[str] 其中str为json格式
        """
        res_list = []
        item_list = qt_model.GetSteelBarMaterialData(ids)
        for item in item_list:
            res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="钢筋", standard=item.Standard, database=item.Database,
                                         data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                         modified=item.IsModifiedByUser, construct_factor=item.ConstructionCoefficient,
                                         creep_id=-1, f_cuk=0)))
        return res_list

    @staticmethod
    def get_user_define_material(ids=None):
        """
        获取自定义材料信息
        Args:
            ids: 材料号,默认时输出全部材料
        Example:
            odb.get_user_define_material() # 获取所有自定义材料信息
        Returns:  list[str] 其中str为json格式
        """
        try:
            res_list = []
            item_list = qt_model.GetUserDefinedMaterialData(ids)
            for item in item_list:
                creep_id = -1 if item.IsCalShrinkCreep is False else item.ConcreteTimeDependency.Id
                res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="自定义", standard="null", database="null",
                                             data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                             construct_factor=item.ConstructionCoefficient, creep_id=creep_id, f_cuk=item.Fcuk)))
            return res_list
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 获取模型边界信息
    @staticmethod
    def get_boundary_group_names():
        """
        获取自边界组名称
        Args:无
        Example:
            odb.get_boundary_group_names()
        Returns: json字符串,包含信息为list[str]
        """
        try:
            res_list = list(qt_model.GetBoundaryGroupNames())
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_general_support_data(group_name: str = None):
        """
        获取一般支承信息
        Args:
             group_name:默认输出所有边界组信息
        Example:
            odb.get_general_support_data()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            if group_name is None:
                group_names = Odb.get_boundary_group_names()
            else:
                group_names = [group_name]
            for group in group_names:
                item_list = qt_model.GetGeneralSupportData(group)
                for data in item_list:
                    res_list.append(str(GeneralSupport(data.Id, node_id=data.Node.Id,
                                                       boundary_info=(data.IsFixedX, data.IsFixedY, data.IsFixedZ,
                                                                      data.IsFixedRx, data.IsFixedRy, data.IsFixedRZ),
                                                       group_name=group, node_system=int(data.NodalCoordinateSystem))))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_elastic_link_data(group_name: str = None):
        """
        获取弹性连接信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_elastic_link_data()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            if group_name is None:
                group_names = Odb.get_boundary_group_names()
            else:
                group_names = [group_name]
            for group in group_names:
                item_list = qt_model.GetElasticLinkData(group)
                for data in item_list:
                    res_list.append(str(ElasticLink(link_id=data.Id, link_type=int(data.Type) + 1,
                                                    start_id=data.StartNode.Id, end_id=data.EndNode.Id, beta_angle=data.Beta,
                                                    boundary_info=(data.Kx, data.Ky, data.Kz, data.Krx, data.Kry, data.Krz),
                                                    group_name=group, dis_ratio=data.DistanceRatio, kx=data.Kx)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_elastic_support_data(group_name: str = None):
        """
        获取弹性支承信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_elastic_support_data()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            if group_name is None:
                group_names = Odb.get_boundary_group_names()
            else:
                group_names = [group_name]
            for group in group_names:
                item_list = qt_model.GetElasticSupportData(group)
                for data in item_list:
                    res_list.append(str(ElasticSupport(support_id=data.Id, node_id=data.Node.Id, support_type=int(data.Type) + 1,
                                                       boundary_info=(data.Kx, data.Ky, data.Kz, data.Krx, data.Kry, data.Krz),
                                                       group_name=group, node_system=int(data.NodalCoordinateSystem))))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_master_slave_link_data(group_name: str = None):
        """
        获取主从连接信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_master_slave_link_data()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            if group_name is None:
                group_names = Odb.get_boundary_group_names()
            else:
                group_names = [group_name]
            for group in group_names:
                item_list = qt_model.GetMasterSlaveLinkData(group)
                for data in item_list:
                    res_list.append(str(MasterSlaveLink(link_id=data.Id, master_id=data.MasterNode.Id, slave_id=data.SlaveNode.Id,
                                                        boundary_info=(data.IsFixedX, data.IsFixedY, data.IsFixedZ,
                                                                       data.IsFixedRx, data.IsFixedRy, data.IsFixedRZ),
                                                        group_name=group)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_node_local_axis_data():
        """
        获取节点坐标信息
        Args:无
        Example:
            odb.get_node_local_axis_data()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            for group in Odb.get_boundary_group_names():
                item_list = qt_model.GetNodalLocalAxisData(group)
                for data in item_list:
                    res_list.append(str(NodalLocalAxis(data.Node.Id, (data.VectorX.X, data.VectorX.Y, data.VectorX.Z),
                                                       (data.VectorY.X, data.VectorY.Y, data.VectorY.Z))))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_beam_constraint_data(group_name: str = None):
        """
           获取节点坐标信息
           Args:
               group_name:默认输出所有边界组信息
           Example:
               odb.get_beam_constraint_data()
           Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            if group_name is None:
                group_names = Odb.get_boundary_group_names()
            else:
                group_names = [group_name]
            for group in group_names:
                item_list = qt_model.GetBeamConstraintData(group)
                for data in item_list:
                    info_i = (
                        not data.IsIFreedX, not data.IsIFreedY, not data.IsIFreedZ, not data.IsIFreedRx, not data.IsIFreedRy, not data.IsIFreedRZ)
                    info_j = (
                        not data.IsJFreedX, not data.IsJFreedY, not data.IsJFreedZ, not data.IsJFreedRx, not data.IsJFreedRy, not data.IsJFreedRZ)
                    res_list.append(str(BeamConstraint(constraint_id=data.Id, beam_id=data.Beam.Id, info_i=info_i, info_j=info_j, group_name=group)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_constraint_equation_data(group_name: str = None):
        """
         获取约束方程信息
         Args:
             group_name:默认输出所有边界组信息
         Example:
             odb.get_constraint_equation_data()
         Returns: json字符串,包含信息为list[dict]
         """
        try:
            res_list = []
            if group_name is None:
                group_names = Odb.get_boundary_group_names()
            else:
                group_names = [group_name]
            for group in group_names:
                item_list = qt_model.GetConstraintEquationData(group)
                for data in item_list:
                    master_info = []
                    for info in data.ConstraintEquationMasterDofDatas:
                        master_info.append((info.MasterNode.Id, int(info.MasterDof) + 1, info.Factor))
                    res_list.append(
                        str(ConstraintEquation(data.Id, name=data.Name, sec_node=data.SecondaryNode.Id, sec_dof=int(data.SecondaryDof) + 1,
                                               master_info=master_info, group_name=group)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 获取施工阶段信息
    @staticmethod
    def get_stage_name():
        """
        获取所有施工阶段名称
        Args: 无
        Example:
            odb.get_stage_name()
        Returns: json字符串,包含信息为list[int]
        """
        try:
            res_list = list(qt_model.GetStageNames())
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_elements_of_stage(stage_id: int):
        """
        获取指定施工阶段单元编号信息
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_elements_of_stage(stage_id=1)
        Returns: json字符串,包含信息为list[int]
        """
        try:
            res_list = list(qt_model.GetElementIdsOfStage(stage_id))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_nodes_of_stage(stage_id: int):
        """
        获取指定施工阶段节点编号信息
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_nodes_of_stage(stage_id=1)
        Returns: json字符串,包含信息为list[int]
        """
        res_list = list(qt_model.GetNodeIdsOfStage(stage_id))
        return json.dumps(res_list)

    @staticmethod
    def get_groups_of_stage(stage_id: int):
        """
        获取施工阶段结构组、边界组、荷载组名集合
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_groups_of_stage(stage_id=1)
        Returns: json字符串,包含信息为dict
        """
        try:
            res_dict = {"结构组": list(qt_model.GetStructtureGroupOfStage(stage_id)),
                        "边界组": list(qt_model.GetBoundaryGroupOfStage(stage_id)),
                        "荷载组": list(qt_model.GetLoadGroupOfStage(stage_id))}
            return json.dumps(res_dict)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 荷载信息
    @staticmethod
    def get_load_case_names():
        """
        获取荷载工况名
        Args: 无
        Example:
            odb.get_load_case_names()
        Returns: json字符串,包含信息为list[str]
        """
        res_list = list(qt_model.GetLoadCaseNames())
        return json.dumps(res_list)

    @staticmethod
    def get_pre_stress_load(case_name: str):
        """
        获取预应力荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_pre_stress_load(case_name="荷载工况1")
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            item_list = qt_model.GetPrestressLoadData(case_name)
            for data in item_list:
                res_list.append(str(PreStressLoad(case_name=case_name, tendon_name=data.Tendon.Name,
                                                  tension_type=int(data.TendonTensionType), force=data.TensionForce, group_name=data.LoadGroup.Name)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_node_mass_data():
        """
        获取节点质量
        Args: 无
        Example:
            odb.get_node_mass_data()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            item_list = qt_model.GetNodalMassLoadData()
            for data in item_list:
                res_list.append(str(NodalMass(data.Node.Id, mass_info=(data.MassAlongZ,
                                                                       data.InertialMassMomentAlongX,
                                                                       data.InertialMassMomentAlongY,
                                                                       data.InertialMassMomentAlongZ))))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_nodal_force_load(case_name: str):
        """
        获取节点力荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_nodal_force_load(case_name="荷载工况1")
        Returns: json字符串,包含信息为list[dict]
        """
        res_list = []
        item_list = qt_model.GetNodeForceLoadData(case_name)
        for data in item_list:
            load = data.Force
            res_list.append(str(NodalForce(node_id=data.Node.Id, case_name=case_name,
                                           load_info=(load.ForceX, load.ForceY, load.ForceZ,
                                                      load.MomentX, load.MomentY, load.MomentZ), group_name=data.LoadGroup.Name)))
        return json.dumps(res_list)

    @staticmethod
    def get_nodal_displacement_load(case_name: str):
        """
        获取节点位移荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_nodal_displacement_load(case_name="荷载工况1")
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            item_list = qt_model.GetNodeForceLoadData(case_name)
            for data in item_list:
                load = data.NodalForceDisplacement
                res_list.append(str(NodalForceDisplacement(node_id=data.Node.Id, case_name=case_name,
                                                           load_info=(load.DispX, load.DispY, load.DispZ,
                                                                      load.DispRx, load.DispRy, load.DispRz), group_name=data.LoadGroup.Name)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_beam_element_load(case_name: str):
        """
        获取梁单元荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_beam_element_load(case_name="荷载工况1")
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            item_list_concentrated_load = qt_model.GetBeamConcentratedLoadData(case_name)
            for item in item_list_concentrated_load:
                load_bias = (item.FrameLoadBias.IsBias, item.FrameLoadBias.LoadBiasPosition,
                             int(item.FrameLoadBias.CoordinateSystem) + 1, item.FrameLoadBias.Distance)
                res_list.append(str(BeamElementLoad(item.ElementId, case_name, int(item.ElementLoadType) + 1, int(item.LoadCoordinateSystem),
                                                    list_x=[item.Distance], list_load=[item.Force], group_name=item.LoadGroup.Name,
                                                    load_bias=load_bias, projected=False)))
            item_list_distribute_load = qt_model.GetBeamDistributeLoadData(case_name)
            for item in item_list_distribute_load:
                load_bias = (item.FrameLoadBias.IsBias, item.FrameLoadBias.LoadBiasPosition,
                             int(item.FrameLoadBias.CoordinateSystem) + 1, item.FrameLoadBias.Distance)
                res_list.append(str(BeamElementLoad(item.ElementId, case_name, int(item.ElementLoadType) + 1, int(item.LoadCoordinateSystem),
                                                    list_x=[item.StartDistance, item.EndDistance], list_load=[item.StartForce, item.EndForce],
                                                    group_name=item.LoadGroup.Name, load_bias=load_bias, projected=item.IsProjection)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_plate_element_load(case_name: str):
        """
        获取梁单元荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_beam_element_load(case_name="荷载工况1")
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            item_list_concentrated_load = qt_model.GetPlateConcentratedLoadData(case_name)
            for item in item_list_concentrated_load:
                res_list.append(str(PlateElementLoad(element_id=item.ElementId, case_name=case_name, load_type=int(item.ElementLoadType) + 1,
                                                     load_place=0, coord_system=int(item.LoadCoordinateSystem) + 1,
                                                     group_name=item.LoadGroup.Name, load_list=[item.P], xy_list=(item.Dx, item.Dy))))
            line_load_list = qt_model.GetPlateDistributeLineLoadData(case_name)
            for item in line_load_list:
                res_list.append(str(PlateElementLoad(element_id=item.ElementId, case_name=case_name, load_type=int(item.ElementLoadType) + 1,
                                                     load_place=int(item.PlateLoadPosition) - 1, coord_system=int(item.LoadCoordinateSystem) + 1,
                                                     group_name=item.LoadGroup.Name, load_list=[item.P1, item.P2], xy_list=None)))
            line_load_list = qt_model.GetPlateDistributeAreaLoadData(case_name)
            for item in line_load_list:
                res_list.append(str(PlateElementLoad(element_id=item.ElementId, case_name=case_name, load_type=int(item.ElementLoadType) + 1,
                                                     load_place=0, coord_system=int(item.LoadCoordinateSystem) + 1,
                                                     group_name=item.LoadGroup.Name, load_list=[item.P1, item.P2, item.P3, item.P4], xy_list=None)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_initial_tension_load(case_name: str):
        """
        获取初拉力荷载数据
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_initial_tension_load(case_name="荷载工况1")
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            item_list_load = qt_model.GetInitialTensionLoadData(case_name)
            for item in item_list_load:
                res_list.append(str(InitialTension(element_id=item.ElementId, case_name=case_name, group_name=item.LoadGroup.Name,
                                                   tension_type=int(item.CableTensionType), tension=item.Tension)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_cable_length_load(case_name: str):
        """
        获取指定荷载工况的初拉力荷载数据
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_cable_length_load(case_name="荷载工况1")
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            item_list_load = qt_model.GetCableLengthLoadData(case_name)
            for item in item_list_load:
                res_list.append(str(CableLengthLoad(element_id=item.ElementId, case_name=case_name, group_name=item.LoadGroup.Name,
                                                    tension_type=int(item.CableTensionType), length=item.UnstressedLength)))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_deviation_parameter():
        """
        获取制造偏差参数
        Args: 无
        Example:
            odb.get_deviation_parameter()
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            beam_list_parameter = qt_model.GetBeamDeviationParameterData()
            for item in beam_list_parameter:
                res_list.append(str(DeviationParameter(item.Name, element_type=1,
                                                       parameters=[item.AxialDeviation, item.StartAngleDeviationDirectX,
                                                                   item.StartAngleDeviationDirectY, item.StartAngleDeviationDirectZ,
                                                                   item.EndAngleDeviationDirectX, item.EndAngleDeviationDirectY,
                                                                   item.EndAngleDeviationDirectZ])))
            plate_list_parameter = qt_model.GetPlateDeviationParameterData()
            for item in plate_list_parameter:
                res_list.append(str(DeviationParameter(item.Name, element_type=2,
                                                       parameters=[item.DisplacementDirectX, item.DisplacementDirectY, item.DisplacementDirectZ,
                                                                   item.RotationDirectX, item.RotationDirectY])))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_deviation_load(case_name: str):
        """
        获取指定荷载工况的制造偏差荷载
        Args:
            case_name:荷载工况名
        Example:
            odb.get_deviation_load(case_name="荷载工况1")
        Returns: json字符串,包含信息为list[dict]
        """
        try:
            res_list = []
            beam_list_load = qt_model.GetBeamDeviationLoadData(case_name)
            for item in beam_list_load:
                res_list.append(str(DeviationLoad(item.Element.Id, case_name=case_name,
                                                  parameters=[item.BeamDeviationParameter.Name],
                                                  group_name=item.LoadGroup.Name)))
            plate_list_load = qt_model.GetPlateDeviationLoadData(case_name)
            for item in plate_list_load:
                res_list.append(str(DeviationLoad(item.Element.Id, case_name=case_name,
                                                  parameters=[item.PlateDeviation[0].Name, item.PlateDeviation[0].Name,
                                                              item.PlateDeviation[2].Name, item.PlateDeviation[3].Name])))
            return json.dumps(res_list)
        except Exception as ex:
            raise Exception(ex)
    # endregion
