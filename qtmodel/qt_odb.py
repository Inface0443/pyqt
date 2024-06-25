from __main__ import qt_model
from .res_db import *
from .qt_db import *


class Odb:
    """
    获取模型计算结果和模型信息
    """

    # region 静力结果查看
    @staticmethod
    def get_element_stress(element_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取单元应力,支持单个单元和单元列表
        Args:
            element_id: 单元编号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        Example:
            odb.get_element_stress(1,stage_id=1)
            odb.get_element_stress([1,2,3],stage_id=1)
            odb.get_element_stress(1,stage_id=-1,case_name="工况名")
        Returns: list[json_str] or json_str
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,element_id仅支持 int和 list[int]")
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
                raise TypeError(f"操作错误，不存在{item.ElementType}类型")
        if len(list_res) == 1:
            return list_res[0]
        return list_res

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
            odb.get_element_force(1,stage_id=1)
            odb.get_element_force([1,2,3],stage_id=1)
            odb.get_element_force(1,stage_id=-1,case_name="工况名")
        Returns: list[json_str] or json_str
        """
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
                raise TypeError(f"操作错误，不存在{item.ElementType}类型")
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    @staticmethod
    def get_reaction(node_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取节点,支持单个节点和节点列表
        Args:
            node_id: 节点编号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        Example:
            odb.get_reaction(1,stage_id=1)
            odb.get_reaction([1,2,3],stage_id=1)
            odb.get_reaction(1,stage_id=-1,case_name="工况名")
        Returns: list[json_str] or json_str
        """
        if type(node_id) != int and type(node_id) != list:
            raise TypeError("类型错误,beam_id int和 list[int]")
        bs_list = qt_model.GetSupportReaction(node_id, stage_id, result_kind, increment_type, case_name)
        list_res = []
        for item in bs_list:
            force = [item.Force.Fx, item.Force.Fy, item.Force.Fz, item.Force.Mx, item.Force.My, item.Force.Mz]
            list_res.append(str(SupportReaction(item.NodeId, force)))
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    @staticmethod
    def get_node_displacement(node_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, case_name=""):
        """
        获取节点,支持单个节点和节点列表
        Args:
            node_id: 节点号
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        Example:
            odb.get_node_displacement(1,stage_id=1)
            odb.get_node_displacement([1,2,3],stage_id=1)
            odb.get_node_displacement(1,stage_id=-1,case_name="工况名")
        Returns: list[json_str] or json_str
        """
        if type(node_id) != int and type(node_id) != list:
            raise TypeError("类型错误,node_id仅支持 int和 list[int]")
        bf_list = qt_model.GetNodeDisplacement(node_id, stage_id, result_kind, increment_type, case_name)
        list_res = []
        for item in bf_list:
            displacements = [item.Displacement.Dx, item.Displacement.Dy, item.Displacement.Dz,
                             item.Displacement.Rx, item.Displacement.Ry, item.Displacement.Rz]
            list_res.append(str(NodeDisplacement(item.NodeId, displacements)))
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    # endregion

    # region 绘制模型结果
    @staticmethod
    def plot_reaction_result(file_path: str, component: int = 1, load_case_name: str = "", stage_id: int = 1,
                             envelope_type: int = 1, show_number: bool = True, show_legend: bool = True,
                             text_rotation=0, digital_count=0, show_exponential: bool = True, max_min_kind: int = -1,
                             show_increment: bool = False):
        """
        保存结果图片到指定文件甲
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Fx 1-Fy 2-Fz 3-Fxyz 4-Mx 5-My 6-Mz 7-Mxyz
            load_case_name: 详细荷载工况名，参考桥通结果输出，例如： CQ:成桥(合计)
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            show_number: 数值选项卡开启
            show_legend: 图例选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            show_increment: 是否显示增量结果
        Example:
            odb.plot_reaction_result(r"aaa.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotReactionResult(file_path, component=component, loadCaseName=load_case_name, stageId=stage_id, envelopeType=envelope_type,
                                        showNumber=show_number, showLegend=show_legend, textRotationAngle=text_rotation, digitalCount=digital_count,
                                        showAsExponential=show_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_displacement_result(file_path: str, component: int = 1, load_case_name: str = "", stage_id: int = 1,
                                 envelope_type: int = 1, show_deformed: bool = True, show_pre_deformed: bool = True,
                                 deformed_scale: float = 1.0, actual_deformed: bool = False,
                                 show_number: bool = True, show_legend: bool = True,
                                 text_rotation=0, digital_count=0, show_exponential: bool = True, max_min_kind: int = 1,
                                 show_increment: bool = False):
        """
        保存结果图片到指定文件甲
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Dx 1-Dy 2-Dz 3-Rx 4-Ry 5-Rz 6-Dxy 7-Dyz 8-Dxz 9-Dxyz
            load_case_name: 详细荷载工况名，参考桥通结果输出，例如： CQ:成桥(合计)
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            envelope_type: 施工阶段包络类型 1-最大 2-最小
            show_deformed: 变形选项卡开启
            show_pre_deformed: 显示变形前
            deformed_scale:变形比例
            actual_deformed:是否显示实际变形
            show_number: 数值选项卡开启
            show_legend: 图例选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值
            digital_count: 小数点位数
            show_exponential: 指数显示开启
            show_increment: 是否显示增量结果
        Example:
            odb.plot_displacement_result(r"aaa.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotDisplacementResult(file_path, component=component, loadCaseName=load_case_name, stageId=stage_id, envelopeType=envelope_type,
                                            showAsDeformedShape=show_deformed, showUndeformedShape=show_pre_deformed,
                                            deformedScale=deformed_scale, deformedActual=actual_deformed,
                                            showNumber=show_number, showLegend=show_legend, textRotationAngle=text_rotation,
                                            digitalCount=digital_count,
                                            showAsExponential=show_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_beam_element_force(file_path: str, component: int = 0, load_case_name: str = "合计", stage_id: int = 1,
                                envelope_type: int = 1, show_line_chart: bool = True, show_number: bool = False,
                                position: int = 0, flip_plot: bool = True, line_scale: float = 1.0,
                                show_deformed: bool = True, show_pre_deformed: bool = False,
                                deformed_actual: bool = False, deformed_scale: float = 1.0,
                                show_legend: bool = True, text_rotation: int = 0, digital_count: int = 0,
                                show_exponential: bool = True, max_min_kind: int = 0, show_increment: bool = False):
        """
        绘制梁单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            component: 分量编号 0-Fx 1-Fy 2-Fz 3-Mx 4-My 5-Mz
            load_case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelope_type: 包络类型
            show_line_chart: 是否显示线图
            show_number: 是否显示数值
            position: 位置编号
            flip_plot: 是否翻转绘图
            line_scale: 线的比例
            show_deformed: 是否显示变形形状
            show_pre_deformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment: 是否显示增量结果
        Example:
            odb.plot_beam_element_force(r"aaa.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotBeamElementForce(
                filePath=file_path, component=component, loadCaseName=load_case_name, stageId=stage_id, envelopeType=envelope_type,
                showLineChart=show_line_chart, showNumber=show_number, position=position, flipPlot=flip_plot, lineScale=line_scale,
                showAsDeformedShape=show_deformed, showUndeformedShape=show_pre_deformed, deformedActual=deformed_actual,
                deformedScale=deformed_scale, showLegend=show_legend, textRotationAngle=text_rotation, digitalCount=digital_count,
                showAsExponential=show_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_truss_element_force(file_path: str, load_case_name: str = "合计", stage_id: int = 1,
                                 envelope_type: int = 1, show_line_chart: bool = True, show_number: bool = False,
                                 position: int = 0, flip_plot: bool = True, line_scale: float = 1.0,
                                 show_deformed: bool = True, show_pre_deformed: bool = False,
                                 deformed_actual: bool = False, deformed_scale: float = 1.0,
                                 show_legend: bool = True, text_rotation_angle: int = 0, digital_count: int = 0,
                                 show_as_exponential: bool = True, max_min_kind: int = 0, show_increment: bool = False):
        """
        绘制杆单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            load_case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelope_type: 包络类型
            show_line_chart: 是否显示线图
            show_number: 是否显示数值
            position: 位置编号
            flip_plot: 是否翻转绘图
            line_scale: 线的比例
            show_deformed: 是否显示变形形状
            show_pre_deformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotation_angle: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            show_as_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment:是否显示增量结果
        Example:
            odb.plot_truss_element_force(r"aaa.png",load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotTrussElementForce(
                filePath=file_path, loadCaseName=load_case_name, stageId=stage_id, envelopeType=envelope_type,
                showLineChart=show_line_chart, showNumber=show_number, position=position, flipPlot=flip_plot, lineScale=line_scale,
                showAsDeformedShape=show_deformed, showUndeformedShape=show_pre_deformed, deformedActual=deformed_actual,
                deformedScale=deformed_scale, showLegend=show_legend, textRotationAngle=text_rotation_angle, digitalCount=digital_count,
                showAsExponential=show_as_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def plot_plate_element_force(file_path: str, component: int = 0, force_kind: int = 0, load_case_name: str = "合计",
                                 stage_id: int = 1, envelope_type: int = 1, show_number: bool = False,
                                 show_deformed: bool = True, show_pre_deformed: bool = False,
                                 deformed_actual: bool = False, deformed_scale: float = 1.0,
                                 show_legend: bool = True, text_rotation_angle: int = 0, digital_count: int = 0,
                                 show_as_exponential: bool = True, max_min_kind: int = 0, show_increment: bool = False):
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
            show_as_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment: 是否显示增量结果
        Example:
            odb.plot_plate_element_force(r"aaa.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: 无
        """
        try:
            qt_model.PlotPlateElementForce(
                filePath=file_path, component=component, forceKind=force_kind, loadCaseName=load_case_name, stageId=stage_id,
                envelopeType=envelope_type, showNumber=show_number, showAsDeformedShape=show_deformed,
                showUndeformedShape=show_pre_deformed, deformedActual=deformed_actual, deformedScale=deformed_scale,
                showLegend=show_legend, textRotationAngle=text_rotation_angle, digitalCount=digital_count,
                showAsExponential=show_as_exponential, maxMinValueKind=max_min_kind, showIncrementResult=show_increment)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 获取模型信息
    @staticmethod
    def get_section_shape(sec_id: int):
        """
        获取截面形状信息
        Args:
            sec_id: 目标截面编号
        Example:
            odb.get_section_shape(1)
        Returns: str
        """
        try:
            return qt_model.GetSectionShape(sec_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_section_data(sec_id: int):
        """
        获取截面详细信息，截面特性详见UI自定义特性截面
        Args:
            sec_id: 目标截面编号
        Example:
            odb.get_section_data(1)
        Returns: str
        """
        try:
            return qt_model.GetSectionInfo(sec_id)
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
        获取节点编号，为-1时则表示未找到该坐标节点
        Args:
            x: 目标点X轴坐标
            y: 目标点Y轴坐标
            z: 目标点Z轴坐标
            tolerance: 距离容许误差
        Example:
            odb.get_node_id(1,1,1)
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
            odb.get_group_elements("默认结构组")
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
            odb.get_group_nodes("默认结构组")
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
            odb.get_node_data(1)    # 获取单个节点信息
            odb.get_node_data([1,2])    # 获取多个节点信息
        Returns: list[json_str] 或 json_str
        """
        try:
            if ids is None:
                node_list = qt_model.GetNodeData()
            else:
                node_list = qt_model.GetNodeData(ids)
            res_list = []
            for item in node_list:
                res_list.append(str(Node(item.Id, item.XCoor, item.YCoor, item.ZCoor)))
            if len(res_list) == 1:
                return res_list[0]
            return res_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_element_data(ids=None):
        """
        获取单元信息
        Args: 无
        Example:
            odb.get_element_data() # 获取所有单元结果
            odb.get_element_data(1) # 获取指定编号单元信息
        Returns: list[json_str]
        """
        try:
            item_list = []
            target_ids = []
            if ids is None:
                item_list.extend(Odb.get_beam_element())
                item_list.extend(Odb.get_plate_element())
                item_list.extend(Odb.get_cable_element())
                item_list.extend(Odb.get_link_element())
                if len(item_list) == 1:
                    return item_list[0]
                else:
                    return item_list
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
            return item_list
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_element_type(ele_id: int) -> str:
        """
        获取单元类型
        Args:
            ele_id: 单元号
        Example:
            odb.get_element_type(1) # 获取所有单元信息
        Returns: str类型 返回 BEAM PLATE CABLE LINK
        """
        try:
            return qt_model.GetElementType(ele_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def get_beam_element(ids=None) :
        """
        获取梁单元信息
        Args:
            ids: 梁单元号，默认时获取所有梁单元
        Example:
            odb.get_beam_element() # 获取所有单元信息
        Returns: list[json_str]
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
    def get_plate_element(ids=None) :
        """
        获取板单元信息
        Args:
            ids: 板单元号，默认时获取所有板单元
        Example:
            odb.get_plate_element() # 获取所有单元信息
        Returns: list[json_str]
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
    def get_cable_element(ids=None) :
        """
        获取索单元信息
        Args:
            ids: 索单元号，默认时获取所有索单元
        Example:
            odb.get_cable_element() # 获取所有单元信息
        Returns: list[json_str]
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
    def get_link_element(ids=None) :
        """
        获取杆单元信息
        Args:
            ids: 杆单元号，默认时输出全部杆单元
        Example:
            odb.get_link_element() # 获取所有单元信息
        Returns: list[json_str]
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
    def get_material_data(ids=None):
        """
        获取材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        Example:
            odb.get_material_data() # 获取所有材料信息
        Returns: list[json_str]
        """
        mat_list = []
        if ids is None:
            mat_list.extend(Odb.get_concrete_material())
            mat_list.extend(Odb.get_steel_plate_material())
            mat_list.extend(Odb.get_pre_stress_bar_material())
            mat_list.extend(Odb.get_steel_bar_material())
            mat_list.extend(Odb.get_user_define_material())

    @staticmethod
    def get_concrete_material(ids=None):
        """
        获取混凝土材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        Example:
            odb.get_concrete_material() # 获取所有材料信息
        Returns: list[json_str]
        """
        res_list = []
        item_list = qt_model.GetConcreteMaterialData(ids)
        for item in item_list:
            creep_id = -1 if item.IsCalShrinkCreep is False else item.ConcreteTimeDependency.Id
            res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="混凝土", standard=item.Standard, database=item.Database,
                                         data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                         modified=item.IsModifiedByUser, construct_factor=item.ConstructionCoefficient,
                                         creep_id=creep_id, f_cuk=item.StrengthCheck.Fcuk)))
        return res_list

    @staticmethod
    def get_steel_plate_material(ids=None):
        """
        获取钢材材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        Example:
            odb.get_steel_plate_material() # 获取所有钢材材料信息
        Returns: list[json_str]
        """
        steel_plate_dictionary = {
            "Q235(≤16)": "Q235(0_16)", "Q235(16~40)": "Q235(16_40)", "Q235(40~100)": "Q235(40_100)", "Q345(≤16)": "Q345(0_16)",
            "Q345(16~40)": "Q345(16_40)", "Q345(40~63)": "Q345(40_63)", "Q345(63~80)": "Q345(63_80)", "Q345(80~100)": "Q345(80_100)",
            "Q390(≤16)": "Q390(0_16)", "Q390(16~40)": "Q390(16_40)", "Q390(40~63)": "Q390(40_63)", "Q390(63~100)": "Q390(63_100)",
            "Q420(≤16)": "Q420(0_16)", "Q420(16~40)": "Q420(16_40)", "Q420(40~63)": "Q420(40_63)", "Q420(63~100)": "Q420(63_100)",
            "Q235qD": "Q235qD", "Q345qD": "Q345qD", "Q345qE": "Q345qE", "Q370qD": "Q370qD", "Q370qE": "Q370qE", "Q420qD": "Q420qD",
            "Q420qE": "Q420qE", "Q500qD": "Q500qD", "Q500qE": "Q500qE", "ZG230-450Ⅱ": "ZG230-450II", "ZG270-500Ⅱ": "ZG270-500II",
            "35号锻钢": "35号锻钢", "35CrMo": "35CrMo",
        }
        res_list = []
        item_list = qt_model.GetSteelPlateMaterialData(ids)
        for item in item_list:
            res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="钢材", standard=item.Standard,
                                         database=steel_plate_dictionary[item.StrengthCheck.Database],
                                         data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                         modified=item.IsModifiedByUser, construct_factor=item.ConstructionCoefficient,
                                         creep_id=-1, f_cuk=0)))
        return res_list

    @staticmethod
    def get_pre_stress_bar_material(ids=None):
        """
        获取钢材材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        Example:
            odb.get_pre_stress_bar_material() # 获取所有预应力材料信息
        Returns: list[json_str]
        """

        res_list = []
        item_list = qt_model.GetPreStressedBarMaterialData(ids)
        for item in item_list:
            res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="预应力", standard=item.Standard, database=item.Database,
                                         data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                         modified=item.IsModifiedByUser, construct_factor=item.ConstructionCoefficient,
                                         creep_id=-1, f_cuk=0)))
        return res_list

    @staticmethod
    def get_steel_bar_material(ids=None):
        """
        获取钢筋材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        Example:
            odb.get_steel_bar_material() # 获取所有钢筋材料信息
        Returns: list[json_str]
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
            ids: 材料号，默认时输出全部材料
        Example:
            odb.get_user_define_material() # 获取所有自定义材料信息
        Returns: list[json_str]
        """
        res_list = []
        item_list = qt_model.GetUserDefinedMaterialData(ids)
        for item in item_list:
            creep_id = -1 if item.IsCalShrinkCreep is False else item.ConcreteTimeDependency.Id
            res_list.append(str(Material(mat_id=item.Id, name=item.Name, mat_type="自定义", standard="null", database="null",
                                     data_info=[item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                     modified=item.IsModifiedByUser, construct_factor=item.ConstructionCoefficient,
                                     creep_id=creep_id, f_cuk=item.Fcuk)))
        return res_list

    # endregion

    # region 获取模型边界信息
    @staticmethod
    def get_boundary_group_names():
        """
        获取自边界组名称
        Args:无
        Example:
            odb.get_boundary_group_names()
        Returns: list[str]
        """
        return list(qt_model.GetBoundaryGroupNames())

    @staticmethod
    def get_general_support_data(group_name: str = None):
        """
        获取一般支承信息
        Args:
             group_name:默认输出所有边界组信息
        Example:
            odb.get_general_support_data()
        Returns: list[json_str]
        """
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
        return res_list

    @staticmethod
    def get_elastic_link_data(group_name: str = None):
        """
        获取弹性连接信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_elastic_link_data()
        Returns: list[json_str]
        """
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
        return res_list

    @staticmethod
    def get_elastic_support_data(group_name: str = None):
        """
        获取弹性支承信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_elastic_support_data()
        Returns: list[json_str]
        """
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
        return res_list

    @staticmethod
    def get_master_slave_link_data(group_name: str = None):
        """
        获取主从连接信息
        Args:
            group_name:默认输出所有边界组信息
        Example:
            odb.get_master_slave_link_data()
        Returns: list[json_str]
        """
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
        return res_list

    @staticmethod
    def get_node_local_axis_data():
        """
        获取节点坐标信息
        Args:无
        Example:
            odb.get_node_local_axis_data()
        Returns: list[json_str]
        """
        res_list = []
        for group in Odb.get_boundary_group_names():
            item_list = qt_model.GetNodalLocalAxisData(group)
            for data in item_list:
                res_list.append(str(NodalLocalAxis(data.Node.Id, (data.VectorX.X, data.VectorX.Y, data.VectorX.Z),
                                                   (data.VectorY.X, data.VectorY.Y, data.VectorY.Z))))
        return res_list

    @staticmethod
    def get_beam_constraint_data(group_name: str = None):
        """
           获取节点坐标信息
           Args:
               group_name:默认输出所有边界组信息
           Example:
               odb.get_beam_constraint_data()
           Returns: list[json_str]
        """
        res_list = []
        if group_name is None:
            group_names = Odb.get_boundary_group_names()
        else:
            group_names = [group_name]
        for group in group_names:
            item_list = qt_model.GetBeamConstraintData(group)
            for data in item_list:
                info_i = (not data.IsIFreedX, not data.IsIFreedY, not data.IsIFreedZ, not data.IsIFreedRx, not data.IsIFreedRy, not data.IsIFreedRZ)
                info_j = (not data.IsJFreedX, not data.IsJFreedY, not data.IsJFreedZ, not data.IsJFreedRx, not data.IsJFreedRy, not data.IsJFreedRZ)
                res_list.append(str(BeamConstraint(constraint_id=data.Id, beam_id=data.Beam.Id, info_i=info_i, info_j=info_j, group_name=group)))
        return res_list

    @staticmethod
    def get_constraint_equation_data(group_name: str = None):
        """
         获取约束方程信息
         Args:
             group_name:默认输出所有边界组信息
         Example:
             odb.get_constraint_equation_data()
         Returns: list[json_str]
         """
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
                res_list.append(str(ConstraintEquation(data.Id, name=data.Name, sec_node=data.SecondaryNode.Id, sec_dof=int(data.SecondaryDof) + 1,
                                                       master_info=master_info, group_name=group)))
        return res_list

    # endregion

    # region 获取施工阶段信息
    @staticmethod
    def get_elements_of_stage(stage_id: int) -> list[int]:
        """
        获取指定施工阶段单元编号信息
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_elements_of_stage(1)
        Returns: list[int]
        """
        return list(qt_model.GetElementIdsOfStage(stage_id))

    @staticmethod
    def get_nodes_of_stage(stage_id: int) -> list[int]:
        """
        获取指定施工阶段节点编号信息
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_nodes_of_stage(1)
        Returns: list[int]
        """
        return list(qt_model.GetNodeIdsOfStage(stage_id))

    @staticmethod
    def get_groups_of_stage(stage_id: int) -> dict:
        """
        获取施工阶段结构组、边界组、荷载组名集合
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_groups_of_stage(1)
        Returns: dict
        """
        res_dict = {"结构组": list(qt_model.GetStructtureGroupOfStage(stage_id)),
                    "边界组": list(qt_model.GetBoundaryGroupOfStage(stage_id)),
                    "荷载组": list(qt_model.GetLoadGroupOfStage(stage_id))}
        return res_dict

    # endregion

    # region 荷载信息
    @staticmethod
    def get_load_case_names():
        """
        获取荷载工况名
        Args: 无
        Example:
            odb.get_load_case_names()
        Returns: list[str]
        """
        return qt_model.GetLoadCaseNames()

    @staticmethod
    def get_pre_stress_load(case_name: str):
        """
        获取预应力荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_pre_stress_load("荷载工况1")
        Returns: list[json_str]
        """
        res_list = []
        item_list = qt_model.GetPrestressLoadData(case_name)
        for data in item_list:
            res_list.append(str(PreStressLoad(case_name=case_name, tendon_name=data.Tendon.Name,
                                              tension_type=int(data.TendonTensionType), force=data.TensionForce, group_name=data.LoadGroup.Name)))
        return res_list

    @staticmethod
    def get_node_mass_data():
        """
        获取节点质量
        Args: 无
        Example:
            odb.get_node_mass_data()
        Returns: list[json_str]
        """
        res_list = []
        item_list = qt_model.GetNodalMassLoadData()
        for data in item_list:
            res_list.append(str(NodalMass(data.Node.Id, mass_info=(data.MassAlongZ,
                                                                   data.InertialMassMomentAlongX,
                                                                   data.InertialMassMomentAlongY,
                                                                   data.InertialMassMomentAlongZ))))
        return res_list

    @staticmethod
    def get_nodal_force_load(case_name: str):
        """
        获取节点力荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_nodal_force_load("荷载工况1")
        Returns: list[json_str]
        """
        res_list = []
        item_list = qt_model.GetNodeForceLoadData(case_name)
        for data in item_list:
            load = data.Force
            res_list.append(str(NodalForce(node_id=data.Node.Id, case_name=case_name,
                                           load_info=(load.ForceX, load.ForceY, load.ForceZ,
                                                      load.MomentX, load.MomentY, load.MomentZ), group_name=data.LoadGroup.Name)))
        return res_list

    @staticmethod
    def get_nodal_displacement_load(case_name: str):
        """
        获取节点位移荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_nodal_displacement_load("荷载工况1")
        Returns: list[json_str]
        """
        res_list = []
        item_list = qt_model.GetNodeForceLoadData(case_name)
        for data in item_list:
            load = data.NodalForceDisplacement
            res_list.append(str(NodalForceDisplacement(node_id=data.Node.Id, case_name=case_name,
                                                       load_info=(load.DispX, load.DispY, load.DispZ,
                                                                  load.DispRx, load.DispRy, load.DispRz), group_name=data.LoadGroup.Name)))
        return res_list

    @staticmethod
    def get_beam_element_load(case_name: str):
        """
        获取梁单元荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_beam_element_load("荷载工况1")
        Returns: list[json_str]
        """
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
        return res_list

    @staticmethod
    def get_plate_element_load(case_name: str):
        """
        获取梁单元荷载
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_beam_element_load("荷载工况1")
        Returns: list[json_str]
        """
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
        return res_list

    @staticmethod
    def get_initial_tension_load(case_name: str):
        """
            获取初拉力荷载数据
            Args:
                case_name: 荷载工况名
            Example:
                odb.get_initial_tension_load("荷载工况1")
            Returns: list[json_str]
        """
        res_list = []
        item_list_load = qt_model.GetInitialTensionLoadData(case_name)
        for item in item_list_load:
            res_list.append(str(InitialTension(element_id=item.ElementId, case_name=case_name, group_name=item.LoadGroup.Name,
                                               tension_type=int(item.CableTensionType), tension=item.Tension)))
        return res_list

    @staticmethod
    def get_cable_length_load(case_name: str):
        """
        获取初拉力荷载数据
        Args:
            case_name: 荷载工况名
        Example:
            odb.get_cable_length_load("荷载工况1")
        Returns: list[json_str]
        """
        res_list = []
        item_list_load = qt_model.GetCableLengthLoadData(case_name)
        for item in item_list_load:
            res_list.append(str(CableLengthLoad(element_id=item.ElementId, case_name=case_name, group_name=item.LoadGroup.Name,
                                                tension_type=int(item.CableTensionType), length=item.UnstressedLength)))
        return res_list

    @staticmethod
    def get_deviation_parameter():
        """
        获取制造偏差参数
        Args: 无
        Example:
            odb.get_deviation_parameter()
        Returns: list[json_str]
        """
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
        return res_list

    @staticmethod
    def get_deviation_load(case_name: str):
        """
        获取制造偏差荷载
        Args:
            case_name:荷载工况名
        Example:
            odb.get_deviation_load("荷载工况1")
        Returns: list[json_str]
        """
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
        return res_list
    # endregion
