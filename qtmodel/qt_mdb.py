from __main__ import qt_model
from typing import Union, List


class Mdb:
    """
    建模与模型修改计算，所有函数均无返回值
    """

    # region 项目管理
    @staticmethod
    def update_bim():
        """
        刷新Bim模型信息
        Args: 无
        Example:
           mdb.update_bim()
        Returns: 无
        """
        try:
            qt_model.PostLoggerRequest()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_model():
        """
        刷新模型信息
        Args: 无
        Example:
            mdb.update_model()
        Returns: 无
        """
        try:
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_app_stage(num: int = 1):
        """
        切换模型前后处理状态
        Args:
            num: 1-前处理  2-后处理
        Example:
            mdb.update_app_stage(num=1)
            mdb.update_app_stage(num=2)
        Returns: 无
        """
        try:
            qt_model.UpdateAppStage(num)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def do_solve():
        """
        运行分析
        Args: 无
        Example:
            mdb.do_solve()
        Returns: 无
        """
        try:
            qt_model.DoSolve()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def initial():
        """
        初始化模型,新建模型
        Args: 无
        Example:
            mdb.initial()
        Returns: 无
        """
        try:
            qt_model.Initial()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def open_file(file_path: str):
        """
        打开bfmd文件
        Args:
            file_path: 文件全路径
        Example:
            mdb.open_file(file_path="a.bfmd")
        Returns: 无
        """
        try:
            if not file_path.endswith(".bfmd"):
                raise Exception("操作错误，仅支持bfmd文件")
            qt_model.OpenFile(file_path)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def close_project():
        """
        关闭项目
        Args: 无
        Example:
            mdb.close_project()
        Returns: 无
        """
        try:
            qt_model.CloseFile()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def save_file(file_path: str):
        """
        保存bfmd文件
        Args:
            file_path: 文件全路径
        Example:
            mdb.save_file(file_path="a.bfmd")
        Returns: 无
        """
        try:
            qt_model.SaveFile(file_path)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def import_command(command: str, command_type: int = 1):
        """
        导入命令
        Args:
            command:命令字符
            command_type:命令类型,默认桥通命令 1-桥通命令 2-mct命令
        Example:
            mdb.import_command(command="*SECTION")
            mdb.import_command(command="*SECTION",command_type=2)
        Returns: 无
        """
        try:
            if command_type == 2:
                qt_model.ImportMctCommand(command)
            else:
                qt_model.ImportQtCommand(command)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def import_file(file_path: str):
        """
        导入文件
        Args:
            file_path:导入文件(.mct/.qdat/.dxf/.3dx)
        Example:
            mdb.import_file(file_path="a.mct")
        Returns: 无
        """
        try:
            qt_model.ImportFile(file_path)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def export_file(file_path: str, convert_sec_group: bool = False, type_kind: int = 1, group_name: (Union[str, List[str]]) = None):
        """
        导入命令
        Args:
            file_path:导出文件全路径，支持格式(.mct/.qdat/.obj/.txt/.py)
            convert_sec_group:是否将变截面组转换为变截面
            type_kind:输出文件类型  1-详细文件  2-计算文件
            group_name:obj与 APDL导出时指定结构组导出
        Example:
            mdb.export_file(file_path="a.mct")
        Returns: 无
        """
        try:
            qt_model.ExportFile(filePath=file_path, convertSectionGroup=convert_sec_group, typeKind=type_kind, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 分析设置
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
        try:
            qt_model.UpdateGlobalSetting(solverType=solver_type, calculationType=calculation_type, threadCount=thread_count)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_construction_stage_setting(do_analysis: bool, to_end_stage: bool, other_stage_id: int = 1, analysis_type: int = 0,
                                          do_creep_analysis: bool = True, cable_tension_position: int = 0, consider_completion_stage: bool = True,
                                          shrink_creep_type: int = 2, creep_load_type: int = 1,
                                          sub_step_info: tuple[bool, float, float, float, float, float] = None):
        """
        更新施工阶段设置
        Args:
            do_analysis: 是否进行分析
            to_end_stage: 是否计算至最终阶段
            other_stage_id: 计算至其他阶段时ID
            analysis_type: 分析类型 (0-线性 1-非线性 2-部分非线性)
            do_creep_analysis: 是否进行徐变分析
            cable_tension_position: 索力张力位置 (0-I端 1-J端 2-平均索力)
            consider_completion_stage: 是否考虑成桥内力对运营阶段影响
            shrink_creep_type: 收缩徐变类型 (0-仅徐变 1-仅收缩 2-收缩徐变)
            creep_load_type: 徐变荷载类型  (1-开始  2-中间  3-结束)
            sub_step_info: 子步信息 [是否开启子部划分设置,10天步数,100天步数,1000天步数,5000天步数,10000天步数] None时为UI默认值
        Example:
            mdb.update_construction_stage_setting(do_analysis=True, to_end_stage=False, other_stage_id=1,analysis_type=0,
                do_creep_analysis=True, cable_tension_position=0, consider_completion_stage=True,shrink_creep_type=2)
        Returns: 无
        """
        try:
            qt_model.UpdateConstructionStageSetting(
                doAnalysis=do_analysis, toEndStage=to_end_stage, otherStageId=other_stage_id, analysisType=analysis_type,
                doCreepAnalysis=do_creep_analysis, cableTensionPosition=cable_tension_position, considerCompletionStage=consider_completion_stage,
                shrinkCreepType=shrink_creep_type, creepLoadType=creep_load_type,
                subStepInfo=sub_step_info)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_non_linear_setting(non_linear_type: int = 1, non_linear_method: int = 1, max_loading_steps: int = 1, max_iteration_times: int = 30,
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
        try:
            qt_model.UpdateNonLinearSetting(
                nonLinearType=non_linear_type, nonLinearMethod=non_linear_method, maxLoadingSteps=max_loading_steps,
                maxIterationTimes=max_iteration_times, relativeAccuracyOfDisplacement=accuracy_of_displacement,
                relativeAccuracyOfInternalForce=accuracy_of_force)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_operation_stage_setting(do_analysis: bool = True, final_stage: str = "", static_load_cases: list[str] = None,
                                       sink_load_cases: list[str] = None, live_load_cases: list[str] = None, ):
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
        try:
            qt_model.UpdateOperationStageSetting(
                doAnalysis=do_analysis, finalStage=final_stage,
                staticLoadCaseNames=static_load_cases, sinkLoadCaseNames=sink_load_cases, liveLoadCaseNames=live_load_cases)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_self_vibration_setting(do_analysis: bool = True, method: int = 1, matrix_type: int = 0, mode_num: int = 3):
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
        try:
            qt_model.UpdateSelfVibrationSetting(doAnalysis=do_analysis, method=method, matrixType=matrix_type, modeNumber=mode_num)
        except Exception as ex:
            raise Exception(ex)

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
        try:
            if isinstance(damping_ratio, float) and damping_ratio > 0:
                qt_model.UpdateResponseSpectrumSetting(doAnalysis=do_analysis, kind=kind, isDampingByMode=by_mode, dampingRatio=damping_ratio)
            elif isinstance(damping_ratio, list) and all(x > 0 for x in damping_ratio):
                qt_model.UpdateResponseSpectrumSetting(doAnalysis=do_analysis, kind=kind, isDampingByMode=by_mode, dampingRatio=damping_ratio)
            else:
                raise Exception("操作失败,要求阻尼比大于零")
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 节点操作
    @staticmethod
    def add_node(node_data: list[float], intersected: bool = True,
                 is_merged: bool = False, merge_error: float = 1e-4):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        Args:
             node_data: [id,x,y,z]  或 [x,y,z]
             intersected: 是否交叉分割
             is_merged: 是否忽略位置重复节点
             merge_error: 合并容许误差
        Example:
            mdb.add_node(node_data=[1,2,3])
            mdb.add_node(node_data=[1,1,2,3])
        Returns: 无
        """
        try:
            if len(node_data) == 4:
                qt_model.AddNode(id=node_data[0], x=node_data[1], y=node_data[2], z=node_data[3],
                                 intersected=intersected, isMerged=is_merged, merge_error=merge_error)
            elif len(node_data) == 3:
                qt_model.AddNode(x=node_data[0], y=node_data[1], z=node_data[2],
                                 intersected=intersected, isMerged=is_merged, merge_error=merge_error)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_nodes(node_data: list[list[float]], intersected: bool = True,
                  is_merged: bool = False, merge_error: float = 1e-4):
        """
        根据坐标信息和节点编号添加一组节点，需要指定节点号
        Args:
             node_data: [[id,x,y,z]...]
             intersected: 是否交叉分割
             is_merged: 是否忽略位置重复节点
             merge_error: 合并容许误差
        Example:
            mdb.add_nodes(node_data=[[1,1,2,3],[1,1,2,3]])
        Returns: 无
        """
        try:
            qt_model.AddNodes(nodeData=node_data, intersected=intersected, isMerged=is_merged, merge_error=merge_error)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_node(node_id: int, x: float = 1, y: float = 1, z: float = 1):
        """
        根据节点号修改节点坐标
        Args:
             node_id: 节点编号
             x: 更新后x坐标
             y: 更新后y坐标
             z: 更新后z坐标
        Example:
            mdb.update_node(node_id=1,x=2,y=2,z=2)
        Returns: 无
        """
        try:
            qt_model.UpdateNode(id=node_id, x=x, y=y, z=z)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_node_id(node_id: int, new_id: int):
        """
        修改节点Id
        Args:
             node_id: 节点编号
             new_id: 新节点编号
        Example:
            mdb.update_node_id(node_id=1,new_id=2)
        Returns: 无
        """
        try:
            qt_model.UpdateNodeId(nodeId=node_id, newId=new_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def merge_nodes(ids: list[int] = None, tolerance: float = 1e-4):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        Args:
             ids: 合并节点集合  默认全部节点
             tolerance: 合并容许误差
        Example:
            mdb.merge_nodes()
        Returns: 无
        """
        try:
            if ids is None:
                qt_model.MergeNode(tolerance)
            else:
                qt_model.MergeNodeByIds(ids, tolerance)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_node(ids=None):
        """
        删除指定节点,不输入参数时默认删除所有节点
        Args:
            ids:节点编号
        Example:
            mdb.remove_node()
            mdb.remove_node(ids=1)
            mdb.remove_node(ids=[1,2,3])
        Returns: 无
        """
        try:
            if ids is None:
                qt_model.RemoveAllNodes()
            elif type(ids) == int:
                qt_model.RemoveNode(id=ids)
            else:
                qt_model.RemoveNodes(ids=ids)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def renumber_node():
        """
        节点编号重拍
        Args: 无
        Example:
            mdb.renumber_node()
        Returns: 无
        """
        try:
            qt_model.RenumberNodeId()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def move_node(node_id: int, offset_x: float = 0, offset_y: float = 0, offset_z: float = 0):
        """
        移动节点坐标
        Args:
            node_id:节点号
            offset_x:X轴偏移量
            offset_y:Y轴偏移量
            offset_z:Z轴偏移量
        Example:
            mdb.move_node(node_id=1,offset_x=1.5,offset_y=1.5,offset_z=1.5)
        Returns: 无
        """
        try:
            qt_model.MoveNode(node_id, offsets=[offset_x, offset_y, offset_z])
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_structure_group(name: str = "", index: int = -1, node_ids: list[int] = None, element_ids: list[int] = None):
        """
        添加结构组
        Args:
            name: 结构组名
            index: 结构组编号(非必须参数)，默认自动识别当前编号
            node_ids: 节点编号列表(可选参数)
            element_ids: 单元编号列表(可选参数)
        Example:
            mdb.add_structure_group(name="新建结构组1")
            mdb.add_structure_group(name="新建结构组2",node_ids=[1,2,3,4],element_ids=[1,2])
        Returns: 无
        """
        try:
            qt_model.AddStructureGroup(name=name, id=index, nodeIds=node_ids, elementIds=element_ids)
            qt_model.UpdateModel()
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
                qt_model.RemoveStructureGroup(name=name)
            else:
                qt_model.RemoveAllStructureGroup()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_structure_to_group(name: str = "", node_ids: list[int] = None, element_ids: list[int] = None):
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
            if node_ids is None:
                node_ids = []
            if element_ids is None:
                element_ids = []
            qt_model.AddStructureToGroup(name=name, nodeIds=node_ids, elementIds=element_ids)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_structure_in_group(name: str = "", node_ids: list[int] = None, element_ids=None):
        """
        为结构组删除节点和/或单元
        Args:
            name: 结构组名
            node_ids: 节点编号列表(可选参数)
            element_ids: 单元编号列表(可选参数)
        Example:
            mdb.add_structure_to_group(name="现有结构组1",node_ids=[1,2,3,4],element_ids=[1,2])
        Returns: 无
        """
        try:
            if node_ids is None:
                node_ids = []
            if element_ids is None:
                element_ids = []
            qt_model.RemoveStructureOnGroup(name=name, nodeIds=node_ids, elementIds=element_ids)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 单元操作
    @staticmethod
    def add_element(index: int = 1, ele_type: int = 1, node_ids: list[int] = None, beta_angle: float = 0, mat_id: int = -1, sec_id: int = -1):
        """
        根据单元编号和单元类型添加单元
        Args:
            index:单元编号
            ele_type:单元类型 1-梁 2-索 3-杆 4-板
            node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]
            beta_angle:贝塔角
            mat_id:材料编号
            sec_id:截面编号
        Example:
            mdb.add_element(index=1,ele_type=1,node_ids=[1,2],beta_angle=1,mat_id=1,sec_id=1)
        Returns: 无
        """
        try:
            if node_ids is None and ele_type != 4:
                raise Exception("操作错误,请输入此单元所需节点列表,[i,j]")
            if node_ids is None and ele_type == 4:
                raise Exception("操作错误,请输入此板单元所需节点列表,[i,j,k,l]")
            if ele_type == 1:
                qt_model.AddBeam(id=index, idI=node_ids[0], idJ=node_ids[1], betaAngle=beta_angle, materialId=mat_id, sectionId=sec_id)
            elif ele_type == 2:
                qt_model.AddCable(id=index, idI=node_ids[0], idJ=node_ids[1], betaAngle=beta_angle, materialId=mat_id, sectionId=sec_id)
            elif ele_type == 3:
                qt_model.AddLink(id=index, idI=node_ids[0], idJ=node_ids[1], betaAngle=beta_angle, materialId=mat_id, sectionId=sec_id)
            else:
                qt_model.AddPlate(id=index, idI=node_ids[0], idJ=node_ids[1], idK=node_ids[2], idL=node_ids[3], betaAngle=beta_angle,
                                  materialId=mat_id,
                                  sectionId=sec_id)
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
                [编号,类型(4-板),materialId,thicknessId,betaAngle,nodeI,nodeJ,nodeK,nodeL]
        Example:
            mdb.add_elements(ele_data=[
                [1,1,1,1,0,1,2],
                [2,2,1,1,0,1,2],
                [3,3,1,1,0,1,2,1,100],
                [4,4,1,1,0,1,2,3,4]])
        Returns: 无
        """
        try:
            qt_model.AddElements(eleData=ele_data)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_element_material(index: int, mat_id: int):
        """
        更新指定单元的材料号
        Args:
            index: 单元编号
            mat_id: 材料编号
        Example:
            mdb.update_element_material(index=1,mat_id=2)
        Returns: 无
        """
        try:
            qt_model.UpdateElementMaterial(elementId=index, materialId=mat_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_element_beta_angle(index: int, beta_angle: float):
        """
        更新指定单元的贝塔角
        Args:
            index: 单元编号
            beta_angle: 贝塔角度数
        Example:
            mdb.update_element_beta_angle(index=1,beta_angle=90)
        Returns: 无
        """
        try:
            qt_model.UpdateElementBetaAngle(elementId=index, betaAngle=beta_angle)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_element_section(index: int, sec_id: int):
        """
        更新杆系单元截面或板单元板厚
        Args:
            index: 单元编号
            sec_id: 截面号
        Example:
            mdb.update_element_section(index=1,sec_id=2)
        Returns: 无
        """
        try:
            if qt_model.GetSectionType(index) == "PLATE":
                qt_model.UpdatePlateThickness(elementId=index, thicknessId=sec_id)
            else:
                qt_model.UpdateFrameSection(elementId=index, sectionId=sec_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_element_node(index: int, nodes: list[float]):
        """
        更新单元节点
        Args:
            index: 单元编号
            nodes: 杆系单元时为[node_i,node_j] 板单元[i,j,k,l]
        Example:
            mdb.update_element_node(1,[1,2])
            mdb.update_element_node(2,[1,2,3,4])
        Returns: 无
        """
        try:
            qt_model.UpdateElementNodes(elementId=index, nodeIds=nodes)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_element(index: int = None):
        """
        删除指定编号的单元
        Args:
            index: 单元编号,默认时删除所有单元
        Example:
            mdb.remove_element()
            mdb.remove_element(index=1)
        Returns: 无
        """
        try:
            if index is None:
                qt_model.RemoveAllElements()
            else:
                qt_model.RemoveElement(index=index)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 材料操作
    @staticmethod
    def add_material(index: int = -1, name: str = "", mat_type: int = 1, standard: int = 1, database: str = "C50",
                     construct_factor: float = 1, modified: bool = False, data_info: list[float] = None, creep_id: int = -1, f_cuk: float = 0):
        """
        添加材料
        Args:
            index:材料编号,默认自动识别 (可选参数)
            name:材料名称
            mat_type: 材料类型,1-混凝土 2-钢材 3-预应力 4-钢筋 5-自定义
            standard:规范序号,参考UI 默认从1开始
            database:数据库名称
            construct_factor:构造系数
            modified:是否修改默认材料参数,默认不修改 (可选参数)
            data_info:材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (可选参数)
            creep_id:徐变材料id (可选参数)
            f_cuk: 立方体抗压强度标准值 (可选参数)
        Example:
            mdb.add_material(index=1,name="混凝土材料1",mat_type=1,standard=1,database="C50")
            mdb.add_material(index=1,name="自定义材料1",mat_type=5,data_info=[3.5e10,2.5e4,0.2,1.5e-5])
        Returns: 无
        """
        try:
            if mat_type == 5:
                modified = True
            if modified and len(data_info) != 4:
                raise Exception("操作错误,modify_info数据无效!")
            if not modified:
                qt_model.AddMaterial(id=index, name=name, materialType=mat_type, standardIndex=standard,
                                     database=database, constructFactor=construct_factor, isModified=modified,
                                     timeParameterId=creep_id, fcuk=f_cuk)
            else:
                qt_model.AddMaterial(id=index, name=name, materialType=mat_type, standardIndex=standard,
                                     database=database, constructFactor=construct_factor, isModified=modified,
                                     elasticModulus=data_info[0], unitWeight=data_info[1],
                                     posiRatio=data_info[2], temperatureCoefficient=data_info[3],
                                     timeParameterId=creep_id, fcuk=f_cuk)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_time_material(index: int = -1, name: str = "", code_index: int = 1, time_parameter: list[float] = None):
        """
        添加收缩徐变材料
        Args:
            index: 指定收缩徐变编号,默认则自动识别 (可选参数)
            name: 收缩徐变名
            code_index: 收缩徐变规范索引
            time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)
        Example:
            mdb.add_time_material(index=1,name="收缩徐变材料1",code_index=1)
        Returns: 无
        """
        try:
            if time_parameter is None:  # 默认不修改收缩徐变相关参数
                qt_model.AddTimeParameter(id=index, name=name, codeId=code_index)
            elif code_index == 1:  # 公规 JTG 3362-2018
                if len(time_parameter) != 4:
                    raise Exception("操作错误,time_parameter数据无效!")
                qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, rh=time_parameter[0], bsc=time_parameter[1],
                                          timeStart=time_parameter[2], flyashCotent=time_parameter[3])
            elif code_index == 2:  # 公规 JTG D62-2004
                if len(time_parameter) != 3:
                    raise Exception("操作错误,time_parameter数据无效!")
                qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, rh=time_parameter[0], bsc=time_parameter[1],
                                          timeStart=time_parameter[2])
            elif code_index == 3:  # 公规 JTJ 023-85
                if len(time_parameter) != 4:
                    raise Exception("操作错误,time_parameter数据无效!")
                qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, creepBaseF1=time_parameter[0], creepNamda=time_parameter[1],
                                          shrinkSpeek=time_parameter[2], shrinkEnd=time_parameter[3])
            elif code_index == 4:  # 铁规 TB 10092-2017
                if len(time_parameter) != 5:
                    raise Exception("操作错误,time_parameter数据无效!")
                qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, rh=time_parameter[0], creepBaseF1=time_parameter[1],
                                          creepNamda=time_parameter[2], shrinkSpeek=time_parameter[3], shrinkEnd=time_parameter[4])
            elif code_index == 5:  # 地铁 GB 50157-2013
                if len(time_parameter) != 3:
                    raise Exception("操作错误,time_parameter数据无效!")
                qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, rh=time_parameter[0], shrinkSpeek=time_parameter[1],
                                          shrinkEnd=time_parameter[2])
            elif code_index == 6:  # 老化理论
                if len(time_parameter) != 4:
                    raise Exception("操作错误,time_parameter数据无效!")
                qt_model.AddTimeParameter(id=index, name=name, codeId=code_index, creepEnd=time_parameter[0], creepSpeek=time_parameter[1],
                                          shrinkSpeek=time_parameter[2], shrinkEnd=time_parameter[3])
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_material_creep(index: int = 1, creep_name: str = "", f_cuk: float = 0):
        """
        将收缩徐变参数连接到材料
        Args:
            index: 材料编号
            creep_name: 收缩徐变名称
            f_cuk: 材料标准抗压强度,仅自定义材料是需要输入
        Example:
            mdb.update_material_creep(index=1,creep_name="C60",f_cuk=5e7)
        Returns: 无
        """
        try:
            qt_model.UpdateMaterialCreep(materialId=index, creepName=creep_name, fcuk=f_cuk)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_material(index: int = -1):
        """
        删除指定材料
        Args:
            index:指定材料编号，默认则删除所有材料
        Example:
            mdb.remove_material()
            mdb.remove_material(index=1)
        Returns: 无
        """
        try:
            if index == -1:
                qt_model.RemoveAllMaterial()
            else:
                qt_model.RemoveMaterial(id=index)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 截面操作
    @staticmethod
    def add_section(index: int = -1, name: str = "", sec_type: str = "矩形", sec_info: list[float] = None,
                    symmetry: bool = True, charm_info: list[str] = None, sec_right: list[float] = None,
                    charm_right: list[str] = None, box_num: int = 3, box_height: float = 2,
                    mat_combine: list[float] = None, rib_info: dict[str, list[float]] = None,
                    rib_place: list[tuple[int, int, float, str, int, str]] = None,
                    loop_segments: list[dict] = None, sec_lines: list[tuple[float, float, float, float, float]] = None,
                    secondary_loop_segments: list[dict] = None, sec_property: list[float] = None,
                    bias_type: str = "中心", center_type: str = "质心", shear_consider: bool = True, bias_x: float = 0, bias_y: float = 0):
        """
        添加单一截面信息,如果截面存在则自动覆盖
        Args:
            index: 截面编号,默认自动识别
            name:截面名称
            sec_type:参数截面类型名称(详见UI界面)
            sec_info:截面信息 (必要参数)
            symmetry:混凝土截面是否对称 (仅混凝土箱梁截面需要)
            charm_info:混凝土截面倒角信息 (仅混凝土箱梁截面需要)
            sec_right:混凝土截面右半信息 (对称时可忽略，仅混凝土箱梁截面需要)
            charm_right:混凝土截面右半倒角信息 (对称时可忽略，仅混凝土箱梁截面需要)
            box_num: 混凝土箱室数 (仅混凝土箱梁截面需要)
            box_height: 混凝土箱梁梁高 (仅混凝土箱梁截面需要)
            mat_combine: 组合截面材料信息 (仅组合材料需要) [弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c]
            rib_info:肋板信息
            rib_place:肋板位置 list[tuple[布置具体部位,参考点0-下/左,距参考点间距,肋板名，加劲肋位置0-上/左 1-下/右 2-两侧,加劲肋名]]
                布置具体部位(工字钢梁):1-上左 2-上右 3-腹板 4-下左 5-下右
                布置具体部位(箱型钢梁):1-上左 2-上中 3-上右 4-左腹板 5-右腹板 6-下左 7-下中 8-下右
            sec_info:截面特性列表，共计26个参数参考UI截面
            loop_segments:线圈坐标集合 list[dict] dict示例:{"main":[(x1,y1),(x2,y2)...],"sub1":[(x1,y1),(x2,y2)...],"sub2":[(x1,y1),(x2,y2)...]}
            sec_lines:线宽集合[(x1,y1,x2,y3,thick),]
            secondary_loop_segments:辅材线圈坐标集合 list[dict] (同loop_segments)
            sec_property:截面特性(参考UI界面共计26个参数)，可选参数，指定截面特性时不进行截面计算
            bias_type:偏心类型 默认中心
            center_type:中心类型 默认质心
            shear_consider:考虑剪切 bool 默认考虑剪切变形
            bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要,相对于center_type偏移)
            bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要,相对于center_type偏移)
        Example:
            mdb.add_section(name="截面1",sec_type="矩形",sec_info=[2,4],bias_type="中心")
            mdb.add_section(name="截面2",sec_type="混凝土箱梁",box_height=2,box_num=3,
                sec_info=[0.02,0,12,3,1,2,1,5,6,0.2,0.4,0.1,0.13,0.28,0.3,0.5,0.5,0.5,0.2],
                charm_info=["1*0.2,0.1*0.2","0.5*0.15,0.3*0.2","0.4*0.2","0.5*0.2"])
            mdb.add_section(name="钢梁截面1",sec_type="工字钢梁",sec_info=[0,0,0.5,0.5,0.5,0.5,0.7,0.02,0.02,0.02])
            mdb.add_section(name="钢梁截面2",sec_type="箱型钢梁",sec_info=[0,0.15,0.25,0.5,0.25,0.15,0.4,0.15,0.7,0.02,0.02,0.02,0.02],
                rib_info = {"板肋1": [0.1,0.02],"T形肋1":[0.1,0.02,0.02,0.02]},
                rib_place = [(1, 0, 0.1, "板肋1", 2, "默认名称1"),
                            (1, 0, 0.2, "板肋1", 2, "默认名称1")])
        Returns: 无
            """
        try:
            if sec_type == "混凝土箱梁":
                qt_model.AddSection(id=index, name=name, secType=sec_type, secInfo=sec_info, charmInfo=charm_info,
                                    symmetry=symmetry, boxNum=box_num, H=box_height, charmInfoR=charm_right, secInfoR=sec_right,
                                    biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                    biasX=bias_x, biasY=bias_y, secProperty=sec_property)
            elif sec_type == "工字钢梁" or sec_type == "箱型钢梁":
                rib_names = list(rib_info.keys())
                rib_data = list(rib_info.values())
                qt_model.AddSection(id=index, name=name, secType=sec_type, secInfo=sec_info,
                                    ribNameList=rib_names, ribInfoList=rib_data,
                                    ribPlaceList=rib_place, biasType=bias_type, centerType=center_type,
                                    shearConsider=shear_consider, biasX=bias_x, biasY=bias_y, secProperty=sec_property)
            elif sec_type == "特性截面" or sec_type.startswith("自定义"):
                qt_model.AddSection(id=index, name=name, secType=sec_type, secInfo=sec_info, biasType=bias_type,
                                    loopSegments=loop_segments, secLines=sec_lines,
                                    secondaryLoopSegments=secondary_loop_segments, matCombine=mat_combine,
                                    shearConsider=shear_consider, centerType=center_type,
                                    biasX=bias_x, biasY=bias_y, secProperty=sec_property)
            else:
                qt_model.AddSection(id=index, name=name, secType=sec_type, secInfo=sec_info, matCombine=mat_combine,
                                    biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                    biasX=bias_x, biasY=bias_y, secProperty=sec_property)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_single_section(index: int = -1, name: str = "", sec_type: str = "矩形", sec_dict: dict = None):
        """
        以字典形式添加单一截面
        Args:
            index:截面编号
            name:截面名称
            sec_type:截面类型
            sec_dict:截面始端编号
        Example:
            mdb.add_single_section(index=1,name="变截面1",sec_type="矩形",
                sec_dict={"sec_info":[1,2],"bias_type":"中心"})
        Returns: 无
        """
        try:
            qt_model.AddSingleSection(id=index, name=name, secType=sec_type, secDict=sec_dict)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_tapper_section(index: int = -1, name: str = "", sec_type: str = "矩形", sec_begin: dict = None, sec_end: dict = None,
                           shear_consider: bool = True, sec_normalize: bool = False):
        """
        添加变截面,字典参数参考单一截面,如果截面存在则自动覆盖
        Args:
            index:截面编号
            name:截面名称
            sec_type:截面类型
            sec_begin:截面始端编号
            sec_end:截面末端编号
            shear_consider:考虑剪切变形
            sec_normalize:变截面线段线圈重新排序
        Example:
            mdb.add_tapper_section(index=1,name="变截面1",sec_type="矩形",
                sec_begin={"sec_info":[1,2],"bias_type":"中心"},
                sec_end={"sec_info":[2,2],"bias_type":"中心"})
        Returns: 无
        """
        try:
            qt_model.AddTapperSection(id=index, name=name, secType=sec_type, secBegin=sec_begin, secEnd=sec_end,
                                      shearConsider=shear_consider, secNormalize=sec_normalize)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_tapper_section_by_id(index: int = -1, name: str = "", begin_id: int = 1, end_id: int = 1):
        """
        添加变截面,需先建立单一截面
        Args:
            index:截面编号
            name:截面名称
            begin_id:截面始端编号
            end_id:截面末端编号
        Example:
            mdb.add_tapper_section_by_id(name="变截面1",begin_id=1,end_id=2)
        Returns: 无
        """
        try:
            qt_model.AddTapperSectionById(id=index, name=name, beginId=begin_id, endId=end_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_section(index: int = -1):
        """
        删除截面信息
        Args:
            index: 截面编号,参数为默认时删除全部截面
        Example:
            mdb.remove_section()
            mdb.remove_section(1)
        Returns: 无
        """
        try:
            if index == -1:
                qt_model.RemoveAllSection()
            else:
                qt_model.RemoveSection(id=index)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 板厚操作
    @staticmethod
    def add_thickness(index: int = -1, name: str = "", t: float = 0,
                      thick_type: int = 0, bias_info: tuple[int, float] = None,
                      rib_pos: int = 0, dist_v: float = 0, dist_l: float = 0, rib_v=None, rib_l=None):
        """
        添加板厚
        Args:
            index: 板厚id
            name: 板厚名称
            t:   板厚度
            thick_type: 板厚类型 0-普通板 1-加劲肋板
            bias_info: 默认不偏心,偏心时输入列表[type,value]
                _type:0-厚度比 1-数值_
            rib_pos: 肋板位置 0-下部 1-上部
            dist_v: 纵向截面肋板间距
            dist_l: 横向截面肋板间距
            rib_v: 纵向肋板信息
            rib_l: 横向肋板信息
        Example:
            mdb.add_thickness(name="厚度1", t=0.2,thick_type=0,bias_info=(0,0.8))
            mdb.add_thickness(name="厚度2", t=0.2,thick_type=1,rib_pos=0,dist_v=0.1,rib_v=[1,1,0.02,0.02])
        Returns: 无
        """
        try:
            if rib_v is None:
                rib_v = []
            if rib_l is None:
                rib_l = []
            if bias_info is None:
                qt_model.AddThickness(id=index, name=name, t=t, thickType=thick_type, isBiased=False, ribPos=rib_pos,
                                      verticalDis=dist_v, lateralDis=dist_l, verticalRib=rib_v, lateralRib=rib_l)
            else:
                qt_model.AddThickness(id=index, name=name, t=t, thickType=thick_type, isBiased=False, ribPos=rib_pos,
                                      offSetType=bias_info[0], offSetValue=bias_info[1],
                                      verticalDis=dist_v, lateralDis=dist_l, verticalRib=rib_v, lateralRib=rib_l)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_thickness(index: int = -1):
        """
        删除板厚
        Args:
             index:板厚编号,默认时删除所有板厚信息
        Example:
            mdb.remove_thickness()
            mdb.remove_thickness(index=1)
        Returns: 无
        """
        try:
            if index == -1:
                qt_model.RemoveAllThickness()
            else:
                qt_model.RemoveThickness(id=index)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_tapper_section_group(ids: list[int] = None, name: str = "", factor_w: float = 1.0, factor_h: float = 1.0,
                                 ref_w: int = 0, ref_h: int = 0, dis_w: float = 0, dis_h: float = 0):
        """
        添加变截面组
        Args:
             ids:变截面组编号
             name: 变截面组名
             factor_w: 宽度方向变化阶数 线性(1.0) 非线性(!=1.0)
             factor_h: 高度方向变化阶数 线性(1.0) 非线性(!=1.0)
             ref_w: 宽度方向参考点 0-i 1-j
             ref_h: 高度方向参考点 0-i 1-j
             dis_w: 宽度方向距离
             dis_h: 高度方向距离
        Example:
            mdb.add_tapper_section_group(ids=[1,2,3,4],name="变截面组1")
        Returns: 无
        """
        try:
            qt_model.AddTapperSectionGroup(ids=ids, name=name, factorW=factor_w, factorH=factor_h, w=ref_w, h=ref_h, disW=dis_w, disH=dis_h)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_section_bias(index: int = 1, bias_type: str = "中心", center_type: str = "质心", shear_consider: bool = True,
                            bias_point: list[float] = None):
        """
        更新截面偏心
        Args:
             index:截面编号
             bias_type:偏心类型
             center_type:中心类型
             shear_consider:考虑剪切
             bias_point:自定义偏心点(仅自定义类型偏心需要)
        Example:
            mdb.update_section_bias(index=1,bias_type="中上",center_type="几何中心")
            mdb.update_section_bias(index=1,bias_type="自定义",bias_point=[0.1,0.2])
        Returns: 无
        """
        try:
            if center_type == "自定义":
                if len(bias_point) != 2:
                    raise Exception("操作错误,bias_point数据无效!")
                qt_model.UpdateSectionBias(id=index, biasType=bias_type, centerType=center_type,
                                           shearConsider=shear_consider, horizontalPos=bias_point[0], verticalPos=bias_point[1])
            else:
                qt_model.UpdateSectionBias(id=index, biasType=bias_type, centerType=center_type,
                                           shearConsider=shear_consider)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 边界操作
    @staticmethod
    def add_boundary_group(name: str = ""):
        """
        新建边界组
        Args:
            name:边界组名
        Example:
            mdb.add_boundary_group(name="边界组1")
        Returns: 无
        """
        try:
            qt_model.AddBoundaryGroup(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_boundary_group(name: str = ""):
        """
        按照名称删除边界组
        Args:
            name: 边界组名称，默认删除所有边界组 (非必须参数)
        Example:
            mdb.remove_boundary_group()
            mdb.remove_boundary_group(name="边界组1")
        Returns: 无
        """
        try:
            if name != "":
                qt_model.RemoveBoundaryGroup(name)
            else:
                qt_model.RemoveAllBoundaryGroup()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_all_boundary():
        """
        根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息
        Args:无
        Example:
            mdb.remove_all_boundary()
        Returns: 无
        """
        try:
            qt_model.RemoveAllBoundary()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_boundary(remove_id: int, bd_type: int, group: str = "默认边界组"):
        """
        根据节点号删除一般支撑、弹性支承/根据单元号删除梁端约束/根据主节点号删除主从约束/根据从节点号删除约束方程
        Args:
            remove_id:节点号 or 单元号 or主节点号  or 从节点号
            bd_type:边界类型
                _1-一般支承 2-弹性支承 3-主从约束 4-弹性连接 5-约束方程 6-梁端约束_
            group:边界所处边界组名
        Example:
            mdb.remove_boundary(remove_id = 1, bd_type = 1,group="边界组1")
        Returns: 无
        """
        try:
            type_list = ["一般支承", "弹性支承", "主从约束", "弹性连接", "约束方程", "梁端约束"]
            bd_name = type_list[bd_type - 1]
            qt_model.RemoveBoundary(controlId=remove_id, type=bd_name, group=group)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_general_support(node_id: (Union[int, List[int]]) = 1, boundary_info: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加一般支承
        Args:
             node_id:节点编号,支持整数或整数型列表
             boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]  ture-固定 false-自由
             group_name:边界组名,默认为默认边界组
        Example:
            mdb.add_general_support(node_id=1, boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        try:
            if boundary_info is None or len(boundary_info) != 6:
                raise Exception("操作错误，要求输入一般支承列表长度为6")
            qt_model.AddGeneralSupport(nodeId=node_id, boundaryInfo=boundary_info, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_elastic_support(node_id: (Union[int, List[int]]) = 1, support_type: int = 1, boundary_info: list[float] = None,
                            group_name: str = "默认边界组"):
        """
        添加弹性支承
        Args:
             node_id:节点编号,支持数或列表
             support_type:支承类型 1-线性  2-受拉  3-受压
             boundary_info:边界信息 受拉和受压时列表长度为2-[direct(1-X 2-Y 3-Z),stiffness]  线性时列表长度为6-[kx,ky,kz,krx,kry,krz]
             group_name:边界组
        Example:
            mdb.add_elastic_support(node_id=1,support_type=1,boundary_info=[1e6,0,1e6,0,0,0])
            mdb.add_elastic_support(node_id=1,support_type=2,boundary_info=[1,1e6])
            mdb.add_elastic_support(node_id=1,support_type=3,boundary_info=[1,1e6])
        Returns: 无
        """
        try:
            qt_model.AddElasticSupport(nodeId=node_id, supportType=support_type, boundaryInfo=boundary_info,
                                       groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_elastic_link(link_type: int = 1, start_id: int = 1, end_id: int = 2, beta_angle: float = 0,
                         boundary_info: list[float] = None,
                         group_name: str = "默认边界组", dis_ratio: float = 0.5, kx: float = 0):
        """
        添加弹性连接
        Args:
             link_type:节点类型 1-一般弹性连接 2-刚性连接 3-受拉弹性连接 4-受压弹性连接
             start_id:起始节点号
             end_id:终节点号
             beta_angle:贝塔角
             boundary_info:边界信息
             group_name:边界组名
             dis_ratio:距i端距离比 (仅一般弹性连接需要)
             kx:受拉或受压刚度
        Example:
            mdb.add_elastic_link(link_type=1,start_id=1,end_id=2,boundary_info=[1e6,1e6,1e6,0,0,0])
            mdb.add_elastic_link(link_type=2,start_id=1,end_id=2)
            mdb.add_elastic_link(link_type=3,start_id=1,end_id=2,kx=1e6)
        Returns: 无
        """
        try:
            qt_model.AddElasticLink(linkType=link_type, startId=start_id, endId=end_id, beta=beta_angle,
                                    boundaryInfo=boundary_info, groupName=group_name, disRatio=dis_ratio, kDx=kx)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_master_slave_links(node_ids: list[tuple[int, int]] = None, boundary_info: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加主从约束
        Args:
             node_ids:主节点号和从节点号，主节点号位于首位
             boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             group_name:边界组名
        Example:
            mdb.add_master_slave_links(node_ids=[(1,2),(1,3),(4,5),(4,6)],boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        try:
            qt_model.AddMasterSlaveLinks(nodeIds=node_ids, boundaryInfo=boundary_info, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_master_slave_link(master_id: int = 1, slave_id: (Union[int, List[int]]) = None,
                              boundary_info: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加主从约束
        Args:
             master_id:主节点号
             slave_id:从节点号，支持整数或整数型列表
             boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             group_name:边界组名
        Example:
            mdb.add_master_slave_link(master_id=1,slave_id=[2,3],boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        try:
            qt_model.AddMasterSlaveLink(masterId=master_id, slaveId=slave_id, boundaryInfo=boundary_info, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_node_axis(input_type: int = 1, node_id: int = 1, coord_info: list = None):
        """
        添加节点坐标
        Args:
             input_type:输入方式 1-角度 2-三点  3-向量
             node_id:节点号
             coord_info:局部坐标信息 -List<float>(角)  -List<List<float>>(三点 or 向量)
        Example:
            mdb.add_node_axis(input_type=1,node_id=1,coord_info=[45,45,45])
            mdb.add_node_axis(input_type=2,node_id=1,coord_info=[[0,0,1],[0,1,0],[1,0,0]])
            mdb.add_node_axis(input_type=3,node_id=1,coord_info=[[0,0,1],[0,1,0]])
        Returns: 无
        """
        try:
            if coord_info is None:
                raise Exception("操作错误，输入坐标系信息不能为空")
            if input_type == 1:
                qt_model.AddNodalAxis(inputType=input_type, nodeId=node_id, angleInfo=coord_info)
            else:
                qt_model.AddNodalAxis(inputType=input_type, nodeId=node_id, nodeInfo=coord_info)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_beam_constraint(beam_id: int = 2, info_i: list[bool] = None, info_j: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加梁端约束
        Args:
             beam_id:梁号
             info_i:i端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             info_j:j端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             group_name:边界组名
        Example:
            mdb.add_beam_constraint(beam_id=2,info_i=[True,True,True,False,False,False],info_j=[True,True,True,False,False,False])
        Returns: 无
        """
        try:
            if info_i is None or len(info_i) != 6:
                raise Exception("操作错误，要求输入I端约束列表长度为6")
            if info_j is None or len(info_j) != 6:
                raise Exception("操作错误，要求输入J端约束列表长度为6")
            qt_model.AddBeamConstraint(beamId=beam_id, infoI=info_i, infoJ=info_j, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_constraint_equation(name: str, sec_node: int, sec_dof: int,
                                master_info: list[tuple[int, int, float]] = None, group_name: str = "默认边界组"):
        """
        添加约束方程
        Args:
             name:约束方程名
             sec_node:从节点号
             sec_dof: 从节点自由度 1-x 2-y 3-z 4-rx 5-ry 6-rz
             master_info:主节点约束信息列表
             group_name:边界组名
        Example:
            mdb.add_beam_constraint(beam_id=2,info_i=[True,True,True,False,False,False],info_j=[True,True,True,False,False,False])
        Returns: 无
        """
        try:
            qt_model.AddConstraintEquation(name=name, nodeId=sec_node, dofDirect=sec_dof, masterNodeInfo=master_info, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 移动荷载操作
    @staticmethod
    def add_standard_vehicle(name: str, standard_code: int = 1, load_type: str = "高速铁路",
                             load_length: float = 0, n: int = 6, calc_fatigue: bool = False):
        """
        添加标准车辆
        Args:
             name: 车辆荷载名称
             standard_code: 荷载规范
                _1-中国铁路桥涵规范(TB10002-2017)_
                _2-城市桥梁设计规范(CJJ11-2019)_
                _3-公路工程技术标准(JTJ 001-97)_
                _4-公路桥涵设计通规(JTG D60-2004)_
                _5-公路桥涵设计通规(JTG D60-2015)_
                _6-城市轨道交通桥梁设计规范(GB/T51234-2017)_
                _7-市域铁路设计规范2017(T/CRS C0101-2017)
             load_type: 荷载类型,支持类型参考软件内界面
             load_length: 默认为0即不限制荷载长度  (铁路桥涵规范2017 所需参数)
             n:车厢数: 默认6节车厢 (城市轨道交通桥梁规范2017 所需参数)
             calc_fatigue:计算公路疲劳 (公路桥涵设计通规2015 所需参数)
        Example:
            mdb.add_standard_vehicle("高速铁路",standard_code=1,load_type="高速铁路")
        Returns: 无
        """
        try:
            qt_model.AddStandardVehicle(name=name, standardIndex=standard_code, loadType=load_type,
                                        loadLength=load_length, N=n, calcFatigue=calc_fatigue)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_user_vehicle(name: str, load_type: str = "车辆荷载", p: (Union[float, List[float]]) = 270000, q: float = 10500,
                         dis: list[float] = None, load_length: float = 500, n: int = 6, empty_load: float = 90000,
                         width: float = 1.5, wheelbase: float = 1.8, min_dis: float = 1.5,
                         unit_force: str = "N", unit_length: str = "M"):
        """
            添加标准车辆
        Args:
             name: 车辆荷载名称
             load_type: 荷载类型,支持类型 -车辆/车道荷载 列车普通活载 城市轻轨活载 旧公路人群荷载 轮重集合
             p: 荷载Pk或Pi列表
             q: 均布荷载Qk或荷载集度dW
             dis:荷载距离Li列表
             load_length: 荷载长度  (列车普通活载 所需参数)
             n:车厢数: 默认6节车厢 (列车普通活载 所需参数)
             empty_load:空载 (列车普通活载、城市轻轨活载 所需参数)
             width:宽度 (旧公路人群荷载 所需参数)
             wheelbase:轮间距 (轮重集合 所需参数)
             min_dis:车轮距影响面最小距离 (轮重集合 所需参数))
             unit_force:荷载单位 默认为"N"
             unit_length:长度单位 默认为"M"
        Example:
            mdb.add_user_vehicle(name="车道荷载",load_type="车道荷载",p=270000,q=10500)
        Returns: 无
        """
        try:
            qt_model.AddUserVehicle(name=name, loadType=load_type, p=p, q=q, dis=dis, loadLength=load_length,
                                    num=n, emptyLoad=empty_load, width=width, wheelbase=wheelbase,
                                    minDistance=min_dis, unitForce=unit_force, unitLength=unit_length)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_node_tandem(name: str, start_id: int, node_ids: list[int]):
        """
        添加节点纵列
        Args:
             name:节点纵列名
             start_id:起始节点号
             node_ids:节点列表
        Example:
            mdb.add_node_tandem(name="节点纵列1",start_id=1,node_ids=[i+1 for i in range(12)])
        Returns: 无
        """
        try:
            if node_ids is None:
                raise Exception("操作错误，输入节点列表不能为空")
            qt_model.AddNodeTandem(name=name, startId=start_id, nodeIds=node_ids)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_influence_plane(name: str, tandem_names: list[str]):
        """
        添加影响面
        Args:
             name:影响面名称
             tandem_names:节点纵列名称组
        Example:
            mdb.add_influence_plane(name="影响面1",tandem_names=["节点纵列1","节点纵列2"])
        Returns: 无
        """
        try:
            qt_model.AddInfluencePlane(name=name, tandemNames=tandem_names)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_lane_line(name: str, influence_name: str, tandem_name: str, offset: float = 0, lane_width: float = 0):
        """
        添加车道线
        Args:
             name:车道线名称
             influence_name:影响面名称
             tandem_name:节点纵列名
             offset:偏移
             lane_width:车道宽度
        Example:
            mdb.add_lane_line(name="车道1",influence_name="影响面1",tandem_name="节点纵列1",offset=0,lane_width=3.1)
        Returns: 无
        """
        try:
            qt_model.AddLaneLine(name, influenceName=influence_name, tandemName=tandem_name, offset=offset, laneWidth=lane_width)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_live_load_case(name: str, influence_plane: str, span: float,
                           sub_case: list[tuple[str, float, list[str]]] = None,
                           trailer_code: str = "", special_code: str = ""):
        """
        添加移动荷载工况
        Args:
             name:活载工况名
             influence_plane:影响线名
             span:跨度
             sub_case:子工况信息 [(车辆名称,系数,["车道1","车道2"])...]
             trailer_code:考虑挂车时挂车车辆名
             special_code:考虑特载时特载车辆名
        Example:
            mdb.add_live_load_case(name="活载工况1",influence_plane="影响面1",span=100,sub_case=[("车辆名称",1.0,["车道1","车道2"]),])
        Returns: 无
        """
        try:
            if sub_case is None:
                raise Exception("操作错误，子工况信息列表不能为空")
            qt_model.AddLiveLoadCase(name=name, influencePlane=influence_plane, span=span, subCase=sub_case,
                                     trailerCode=trailer_code, specialCode=special_code)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_car_relative_factor(name: str, code_index: int, cross_factors: list[float] = None, longitude_factor: float = -1,
                                impact_factor: float = -1, frequency: float = 14):
        """
        添加移动荷载工况汽车折减
        Args:
             name:活载工况名
             code_index: 汽车折减规范编号  1-公规2015 2-公规2004 3-无
             cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取
             longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取
             impact_factor:冲击系数大于1时为自定义，否则按照规范自动选取
             frequency:桥梁基频
        Example:
            mdb.add_car_relative_factor(name="活载工况1",code_index=1,cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5])
        Returns: 无
        """
        try:
            qt_model.AddCarRelativeFactor(name=name, codeIndex=code_index, crossFactors=cross_factors,
                                          longitudeFactor=longitude_factor,
                                          impactFactor=impact_factor, frequency=frequency)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_train_relative_factor(name: str, code_index: int = 1, cross_factors: list[float] = None, calc_fatigue: bool = False,
                                  line_count: int = 0, longitude_factor: int = -1, impact_factor: int = -1,
                                  fatigue_factor: int = -1, bridge_kind: int = 0, fill_thick: float = 0.5,
                                  rise: float = 1.5, calc_length: float = 50):
        """
        添加移动荷载工况汽车折减
        Args:
            name:活载工况名
            code_index: 汽车折减规范编号  1-铁规2017_ZK_ZC 2-铁规2017_ZKH_ZH 3-无
            cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取
            calc_fatigue:是否计算疲劳
            line_count: 疲劳加载线路数
            longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取
            impact_factor:强度冲击系数大于1时为自定义，否则按照规范自动选取
            fatigue_factor:疲劳系数
            bridge_kind:桥梁类型 0-无 1-简支 2-结合 3-涵洞 4-空腹式
            fill_thick:填土厚度 (规ZKH ZH钢筋/素混凝土、石砌桥跨结构以及涵洞所需参数)
            rise:拱高 (规ZKH ZH活载-空腹式拱桥所需参数)
            calc_length:计算跨度(铁规ZKH ZH活载-空腹式拱桥所需参数)或计算长度(铁规ZK ZC活载所需参数)
        Example:
            mdb.add_train_relative_factor(name="活载工况1",code_index=1,cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5],calc_length=50)
        Returns: 无
        """
        try:
            qt_model.AddTrainRelativeFactor(name=name, codeIndex=code_index, crossFactors=cross_factors, calculateFatigue=calc_fatigue,
                                            longitudeFactor=longitude_factor, fatigueLineCount=line_count, fatigueFactor=fatigue_factor,
                                            impactFactor=impact_factor, bridgeKind=bridge_kind, fillThick=fill_thick, rise=rise, lambDa=calc_length)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_metro_relative_factor(name: str, cross_factors: list[float] = None, longitude_factor: int = -1, impact_factor: int = -1):
        """
        添加移动荷载工况汽车折减
        Args:
             name:活载工况名
             cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取
             longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取
             impact_factor:强度冲击系数大于1时为自定义，否则按照规范自动选取
        Example:
            mdb.add_metro_relative_factor(name="活载工况1",cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5],
                longitude_factor=1,impact_factor=1)
        Returns: 无
        """
        try:
            qt_model.AddMetroRelativeFactor(name=name, crossFactors=cross_factors,
                                            longitudeFactor=longitude_factor,
                                            impactFactor=impact_factor)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_vehicle(name: str = ""):
        """
        删除车辆信息
        Args:
             name:车辆名称
        Example:
            mdb.remove_vehicle(name="车辆名称")
        Returns: 无
        """
        try:
            qt_model.RemoveVehicle(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_node_tandem(index: int = -1, name: str = ""):
        """
        按照 节点纵列编号/节点纵列名 删除节点纵列
        Args:
             index:节点纵列编号
             name:节点纵列名
        Example:
            mdb.remove_node_tandem(index=1)
            mdb.remove_node_tandem(name="节点纵列1")
        Returns: 无
        """
        try:
            if index != -1:
                qt_model.RemoveNodeTandem(id=index)
            elif name != "":
                qt_model.RemoveNodeTandem(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_influence_plane(index: int = -1, name: str = ""):
        """
        按照 影响面编号/影响面名称 删除影响面
        Args:
             index:影响面编号
             name:影响面名称
        Example:
            mdb.remove_influence_plane(index=1)
            mdb.remove_influence_plane(name="影响面1")
        Returns: 无
        """
        try:
            if index != -1:
                qt_model.RemoveInfluencePlane(id=index)
            elif name != "":
                qt_model.RemoveInfluencePlane(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_lane_line(name: str = "", index: int = -1):
        """
        按照 车道线编号/车道线名称 删除车道线
        Args:
             name:车道线名称
             index:车道线编号
        Example:
            mdb.remove_lane_line(index=1)
            mdb.remove_lane_line(name="车道线1")
        Returns: 无
        """
        try:
            if index != -1:
                qt_model.RemoveLaneLine(id=index)
            elif name != "":
                qt_model.RemoveLaneLine(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_live_load_case(name: str = ""):
        """
        删除移动荷载工况
        Args:
             name:移动荷载工况名
        Example:
            mdb.remove_live_load_case(name="活载工况1")
        Returns: 无
        """
        try:
            qt_model.RemoveLiveLoadCase(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 动力荷载操作
    @staticmethod
    def add_load_to_mass(name: str, factor: float = 1):
        """
        添加荷载转为质量
        Args:
            name: 荷载工况名称
            factor: 系数
        Example:
            mdb.add_load_to_mass(name="荷载工况",factor=1)
        Returns: 无
        """
        try:
            qt_model.AddLoadToMass(name=name, factor=factor)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_nodal_mass(node_id: (Union[int, List[int]]) = 1, mass_info: tuple[float, float, float, float] = None):
        """
        添加节点质量
        Args:
             node_id:节点编号，支持单个编号和编号列表
             mass_info:[m,rmX,rmY,rmZ]
        Example:
            mdb.add_nodal_mass(node_id=1,mass_info=(100,0,0,0))
        Returns: 无
        """
        try:
            if mass_info is None:
                raise Exception("操作错误，节点质量信息列表不能为空")
            qt_model.AddNodalMass(nodeId=node_id, massInfo=mass_info)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_nodal_mass(node_id: (Union[int, List[int]]) = -1):
        """
        删除节点质量
        Args:
             node_id:节点号，默认删除所有节点质量
        Example:
            mdb.remove_nodal_mass(node_id=1)
        Returns: 无
        """
        try:
            if node_id == -1:
                qt_model.RemoveAllNodalMass()
            else:
                qt_model.RemoveNodalMass(nodeId=node_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_load_to_mass(name: str):
        """
        删除荷载转为质量
        Args:
             name:荷载工况名
        Example:
            mdb.remove_load_to_mass(name="荷载工况")
        Returns: 无
        """
        try:
            qt_model.RemoveLoadToMass(name=name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_spectrum_function(name: str = "", factor: float = 1.0, kind: int = 0, function_info: list[tuple[float, float]] = None):
        """
        添加反应谱函数
        Args:
            name:反应谱函数名
            factor:反应谱调整系数
            kind:反应谱类型 0-无量纲 1-加速度 2-位移
            function_info:反应谱函数信息
        Example:
            mdb.add_spectrum_function(name="反应谱函数1",factor=1.0,function_info=[(0,0.02),(1,0.03)])
        Returns: 无
        """
        try:
            qt_model.AddResponseSpectrumFunction(name=name, factor=factor, kind=kind, functionInfo=function_info)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_spectrum_case(name: str = "", description: str = "", kind: int = 1, info_x: tuple[str, float] = None,
                          info_y: tuple[str, float] = None, info_z: tuple[str, float] = None):
        """
        添加反应谱工况
        Args:
             name:荷载工况名
             description:说明
             kind:组合方式 1-求模 2-求和
             info_x: 反应谱X向信息 (X方向函数名,系数)
             info_y: 反应谱Y向信息 (Y方向函数名,系数)
             info_z: 反应谱Z向信息 (Z方向函数名,系数)
        Example:
            mdb.add_spectrum_case(name="反应谱工况",info_x=("函数1",1.0))
        Returns: 无
        """
        try:
            if info_x is None and info_y is None and info_z is None:
                raise Exception("添加反应谱函数错误,无反应谱分项信息")
            qt_model.AddResponseSpectrumCase(name=name, description=description, kind=kind, infoX=info_x, info_y=info_y, info_z=info_z)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 钢束操作
    @staticmethod
    def add_tendon_group(name: str = "", index: int = -1):
        """
        按照名称添加钢束组，添加时可指定钢束组id
        Args:
            name: 钢束组名称
            index: 钢束组编号(非必须参数)，默认自动识别
        Example:
            mdb.add_tendon_group(name="钢束组1")
        Returns: 无
        """
        try:
            qt_model.AddTendonGroup(name=name, id=index)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_tendon_group(name: str = ""):
        """
        按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组
        Args:
             name:钢束组名称,默认自动识别 (可选参数)
        Example:
            mdb.remove_tendon_group(name="钢束组1")
        Returns: 无
        """
        try:
            if name != "":
                qt_model.RemoveTendonGroup(name=name)
            else:
                qt_model.RemoveAllStructureGroup()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_tendon_property(name: str = "", tendon_type: int = 0, material_id: int = 1, duct_type: int = 1,
                            steel_type: int = 1, steel_detail: list[float] = None, loos_detail: tuple[int, int, int] = None,
                            slip_info: tuple[float, float] = None):
        """
        添加钢束特性
        Args:
             name:钢束特性名
             tendon_type: 0-PRE 1-POST
             material_id: 钢材材料编号
             duct_type: 1-金属波纹管  2-塑料波纹管  3-铁皮管  4-钢管  5-抽芯成型
             steel_type: 1-钢绞线  2-螺纹钢筋
             steel_detail: 钢束详细信息
                _钢绞线[钢束面积,孔道直径,摩阻系数,偏差系数]_
                _螺纹钢筋[钢筋直径,钢束面积,孔道直径,摩阻系数,偏差系数,张拉方式(1-一次张拉 2-超张拉)]_
             loos_detail: 松弛信息[规范,张拉,松弛] (仅钢绞线需要,默认为[1,1,1])
                _规范:1-公规 2-铁规_
                _张拉方式:1-一次张拉 2-超张拉_
                _松弛类型：1-一般松弛 2-低松弛_
             slip_info: 滑移信息[始端距离,末端距离] 默认为[0.006, 0.006]
        Example:
            mdb.add_tendon_property(name="钢束1",tendon_type=0,material_id=1,duct_type=1,steel_type=1,
                                    steel_detail=[0.00014,0.10,0.25,0.0015],loos_detail=(1,1,1))
        Returns: 无
        """
        try:
            if steel_detail is None:
                raise Exception("操作错误，钢束特性信息不能为空")
            if loos_detail is None:
                loos_detail = (1, 1, 1)
            if slip_info is None:
                slip_info = (0.006, 0.006)
            qt_model.AddTendonProperty(name=name, tendonType=tendon_type, materialId=material_id,
                                       ductType=duct_type, steelType=steel_type, steelDetail=steel_detail,
                                       loosDetail=loos_detail, slipInfo=slip_info)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_tendon_3d(name: str, property_name: str = "", group_name: str = "默认钢束组",
                      num: int = 1, line_type: int = 1, position_type=1,
                      control_points: list[tuple[float, float, float, float]] = None,
                      point_insert: tuple[float, float, float] = None,
                      tendon_direction: tuple[float, float, float] = None,
                      rotation_angle: float = 0, track_group: str = "默认结构组", projection: bool = True):
        """
        添加三维钢束
        Args:
             name:钢束名称
             property_name:钢束特性名称
             group_name:默认钢束组
             num:根数
             line_type:1-导线点  2-折线点
             position_type: 定位方式 1-直线  2-轨迹线
             control_points: 控制点信息[(x1,y1,z1,r1),(x2,y2,z2,r2)....]
             point_insert: 定位方式
                _直线: 插入点坐标[x,y,z]_
                _轨迹线:  [插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id]_
             tendon_direction:直线钢束X方向向量  默认为[1,0,0] (轨迹线不用赋值)
                _x轴-[1,0,0] y轴-[0,1,0] z轴-[0,0,1]_
             rotation_angle:绕钢束旋转角度
             track_group:轨迹线结构组名  (直线时不用赋值)
             projection:直线钢束投影 (默认为true)
        Example:
            mdb.add_tendon_3d("BB1",property_name="22-15",num=2,position_type=1,
                    control_points=[(0,0,-1,0),(10,0,-1,0)],point_insert=(0,0,0))
            mdb.add_tendon_3d("BB1",property_name="22-15",num=2,position_type=2,
                    control_points=[(0,0,-1,0),(10,0,-1,0)],point_insert=(1,1,1),track_group="轨迹线结构组1")
        Returns: 无
        """
        try:
            if tendon_direction is None:
                tendon_direction = (1, 0, 0)
            if control_points is None:
                raise Exception("操作错误，钢束形状控制点不能为空")
            if point_insert is None or len(point_insert) != 3:
                raise Exception("操作错误，钢束插入点信息不能为空且长度必须为3")
            qt_model.AddTendon3D(name=name, propertyName=property_name, groupName=group_name, num=num, lineType=line_type,
                                 positionType=position_type, controlPoints=control_points,
                                 pointInsert=point_insert, tendonDirection=tendon_direction,
                                 rotationAngle=rotation_angle, trackGroup=track_group, isProject=projection)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_tendon_2d(name: str, property_name: str = "", group_name: str = "默认钢束组",
                      num: int = 1, line_type: int = 1, position_type: int = 1, symmetry: int = 0,
                      control_points: list[tuple[float, float, float]] = None,
                      control_points_lateral: list[tuple[float, float, float]] = None,
                      point_insert: tuple[float, float, float] = None,
                      tendon_direction: tuple[float, float, float] = None,
                      rotation_angle: float = 0, track_group: str = "默认结构组", projection: bool = True):
        """
        添加三维钢束
        Args:
             name:钢束名称
             property_name:钢束特性名称
             group_name:默认钢束组
             num:根数
             line_type:1-导线点  2-折线点
             position_type: 定位方式 1-直线  2-轨迹线
             symmetry: 对称点 0-左 1-右 2-无
             control_points: 控制点信息[(x1,z1,r1),(x2,z2,r2)....]
             control_points_lateral: 控制点横弯信息[(x1,y1,r1),(x2,y2,r2)....]，无横弯时不必输入
             point_insert: 定位方式
                _直线: 插入点坐标[x,y,z]_
                _轨迹线:  [插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id]_
             tendon_direction:直线钢束X方向向量  默认为[1,0,0] (轨迹线不用赋值)
                _x轴-[1,0,0] y轴-[0,1,0] z轴-[0,0,1]_
             rotation_angle:绕钢束旋转角度
             track_group:轨迹线结构组名  (直线时不用赋值)
             projection:直线钢束投影 (默认为true)
        Example:
            mdb.add_tendon_2d(name="BB1",property_name="22-15",num=2,position_type=1,
                    control_points=[(0,-1,0),(10,-1,0)],point_insert=(0,0,0))
            mdb.add_tendon_2d(name="BB1",property_name="22-15",num=2,position_type=2,
                    control_points=[(0,-1,0),(10,-1,0)],point_insert=(1,1,1),track_group="轨迹线结构组1")
        Returns: 无
        """
        try:
            if tendon_direction is None:
                tendon_direction = (1, 0, 0)
            if control_points is None:
                raise Exception("操作错误，钢束形状控制点不能为空")
            if point_insert is None or len(point_insert) != 3:
                raise Exception("操作错误，钢束插入点信息不能为空且长度必须为3")
            qt_model.AddTendon2D(name=name, propertyName=property_name, groupName=group_name, num=num, lineType=line_type,
                                 positionType=position_type, symmetry=symmetry, controlPoints=control_points,
                                 controlPointsLateral=control_points_lateral,
                                 pointInsert=point_insert, tendonDirection=tendon_direction,
                                 rotationAngle=rotation_angle, trackGroup=track_group, isProject=projection)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_tendon_element(ids: list[int] = None):
        """
        赋予钢束构件
        Args:
            ids: 钢束构件所在单元编号集合
        Example:
           mdb.update_tendon_element(ids=[1,2,3,4])
        Returns: 无
        """
        try:
            qt_model.UpdatePreStressElement(ids)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_tendon(name: str = "", index: int = -1):
        """
        按照名称或编号删除钢束,默认时删除所有钢束
        Args:
             name:钢束名称
             index:钢束编号
        Example:
            mdb.remove_tendon(name="钢束1")
            mdb.remove_tendon(index=1)
            mdb.remove_tendon()
        Returns: 无
        """
        try:
            if name != "":
                qt_model.RemoveTendon(name=name)
            elif index != -1:
                qt_model.RemoveTendon(id=index)
            else:
                qt_model.RemoveAllTendon()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_tendon_property(name: str = "", index: int = -1):
        """
        按照名称或编号删除钢束组,默认时删除所有钢束组
        Args:
             name:钢束组名称
             index:钢束组编号
        Example:
            mdb.remove_tendon_property(name="钢束特性1")
            mdb.remove_tendon_property(index=1)
            mdb.remove_tendon_property()
        Returns: 无
        """
        try:
            if name != "":
                qt_model.RemoveTendonProperty(name=name)
            elif index != -1:
                qt_model.RemoveTendonProperty(id=index)
            else:
                qt_model.RemoveAllTendonGroup()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 静力荷载操作
    @staticmethod
    def add_load_group(name: str = ""):
        """
        根据荷载组名称添加荷载组
        Args:
             name: 荷载组名称
        Example:
            mdb.add_load_group(name="荷载组1")
        Returns: 无
        """
        try:
            if name != "":
                qt_model.AddLoadGroup(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_load_group(name: str = ""):
        """
        根据荷载组名称删除荷载组,参数为默认时删除所有荷载组
        Args:
             name: 荷载组名称
        Example:
            mdb.remove_load_group(name="荷载组1")
        Returns: 无
        """
        try:
            if name != "":
                qt_model.RemoveLoadGroup(name=name)
            else:
                qt_model.RemoveAllLoadGroup()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_pre_stress(case_name: str = "", tendon_name: (Union[str, List[str]]) = "", tension_type: int = 2,
                       force: float = 1395000, group_name: str = "默认荷载组"):
        """
        添加预应力
        Args:
             case_name:荷载工况名
             tendon_name:钢束名,支持钢束名或钢束名列表
             tension_type:预应力类型
                _0-始端 1-末端 2-两端_
             force:预应力
             group_name:边界组
        Example:
            mdb.add_pre_stress(case_name="荷载工况名",tendon_name="钢束1",force=1390000)
        Returns: 无
        """
        try:
            qt_model.AddPreStress(caseName=case_name, tendonName=tendon_name, preType=tension_type, force=force, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_pre_stress(case_name: str = "", tendon_name: str = ""):
        """
        删除预应力
        Args:
             case_name:荷载工况
             tendon_name:钢束组
        Example:
            mdb.remove_pre_stress(case_name="工况1",tendon_name="钢束1")
        Returns: 无
        """
        try:
            qt_model.RemovePreStress(caseName=case_name, tendonName=tendon_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_nodal_force(node_id: (Union[int, List[int]]) = 1, case_name: str = "", load_info: list[float] = None,
                        group_name: str = "默认荷载组"):
        """
        添加节点荷载
        Args:
            node_id:节点编号
            case_name:荷载工况名
            load_info:荷载信息列表 [Fx,Fy,Fz,Mx,My,Mz]
            group_name:荷载组名
        Example:
            mdb.add_nodal_force(case_name="荷载工况1",node_id=1,load_info=[1,1,1,1,1,1],group_name="默认结构组")
        Returns: 无
        """
        try:
            if load_info is None or len(load_info) != 6:
                raise Exception("操作错误，节点荷载列表信息不能为空，且其长度必须为6")
            qt_model.AddNodalForce(caseName=case_name, nodeId=node_id, loadInfo=load_info, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_nodal_force(node_id: int = -1, case_name: str = ""):
        """
        删除节点荷载
        Args:
             case_name:荷载工况名
             node_id:节点编号
        Example:
            mdb.remove_nodal_force(case_name="荷载工况1",node_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveNodalForce(caseName=case_name, nodeId=node_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_node_displacement(node_id: (Union[int, List[int]]) = None, case_name: str = "",
                              load_info: tuple[float, float, float, float, float, float] = None,
                              group_name: str = "默认荷载组"):
        """
        添加节点位移
        Args:
            node_id:节点编号,支持整型或整数型列表
            case_name:荷载工况名
            load_info:节点位移列表 [Dx,Dy,Dz,Rx,Ry,Rz]
            group_name:荷载组名
        Example:
            mdb.add_node_displacement(case_name="荷载工况1",node_id=1,load_info=(1,0,0,0,0,0),group_name="默认荷载组")
            mdb.add_node_displacement(case_name="荷载工况1",node_id=[1,2,3],load_info=(1,0,0,0,0,0),group_name="默认荷载组")
        Returns: 无
        """
        try:
            if load_info is None or len(load_info) != 6:
                raise Exception("操作错误，节点位移列表信息不能为空，且其长度必须为6")
            qt_model.AddNodeDisplacement(caseName=case_name, nodeId=node_id, loadInfo=load_info, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_nodal_displacement(node_id: (Union[int, List[int]]) = -1, case_name: str = ""):
        """
        删除节点位移
        Args:
            node_id:节点编号,支持数或列表
            case_name:荷载工况名
        Example:
            mdb.remove_nodal_displacement(case_name="荷载工况1",node_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveNodalDisplacement(caseName=case_name, nodeId=node_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_beam_element_load(element_id: (Union[int, List[int]]) = 1, case_name: str = "", load_type: int = 1, coord_system: int = 3,
                              is_abs=False, list_x: (Union[float, List[float]]) = None, list_load: (Union[float, List[float]]) = None,
                              group_name="默认荷载组", load_bias: tuple[bool, int, int, float] = None,
                              projected: bool = False):
        """
        添加梁单元荷载
        Args:
            element_id:单元编号,支持数或列表
            case_name:荷载工况名
            load_type:荷载类型
               _ 1-集中力 2-集中弯矩 3-分布力 4-分布弯矩
            coord_system:坐标系
                _1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z_
            is_abs: 荷载位置输入方式，True-绝对值   False-相对值
            list_x:荷载位置信息 ,荷载距离单元I端的距离，可输入绝对距离或相对距离
            list_load:荷载数值信息
            group_name:荷载组名
            load_bias:偏心荷载 (是否偏心,0-中心 1-偏心,偏心坐标系-int,偏心距离)
            projected:荷载是否投影
        Example:
            mdb.add_beam_element_load(case_name="荷载工况1",element_id=1,load_type=1,list_x=[0.1,0.5,0.8],list_load=[100,100,100])
            mdb.add_beam_element_load(case_name="荷载工况1",element_id=1,load_type=3,list_x=[0.4,0.8],list_load=[100,200])
        Returns: 无
        """
        try:
            qt_model.AddBeamElementLoad(caseName=case_name, elementId=element_id, loadType=load_type, isAbs=is_abs,
                                        coordinateSystem=coord_system, listX=list_x, listLoad=list_load, groupName=group_name,
                                        biasInfo=load_bias, isProject=projected)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_beam_element_load(element_id: (Union[int, List[int]]) = 1, case_name: str = "", load_type: int = 1):
        """
        删除梁单元荷载
        Args:
            element_id:单元号支持数或列表
            case_name:荷载工况名
            load_type:荷载类型
                _1-集中力   2-集中弯矩  3-分布力   4-分布弯矩_
        Example:
            mdb.remove_beam_element_load(case_name="工况1",element_id=1,load_type=1)
        Returns: 无
        """
        try:
            qt_model.RemoveBeamElementLoad(caseName=case_name, elementId=element_id, loadType=load_type)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_initial_tension_load(element_id: (Union[int, List[int]]) = 1, case_name: str = "", group_name: str = "默认荷载组", tension: float = 0,
                                 tension_type: int = 1):
        """
        添加初始拉力
        Args:
             element_id:单元编号支持数或列表
             case_name:荷载工况名
             tension:初始拉力
             tension_type:张拉类型  0-增量 1-全量
             group_name:荷载组名
        Example:
            mdb.add_initial_tension_load(element_id=1,case_name="工况1",tension=100,tension_type=1)
        Returns: 无
        """
        try:
            qt_model.AddInitialTensionLoad(elementId=element_id, caseName=case_name, tension=tension, tensionType=tension_type, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_initial_tension_load(case_name: str, element_id: (Union[int, List[int]]) = 1):
        """
        删除初始拉力
        Args:
            element_id:单元编号支持数或列表
            case_name:荷载工况名
        Example:
            mdb.remove_initial_tension_load(case_name="工况1",element_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveInitialTensionLoad(elementId=element_id, caseName=case_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_cable_length_load(element_id: (Union[int, List[int]]) = 1, case_name: str = "", group_name: str = "默认荷载组", length: float = 0,
                              tension_type: int = 1):
        """
        添加索长张拉
        Args:
            element_id:单元编号支持数或列表
            case_name:荷载工况名
            length:长度
            tension_type:张拉类型  0-增量 1-全量
            group_name:荷载组名
        Example:
            mdb.add_cable_length_load(element_id=1,case_name="工况1",length=1,tension_type=1)
        Returns: 无
        """
        try:
            qt_model.AddCableLengthLoad(elementId=element_id, caseName=case_name, groupName=group_name, length=length, tensionType=tension_type)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_cable_length_load(case_name: str, element_id: (Union[int, List[int]])):
        """
        删除索长张拉
        Args:
            element_id:单元号支持数或列表
            case_name:荷载工况名
        Example:
            mdb.remove_cable_length_load(case_name="工况1",element_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveCableLengthLoad(elementId=element_id, caseName=case_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_plate_element_load(element_id: (Union[int, List[int]]) = 1, case_name: str = "",
                               load_type: int = 1, load_place: int = 1, coord_system: int = 3,
                               group_name: str = "默认荷载组", list_load: (Union[float, List[float]]) = None,
                               list_xy: tuple[float, float] = None):
        """
        添加版单元荷载
        Args:
             element_id:单元编号支持数或列表
             case_name:荷载工况名
             load_type:荷载类型
                _1-集中力  2-集中弯矩  3-分布力  4-分布弯矩_
             load_place:荷载位置
                _0-面IJKL 1-边IJ  2-边JK  3-边KL  4-边LI  (仅分布荷载需要)_
             coord_system:坐标系  (默认3)
                _1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z_
             group_name:荷载组名
             list_load:荷载列表
             list_xy:荷载位置信息 [IJ方向绝对距离x,IL方向绝对距离y]  (仅集中荷载需要)
        Example:
            mdb.add_plate_element_load(element_id=1,case_name="工况1",load_type=1,group_name="默认荷载组",list_load=[1000],list_xy=(0.2,0.5))
        Returns: 无
        """
        try:
            if load_type == 2 or load_type == 4:
                raise Exception("操作错误，板单元暂不支持弯矩荷载")
            if load_type == 1:
                qt_model.AddPlateElementLoad(elementId=element_id, caseName=case_name, loadType=load_type,
                                             coordSystem=coord_system, groupName=group_name, loads=list_load)
            elif load_type == 3:
                if load_place == 0:
                    load_type = load_type + 2
                qt_model.AddPlateElementLoad(elementId=element_id, caseName=case_name, loadType=load_type, loadPosition=load_place,
                                             distanceList=list_xy, coordSystem=coord_system, groupName=group_name, loads=list_load)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_plate_element_load(case_name: str, element_id: (Union[int, List[int]]), load_type: int):
        """
        删除指定荷载工况下指定单元的板单元荷载
        Args:
            element_id:单元编号，支持数或列表
            case_name:荷载工况名
            load_type: 板单元类型 1集中力   2-集中弯矩  3-分布线力  4-分布线弯矩  5-分布面力  6-分布面弯矩
        Example:
            mdb.remove_plate_element_load(case_name="工况1",element_id=1,load_type=1)
        Returns: 无
        """
        try:
            qt_model.RemovePlateElementLoad(elementId=element_id, caseName=case_name, loadType=load_type)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_deviation_parameter(name: str = "", element_type: int = 1, parameters: list[float] = None):
        """
        添加制造误差
        Args:
            name:名称
            element_type:单元类型  1-梁单元  2-板单元
            parameters:参数列表
                _梁杆单元:[轴向,I端X向转角,I端Y向转角,I端Z向转角,J端X向转角,J端Y向转角,J端Z向转角]_
                _板单元:[X向位移,Y向位移,Z向位移,X向转角,Y向转角]_
        Example:
            mdb.add_deviation_parameter(name="梁端制造误差",element_type=1,parameters=[1,0,0,0,0,0,0])
            mdb.add_deviation_parameter(name="板端制造误差",element_type=1,parameters=[1,0,0,0,0])
        Returns: 无
        """
        try:
            if parameters is None:
                raise Exception("操作错误，制造误差信息不能为空")
            if len(parameters) != 5 or len(parameters) != 7:
                raise Exception("操作错误，误差列表有误")
            qt_model.AddDeviationParameter(name=name, elementType=element_type, parameterInfo=parameters)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_deviation_parameter(name: str, para_type: int = 1):
        """
        删除指定制造偏差参数
        Args:
            name:制造偏差参数名
            para_type:制造偏差类型 1-梁单元  2-板单元
        Example:
            mdb.remove_deviation_parameter(name="参数1",para_type=1)
        Returns: 无
        """
        try:
            qt_model.RemoveDeviationParameter(name=name, paraType=para_type)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_deviation_load(element_id: (Union[int, List[int]]) = 1, case_name: str = "",
                           parameters: (Union[str, List[str]]) = None, group_name: str = "默认荷载组"):
        """
        添加制造误差荷载
        Args:
            element_id:单元编号，支持数或列表
            case_name:荷载工况名
            parameters:参数名列表
                _梁杆单元时:制造误差参数名称_
                _板单元时: [I端误差名,J端误差名,K端误差名,L端误差名]_
            group_name:荷载组名
        Example:
            mdb.add_deviation_load(element_id=1,case_name="工况1",parameters="梁端误差")
            mdb.add_deviation_load(element_id=2,case_name="工况1",parameters=["板端误差1","板端误差2","板端误差3","板端误差4"])
        Returns: 无
        """
        try:
            if parameters is None:
                raise Exception("操作错误，制造误差名称信息不能为空")
            qt_model.AddDeviationLoad(elementId=element_id, caseName=case_name, parameterName=parameters, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_deviation_load(case_name: str, element_id: (Union[int, List[int]])):
        """
        删除指定制造偏差荷载
        Args:
            case_name:荷载工况名
            element_id:单元编号，支持数或列表
        Example:
            mdb.remove_deviation_load(case_name="工况1",element_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveDeviationLoad(caseName=case_name, elementId=element_id)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_element_temperature(element_id: (Union[int, List[int]]) = 1, case_name: str = "", temperature: float = 1, group_name: str = "默认荷载组"):
        """
        添加单元温度
        Args:
            element_id:单元编号，支持数或列表
            case_name:荷载工况名
            temperature:最终温度
            group_name:荷载组名
        Example:
            mdb.add_element_temperature(element_id=1,case_name="自重",temperature=1,group_name="默认荷载组")
        Returns: 无
        """
        try:
            qt_model.AddElementTemperature(elementId=element_id, caseName=case_name, temperature=temperature, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_element_temperature(case_name: str, element_id: (Union[int, List[int]]), group_name: str = "默认荷载组"):
        """
        删除指定单元温度
        Args:
            case_name:荷载工况名
            element_id:单元编号，支持数或列表
            group_name:指定荷载组,后续升级开放指定荷载组删除功能
        Example:
            mdb.remove_element_temperature(case_name="荷载工况1",element_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveElementTemperature(caseName=case_name, elementId=element_id, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_gradient_temperature(element_id: (Union[int, List[int]]) = 1, case_name: str = "", temperature: float = 1, section_oriental: int = 1,
                                 element_type: int = 1, group_name: str = "默认荷载组"):
        """
        添加梯度温度
            element_id:单元编号，支持数或列表
            case_name:荷载工况名
            temperature:温差
            section_oriental:截面方向,默认截面Y向 (仅梁单元需要, 0-截面Y向  1-截面Z向)
            element_type:单元类型,默认为梁单元 (1-梁单元  2-板单元)
            group_name:荷载组名
        Example:
            mdb.add_gradient_temperature(element_id=1,case_name="荷载工况1",group_name="荷载组名1",temperature=10)
            mdb.add_gradient_temperature(element_id=2,case_name="荷载工况2",group_name="荷载组名2",temperature=10,element_type=2)
        Returns: 无
        """
        try:
            qt_model.AddGradientTemperature(elementId=element_id, caseName=case_name, temperature=temperature,
                                            sectionOriental=section_oriental, elementType=element_type, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_gradient_temperature(case_name: str, element_id: (Union[int, List[int]]), group_name: str = "默认荷载组"):
        """
        删除梁或板单元梯度温度
        Args:
            case_name:荷载工况名
            element_id:单元编号，支持数或列表
            group_name:指定荷载组,后续升级开放指定荷载组删除功能
        Example:
            mdb.remove_gradient_temperature(case_name="工况1",element_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveGradientTemperature(caseName=case_name, elementId=element_id, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_beam_section_temperature(element_id: (Union[int, List[int]]) = 1, case_name: str = "", code_index: int = 1,
                                     paving_thick: float = 0, temperature_type: int = 1,
                                     paving_type: int = 1, zone_index: str = 1, group_name: str = "默认荷载组",
                                     modify: bool = False, temp_list: tuple[float, float] = None):
        """
        添加梁截面温度
        Args:
            element_id:单元编号，支持整数或整数型列表
            case_name:荷载工况名
            code_index:规范编号  (1-公路规范2015  2-AASHTO2017)
            paving_thick:铺设厚度(m)
            temperature_type:温度类型,默认升温  (1-升温 2-降温)
            paving_type:铺设类型，默认为1 (1-沥青混凝土(默认)  2-水泥混凝土)
            zone_index: 区域号 (仅规范二需要)
            group_name:荷载组名
            modify:是否修改规范温度
            temp_list:温度列表[T1,T2,T3,t]or[T1,T2]  (仅修改时需要)
        Example:
            mdb.add_beam_section_temperature(element_id=1,case_name="工况1",paving_thick=0.1)
        Returns: 无
        """
        try:
            qt_model.AddBeamSectionTemperature(elementId=element_id, caseName=case_name, pavingThickness=paving_thick,
                                               temperatureType=temperature_type, codeIndex=code_index, zoneIndex=zone_index,
                                               pavingType=paving_type, groupName=group_name, isModify=modify, modifyInfo=temp_list)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_beam_section_temperature(case_name: str, element_id: (Union[int, List[int]]), group_name: str = "默认荷载组"):
        """
        删除指定梁或板单元梁截面温度
        Args:
            case_name:荷载工况名
            element_id:单元编号，支持数或列表
            group_name:指定荷载组,后续升级开放指定荷载组删除功能
        Example:
            mdb.remove_beam_section_temperature(case_name="工况1",element_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveBeamSectionTemperature(caseName=case_name, elementId=element_id, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_index_temperature(element_id: (Union[int, List[int]]) = 1, case_name: str = "", temperature: float = 0, index: float = 1,
                              group_name: str = "默认荷载组"):
        """
        添加指数温度
        Args:
            element_id:单元编号，支持数或列表
            case_name:荷载工况名
            temperature:温差
            index:指数
            group_name:荷载组名
        Example:
            mdb.add_index_temperature(element_id=1,case_name="工况1",temperature=20,index=2)
        Returns: 无
        """
        try:
            qt_model.AddIndexTemperature(elementId=element_id, caseName=case_name, temperature=temperature, index=index, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_index_temperature(case_name: str, element_id: (Union[int, List[int]]) = 1, group_name: str = "默认荷载组"):
        """
        删除梁单元指数温度
        Args:
            case_name:荷载工况名
            element_id:单元编号，支持数或列表
            group_name:指定荷载组,后续升级开放指定荷载组删除功能
        Example:
            mdb.remove_index_temperature(case_name="工况1",element_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveIndexTemperature(caseName=case_name, elementId=element_id, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_top_plate_temperature(element_id: (Union[int, List[int]]) = 1, case_name: str = "", temperature: float = 0, group_name: str = "默认荷载组"):
        """
        添加顶板温度
        Args:
             element_id:单元编号
             case_name:荷载
             temperature:温差，最终温度于初始温度之差
             group_name:荷载组名
        Example:
            mdb.add_top_plate_temperature(element_id=1,case_name="工况1",temperature=40,group_name="默认荷载组")
        Returns: 无
        """
        try:
            qt_model.AddTopPlateTemperature(elementId=element_id, caseName=case_name, temperature=temperature, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_top_plate_temperature(case_name: str, element_id: (Union[int, List[int]]) = 1, group_name: str = "默认荷载组"):
        """
        删除梁单元顶板温度
        Args:
            case_name:荷载工况名
            element_id:单元编号，支持数或列表
            group_name:指定荷载组,后续升级开放指定荷载组删除功能
        Example:
            mdb.remove_top_plate_temperature(case_name="荷载工况1",element_id=1)
        Returns: 无
        """
        try:
            qt_model.RemoveTopPlateTemperature(caseName=case_name, elementId=element_id, groupName=group_name)
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 沉降操作
    @staticmethod
    def add_sink_group(name: str = "", sink: float = 0.1, node_ids: (Union[int, List[int]]) = None):
        """
        添加沉降组
        Args:
             name: 沉降组名
             sink: 沉降值
             node_ids: 节点编号，支持数或列表
        Example:
            mdb.add_sink_group(name="沉降1",sink=0.1,node_ids=[1,2,3])
        Returns: 无
        """
        try:
            if node_ids is None:
                raise Exception("操作错误，沉降定义中节点信息不能为空")
            qt_model.AddSinkGroup(name=name, sinkValue=sink, nodeIds=node_ids)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_sink_group(name: str = ""):
        """
        按照名称删除沉降组
        Args:
             name:沉降组名,默认删除所有沉降组
        Example:
            mdb.remove_sink_group()
            mdb.remove_sink_group(name="沉降1")
        Returns: 无
        """
        try:
            if name == "":
                qt_model.RemoveAllSinkGroup()
            else:
                qt_model.RemoveSinkGroup(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_sink_case(name: str, sink_groups: (Union[str, List[str]]) = None):
        """
        添加沉降工况
        Args:
            name:荷载工况名
            sink_groups:沉降组名，支持字符串或列表
        Example:
            mdb.add_sink_case(name="沉降工况1",sink_groups=["沉降1","沉降2"])
        Returns: 无
        """
        try:
            if sink_groups is None:
                raise Exception("操作错误，沉降工况定义中沉降组信息不能为空")
            qt_model.AddSinkCase(name=name, sinkGroups=sink_groups)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_sink_case(name=""):
        """
        按照名称删除沉降工况,不输入名称时默认删除所有沉降工况
        Args:
            name:沉降工况名
        Example:
            mdb.remove_sink_case()
            mdb.remove_sink_case(name="沉降1")
        Returns: 无
        """
        try:
            if name == "":
                qt_model.RemoveAllSinkCase()
            else:
                qt_model.RemoveSinkCase()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_concurrent_reaction(names: (Union[str, List[str]])):
        """
        添加并发反力组
        Args:
             names: 结构组名称集合
        Example:
            mdb.add_concurrent_reaction(names=["默认结构组"])
        Returns: 无
        """
        try:
            if names is None:
                raise Exception("操作错误，添加并发反力组时结构组名称不能为空")
            qt_model.AddConcurrentReaction(names=names)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_concurrent_reaction():
        """
        删除所有并发反力组
        Args:无
        Example:
            mdb.remove_concurrent_reaction()
        Returns: 无
        """
        try:
            qt_model.RemoveConcurrentRection()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_concurrent_force(names: (Union[str, List[str]])):
        """
        创建并发内力组
        Args:
            names: 结构组名称集合
        Example:
            mdb.add_concurrent_force(names=["默认结构组"])
        Returns: 无
        """
        try:
            qt_model.AddConcurrentForce(names=names)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_concurrent_force():
        """
        删除所有并发内力组
        Args: 无
        Example:
            mdb.remove_concurrent_force()
        Returns: 无
        """
        try:
            qt_model.RemoveConcurrentForce()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_load_case(name: str = "", case_type: str = "施工阶段荷载"):
        """
        添加荷载工况
        Args:
            name:沉降名
            case_type:荷载工况类型
            -"施工阶段荷载", "恒载", "活载", "制动力", "风荷载","体系温度荷载","梯度温度荷载",
            -"长轨伸缩挠曲力荷载", "脱轨荷载", "船舶撞击荷载","汽车撞击荷载","长轨断轨力荷载", "用户定义荷载"
        Example:
            mdb.add_load_case(name="工况1",case_type="施工阶段荷载")
        Returns: 无
        """
        try:
            qt_model.AddLoadCase(name=name, loadCaseType=case_type)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_load_case(index: int = -1, name: str = ""):
        """
        删除荷载工况,参数均为默认时删除全部荷载工况
        Args:
            index:荷载编号
            name:荷载名
        Example:
            mdb.remove_load_case(index=1)
            mdb.remove_load_case(name="工况1")
            mdb.remove_load_case()
        Returns: 无
        """
        try:
            if name != "":
                qt_model.DeleteLoadCase(name=name)
            elif index != -1:
                qt_model.DeleteLoadCase(id=index)
            else:
                qt_model.DeleteAllLoadCase()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 施工阶段操作
    @staticmethod
    def add_construction_stage(name: str = "", duration: int = 0,
                               active_structures: list[tuple[str, int, int, int]] = None,
                               delete_structures: list[str] = None,
                               active_boundaries: list[tuple[str, int]] = None,
                               delete_boundaries: list[str] = None,
                               active_loads: list[tuple[str, int]] = None,
                               delete_loads: list[tuple[str, int]] = None,
                               temp_loads: list[str] = None, index=-1):
        """
        添加施工阶段信息
        Args:
           name:施工阶段信息
           duration:时长
           active_structures:激活结构组信息 [(结构组名,龄期,安装方法,计自重施工阶段id),...]
                               _计自重施工阶段id: 0-不计自重,1-本阶段 n-第n阶段)_
                               _安装方法：1-变形法 2-无应力法 3-接线法 4-切线法
           delete_structures:钝化结构组信息 [结构组1，结构组2,...]
           active_boundaries:激活边界组信息 [(边界组1，位置),...]
                               _位置:  0-变形前 1-变形后_
           delete_boundaries:钝化边界组信息 [边界组1，边界组2,...]
           active_loads:激活荷载组信息 [(荷载组1,时间),...]
                               _时间: 0-开始 1-结束_
           delete_loads:钝化荷载组信息 [(荷载组1,时间),...]
                               _时间: 0-开始 1-结束_
           temp_loads:临时荷载信息 [荷载组1，荷载组2,..]
           index:施工阶段插入位置,从0开始,默认添加到最后
        Example:
           mdb.add_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
                active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
        Returns: 无
        """
        try:
            qt_model.AddConstructionStage(name=name, duration=duration, activeStructures=active_structures, inActiveStructures=delete_structures,
                                          activeBoundaries=active_boundaries, inActiveBoundaries=delete_boundaries, activeLoads=active_loads,
                                          inActiveLoads=delete_loads, tempLoads=temp_loads, id=index)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_construction_stage(name: str = "", duration: int = 0,
                                  active_structures: list[tuple[str, int, int, int]] = None,
                                  delete_structures: list[str] = None,
                                  active_boundaries: list[tuple[str, int]] = None,
                                  delete_boundaries: list[str] = None,
                                  active_loads: list[tuple[str, int]] = None,
                                  delete_loads: list[tuple[str, int]] = None,
                                  temp_loads: list[str] = None):
        """
        添加施工阶段信息
        Args:
           name:施工阶段信息
           duration:时长
           active_structures:激活结构组信息 [(结构组名,龄期,安装方法,计自重施工阶段id),...]
                               _计自重施工阶段id: 0-不计自重,1-本阶段 n-第n阶段)_
                               _安装方法：1-变形法 2-接线法 3-无应力法_
           delete_structures:钝化结构组信息 [结构组1，结构组2,...]
           active_boundaries:激活边界组信息 [(边界组1，位置),...]
                               _位置:  0-变形前 1-变形后_
           delete_boundaries:钝化边界组信息 [边界组1，结构组2,...]
           active_loads:激活荷载组信息 [(荷载组1,时间),...]
                               _时间: 0-开始 1-结束_
           delete_loads:钝化荷载组信息 [(荷载组1,时间),...]
                               _时间: 0-开始 1-结束_
           temp_loads:临时荷载信息 [荷载组1，荷载组2,..]
        Example:
           mdb.update_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
               active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
        Returns: 无
        """
        try:
            qt_model.UpdateConstructionStage(name=name, duration=duration, activeStructures=active_structures, inActiveStructures=delete_structures,
                                             activeBoundaries=active_boundaries, inActiveBoundaries=delete_boundaries, activeLoads=active_loads,
                                             inActiveLoads=delete_loads, tempLoads=temp_loads)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_weight_stage(stage_name: str = "", structure_group_name: str = "", weight_stage_id: int = 1):
        """
        添加施工阶段信息
        Args:
           stage_name:施工阶段信息
           structure_group_name:结构组名
           weight_stage_id: 计自重阶段号 (0-不计自重,1-本阶段 n-第n阶段)
        Example:
           mdb.update_weight_stage(stage_name="施工阶段1",structure_group_name="默认结构组",weight_stage_id=1)
        Returns: 无
        """
        try:
            qt_model.UpdateWeightStage(stageName=stage_name, structureGroupName=structure_group_name, weightStageId=weight_stage_id)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_construction_stage(name: str = ""):
        """
        按照施工阶段名删除施工阶段,默认删除所有施工阶段
        Args:
            name:所删除施工阶段名称
        Example:
            mdb.remove_construction_stage(name="施工阶段1")
        Returns: 无
        """
        try:
            if name == "":
                qt_model.RemoveAllConstructionStage()
            else:
                qt_model.RemoveConstructionStage(name=name)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    # endregion

    # region 荷载组合操作
    @staticmethod
    def add_load_combine(name: str = "", combine_type: int = 1, describe: str = "", combine_info: list[tuple[str, str, float]] = None):
        """
        添加荷载组合
        Args:
            name:荷载组合名
            combine_type:荷载组合类型 1-叠加  2-判别  3-包络
            describe:描述
            combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下
                _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合_
                _"MV"-移动荷载工况  "SM"-沉降荷载工况_ "RS"-反应谱工况_
        Example:
            mdb.add_load_combine(name="荷载组合1",combine_type=1,describe="无",combine_info=[("CS","合计值",1),("CS","恒载",1)])
        Returns: 无
        """
        try:
            if combine_info is None:
                combine_info = []
            qt_model.AddLoadCombine(name=name, loadCombineType=combine_type, describe=describe, caseAndFactor=combine_info)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_load_combine(name: str = "", combine_type: int = 1, describe: str = "", combine_info: list[tuple[str, str, float]] = None):
        """
        更新荷载组合
        Args:
            name:荷载组合名
            combine_type:荷载组合类型 (1-叠加  2-判别  3-包络)
            describe:描述
            combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下
                _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合_
                _"MV"-移动荷载工况  "SM"-沉降荷载工况_
        Example:
            mdb.update_load_combine(name="荷载组合1",combine_type=1,describe="无",combine_info=[("CS","合计值",1),("CS","恒载",1)])
        Returns: 无
        """
        try:
            if combine_info is None:
                combine_info = []
            qt_model.UpdateLoadCombine(name=name, loadCombineType=combine_type, describe=describe, caseAndFactor=combine_info)
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_load_combine(name: str = ""):
        """
        删除荷载组合
        Args:
             name:指定删除荷载组合名，默认时则删除所有荷载组合
        Example:
            mdb.remove_load_combine(name="荷载组合1")
        Returns: 无
        """
        try:
            if name != "":
                qt_model.DeleteLoadCombine(name=name)
            else:
                qt_model.DeleteAllLoadCombine()
            qt_model.UpdateModel()
        except Exception as ex:
            raise Exception(ex)

    # endregion
