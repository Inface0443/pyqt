from ..core.qt_server import QtServer


class OdbResultPlot:
    """
    用于绘制结果图像
    """

    # region 绘制模型结果
    @staticmethod
    def plot_reaction_result(file_path: str="", stage_id: int = 1, case_name: str = "", show_increment: bool = False,
                             envelop_type: int = 1, component: int = 1,
                             show_number: bool = True, text_rotation=0, max_min_kind: int = -1,
                             show_legend: bool = True, digital_count=3, text_exponential: bool = True, arrow_scale: float = 1,
                             is_time_history: bool = False, time_kind: int = 1, time_tick: float = 1.0) -> str:
        """
        保存结果图片到指定文件甲
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelop_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 1-Fx 2-Fy 3-Fz 4-Fxyz 5-Mx 6-My 7-Mz 8-Mxyz
            show_number: 数值选项卡开启
            show_legend: 图例选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            max_min_kind: 数值选项卡内最大最小值显示 0-不显示最大最小值  1-显示最大值和最小值  2-最大绝对值 3-最大值 4-最小值
            digital_count: 小数点位数
            text_exponential: 指数显示开启
            arrow_scale:箭头大小
            is_time_history:是否为时程分析结果
            time_kind:时程分析类型 1-时刻 2-最大 3-最小
            time_tick:时程分析时刻
        Example:
            odb.plot_reaction_result(file_path=r"D:\\图片\\反力图.png",component=1,case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "component": component,
            "show_number": show_number,
            "text_rotation": text_rotation,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "arrow_scale": arrow_scale,
            "is_time_history": is_time_history,
            "time_kind": time_kind,
            "time_tick": time_tick,
        }
        return QtServer.send_get("PLOT-REACTION-RESULT", payload)

    @staticmethod
    def plot_displacement_result(file_path: str="", stage_id: int = 1, case_name: str = "", show_increment: bool = False,
                                 envelop_type: int = 1, component: int = 1,
                                 show_deformed: bool = True, deformed_scale: float = 1.0, deformed_actual: bool = False,
                                 show_number: bool = True, text_rotation=0, max_min_kind: int = 1,
                                 show_legend: bool = True, digital_count=3, text_exponential: bool = True, show_undeformed: bool = True,
                                 is_time_history: bool = False, deform_kind: int = 1, time_kind: int = 1, time_tick: float = 1.0)  ->str:
        """
        保存结果图片到指定文件甲
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelop_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 1-Dx 2-Dy 3-Dz 4-Rx 5-Ry 6-Rz 7-Dxy 8-Dyz 9-Dxz 10-Dxyz
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            max_min_kind: 数值选项卡内最大最小值显示 0-不显示最大最小值  1-显示最大值和最小值  2-最大绝对值 3-最大值 4-最小值
            show_legend: 图例选项卡开启
            digital_count: 小数点位数
            text_exponential: 指数显示开启
            show_undeformed: 显示变形前
            is_time_history:是否为时程分析结果
            time_kind:时程分析类型 1-时刻 2-最大 3-最小
            deform_kind:时程分析变形类型 1-位移 2-速度 3-加速度
            time_tick:时程分析时刻
        Example:
            odb.plot_displacement_result(file_path=r"D:\\图片\\变形图.png",component=1,case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "component": component,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotation": text_rotation,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "show_undeformed": show_undeformed,
            "is_time_history": is_time_history,
            "time_kind": time_kind,
            "deform_kind": deform_kind,
            "time_tick": time_tick,
        }
        return QtServer.send_get("PLOT-DISPLACEMENT-RESULT", payload)

    @staticmethod
    def plot_beam_element_force(file_path: str="", stage_id: int = 1, case_name: str = "合计", show_increment: bool = False,
                                envelop_type: int = 1, component: int = 1,
                                show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 1,
                                show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                                show_undeformed: bool = False, position: int = 1,
                                is_time_history: bool = False, time_kind: int = 1, time_tick: float = 1.0) -> str:
        """
        绘制梁单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelop_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 1-Dx 2-Dy 3-Dz 4-Rx 5-Ry 6-Rz 7-Dxy 8-Dyz 9-Dxz 10-Dxyz
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            text_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 0-不显示最大最小值  1-显示最大值和最小值  2-最大绝对值 3-最大值 4-最小值
            show_legend: 图例选项卡开启
            show_undeformed: 显示变形前
            position: 位置编号 1-始端 2-末端 3-绝对最大 4-全部
            is_time_history:是否为时程分析结果
            time_kind:时程分析类型 1-时刻 2-最大 3-最小
            time_tick:时程分析时刻
        Example:
            odb.plot_beam_element_force(file_path=r"D:\\图片\\梁内力.png",component=1,case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "component": component,
            "show_line_chart": show_line_chart,
            "line_scale": line_scale,
            "flip_plot": flip_plot,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotation": text_rotation,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
            "position": position,
            "is_time_history": is_time_history,
            "time_kind": time_kind,
            "time_tick": time_tick,
        }
        return QtServer.send_get("PLOT-BEAM-ELEMENT-FORCE", payload)

    @staticmethod
    def plot_truss_element_force(file_path: str="", stage_id: int = 1, case_name: str = "合计", show_increment: bool = False,
                                 envelop_type: int = 1, component: int = 1,
                                 show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                 show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                 show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 1,
                                 show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                                 show_undeformed: bool = False, position: int = 1,
                                 is_time_history: bool = False, time_kind: int = 1, time_tick: float = 1.0) ->str:
        """
        绘制杆单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelop_type: 施工阶段包络类型 1-最大 2-最小
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
            text_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 0-不显示最大最小值  1-显示最大值和最小值  2-最大绝对值 3-最大值 4-最小值
            show_legend: 图例选项卡开启
            show_undeformed: 显示变形前
            position: 位置编号 1-始端 2-末端 3-绝对最大 4-全部
            is_time_history:是否为时程分析结果
            time_kind:时程分析类型 1-时刻 2-最大 3-最小
            time_tick:时程分析时刻
        Example:
            odb.plot_truss_element_force(file_path=r"D:\\图片\\杆内力.png",case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "component": component,
            "show_line_chart": show_line_chart,
            "line_scale": line_scale,
            "flip_plot": flip_plot,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotation": text_rotation,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
            "position": position,
            "is_time_history": is_time_history,
            "time_kind": time_kind,
            "time_tick": time_tick,
        }
        return QtServer.send_get("PLOT-TRUSS-ELEMENT-FORCE", payload)

    @staticmethod
    def plot_plate_element_force(file_path: str="", stage_id: int = 1, case_name: str = "合计", show_increment: bool = False,
                                 envelop_type: int = 1, force_kind: int = 1, component: int = 1,
                                 show_number: bool = False, text_rotate: int = 0, max_min_kind: int = 1,
                                 show_deformed: bool = True, deformed_scale: float = 1.0, deformed_actual: bool = False,
                                 show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                                 show_undeformed: bool = False, is_time_history: bool = False, time_kind: int = 1, time_tick: float = 1.0) ->str:
        """
        绘制板单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            component: 分量编号 1-Fxx 2-Fyy 3-Fxy 4-Mxx 5-Myy 6-Mxy
            force_kind: 内力选项 1-单元 2-节点平均
            case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelop_type: 包络类型
            show_number: 是否显示数值
            show_deformed: 是否显示变形形状
            show_undeformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotate: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            text_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment: 是否显示增量结果
            is_time_history:是否为时程分析结果
            time_kind:时程分析类型 1-时刻 2-最大 3-最小
            time_tick:时程分析时刻
        Example:
            odb.plot_plate_element_force(file_path=r"D:\\图片\\板内力.png",component=1,case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "force_kind": force_kind,
            "component": component,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotate": text_rotate,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
            "is_time_history": is_time_history,
            "time_kind": time_kind,
            "time_tick": time_tick,
        }
        return QtServer.send_get("PLOT-PLATE-ELEMENT-FORCE", payload)

    @staticmethod
    def plot_composite_beam_force(file_path: str="", stage_id: int = 1, case_name: str = "合计", show_increment: bool = False,
                                  envelop_type: int = 1, mat_type: int = 1, component: int = 1,
                                  show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                  show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                  show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 1,
                                  show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                                  show_undeformed: bool = False, position: int = 1)  ->str:
        """
        绘制组合梁单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelop_type: 施工阶段包络类型 1-最大 2-最小
            mat_type: 材料类型 1-主材 2-辅材 3-主材+辅材
            component: 分量编号 1-Fx 2-Fy 3-Fz 4-Mx 5-My 6-Mz
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            text_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 0-不显示最大最小值  1-显示最大值和最小值  2-最大绝对值 3-最大值 4-最小值
            show_legend: 图例选项卡开启
            show_undeformed: 显示变形前
            position: 位置编号 1-始端 2-末端 3-绝对最大 4-全部
        Example:
            odb.plot_composite_beam_force(file_path=r"D:\\图片\\组合梁内力.png",mat_type=0,component=1,case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "mat_type": mat_type,
            "component": component,
            "show_line_chart": show_line_chart,
            "line_scale": line_scale,
            "flip_plot": flip_plot,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotation": text_rotation,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
            "position": position,
        }
        return QtServer.send_get("PLOT-COMPOSITE-BEAM-FORCE", payload)

    @staticmethod
    def plot_beam_element_stress(file_path: str="", stage_id: int = 1, case_name: str = "合计", show_increment: bool = False,
                                 envelop_type: int = 1, component: int = 1,
                                 show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                 show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                 show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 1,
                                 show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                                 show_undeformed: bool = False, position: int = 1)  ->str:
        """
        绘制梁单元应力结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelop_type: 施工阶段包络类型 1-最大 2-最小
            component: 分量编号 1-轴力 2-Mzx 3-My 4-组合包络 5-左上 6-右上 7-右下 8-左下
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            text_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 0-不显示最大最小值  1-显示最大值和最小值  2-最大绝对值 3-最大值 4-最小值
            show_legend: 图例选项卡开启
            show_undeformed: 显示变形前
            position: 位置编号 1-始端 2-末端 3-绝对最大 4-全部
        Example:
            odb.plot_beam_element_stress(file_path=r"D:\\图片\\梁应力.png",show_line_chart=False,component=1,case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "component": component,
            "show_line_chart": show_line_chart,
            "line_scale": line_scale,
            "flip_plot": flip_plot,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotation": text_rotation,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
            "position": position,
        }
        return QtServer.send_get("PLOT-BEAM-ELEMENT-STRESS", payload)

    @staticmethod
    def plot_truss_element_stress(file_path: str="", stage_id: int = 1, case_name: str = "合计", show_increment: bool = False, envelop_type: int = 1,
                                  show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                  show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                  show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 1,
                                  show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                                  show_undeformed: bool = False, position: int = 1)  ->str:
        """
        绘制杆单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelop_type: 施工阶段包络类型 1-最大  2-最小
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            text_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 0-不显示最大最小值  1-显示最大值和最小值  2-最大绝对值 3-最大值 4-最小值
            show_legend: 图例选项卡开启
            show_undeformed: 显示变形前
            position: 位置编号 1-始端 2-末端 3-绝对最大 4-全部
        Example:
            odb.plot_truss_element_stress(file_path=r"D:\\图片\\杆应力.png",case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "show_line_chart": show_line_chart,
            "line_scale": line_scale,
            "flip_plot": flip_plot,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotation": text_rotation,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
            "position": position,
        }
        return QtServer.send_get("PLOT-TRUSS-ELEMENT-STRESS", payload)

    @staticmethod
    def plot_composite_beam_stress(file_path: str="", stage_id: int = 1, case_name: str = "合计", show_increment: bool = False,
                                   envelop_type: int = 1, mat_type: int = 0, component: int = 1,
                                   show_line_chart: bool = True, line_scale: float = 1.0, flip_plot: bool = True,
                                   show_deformed: bool = True, deformed_actual: bool = False, deformed_scale: float = 1.0,
                                   show_number: bool = False, text_rotation: int = 0, max_min_kind: int = 1,
                                   show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                                   show_undeformed: bool = False, position: int = 1)  ->str:
        """
        绘制组合梁单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号
            case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)
            show_increment: 是否显示增量结果
            envelop_type: 施工阶段包络类型 1-最大 2-最小
            mat_type: 材料类型 1-主材 2-辅材
            component: 分量编号 1-轴力分量 2-Mz分量 3-My分量 4-包络 5-左上 6-右上 7-左下 8-右下
            show_line_chart: 折线图选项卡开启
            line_scale:折线图比例
            flip_plot:反向绘制
            show_deformed: 变形选项卡开启
            deformed_scale:变形比例
            deformed_actual:是否显示实际变形
            show_number: 数值选项卡开启
            text_rotation: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            text_exponential: 指数显示开启
            max_min_kind: 数值选项卡内最大最小值显示 0-不显示最大最小值  1-显示最大值和最小值  2-最大绝对值 3-最大值 4-最小值
            show_legend: 图例选项卡开启
            show_undeformed: 显示变形前
            position: 位置编号 1-始端 2-末端 3-绝对最大 4-全部
        Example:
            odb.plot_composite_beam_stress(file_path=r"D:\\图片\\组合梁应力.png",component=1,case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "mat_type": mat_type,
            "component": component,
            "show_line_chart": show_line_chart,
            "line_scale": line_scale,
            "flip_plot": flip_plot,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotation": text_rotation,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
            "position": position,
        }
        return QtServer.send_get("PLOT-COMPOSITE-BEAM-STRESS", payload)

    @staticmethod
    def plot_plate_element_stress(file_path: str="", stage_id: int = 1, case_name: str = "合计", show_increment: bool = False,
                                  envelop_type: int = 1, stress_kind: int = 0, component: int = 1,
                                  show_number: bool = False, text_rotate: int = 0, max_min_kind: int = 1,
                                  show_deformed: bool = True, deformed_scale: float = 1.0, deformed_actual: bool = False,
                                  show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                                  show_undeformed: bool = False, position: int = 1)  ->str:
        """
        绘制板单元结果图并保存到指定文件
        Args:
            file_path: 保存路径名
            component: 分量编号 1-Fxx 2-Fyy 3-Fxy 4-Mxx 5-Myy 6-Mxy
            stress_kind: 力类型 1-单元 2-节点平均
            case_name: 详细荷载工况名
            stage_id: 阶段编号
            envelop_type: 包络类型
            show_number: 是否显示数值
            show_deformed: 是否显示变形形状
            show_undeformed: 是否显示未变形形状
            deformed_actual: 是否显示实际变形
            deformed_scale: 变形比例
            show_legend: 是否显示图例
            text_rotate: 数值选项卡内文字旋转角度
            digital_count: 小数点位数
            text_exponential: 是否以指数形式显示
            max_min_kind: 最大最小值显示类型
            show_increment: 是否显示增量结果
            position: 位置 1-板顶 2-板底 3-绝对值最大
        Example:
            odb.plot_plate_element_stress(file_path=r"D:\\图片\\板应力.png",component=1,case_name="CQ:成桥(合计)",stage_id=-1)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "stage_id": stage_id,
            "case_name": case_name,
            "show_increment": show_increment,
            "envelop_type": envelop_type,
            "stress_kind": stress_kind,
            "component": component,
            "show_deformed": show_deformed,
            "deformed_scale": deformed_scale,
            "deformed_actual": deformed_actual,
            "show_number": show_number,
            "text_rotate": text_rotate,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
            "position": position,
        }
        return QtServer.send_get("PLOT-PLATE-ELEMENT-STRESS", payload)

    @staticmethod
    def plot_modal_result(file_path: str="" , mode: int = 1, mode_kind: int = 1, show_number: bool = True,
                          text_rotate: float = 0, max_min_kind: int = 1,
                          show_legend: bool = True, digital_count: int = 3, text_exponential: bool = True,
                          show_undeformed: bool = False)  ->str:
        """
        绘制模态结果，可选择自振模态和屈曲模态结果
        Args:
           file_path: 保存路径名
           mode: 模态号
           mode_kind: 1-自振模态 2-屈曲模态
           show_number: 是否显示数值
           show_undeformed: 是否显示未变形形状
           show_legend: 是否显示图例
           text_rotate: 数值选项卡内文字旋转角度
           digital_count: 小数点位数
           text_exponential: 是否以指数形式显示
           max_min_kind: 最大最小值显示类型
        Example:
           odb.plot_modal_result(file_path=r"D:\\图片\\自振模态.png",mode=1)
           odb.plot_modal_result(file_path=r"D:\\图片\\屈曲模态.png",mode=1,mode_kind=2)
        Returns: Base64字符串
        """
        payload = {
            "file_path": file_path,
            "mode": mode,
            "mode_kind": mode_kind,
            "show_number": show_number,
            "text_rotate": text_rotate,
            "max_min_kind": max_min_kind,
            "show_legend": show_legend,
            "digital_count": digital_count,
            "text_exponential": text_exponential,
            "show_undeformed": show_undeformed,
        }
        return QtServer.send_get("PLOT-MODAL-RESULT", payload)

    @staticmethod
    def get_current_png() -> str:
        """
        获取当前窗口Base64格式(图形)字符串
        Args: 无
        Example:
            odb.get_current_png()
        Returns: Base64格式(图形)字符串
        """
        return QtServer.send_get("GET-CURRENT-PNG", None)
    # endregion
