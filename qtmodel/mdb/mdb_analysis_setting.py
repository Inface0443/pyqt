from typing import Union, List, Optional
from qtmodel.core.qt_server import QtServer
from qtmodel.core.data_helper import QtDataHelper


class MdbAnalysisSetting:
    """
    用于模型分析设置
    """

    # region 分析设置
    @staticmethod
    def update_project_setting(project: str = "", company: str = "", designer: str = "", reviewer: str = "",
                               date_time: str = "", gravity: float = 9.8, temperature: float = 0,
                               description: str = "") -> None:
        """
        更新总体设置
        Args:
            project: 项目名
            company: 公司名
            designer: 设计人员
            reviewer: 复核人员
            date_time: 时间
            gravity: 重力加速度 (m/s²)
            temperature: 设计温度 (摄氏度)
            description: 说明
        Example:
           mdb.update_project_setting(project="项目名",gravity=9.8,temperature=20)
        Returns: 无
        """
        try:
            s = "*PRJ-SET\r\n" + f"{gravity},{temperature}\r\n"
            # 映射 参数 -> KEY 名
            mapping = {
                "PROJECT": project,
                "COMPANY": company,
                "DESIGNER": designer,
                "REVIEWER": reviewer,
                "DATETIME": date_time,
                "DESCRIPTION": description
            }
            for key, val in mapping.items():
                if val:  # 字符串不为空
                    s += f"{key}={val}\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_global_setting(solver_type: int = 0, calculation_type: int = 2, thread_count: int = 12):
        """
        更新整体设置
        Args:
            solver_type:求解器类型 0-稀疏矩阵求解器  1-变带宽求解器
            calculation_type: 计算设置 0-单线程 1-用户自定义  2-自动设置
            thread_count: 线程数
        Example:
           mdb.update_global_setting(solver_type=0,calculation_type=2,thread_count=12)
        Returns: 无
        """
        s = "*GLB-SET\r\n" + f"{solver_type},{calculation_type},{thread_count}\r\n"
        QtServer.send_command(s, "QDAT")

    @staticmethod
    def update_construction_stage_setting(do_analysis: bool = True, to_end_stage: bool = True,
                                          other_stage_name: str = "", analysis_type: int = 0,
                                          do_creep_analysis: bool = True, cable_tension_position: int = 0,
                                          consider_completion_stage: bool = True,
                                          shrink_creep_type: int = 2, creep_load_type: int = 1,
                                          sub_step_info: Optional[tuple[bool, float, float, float, float, float]] = None):
        """
        更新施工阶段设置
        Args:
            do_analysis: 是否进行分析
            to_end_stage: 是否计算至最终阶段
            other_stage_name: 计算至其他阶段时名称
            analysis_type: 分析类型 (0-线性 1-非线性 2-部分非线性)
            do_creep_analysis: 是否进行徐变分析
            cable_tension_position: 索力张力位置 (0-I端 1-J端 2-平均索力)
            consider_completion_stage: 是否考虑成桥内力对运营阶段影响
            shrink_creep_type: 收缩徐变类型 (0-仅徐变 1-仅收缩 2-收缩徐变)
            creep_load_type: 徐变荷载类型  (1-开始  2-中间  3-结束)
            sub_step_info: 子步信息 [是否开启子部划分设置,10天步数,100天步数,1000天步数,5000天步数,10000天步数] None时为UI默认值
        Example:
            mdb.update_construction_stage_setting(do_analysis=True, to_end_stage=False, other_stage_name="1",analysis_type=0,
                do_creep_analysis=True, cable_tension_position=0, consider_completion_stage=True,shrink_creep_type=2)
        Returns: 无
        """
        do_str = "YES" if do_analysis else "NO"
        toend_str = "YES" if to_end_stage else "NO"
        creep_str = "YES" if do_creep_analysis else "NO"
        comp_str = "YES" if consider_completion_stage else "NO"
        s = "*CS-SET\r\n" + f"{do_str},{toend_str},{other_stage_name},{analysis_type},{creep_str},{cable_tension_position},{comp_str}\r\n"
        s += f"{shrink_creep_type},{creep_load_type},"
        s += f"{'YES' if sub_step_info[0] else 'NO'},{','.join(f'{x:g}' for x in sub_step_info[1:])}\r\n" if sub_step_info else "\r\n"
        QtServer.send_command(s, "QDAT")

    @staticmethod
    def update_live_load_setting(lateral_spacing: float = 0.1, vertical_spacing: float = 1, damper_calc_type: int = -1,
                                 displacement_calc_type: int = -1, force_calc_type: int = -1,
                                 reaction_calc_type: int = -1,
                                 link_calc_type: int = -1, constrain_calc_type: int = -1, eccentricity: float = 0.0,
                                 displacement_track: bool = False,
                                 force_track: bool = False,
                                 reaction_track: bool = False,
                                 link_track: bool = False,
                                 constrain_track: bool = False,
                                 damper_groups: Optional[list[str]] = None,
                                 displacement_groups: Optional[list[str]] = None,
                                 force_groups: Optional[list[str]] = None,
                                 reaction_groups: Optional[list[str]] = None,
                                 link_groups: Optional[list[str]] = None,
                                 constrain_groups: Optional[list[str]] = None):
        """
        更新移动荷载分析设置
        Args:
            lateral_spacing: 横向加密间距
            vertical_spacing: 纵向加密间距
            damper_calc_type: 模拟阻尼器约束方程计算类选项(-1-不考虑 0-全部组 1-部分)
            displacement_calc_type: 位移计算选项(-1-不考虑 0-全部组 1-部分)
            force_calc_type: 内力计算选项(-1-不考虑 0-全部组 1-部分)
            reaction_calc_type: 反力计算选项(-1-不考虑 0-全部组 1-部分)
            link_calc_type: 连接计算选项(-1-不考虑 0-全部组 1-部分)
            constrain_calc_type: 约束方程计算选项(-1-不考虑 0-全部组 1-部分)
            eccentricity: 离心力系数
            displacement_track: 是否追踪位移
            force_track: 是否追踪内力
            reaction_track: 是否追踪反力
            link_track: 是否追踪连接
            constrain_track: 是否追踪约束方程
            damper_groups: 模拟阻尼器约束方程计算类选项为组时边界组名称
            displacement_groups: 位移计算类选项为组时结构组名称
            force_groups: 内力计算类选项为组时结构组名称
            reaction_groups: 反力计算类选项为组时边界组名称
            link_groups:  弹性连接计算类选项为组时边界组名称
            constrain_groups: 约束方程计算类选项为组时边界组名称
        Example:
            mdb.update_live_load_setting(lateral_spacing=0.1, vertical_spacing=1, displacement_calc_type=1)
            mdb.update_live_load_setting(lateral_spacing=0.1, vertical_spacing=1, displacement_calc_type=2,displacement_track=True,
                displacement_groups=["结构组1","结构组2"])
        Returns: 无
        """
        s = "*LIV-SET\r\n" + f"{lateral_spacing:g},{vertical_spacing:g},{eccentricity:g},{'YES' if displacement_track else 'NO'},{'YES' if force_track else 'NO'},{'YES' if reaction_track else 'NO'},{'YES' if link_track else 'NO'},{'YES' if constrain_track else 'NO'}\r\n"
        if damper_calc_type != -1:
            s += f"1,{damper_calc_type},{','.join(damper_groups)}\r\n"

        lines = []
        configs = [
            (displacement_track, 2, displacement_calc_type, displacement_groups),
            (force_track, 3, force_calc_type, force_groups),
            (reaction_track, 4, reaction_calc_type, reaction_groups),
            (link_track, 5, link_calc_type, link_groups),
            (constrain_track, 6, constrain_calc_type, constrain_groups),
        ]

        for enabled, code, calc_type, groups in configs:
            if enabled:
                lines.append(QtDataHelper.live_load_set_line(code, calc_type, groups))

        s = "".join(lines)
        QtServer.send_command(s, "QDAT")

    @staticmethod
    def update_non_linear_setting(non_linear_type: int = 1, non_linear_method: int = 1, max_loading_steps: int = 1,
                                  max_iteration_times: int = 30,
                                  accuracy_of_displacement: float = 0.0001, accuracy_of_force: float = 0.0001):
        """
        更新非线性设置
        Args:
            non_linear_type: 非线性类型 0-部分非线性 1-非线性
            non_linear_method: 非线性方法 0-修正牛顿法 1-牛顿法
            max_loading_steps: 最大加载步数
            max_iteration_times: 最大迭代次数
            accuracy_of_displacement: 位移相对精度
            accuracy_of_force: 内力相对精度
        Example:
            mdb.update_non_linear_setting(non_linear_type=-1, non_linear_method=1, max_loading_steps=-1, max_iteration_times=30,
                accuracy_of_displacement=0.0001, accuracy_of_force=0.0001)
        Returns: 无
        """
        s = "*NON-SET\r\n" + f"{non_linear_type},{non_linear_method},{max_loading_steps},{max_iteration_times},{accuracy_of_displacement:g},{accuracy_of_force:g}\r\n"
        QtServer.send_command(s, "QDAT")

    @staticmethod
    def update_operation_stage_setting(do_analysis: bool = True, final_stage: str = "",
                                       static_load_cases: Optional[list[str]] = None,
                                       sink_load_cases: Optional[list[str]] = None,
                                       live_load_cases: Optional[list[str]] = None, ):
        """
        更新运营阶段分析设置
        Args:
            do_analysis: 是否进行运营阶段分析
            final_stage: 最终阶段名
            static_load_cases: 静力工况名列表
            sink_load_cases: 沉降工况名列表
            live_load_cases: 活载工况名列表
        Example:
            mdb.update_operation_stage_setting(do_analysis=True, final_stage="上二恒",static_load_cases=None)
        Returns: 无
        """
        s = "*OP-SET\r\n" + f"{'YES' if do_analysis else 'NO'},{final_stage}\r\n"
        if static_load_cases is not None:
            s += f"ST={','.join(static_load_cases)}\r\n"
        if sink_load_cases is not None:
            s += f"SM={','.join(sink_load_cases)}\r\n"
        if live_load_cases is not None:
            s += f"MV={','.join(live_load_cases)}\r\n"
        QtServer.send_command(s, "QDAT")

    @staticmethod
    def update_self_vibration_setting(do_analysis: bool = True, method: int = 1, matrix_type: int = 0,
                                      mode_num: int = 3):
        """
        更新自振分析设置
        Args:
            do_analysis: 是否进行运营阶段分析
            method: 计算方法 1-子空间迭代法 2-滤频法  3-多重Ritz法  4-兰索斯法
            matrix_type: 矩阵类型 0-集中质量矩阵  1-一致质量矩阵
            mode_num: 振型数量
        Example:
            mdb.update_self_vibration_setting(do_analysis=True,method=1,matrix_type=0,mode_num=3)
        Returns: 无
        """
        s = "*VB-SET\r\n" + f"{'YES' if do_analysis else 'NO'},{method},{matrix_type},{mode_num}\r\n"
        QtServer.send_command(s, "QDAT")

    @staticmethod
    def update_response_spectrum_setting(do_analysis: bool = True, kind: int = 1, by_mode: bool = False,
                                         damping_ratio: (Union[float, List[float]]) = 0.05):
        """
        更新反应谱设置
        Args:
            do_analysis:是否进行反应谱分析
            kind:组合方式 1-SRSS 2-CQC
            by_mode: 是否按照振型输入阻尼比
            damping_ratio:常数阻尼比或振型阻尼比列表
        Example:
            mdb.update_response_spectrum_setting(do_analysis=True,kind=1,damping_ratio=0.05)
        Returns: 无
        """
        if do_analysis:
            if isinstance(damping_ratio, float):
                damping_ratio = [damping_ratio]
            s = "*RS-SET\r\n" + f"{kind},{'YES' if by_mode else 'NO'},{','.join(f'{x:g}' for x in damping_ratio)}\r\n"
            QtServer.send_command(s, "QDAT")

    @staticmethod
    def update_time_history_setting(do_analysis: bool = True, output_all: bool = True, groups: Optional[list[str]] = None):
        """
        更新时程分析设置
        Args:
            do_analysis:是否进行反应谱分析
            output_all:是否输出所有结构组
            groups: 结构组列表
        Example:
            mdb.update_time_history_setting(do_analysis=True,output_all=True)
        Returns: 无
        """
        if do_analysis:
            s = "*TH-SET\r\n" + f"{'YES' if output_all else 'NO'}"
            if groups:
                s += "," + ','.join(groups) + "\r\n"
            else:
                s += "\r\n"
            QtServer.send_command(s, "QDAT")
            QtServer.send_command(s, "QDAT")

    @staticmethod
    def update_bulking_setting(do_analysis: bool = True, mode_count: int = 3, stage_id: int = -1,
                               calculate_kind: int = 1,
                               stressed: bool = True,
                               constant_cases: Optional[list[str]] = None,
                               variable_cases: list[str] = None):
        """
        更新屈曲分析设置
        Args:
            do_analysis:是否进行反应谱分析
            mode_count:模态数量
            stage_id: 指定施工阶段号(默认选取最后一个施工阶段)
            calculate_kind: 1-计为不变荷载 2-计为可变荷载
            stressed:是否指定施工阶段末的受力状态
            constant_cases: 不变荷载工况名称集合
            variable_cases: 可变荷载工况名称集合(必要参数)
        Example:
            mdb.update_bulking_setting(do_analysis=True,mode_count=3,variable_cases=["工况1","工况2"])
        Returns: 无
        """
        if do_analysis:
            s = "*BUK-SET\r\n" + f"{mode_count},{stage_id},{'YES' if stressed else 'NO'},{calculate_kind}\r\n"
            if variable_cases is None:
                raise Exception("操作错误，可变荷载工况名称集合为必要参数")
            else:
                s += f"VL={','.join(variable_cases)}\r\n"
            if constant_cases is not None:
                s += f"CL={','.join(constant_cases)}\r\n"
            QtServer.send_command(s, "QDAT")

    # endregion
