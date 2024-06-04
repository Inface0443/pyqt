from __main__ import qt_model


class Mdb:
    """
    建模与模型修改计算，所有函数均无返回值
    """

    # region 视图控制
    @staticmethod
    def remove_display():
        """
        删除当前所有显示，包括边界荷载钢束等全部显示
        Args: 无
        example:
           mdb.remove_display()
        Returns: 无
        """
        qt_model.DisplayReset()

    @staticmethod
    def save_png(file_path: str):
        """
        保存当前模型窗口图形信息
        Args:
            file_path: 文件全路径
        example:
           mdb.save_png(r"D:\\QT\\aa.png")
        Returns: 无
        """
        qt_model.SavePng(file_path)

    @staticmethod
    def set_render(flag: bool = True):
        """
        消隐设置开关
        Args:
            flag: 默认设置打开消隐
        example:
           mdb.set_render(True)
        Returns: 无
        """
        qt_model.DisplayReset(flag)

    @staticmethod
    def change_construct_stage(stage):
        """
        消隐设置开关
        Args:
            stage: 施工阶段名称或施工阶段号  0-基本
        example:
           mdb.change_construct_stage(0)
           mdb.change_construct_stage("基本")
        Returns: 无
        """
        qt_model.ChangeConstructStage(stage)
    # endregion

    # region 项目管理

    @staticmethod
    def update_bim():
        """
        刷新Bim模型信息
        Args: 无
        example:
           mdb.update_bim()
        Returns: 无
        """
        qt_model.PostLoggerRequest()

    @staticmethod
    def update_model():
        """
        刷新模型信息
        Args: 无
        example:
            mdb.update_model()
        Returns: 无
        """
        qt_model.UpdateModel()

    @staticmethod
    def update_app_stage(num: int = 1):
        """
        切换模型前后处理状态
        Args:
            num: 1-前处理  2-后处理
        example:
            mdb.update_app_stage(1)
            mdb.update_app_stage(2)
        Returns: 无
        """

    @staticmethod
    def do_solve():
        """
        运行分析
        Args: 无
        example:
            mdb.do_solve()
        Returns: 无
        """
        qt_model.DoSolve()

    @staticmethod
    def initial():
        """
        初始化模型,新建模型
        Args: 无
        example:
            mdb.initial()
        Returns: 无
        """
        qt_model.Initial()

    @staticmethod
    def open_file(file_path: str):
        """
        打开bfmd文件
        Args:
            file_path: 文件全路径
        example:
            mdb.open_file("a.bfmd")
        Returns: 无
        """
        if not file_path.endswith(".bfmd"):
            raise Exception("操作错误，仅支持bfmd文件")
        qt_model.OpenFile(file_path)

    @staticmethod
    def close_project():
        """
        关闭项目
        Args: 无
        example:
            mdb.close_project()
        Returns: 无
        """
        qt_model.CloseFile()

    @staticmethod
    def save_file(file_path: str):
        """
        保存bfmd文件
        Args:
            file_path: 文件全路径
        example:
            mdb.save_file("a.bfmd")
        Returns: 无
        """
        qt_model.SaveFile(file_path)

    @staticmethod
    def import_command(command: str, command_type: int = 1):
        """
        导入命令
        Args:
            command:命令字符
            command_type:命令类型 1-桥通命令 目前仅支持桥通命令
        example:
            mdb.import_command("*SECTION")
        Returns: 无
        """
        qt_model.ImportQtCommand(command)

    @staticmethod
    def import_file(file_path: str):
        """
        导入文件
        Args:
            file_path:导入文件(.mct/.qdat/.dxf/.3dx)
        example:
            mdb.import_file("a.mct")
        Returns: 无
        """
        qt_model.ImportFile(file_path)

    @staticmethod
    def export_file(file_path: str):
        """
        导入命令
        Args:
            file_path:导出文件全路径，支持格式(.mct/.qdat/.PGF/.3dx)
        example:
            mdb.export_file("a.mct")
        Returns: 无
        """
        qt_model.ExportFile(file_path)

    # endregion

    # region 节点单元操作
    @staticmethod
    def add_nodes(node_list):
        """
        添加多个节点，可以选择指定节点编号
        Args:
             node_list:节点坐标信息 [[x1,y1,z1],...]或 [[id1,x1,y1,z1]...]
        example:
            mdb.add_nodes([[1,2,3],[4,5,6]])
            mdb.add_nodes([[1,1,2,3],[2,4,5,6]])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddNodes(dataList=node_list)

    @staticmethod
    def add_node(x: float = 1, y: float = 1, z: float = 1, index: int = -1):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        Args:
             x: 节点坐标x
             y: 节点坐标y
             z: 节点坐标z
             index: 节点编号，默认自动识别编号 (可选参数)
        example:
            mdb.add_node(1,2,3)
            mdb.add_node(x= 1,y = 2,z = 4,index = 2)
        Returns: 无
        """
        if index != -1:
            qt_model.AddNode(id=index, x=x, y=y, z=z)
        else:
            qt_model.AddNode(x=x, y=y, z=z)

    @staticmethod
    def update_node_id(node_id: int, new_id: int):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        Args:
             node_id: 节点编号
             new_id: 新节点编号
        example:
            mdb.update_node_id(1,2)
        Returns: 无
        """
        qt_model.UpdateNodeId(nodeId=node_id, newId=new_id)

    @staticmethod
    def merge_nodes(ids: list[int] = None, tolerance: float = 1e-4):
        """
        根据坐标信息和节点编号添加节点，默认自动识别编号
        Args:
             ids: 合并节点集合  默认全部节点
             tolerance: 合并容许误差
        example:
            mdb.merge_nodes()
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if ids is None:
            qt_model.MergeNode(tolerance)
        else:
            qt_model.MergeNodeByIds(ids, tolerance)

    @staticmethod
    def remove_node(ids=None):
        """
        删除指定节点,不输入参数时默认删除所有节点
        Args:
            ids:节点编号
        example:
            mdb.remove_node()
            mdb.remove_node(ids=1)
            mdb.remove_node(ids=[1,2,3])
        Returns: 无
        """
        if ids is None:
            qt_model.RemoveAllNodes()
        elif type(ids) == int:
            qt_model.RemoveNode(id=ids)
        else:
            qt_model.RemoveNodes(ids=ids)

    @staticmethod
    def renumber_node():
        """
        节点编号重拍
        Args: 无
        example:
            mdb.renumber_node()
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.RenumberNodeId()

    @staticmethod
    def move_node(node_id: int, offset_x: float = 0, offset_y: float = 0, offset_z: float = 0):
        """
        移动节点坐标
        Args:
            node_id：节点号
            offset_x:X轴偏移量
            offset_y:Y轴偏移量
            offset_z:Z轴偏移量
        example:
            mdb.move_node(1,1.5,1.5,1.5)
        Returns: 无
        """
        qt_model.MoveNode(node_id, offsets=[offset_x, offset_y, offset_z])

    @staticmethod
    def add_structure_group(name: str = "", index: int = -1):
        """
        添加结构组
        Args:
            name: 结构组名
            index: 结构组编号(非必须参数)，默认自动识别当前编号
        example:
            mdb.add_structure_group(name="新建结构组1")
            mdb.add_structure_group(name="新建结构组2",index=2)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddStructureGroup(name=name, id=index)

    @staticmethod
    def remove_structure_group(name: str = "", index: int = -1):
        """
        可根据结构与组名或结构组编号删除结构组，当组名和组编号均为默认则删除所有结构组
        Args:
            name:结构组名称
            index:结构组编号
        example:
            mdb.remove_structure_group(name="新建结构组1")
            mdb.remove_structure_group(index = 2)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if index != -1:
            qt_model.RemoveStructureGroup(id=index)
        elif name != "":
            qt_model.RemoveStructureGroup(name=name)
        else:
            qt_model.RemoveAllStructureGroup()

    @staticmethod
    def add_structure_to_group(name: str = "", node_ids: list[int] = None, element_ids: list[int] = None):
        """
        为结构组添加节点和/或单元
        Args:
            name: 结构组名
            node_ids: 节点编号列表(可选参数)
            element_ids: 单元编号列表(可选参数)
        example:
            mdb.add_structure_to_group(name="现有结构组1",node_ids=[1,2,3,4],element_ids=[1,2])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if node_ids is None:
            node_ids = []
        if element_ids is None:
            element_ids = []
        qt_model.AddStructureToGroup(name=name, nodeIds=node_ids, elementIds=element_ids)

    @staticmethod
    def remove_structure_in_group(name: str = "", node_ids: list[int] = None, element_ids=None):
        """
        为结构组删除节点和/或单元
        Args:
            name: 结构组名
            node_ids: 节点编号列表(可选参数)
            element_ids: 单元编号列表(可选参数)
        example:
            mdb.add_structure_to_group(name="现有结构组1",node_ids=[1,2,3,4],element_ids=[1,2])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if node_ids is None:
            node_ids = []
        if element_ids is None:
            element_ids = []
        qt_model.RemoveStructureOnGroup(name=name, nodeIds=node_ids, elementIds=element_ids)

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
        example:
            mdb.add_element(index=1,ele_type=1,node_ids=[1,2],beta_angle=1,mat_id=1,sec_id=1)
        Returns: 无
        """
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

    @staticmethod
    def remove_element(index: int = None):
        """
        删除指定编号的单元
        Args:
            index: 单元编号,默认时删除所有单元
        example:
            mdb.remove_element()
            mdb.remove_element(index=1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if index is None:
            qt_model.RemoveAllElements()
        else:
            qt_model.RemoveElement(index=index)

    # endregion

    # region 材料操作
    @staticmethod
    def add_material(index: int = -1, name: str = "", mat_type: str = "混凝土", standard: str = "公路18规范", database: str = "C50",
                     construct_factor: float = 1, modified: bool = False, data_info: list[float] = None, creep_id: int = -1, f_cuk: float = 0):
        """
        添加材料
        Args:
            index:材料编号,默认自动识别 (可选参数)
            name:材料名称
            mat_type: 材料类型
            standard:规范名称
            database:数据库
            construct_factor:构造系数
            modified:是否修改默认材料参数,默认不修改 (可选参数)
            data_info:材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (可选参数)
            creep_id:徐变材料id (可选参数)
            f_cuk: 立方体抗压强度标准值 (可选参数)
        example:
            mdb.add_material(index=1,name="混凝土材料1",mat_type="混凝土",standard="公路18规范",database="C50")
            mdb.add_material(index=1,name="自定义材料1",mat_type="自定义",data_info=[3.5e10,2.5e4,0.2,1.5e-5])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        list_material = ["混凝土", "钢材", "预应力", "钢丝", "钢筋", "自定义"]
        if mat_type not in list_material:
            raise Exception(f"操作错误,material_type不在指定列表:{list_material}中")
        if mat_type == "自定义":
            modified = True
        if modified and len(data_info) != 4:
            raise Exception("操作错误,modify_info数据无效!")
        if not modified:
            qt_model.AddMaterial(id=index, name=name, materialType=mat_type, standardName=standard,
                                 database=database, constructFactor=construct_factor, isModified=modified,
                                 timeParameterId=creep_id, fcuk=f_cuk)
        else:
            qt_model.AddMaterial(id=index, name=name, materialType=mat_type, standardName=standard,
                                 database=database, constructFactor=construct_factor, isModified=modified,
                                 elasticModulus=data_info[0], unitWeight=data_info[1],
                                 posiRatio=data_info[2], temperatureCoefficient=data_info[3],
                                 timeParameterId=creep_id, fcuk=f_cuk)

    @staticmethod
    def add_time_material(index: int = -1, name: str = "", code_index: int = 1, time_parameter: list[float] = None):
        """
        添加收缩徐变材料
        Args:
            index: 指定收缩徐变编号,默认则自动识别 (可选参数)
            name: 收缩徐变名
            code_index: 收缩徐变规范索引
            time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)
        example:
            mdb.add_time_material(index=1,name="收缩徐变材料1",code_index=1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
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

    @staticmethod
    def update_material_creep(index: int = 1, creep_id: int = 1, f_cuk: float = 0):
        """
        将收缩徐变参数连接到材料
        Args:
            index: 材料编号
            creep_id: 收缩徐变编号
            f_cuk: 材料标准抗压强度,仅自定义材料是需要输入
        example:
            mdb.update_material_creep(index=1,creep_id=1,f_cuk=5e7)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.UpdateMaterialCreep(materialId=index, timePatameterId=creep_id, fcuk=f_cuk)

    @staticmethod
    def remove_material(index: int = -1):
        """
        删除指定材料
        Args:
            index:指定材料编号，默认则删除所有材料
        example:
            mdb.remove_material()
            mdb.remove_material(index=1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if index == -1:
            qt_model.RemoveAllMaterial()
        else:
            qt_model.RemoveMaterial(id=index)

    # endregion

    # region 截面操作
    @staticmethod
    def add_parameter_section(index: int = -1, name: str = "", sec_type: str = "矩形", sec_info: list[float] = None,
                              symmetry: bool = True, charm_info: list[str] = None, sec_right: list[float] = None,
                              charm_right: list[str] = None, box_number: int = 3, box_height: float = 2,
                              mat_combine: list[float] = None,
                              bias_type: str = "中心", center_type: str = "质心", shear_consider: bool = True, bias_x: float = 0, bias_y: float = 0):
        """
        添加截面信息
        Args:
            index: 截面编号,默认自动识别
            name:截面名称
            sec_type:参数截面类型名称,支持以下类型
                _"矩形", "圆形", "圆管", "箱型", "实腹八边形",_
                _"空腹八边形", "内八角形", "实腹圆端型", "T形", "倒T形",_
                _"I字形", "马蹄T形", "I字形混凝土", "混凝土箱梁", "带肋钢箱",_
                _"带肋H截面", "钢桁箱梁1", "钢桁箱梁2", "钢桁箱梁3",_
                _"钢工字型带肋", "钢管砼", "钢箱砼"_
            sec_info:截面信息 (必要参数)
            symmetry:混凝土截面是否对称 (仅混凝土箱梁截面需要)
            charm_info:混凝土截面倒角信息 (仅混凝土箱梁截面需要)
            sec_right:混凝土截面右半信息 (对称时可忽略，仅混凝土箱梁截面需要)
            charm_right:混凝土截面右半倒角信息 (对称时可忽略，仅混凝土箱梁截面需要)
            box_number: 混凝土箱室数 (仅混凝土箱梁截面需要)
            box_height: 混凝土箱梁梁高 (仅混凝土箱梁截面需要)
            mat_combine: 组合截面材料信息 (仅组合材料需要)
                _[弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c]_
            bias_type:偏心类型 默认中心
            center_type:中心类型 默认质心
            shear_consider:考虑剪切 bool 默认考虑剪切变形
            bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要)
            bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要)
        example:
            mdb.add_parameter_section(name="截面1",sec_type="矩形",sec_info=[2,4],bias_type="中心")
            mdb.add_parameter_section(name="截面2",sec_type="混凝土箱梁",box_height=2,box_number=3,
                sec_info=[0.02,0,12,3,1,2,1,5,6,0.2,0.4,0.1,0.13,0.28,0.3,0.5,0.5,0.5,0.2],
                charm_info=["1*0.2,0.1*0.2","0.5*0.15,0.3*0.2","0.4*0.2","0.5*0.2"])
        Returns: 无
        """
        sec_type_list = ["矩形", "圆形", "圆管", "箱型", "实腹八边形",
                         "空腹八边形", "内八角形", "实腹圆端型", "T形", "倒T形",
                         "I字形", "马蹄T形", "I字形混凝土", "混凝土箱梁", "带肋钢箱",
                         "带肋H截面", "钢桁箱梁1", "钢桁箱梁2", "钢桁箱梁3", "钢工字型带肋",
                         "钢管砼", "钢箱砼"]
        if sec_type not in sec_type_list:
            raise Exception(f"操作失败，参数截面仅支持以下截面类型{sec_type_list}")
        if sec_info is None:
            raise Exception("操作错误,请输入此截面的截面信息，参数列表可参考截面定义窗口!")
        elif sec_type == "混凝土箱梁":
            if len(sec_info) != 19 or len(charm_info) != 4:
                raise Exception("操作错误，混凝土箱梁参数错误，参数列表可参考截面定义窗口！")
            qt_model.AddParameterSection(id=index, name=name, secType=sec_type, secInfo=sec_info, charmInfo=charm_info,
                                         symmetry=symmetry, N=box_number, H=box_height, charmInfoR=charm_right, secInfoR=sec_right,
                                         biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                         horizontalPos=bias_x, verticalPos=bias_y)
        elif sec_type == "钢管砼" or sec_type == "钢箱砼":
            if len(mat_combine) != 5:
                raise Exception("操作错误，材料比错误，参数列表：[弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c] ！")
            if len(sec_info) != 2 or len(sec_info) != 6:
                raise Exception("操作错误，截面参数列表：[D,t]-钢管砼  [W,H,dw,tw,tt,tb]-钢箱砼")
            qt_model.AddParameterSection(id=index, name=name, secType=sec_type, secInfo=sec_info,
                                         elasticModulusRatio=mat_combine[0], densityRatio=mat_combine[1], steelPoisson=mat_combine[2],
                                         concretePoisson=mat_combine[3], temperatureRatio=mat_combine[4],
                                         biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                         horizontalPos=bias_x, verticalPos=bias_y)
        else:
            qt_model.AddParameterSection(id=index, name=name, secType=sec_type, secInfo=sec_info,
                                         biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                         horizontalPos=bias_x, verticalPos=bias_y)

    @staticmethod
    def update_parameter_section(index: int = -1, name: str = "", sec_type: str = "矩形", sec_info: list[float] = None,
                                 symmetry: bool = True, charm_info: list[str] = None, sec_right: list[float] = None,
                                 charm_right: list[str] = None, box_number: int = 3, box_height: float = 2,
                                 mat_combine: list[float] = None,
                                 bias_type: str = "中心", center_type: str = "质心", shear_consider: bool = True, bias_x: float = 0, bias_y: float = 0):
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        sec_type_list = ["矩形", "圆形", "圆管", "箱型", "实腹八边形",
                         "空腹八边形", "内八角形", "实腹圆端型", "T形", "倒T形",
                         "I字形", "马蹄T形", "I字形混凝土", "混凝土箱梁", "带肋钢箱",
                         "带肋H截面", "钢桁箱梁1", "钢桁箱梁2", "钢桁箱梁3", "钢工字型带肋",
                         "钢管砼", "钢箱砼"]
        if sec_type not in sec_type_list:
            raise Exception(f"操作失败，参数截面仅支持以下截面类型{sec_type_list}")
        if sec_info is None:
            raise Exception("操作错误,请输入此截面的截面信息，参数列表可参考截面定义窗口!")
        elif sec_type == "混凝土箱梁":
            if len(sec_info) != 19 or len(charm_info) != 4:
                raise Exception("操作错误，混凝土箱梁参数错误，参数列表可参考截面定义窗口！")
            qt_model.UpdateParameterSection(id=index, name=name, secType=sec_type, secInfo=sec_info, charmInfo=charm_info,
                                            symmetry=symmetry, N=box_number, H=box_height, charmInfoR=charm_right, secInfoR=sec_right,
                                            biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                            horizontalPos=bias_x, verticalPos=bias_y)
        elif sec_type == "钢管砼" or sec_type == "钢箱砼":
            if len(mat_combine) != 5:
                raise Exception("操作错误，材料比错误，参数列表：[弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c] ！")
            if len(sec_info) != 2 or len(sec_info) != 6:
                raise Exception("操作错误，截面参数列表：[D,t]-钢管砼  [W,H,dw,tw,tt,tb]-钢箱砼")
            qt_model.UpdateParameterSection(id=index, name=name, secType=sec_type, secInfo=sec_info,
                                            elasticModulusRatio=mat_combine[0], densityRatio=mat_combine[1], steelPoisson=mat_combine[2],
                                            concretePoisson=mat_combine[3], temperatureRatio=mat_combine[4],
                                            biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                            horizontalPos=bias_x, verticalPos=bias_y)
        else:
            qt_model.UpdateParameterSection(id=index, name=name, secType=sec_type, secInfo=sec_info,
                                            biasType=bias_type, centerType=center_type, shearConsider=shear_consider,
                                            horizontalPos=bias_x, verticalPos=bias_y)

    @staticmethod
    def add_steel_section(index: int = -1, name: str = "", sec_type: int = 1, sec_info: list[float] = None,
                          rib_info: dict[str, list[float]] = None, rib_place: list[tuple[int, int, int, list[tuple[float, str, int, str]]]] = None,
                          bias_type: str = "中心", center_type: str = "质心", shear_consider: bool = True, bias_x: float = 0, bias_y: float = 0):
        """
        添加钢梁截面,包括参数型钢梁截面和自定义带肋钢梁截面
        Args:
             index:
             name:
             sec_type:截面类型 1-工字钢梁  2-箱型钢梁
             sec_info:截面信息
                _工字钢梁[topDis,botDis,b1,b2,b3,b4,h,t1,t2,tw]_
                _箱型钢梁[topDis,botDis,b1,b2,b3,b4,b5,b6,h,t1,t2,tw1,tw2]_
             rib_info:肋板信息
             rib_place:肋板位置 list[tuple[布置位置,具体位置,参考点位置,肋板间隔列表]]
                _肋板间隔列表: list[tuple[间隔,肋板名，加劲肋位置,加劲肋名]]_
                _布置位置: 0-上...  具体位置 0-桥面1..._
                _参考点位置:0-左  加劲肋位置 0-上/左 1-下/右 2-两侧_
             bias_type:偏心类型
             center_type:中心类型
             shear_consider:考虑剪切
             bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要,相对形心)
             bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要)
        example:
            mdb.add_steel_section(name="钢梁截面1",sec_type=1,sec_info=[0,0,0.5,0.5,0.5,0.5,0.7,0.02,0.02,0.02])
            mdb.add_steel_section(name="钢梁截面2",sec_type=2,sec_info=[0,0.15,0.25,0.5,0.25,0.15,0.4,0.15,0.7,0.02,0.02,0.02,0.02],
                rib_info = {"板肋1": [0.1,0.02],"T形肋1":[0.1,0.02,0.02,0.02]},
                rib_place = [(0, 0, 0, [(0.1, "板肋1", 2, "默认名称1"), (0.2, "板肋1", 2, "默认名称2")]), (0, 0, 1, [(0.1, "T形肋1", 0, "默认名称3")])],
                bias_type="中上")
        Returns: 无
        """
        if sec_info is None:
            raise Exception("操作错误,请输入此截面的截面信息，参数列表可参考截面定义窗口")
        section_type = "工字钢梁" if sec_type == 1 else "箱型钢梁"
        rib_names = list(rib_info.keys())
        rib_data = list(rib_info.values())
        qt_model.AddSteelSection(id=index, name=name, sectionType=section_type, sectionInfoList=sec_info,
                                 ribNameList=rib_names, ribInfoList=rib_data,
                                 ribPlaceList=rib_place, baisType=bias_type, centerType=center_type,
                                 shearConsider=shear_consider, horizontalPos=bias_x, verticalPos=bias_y)

    @staticmethod
    def add_user_section(index: int = -1, name: str = "", sec_type: str = "特性截面", property_info: list[float] = None,
                         main_loop: list[tuple[float, float]] = None, sub_loops: list[list[tuple[float, float]]] = None,
                         sec_lines: list[tuple[float, float, float, float, float]] = None):
        """
        添加自定义截面,目前仅支持特性截面
        Args:
             index:截面编号
             name:截面名称
             sec_type:截面类型
             property_info:截面特性列表
             main_loop:主线圈坐标集合 [(-1,-1),(5,0),(5,5),(-1,5)] 目前只支持单一线圈
             sub_loops:次线圈坐标集合 [[(0,0),(0,1),(1,1,)], [(2,2),(3,2),(3,3)]]
             sec_lines:线宽集合[(x1,y1,x2,y3,thick),]
        example:
            mdb.add_user_section(name="自定义特性截面",property_info=[i for i in range(25)])
        Returns: 无
        """
        if sec_type == "特性截面" and len(property_info) != 25:
            raise Exception(f"操作错误，自定义特性截面列表property_info需要25个参数")
        if property_info is None:
            raise Exception("操作错误,请输入此截面的截面特性，特性列表可参考截面定义窗口")
        qt_model.AddUserSection(id=index, name=name, type=sec_type, propertyInfo=property_info,
                                mainLoop=main_loop, subLoops=sub_loops, secLines=sec_lines)

    @staticmethod
    def add_tapper_section(index: int = -1, name: str = "", begin_id: int = 1, end_id: int = 1):
        """
        添加变截面,需先建立单一截面
        Args:
             index:截面编号
             name:截面名称
             begin_id:截面始端编号
             end_id:截面末端编号
        example:
            mdb.add_tapper_section(name="变截面1",begin_id=1,end_id=2)
        Returns: 无
        """
        qt_model.AddTapperSection(id=index, name=name, beginId=begin_id, endId=end_id)

    @staticmethod
    def remove_section(index: int = -1):
        """
        删除截面信息
        Args:
             index: 截面编号,参数为默认时删除全部截面
        example:
            mdb.remove_section()
            mdb.remove_section(1)
        Returns: 无
        """
        if index == -1:
            qt_model.RemoveAllSection()
        else:
            qt_model.RemoveSection(id=index)

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
        example:
            mdb.add_thickness(name="厚度1", t=0.2,thick_type=0,bias_info=(0,0.8))
            mdb.add_thickness(name="厚度2", t=0.2,thick_type=1,rib_pos=0,dist_v=0.1,rib_v=[1,1,0.02,0.02])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
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
    def remove_thickness(index: int = -1):
        """
        删除板厚
        Args:
             index:板厚编号,默认时删除所有板厚信息
        example:
            mdb.remove_thickness()
            mdb.remove_thickness(index=1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if index == -1:
            qt_model.RemoveAllThickness()
        else:
            qt_model.RemoveThickness(id=index)

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
        example:
            mdb.add_tapper_section_group(ids=[1,2,3,4],name="变截面组1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddTapperSectionGroup(ids=ids, name=name, factorW=factor_w, factorH=factor_h, w=ref_w, h=ref_h, disW=dis_w, disH=dis_h)

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
        example:
            mdb.update_section_bias(index=1,bias_type="中上",center_type="几何中心")
            mdb.update_section_bias(index=1,bias_type="自定义",bias_point=[0.1,0.2])
        Returns: 无
        """
        if center_type == "自定义":
            if len(bias_point) != 2:
                raise Exception("操作错误,bias_point数据无效!")
            qt_model.UpdateSectionBias(id=index, biasType=bias_type, centerType=center_type,
                                       shearConsider=shear_consider, horizontalPos=bias_point[0], verticalPos=bias_point[1])
        else:
            qt_model.UpdateSectionBias(id=index, biasType=bias_type, centerType=center_type,
                                       shearConsider=shear_consider)

    # endregion

    # region 边界操作
    @staticmethod
    def add_boundary_group(name: str = "", index: int = -1):
        """
        新建边界组
        Args:
             name:边界组名
             index:边界组编号，默认自动识别当前编号 (可选参数)
        example:
            mdb.add_boundary_group(name="边界组1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddBoundaryGroup(name=name, id=index)

    @staticmethod
    def remove_boundary_group(name: str = ""):
        """
        按照名称删除边界组
        Args:
            name: 边界组名称，默认删除所有边界组 (非必须参数)
        example:
            mdb.remove_boundary_group()
            mdb.remove_boundary_group(name="边界组1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name != "":
            qt_model.RemoveBoundaryGroup(name)
        else:
            qt_model.RemoveAllBoundaryGroup()

    @staticmethod
    def remove_all_boundary():
        """
        根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息
        Args:无
        example:
            mdb.remove_all_boundary()
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.RemoveAllBoundary()

    @staticmethod
    def remove_boundary(remove_id: int, bd_type: int, group: str = "默认边界组"):
        """
        根据节点号删除一般支撑、弹性支承/根据单元号删除梁端约束/根据主节点号删除主从约束/根据从节点号删除约束方程
        Args:
            remove_id:节点号 or 单元号 or主节点号  or 从节点号
            bd_type:边界类型
                _1-一般支承 2-弹性支承 3-主从约束 4-弹性连接 5-约束方程 6-梁端约束_
            group:边界所处边界组名
        example:
            mdb.remove_boundary(remove_id = 1, bd_type = 1,group="边界组1")
        Returns: 无
        """
        type_list = ["一般支承", "弹性支承", "主从约束", "弹性连接", "约束方程", "梁端约束"]
        bd_name = type_list[bd_type - 1]
        qt_model.RemoveBoundary(controlId=remove_id, type=bd_name, group=group)

    @staticmethod
    def add_general_support(node_id: int = 1, boundary_info: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加一般支承
        Args:
             node_id:节点编号
             boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]
                _ture-固定 false-自由_
             group_name:边界组名,默认为默认边界组
        example:
            mdb.add_general_support(node_id=1, boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        if boundary_info is None or len(boundary_info) != 6:
            raise Exception("操作错误，要求输入一般支承列表长度为6")
        qt_model.AddGeneralSupport(nodeId=node_id, boundaryInfo=boundary_info, groupName=group_name)

    @staticmethod
    def add_elastic_support(node_id: int = 1, support_type: int = 1, boundary_info: list[float] = None, group_name: str = "默认边界组"):
        """
        添加弹性支承
        Args:
             node_id:节点编号
             support_type:支承类型 1-线性  2-受拉  3-受压
             boundary_info:边界信息 受拉和受压时列表长度为1  线性时列表长度为6
             group_name:边界组
        example:
            mdb.add_elastic_support(node_id=1,support_type=1,boundary_info=[1e6,0,1e6,0,0,0])
        Returns: 无
        """
        qt_model.AddElasticSupport(nodeId=node_id, supportType=support_type, boundaryInfo=boundary_info,
                                   groupName=group_name)

    @staticmethod
    def add_master_slave_link(master_id: int = 1, slave_id: int = 2, boundary_info: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加主从约束
        Args:
             master_id:主节点号
             slave_id:从节点号
             boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz]
                _ture-固定 false-自由_
             group_name:边界组名
        example:
            mdb.add_master_slave_link(master_id=1,slave_id=2,boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        qt_model.AddMasterSlaveLink(masterId=master_id, slaveId=slave_id, boundaryInfo=boundary_info, groupName=group_name)

    @staticmethod
    def add_elastic_link(link_type: int = 1, start_id: int = 1, end_id: int = 2, beta_angle: float = 0,
                         boundary_info: list[float] = None,
                         group_name: str = "默认边界组", dis_ratio: float = 0.5, kx: float = 0):
        """
        添加弹性连接
        Args:
             link_type:节点类型
                _1-一般弹性连接 2-刚性连接 3-受拉弹性连接 4-受压弹性连接_
             start_id:起始节点号
             end_id:终节点号
             beta_angle:贝塔角
             boundary_info:边界信息
             group_name:边界组名
             dis_ratio:距i端距离比 (仅一般弹性连接需要)
             kx:受拉或受压刚度
        example:
            mdb.add_elastic_link(link_type=1,start_id=1,end_id=2,boundary_info=[1e6,1e6,1e6,0,0,0])
            mdb.add_elastic_link(link_type=2,start_id=1,end_id=2)
            mdb.add_elastic_link(link_type=3,start_id=1,end_id=2,kx=1e6)
        Returns: 无
        """
        qt_model.AddElasticLink(linkType=link_type, startId=start_id, endId=end_id, beta=beta_angle,
                                boundaryInfo=boundary_info, groupName=group_name, disRatio=dis_ratio, kDx=kx)

    @staticmethod
    def add_beam_constraint(beam_id: int = 2, info_i: list[bool] = None, info_j: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加梁端约束
        Args:
             beam_id:梁号
             info_i:i端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             info_j:j端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             group_name:边界组名
        example:
            mdb.add_beam_constraint(beam_id=2,info_i=[True,True,True,False,False,False],info_j=[True,True,True,False,False,False])
        Returns: 无
        """
        if info_i is None or len(info_i) != 6:
            raise Exception("操作错误，要求输入I端约束列表长度为6")
        if info_j is None or len(info_j) != 6:
            raise Exception("操作错误，要求输入J端约束列表长度为6")
        qt_model.AddBeamConstraint(beamId=beam_id, nodeInfoI=info_i, nodeInfo2=info_j, groupName=group_name)

    @staticmethod
    def add_node_axis(input_type: int = 1, node_id: int = 1, coord_info: list = None):
        """
        添加节点坐标
        Args:
             input_type:输入方式 1-角度 2-三点  3-向量
             node_id:节点号
             coord_info:局部坐标信息 -List<float>(角)  -List<List<float>>(三点 or 向量)
        example:
            mdb.add_node_axis(input_type=1,node_id=1,coord_info=[45,45,45])
            mdb.add_node_axis(input_type=2,node_id=1,coord_info=[[0,0,1],[0,1,0],[1,0,0]])
            mdb.add_node_axis(input_type=3,node_id=1,coord_info=[[0,0,1],[0,1,0]])
        Returns: 无
        """
        if coord_info is None:
            raise Exception("操作错误，输入坐标系信息不能为空")
        if input_type == 1:
            qt_model.AddNodalAxises(inputType=input_type, nodeId=node_id, angleInfo=coord_info)
        else:
            qt_model.AddNodalAxises(inputType=input_type, nodeId=node_id, nodeInfo=coord_info)

    # endregion

    # region 移动荷载操作
    @staticmethod
    def add_standard_vehicle(name: str, standard_code: int = 1, load_type: str = "高速铁路", load_length: float = 0, n: int = 6):
        """
        添加标准车辆
        Args:
             name: 车辆荷载名称
             standard_code: 荷载规范
                _1-中国铁路桥涵规范(Q/CR 9300-2017)_
                _2-城市桥梁设计规范(CJJ11-2019)_
                _3-公路工程技术标准(JTJ 001-97)_
                _4-公路桥涵设计通规(JTG D60-2004)_
                _5-公路桥涵设计通规(JTG D60-2015)_
                _6-城市轨道交通桥梁规范(GB/T51234-2017)_
             load_type: 荷载类型,支持类型如下
                _"公路I级","公路II级","城A车道","城B车道"_
                _"地铁A型车","地铁B型车","地铁C型车","汽10"_
                _"汽15","汽20","汽超20","特载","挂80"_
                _"挂100","挂120","公路疲劳荷载1","公路疲劳荷载2"_
                _"公路疲劳荷载3","汽36轻", "汽38重","高速铁路"_
                _"城际铁路","客货共线铁路","重载铁路","中活载","长大货物车检算荷载"_
             load_length: 默认为0即不限制荷载长度  (铁路桥涵规范2017 所需参数)
             n:车厢数: 默认6节车厢 (城市轨道交通桥梁规范2017 所需参数)
        example:
            mdb.add_standard_vehicle("高速铁路",standard_code=1,load_type="高速铁路")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddStandardVehicle(name=name, standardIndex=standard_code, loadType=load_type, loadLength=load_length, N=n)

    @staticmethod
    def add_node_tandem(name: str, start_id: int, node_ids: list[int]):
        """
        添加节点纵列
        Args:
             name:节点纵列名
             start_id:起始节点号
             node_ids:节点列表
        example:
            mdb.add_node_tandem("节点纵列1",1,[i+1 for i in range(12)])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if node_ids is None:
            raise Exception("操作错误，输入节点列表不能为空")
        qt_model.AddNodeTandem(name=name, startId=start_id, nodeIds=node_ids)

    @staticmethod
    def add_influence_plane(name: str, tandem_names: list[str]):
        """
        添加影响面
        Args:
             name:影响面名称
             tandem_names:节点纵列名称组
        example:
            mdb.add_influence_plane("影响面1",["节点纵列1","节点纵列2"])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddInfluencePlane(name=name, tandemNames=tandem_names)

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
        example:
            mdb.add_lane_line("车道1","影响面1","节点纵列1",offset=0,lane_width=3.1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddLaneLine(name, influenceName=influence_name, tandemName=tandem_name, offset=offset, laneWidth=lane_width)

    @staticmethod
    def add_live_load_case(name: str, influence_plane: str, span: float,
                           car_detail: tuple[list[float], float, float] = None,
                           train_detail: tuple[list[float], float, float, float] = None,
                           metro_detail: tuple[list[float], float, float] = None,
                           sub_case: list[tuple[str, float, list[str]]] = None):
        """
        添加移动荷载工况
        Args:
             name:荷载工况名
             influence_plane:影响线名
             span:跨度
             car_detail: 汽车相关系数 (横向折减列表float[8],纵向折减系数,冲击强度)
             train_detail: 火车相关系数 (横向折减列表float[8],纵向折减系数,强度冲击,疲劳冲击)
             metro_detail: 轻轨相关系数 (横向折减列表float[8],纵向折减系数,冲击强度)
             sub_case:子工况信息 [(车辆名称,系数,["车道1","车道2"])...]
        example:
            mdb.add_live_load_case("活载工况1","影响面1",100,sub_case=[("车辆名称",1.0,["车道1","车道2"]),])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if sub_case is None:
            raise Exception("操作错误，子工况信息列表不能为空")
        qt_model.AddLiveLoadCase(name=name, influencePlane=influence_plane, span=span, subCase=sub_case)

    @staticmethod
    def remove_vehicle(index: int = -1, name: str = ""):
        """
        删除车辆信息
        Args:
             index:车辆荷载编号
             name:车辆名称
        example:
            mdb.remove_vehicle(index=1)
            mdb.remove_vehicle(name="车辆名称")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if id != -1:
            qt_model.RemoveVehicle(id=index)
        elif name != "":
            qt_model.RemoveVehicle(name=name)

    @staticmethod
    def remove_node_tandem(index: int = -1, name: str = ""):
        """
        按照 节点纵列编号/节点纵列名 删除节点纵列
        Args:
             index:节点纵列编号
             name:节点纵列名
        example:
            mdb.remove_node_tandem(index=1)
            mdb.remove_node_tandem(name="节点纵列1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if index != -1:
            qt_model.RemoveNodeTandem(id=index)
        elif name != "":
            qt_model.RemoveNodeTandem(name=name)

    @staticmethod
    def remove_influence_plane(index: int = -1, name: str = ""):
        """
        按照 影响面编号/影响面名称 删除影响面
        Args:
             index:影响面编号
             name:影响面名称
        example:
            mdb.remove_influence_plane(index=1)
            mdb.remove_influence_plane(name="影响面1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if index != -1:
            qt_model.RemoveInfluencePlane(id=index)
        elif name != "":
            qt_model.RemoveInfluencePlane(name=name)

    @staticmethod
    def remove_lane_line(name: str = "", index: int = -1):
        """
        按照 车道线编号/车道线名称 删除车道线
        Args:
             name:车道线名称
             index:车道线编号
        example:
            mdb.remove_lane_line(index=1)
            mdb.remove_lane_line(name="车道线1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if index != -1:
            qt_model.RemoveLaneLine(id=index)
        elif name != "":
            qt_model.RemoveLaneLine(name=name)

    @staticmethod
    def remove_live_load_case(name: str = ""):
        """
        删除移动荷载工况
        Args:
             name:移动荷载工况名
        example:
            mdb.remove_live_load_case(name="活载工况1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.RemoveLiveLoadCase(name=name)

    # endregion

    # region 钢束操作
    @staticmethod
    def add_tendon_group(name: str = "", index: int = -1):
        """
        按照名称添加钢束组，添加时可指定钢束组id
        Args:
            name: 钢束组名称
            index: 钢束组编号(非必须参数)，默认自动识别
        example:
            mdb.add_tendon_group(name="钢束组1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddTendonGroup(name=name, id=index)

    @staticmethod
    def remove_tendon_group(name: str = "", index: int = -1):
        """
        按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组
        Args:
             name:钢束组名称,默认自动识别 (可选参数)
             index:钢束组编号,默认自动识别 (可选参数)
        example:
            mdb.remove_tendon_group(name="钢束组1")
            mdb.remove_tendon_group(index=1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name != "":
            qt_model.RemoveTendonGroup(name=name)
        elif index != -1:
            qt_model.RemoveTendonGroup(id=index)
        else:
            qt_model.RemoveAllStructureGroup()

    @staticmethod
    def add_tendon_property(name: str = "", index: int = -1, tendon_type: int = 0, material_id: int = 1, duct_type: int = 1,
                            steel_type: int = 1, steel_detail: list[float] = None, loos_detail: tuple[int, int, int] = None,
                            slip_info: tuple[int, int] = None):
        """
        添加钢束特性
        Args:
             name:钢束特性名
             index:钢束编号,默认自动识别 (可选参数)
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
        example:
            mdb.add_tendon_property(name="钢束1",tendon_type=0,material_id=1,duct_type=1,steel_type=1,
                                    steel_detail=[0.00014,0.10,0.25,0.0015],loos_detail=(1,1,1))
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if steel_detail is None:
            raise Exception("操作错误，钢束特性信息不能为空")
        if loos_detail is None:
            loos_detail = (1, 1, 1)
        if slip_info is None:
            slip_info = (0.006, 0.006)
        qt_model.AddTendonProperty(name=name, id=index, tendonType=tendon_type, materialId=material_id,
                                   ductType=duct_type, steelType=steel_type, steelDetail=steel_detail,
                                   loosDetail=loos_detail, slipInfo=slip_info)

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
        example:
            mdb.add_tendon_3d("BB1",property_name="22-15",num=2,position_type=1,
                    control_points=[(0,0,-1,0),(10,0,-1,0)],point_insert=(0,0,0))
            mdb.add_tendon_3d("BB1",property_name="22-15",num=2,position_type=2,
                    control_points=[(0,0,-1,0),(10,0,-1,0)],point_insert=(1,1,1),track_group="轨迹线结构组1")
        Returns: 无
        """
        if tendon_direction is None:
            tendon_direction = (1, 0, 0)
        if control_points is None:
            raise Exception("操作错误，钢束形状控制点不能为空")
        if point_insert is None or len(point_insert) != 3:
            raise Exception("操作错误，钢束插入点信息不能为空且长度必须为3")
        qt_model.AddTendon3D(name=name, propertyName=property_name, groupName=group_name, num=num, lineType=line_type,
                             positionType=position_type, controlPoints=control_points,
                             pointInsert=point_insert, tendonDirection=tendon_direction,
                             rotationAngle=rotation_angle, trackGroup=track_group, isProjection=projection)

    @staticmethod
    def remove_tendon(name: str = "", index: int = -1):
        """
        按照名称或编号删除钢束,默认时删除所有钢束
        Args:
             name:钢束名称
             index:钢束编号
        example:
            mdb.remove_tendon(name="钢束1")
            mdb.remove_tendon(index=1)
            mdb.remove_tendon()
        Returns: 无
        """
        if name != "":
            qt_model.RemoveTendon(name=name)
        elif index != -1:
            qt_model.RemoveTendon(id=index)
        else:
            qt_model.RemoveAllTendon()

    @staticmethod
    def remove_tendon_property(name: str = "", index: int = -1):
        """
        按照名称或编号删除钢束组,默认时删除所有钢束组
        Args:
             name:钢束组名称
             index:钢束组编号
        example:
            mdb.remove_tendon_property(name="钢束特性1")
            mdb.remove_tendon_property(index=1)
            mdb.remove_tendon_property()
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name != "":
            qt_model.RemoveTendonProperty(name=name)
        elif index != -1:
            qt_model.RemoveTendonProperty(id=index)
        else:
            qt_model.RemoveAllTendonGroup()

    @staticmethod
    def add_nodal_mass(node_id: int = 1, mass_info: tuple[float, float, float, float] = None):
        """
        添加节点质量
        Args:
             node_id:节点编号
             mass_info:[m,rmX,rmY,rmZ]
        example:
            mdb.add_nodal_mass(node_id=1,mass_info=(100,0,0,0))
        Returns: 无
        """
        if mass_info is None:
            raise Exception("操作错误，节点质量信息列表不能为空")
        qt_model.AddNodalMass(nodeId=node_id, massInfo=mass_info)

    @staticmethod
    def remove_nodal_mass(node_id: int = -1):
        """
        删除节点质量
        Args:
             node_id:节点号
        example:
            mdb.remove_nodal_mass(node_id=1)
        Returns: 无
        """
        qt_model.RemoveNodalMass(nodeId=node_id)

    @staticmethod
    def add_pre_stress(case_name: str = "", tendon_name: str = "", pre_type: int = 2, force: float = 1395000, group_name: str = "默认荷载组"):
        """
        添加预应力
        Args:
             case_name:荷载工况名
             tendon_name:钢束名
             pre_type:预应力类型
                _0-始端 1-末端 2-两端_
             force:预应力
             group_name:边界组
        example:
            mdb.add_pre_stress(case_name="荷载工况名",tendon_name="钢束1",force=1390000)
        Returns: 无
        """
        qt_model.AddPreStress(caseName=case_name, tendonName=tendon_name, preType=pre_type, force=force, groupName=group_name)

    @staticmethod
    def remove_pre_stress(case_name: str = "", tendon_name: str = "", group_name: str = "默认荷载组"):
        """
        删除预应力
        Args:
             case_name:荷载工况
             tendon_name:钢束组
             group_name:边界组名
        example:
            mdb.remove_pre_stress(case_name="工况1",tendon_name="钢束1",group_name="默认荷载组")
        Returns: 无
        """
        qt_model.RemovePreStress(caseName=case_name, tendonName=tendon_name, groupName=group_name)

    # endregion

    # region 荷载操作
    @staticmethod
    def add_load_group(name: str = ""):
        """
        根据荷载组名称添加荷载组
        Args:
             name: 荷载组名称
        example:
            mdb.add_load_group(name="荷载组1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name != "":
            qt_model.AddLoadGroup(name=name)

    @staticmethod
    def remove_load_group(name: str = "", index: int = -1):
        """
        根据荷载组名称或荷载组id删除荷载组,参数为默认时删除所有荷载组
        Args:
             name: 荷载组名称
             index: 荷载组编号
        example:
            mdb.remove_load_group(name="荷载组1")
            mdb.remove_load_group(index=1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name != "":
            qt_model.RemoveLoadGroup(name=name)
        elif index != -1:
            qt_model.RemoveLoadGroup(id=index)
        else:
            qt_model.RemoveAllLoadGroup()

    @staticmethod
    def add_nodal_force(node_id: int = 1, case_name: str = "", load_info: tuple[float, float, float, float, float, float] = None,
                        group_name: str = "默认荷载组"):
        """
        添加节点荷载
             case_name:荷载工况名
             node_id:节点编号
             load_info:荷载信息列表 [Fx,Fy,Fz,Mx,My,Mz]
             group_name:荷载组名
        example:
            mdb.add_nodal_force(case_name="荷载工况1",node_id=1,load_info=(1,1,1,1,1,1),group_name="默认结构组")
        Returns: 无
        """
        if load_info is None or len(load_info) != 6:
            raise Exception("操作错误，节点荷载列表信息不能为空，且其长度必须为6")
        qt_model.AddNodalForce(caseName=case_name, nodeId=node_id, loadInfo=load_info, groupName=group_name)

    @staticmethod
    def remove_nodal_force(node_id: int = -1, case_name: str = ""):
        """
        删除节点荷载
        Args:
             case_name:荷载工况名
             node_id:节点编号
        example:
            mdb.remove_nodal_force(case_name="荷载工况1",node_id=1)
        Returns: 无
        """
        qt_model.RemoveNodalForce(caseName=case_name, nodeId=node_id)

    @staticmethod
    def add_node_displacement(node_id: int = 1, case_name: str = "", load_info: tuple[float, float, float, float, float, float] = None,
                              group_name: str = "默认荷载组"):
        """
        添加节点位移
        Args:
            node_id:节点编号
            case_name:荷载工况名
            load_info:节点位移列表 [Dx,Dy,Dz,Rx,Ry,Rz]
            group_name:荷载组名
        example:
            mdb.add_node_displacement(case_name="荷载工况1",node_id=1,load_info=(1,0,0,0,0,0),group_name="默认荷载组")
        Returns: 无
        """
        if load_info is None or len(load_info) != 6:
            raise Exception("操作错误，节点位移列表信息不能为空，且其长度必须为6")
        qt_model.AddNodeDisplacement(caseName=case_name, nodeId=node_id, loadInfo=load_info, groupName=group_name)

    @staticmethod
    def remove_nodal_displacement(node_id: int = -1, case_name: str = ""):
        """
        删除节点位移
        Args:
            node_id:节点编号
            case_name:荷载工况名
        example:
            mdb.remove_nodal_displacement(case_name="荷载工况1",node_id=1)
        Returns: 无
        """
        qt_model.RemoveNodalDisplacement(caseName=case_name, nodeId=-node_id)

    @staticmethod
    def add_beam_load(beam_id: int = 1, case_name: str = "", load_type: int = 1, coord_system: int = 3,
                      is_abs=False, list_x: list[float, float] = None,
                      list_load: list[float, float] = None, group_name="默认荷载组", load_bias: tuple[bool, int, int, float] = None,
                      projected: bool = False):
        """
        添加梁单元荷载
        Args:
            beam_id:单元编号
            case_name:荷载工况名
            load_type:荷载类型
               _ 1-集中荷载 2-集中弯矩 3-分布弯矩 4-分布弯矩
            coord_system:坐标系
                _1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z_
            is_abs: 荷载位置输入方式，True-绝对值   False-相对值
            list_x:荷载位置信息 ,荷载距离单元I端的距离，可输入绝对距离或相对距离
            list_load:荷载数值信息
            group_name:荷载组名
            load_bias:偏心荷载 (是否偏心,0-中心 1-偏心,偏心坐标系-int,偏心距离)
            projected:是否投影
        example:
            mdb.add_beam_load(case_name="荷载工况1",beam_id=1,load_type=1,list_x=[0.1,0.5,0.8],list_load=[100,100,100])
            mdb.add_beam_load(case_name="荷载工况1",beam_id=1,load_type=3,list_x=[0.4,0.8],list_load=[100,200])
        Returns: 无
        """
        qt_model.AddBeamLoad(caseName=case_name, beamId=beam_id, loadType=load_type,
                             coordinateSystem=coord_system, listX=list_x, listLoad=list_load, groupName=group_name,
                             biasInfo=load_bias, isProject=projected)

    @staticmethod
    def remove_beam_load(element_id: int = 1, case_name: str = "", load_type: int = 1, group_name: str = "默认荷载组"):
        """
        删除梁单元荷载
        Args:
            element_id:单元号
            case_name:荷载工况名
            load_type:荷载类型
                _1-集中力   2-集中弯矩  3-分布力   4-分布弯矩_
            group_name:边界组名
        example:
            mdb.remove_beam_load(case_name="工况1",element_id=1,load_type=1,group_name="默认荷载组")
        Returns: 无
        """
        qt_model.RemoveBeamLoad(caseName=case_name, elementId=element_id, loadType=load_type, groupName=group_name)

    @staticmethod
    def add_initial_tension(element_id: int = 1, case_name: str = "", group_name: str = "默认荷载组", tension: float = 0, tension_type: int = 1):
        """
        添加初始拉力
        Args:
             element_id:单元编号
             case_name:荷载工况名
             tension:初始拉力
             tension_type:张拉类型  1-全量   2-增量
             group_name:荷载组名
        example:
            mdb.add_initial_tension(element_id=1,case_name="工况1",tension=100,tension_type=1)
        Returns: 无
        """
        qt_model.AddInitialTension(elementId=element_id, caseName=case_name, tension=tension, tensionType=tension_type, groupName=group_name)

    @staticmethod
    def add_cable_length_load(element_id: int = 1, case_name: str = "", group_name: str = "默认荷载组", length: float = 0, tension_type: int = 1):
        """
        添加索长张拉
        Args:
            element_id:单元类型
            case_name:荷载工况名
            length:长度
            tension_type:张拉类型  1-全量   2-增量
            group_name:荷载组名
        example:
            mdb.add_cable_length_load(element_id=1,case_name="工况1",length=1,tension_type=1)
        Returns: 无
        """
        qt_model.AddCableLenghtLoad(elementId=element_id, caseName=case_name, groupName=group_name, length=length, tensionType=tension_type)

    @staticmethod
    def add_plate_element_load(element_id: int = 1, case_name: str = "", load_type: int = 1, load_place: int = 1, coord_system: int = 3,
                               group_name: str = "默认荷载组", load_list: list[float] = None, xy_list: tuple[float, float] = None):
        """
        添加版单元荷载
        Args:
             element_id:单元id
             case_name:荷载工况名
             load_type:荷载类型
                _1-集中力  2-集中弯矩  3-分布力  4-分布弯矩_
             load_place:荷载位置
                _0-面IJKL 1-边IJ  2-边JK  3-边KL  4-边LI  (仅分布荷载需要)_
             coord_system:坐标系  (默认3)
                _1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z_
             group_name:荷载组名
             load_list:荷载列表
             xy_list:荷载位置信息 [IJ方向绝对距离x,IL方向绝对距离y]  (仅集中荷载需要)
        example:
            mdb.add_plate_element_load(element_id=1,case_name="工况1",load_type=1,group_name="默认荷载组",load_list=[1000],xy_list=(0.2,0.5))
        Returns: 无
        """
        if load_type == 1 or load_type == 2:
            qt_model.AddPlateElementLoad(elementId=element_id, caseName=case_name, loadType=load_type,
                                         coordSystem=coord_system, groupName=group_name, loads=load_list[0])
        elif load_type == 3 or load_type == 4:
            if load_place == 0:
                load_type = load_type + 2
            qt_model.AddPlateElementLoad(elementId=element_id, caseName=case_name, loadType=load_type, loadPosition=load_place,
                                         distanceList=xy_list, coordSystem=coord_system, groupName=group_name, loads=load_list[0])

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
        example:
            mdb.add_deviation_parameter(name="梁端制造误差",element_type=1,parameters=[1,0,0,0,0,0,0])
            mdb.add_deviation_parameter(name="板端制造误差",element_type=1,parameters=[1,0,0,0,0])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if parameters is None:
            raise Exception("操作错误，制造误差信息不能为空")
        if len(parameters) != 5 or len(parameters) != 7:
            raise Exception("操作错误，误差列表有误")
        qt_model.AddDeviationParameter(name=name, elementType=element_type, parameterInfo=parameters)

    @staticmethod
    def add_deviation_load(element_id: int = 1, case_name: str = "", parameters: list[str] = None, group_name: str = "默认荷载组"):
        """
        添加制造误差荷载
        Args:
            element_id:单元编号
            case_name:荷载工况名
            parameters:参数名列表
                _梁杆单元时-[制造误差参数名称]_
                _板单元时-[I端误差名,J端误差名,K端误差名,L端误差名]_
            group_name:荷载组名
        example:
            mdb.add_deviation_load(element_id=1,case_name="工况1",parameters=["梁端误差"])
            mdb.add_deviation_load(element_id=2,case_name="工况1",parameters=["板端误差1","板端误差2","板端误差3","板端误差4"])
        Returns: 无
        """
        if parameters is None:
            raise Exception("操作错误，制造误差名称信息不能为空")
        qt_model.AddDeviationLoad(elementId=element_id, caseName=case_name, parameterName=parameters, groupName=group_name)

    @staticmethod
    def add_element_temperature(element_id: int = 1, case_name: str = "", temperature: float = 1, group_name: str = "默认荷载组"):
        """
        添加单元温度
        Args:
            element_id:单元编号
            case_name:荷载工况名
            temperature:最终温度
            group_name:荷载组名
        example:
            mdb.add_element_temperature(element_id=1,case_name="自重",temperature=1,group_name="默认荷载组")
        Returns: 无
        """
        qt_model.AddElementTemperature(elementId=element_id, caseName=case_name, temperature=temperature, groupName=group_name)

    @staticmethod
    def add_gradient_temperature(element_id: int = 1, case_name: str = "", temperature: float = 1, section_oriental: int = 1,
                                 element_type: int = 1, group_name: str = ""):
        """
        添加梯度温度
             element_id:单元编号
             case_name:荷载工况名
             temperature:温差
             section_oriental:截面方向 (仅梁单元需要)
                _1-截面Y向(默认)  2-截面Z向_
             element_type:单元类型
                _1-梁单元(默认)  2-板单元_
             group_name:荷载组名
        example:
            mdb.add_gradient_temperature(element_id=1,case_name="荷载工况1",group_name="荷载组名1",temperature=10)
            mdb.add_gradient_temperature(element_id=2,case_name="荷载工况2",group_name="荷载组名2",temperature=10,element_type=2)
        Returns: 无
        """
        qt_model.AddGradientTemperature(elementId=element_id, caseName=case_name, temperature=temperature,
                                        sectionOriental=section_oriental, elementType=element_type, groupNmae=group_name)

    @staticmethod
    def add_beam_section_temperature(element_id: int = 1, case_name: str = "", paving_thick: float = 0, temperature_type: int = 1,
                                     paving_type: int = 1, group_name: str = "默认荷载组", modify: bool = False, temp_list: tuple[float, float] = None):
        """
        添加梁截面温度
        Args:
            element_id:单元编号
            case_name:荷载工况名
            paving_thick:铺设厚度(m)
            temperature_type:温度类型  1-升温(默认) 2-降温
            paving_type:铺设类型
                _1-沥青混凝土(默认)  2-水泥混凝土_
            group_name:荷载组名
            modify:是否修改规范温度
            temp_list:温度列表[T1,T2]  (仅修改时需要)
        example:
            mdb.add_beam_section_temperature(element_id=1,case_name="工况1",paving_thick=0.1)
        Returns: 无
        """
        qt_model.AddBeamSectionTemperature(elementId=element_id, caseName=case_name, pavingThickness=paving_thick, temperatureType=temperature_type,
                                           pavingType=paving_type, groupName=group_name, isModify=modify, temperatures=temp_list)

    @staticmethod
    def add_index_temperature(element_id: int = 1, case_name: str = "", temperature: float = 0, index: float = 1, group_name: str = "默认荷载组"):
        """
        添加指数温度
        Args:
            element_id:单元编号
            case_name:荷载工况名
            temperature:温差
            index:指数
            group_name:荷载组名
        example:
            mdb.add_index_temperature(element_id=1,case_name="工况1",temperature=20,index=2)
        Returns: 无
        """
        qt_model.AddIndexTemperature(elementId=element_id, caseName=case_name, temperature=temperature, index=index, groupName=group_name)

    @staticmethod
    def add_top_plate_temperature(element_id: int = 1, case_name: str = "", temperature: float = 0, group_name: str = "默认荷载组"):
        """
        添加顶板温度
        Args:
             element_id:单元编号
             case_name:荷载
             temperature:最终温度
             group_name:荷载组名
        example:
            mdb.add_top_plate_temperature(element_id=1,case_name="工况1",temperature=40,group_name="默认荷载组")
        Returns: 无
        """
        qt_model.AddTopPlateTemperature(elementId=element_id, caseName=case_name, temperature=temperature, groupName=group_name)

    # endregion

    # region 沉降操作
    @staticmethod
    def add_sink_group(name: str = "", sink: float = 0.1, node_ids: list[int] = None):
        """
        添加沉降组
        Args:
             name: 沉降组名
             sink: 沉降值
             node_ids: 节点编号
        example:
            mdb.add_sink_group(name="沉降1",sink=0.1,node_ids=[1,2,3])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if node_ids is None:
            raise Exception("操作错误，沉降定义中节点信息不能为空")
        qt_model.AddSinkGroup(name=name, sinkValue=sink, nodeIds=node_ids)

    @staticmethod
    def remove_sink_group(name: str = ""):
        """
        按照名称删除沉降组
        Args:
             name:沉降组名,默认删除所有沉降组
        example:
            mdb.remove_sink_group()
            mdb.remove_sink_group(name="沉降1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name == "":
            qt_model.RemoveAllSinkGroup()
        else:
            qt_model.RemoveSinkGroup(name=name)

    @staticmethod
    def add_sink_case(name: str, sink_groups: list[str] = None):
        """
        添加沉降工况
        Args:
            name:荷载工况名
            sink_groups:沉降组名
        example:
            mdb.add_sink_case(name="沉降工况1",sink_groups=["沉降1","沉降2"])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if sink_groups is None:
            raise Exception("操作错误，沉降工况定义中沉降组信息不能为空")
        qt_model.AddSinkCase(name=name, sinkGroups=sink_groups)

    @staticmethod
    def remove_sink_case(name=""):
        """
        按照名称删除沉降工况,不输入名称时默认删除所有沉降工况
        Args:
            name:沉降工况名
        example:
            mdb.remove_sink_case()
            mdb.remove_sink_case(name="沉降1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name == "":
            qt_model.RemoveAllSinkCase()
        else:
            qt_model.RemoveSinkCase()

    @staticmethod
    def add_concurrent_reaction(names: list[str]):
        """
        添加并发反力组
        Args:
             names: 结构组名称集合
        example:
            mdb.add_concurrent_reaction(["默认结构组"])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if names is None:
            raise Exception("操作错误，添加并发反力组时结构组名称不能为空")
        qt_model.AddConcurrentReaction(names=names)

    @staticmethod
    def remove_concurrent_reaction():
        """
        删除所有并发反力组
        Args:无
        example:
            mdb.remove_concurrent_reaction()
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.RemoveConcurrentRection()

    @staticmethod
    def add_concurrent_force(names: list[str]):
        """
        创建并发内力组
        Args:
            names: 结构组名称集合
        example:
            mdb.add_concurrent_force(["默认结构组"])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddConcurrentForce(names=names)

    @staticmethod
    def remove_concurrent_force():
        """
        删除所有并发内力组
        Args: 无
        example:
            mdb.remove_concurrent_force()
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.RemoveConcurrentForce()

    @staticmethod
    def add_load_case(name: str = "", case_type: int = 1):
        """
        添加荷载工况
        Args:
            name:沉降名
            case_type:荷载工况类型
        example:
            mdb.add_load_case(name="工况1",case_type=1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        case_type_list = ["施工阶段荷载", "恒载", "活载", "制动力", "风荷载",
                          "体系温度荷载", "梯度温度荷载", "长轨伸缩挠曲力荷载", "脱轨荷载", "船舶撞击荷载",
                          "汽车撞击荷载", "长轨断轨力荷载", "用户定义荷载"]
        if case_type < 1 or case_type > 13:
            raise TypeError("输入类型错误，荷载工况类型有误，仅支持int类型")
        qt_model.AddLoadCase(name=name, loadCaseType=case_type_list[case_type - 1])

    @staticmethod
    def remove_load_case(index: int = -1, name: str = ""):
        """
        删除荷载工况,参数均为默认时删除全部荷载工况
        Args:
            index:荷载编号
            name:荷载名
        example:
            mdb.remove_load_case(index=1)
            mdb.remove_load_case(name="工况1")
            mdb.remove_load_case()
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name != "":
            qt_model.DeleteLoadCase(name=name)
        elif index != -1:
            qt_model.DeleteLoadCase(id=index)
        else:
            qt_model.DeleteAllLoadCase()

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
           index:施工阶段编号，默认自动添加
        example:
           mdb.add_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
                active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.AddConstructionStage(name=name, duration=duration, activeStructures=active_structures, inActiveStructures=delete_structures
                                      , activeBoundaries=active_boundaries, inActiveBoundaries=delete_boundaries, activeLoads=active_loads,
                                      inActiveLoads=delete_loads, tempLoads=temp_loads, id=index)

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
        example:
           mdb.update_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
               active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.UpdateConstructionStage(name=name, duration=duration, activeStructures=active_structures, inActiveStructures=delete_structures
                                         , activeBoundaries=active_boundaries, inActiveBoundaries=delete_boundaries, activeLoads=active_loads,
                                         inActiveLoads=delete_loads, tempLoads=temp_loads)

    @staticmethod
    def update_weight_stage(stage_name: str = "", structure_group_name: str = "", weight_stage_id: int = 1):
        """
        添加施工阶段信息
        Args:
           stage_name:施工阶段信息
           structure_group_name:结构组名
           weight_stage_id: 计自重阶段号
            _0-不计自重,1-本阶段 n-第n阶段_
        example:
           mdb.update_weight_stage(stage_name="施工阶段1",structure_group_name="默认结构组",weight_stage_id=1)
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        qt_model.UpdateWeightStage(stageName=stage_name, structureGroupName=structure_group_name, weightStageId=weight_stage_id)

    @staticmethod
    def remove_construction_stage(name: str = ""):
        """
        按照施工阶段名删除施工阶段,默认删除所有施工阶段
        Args:
            name:所删除施工阶段名称
        example:
            mdb.remove_construction_stage(name="施工阶段1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name == "":
            qt_model.RemoveAllConstructionStage()
        else:
            qt_model.RemoveConstructionStage(name=name)

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
                _"MV"-移动荷载工况  "SM"-沉降荷载工况_
        example:
            mdb.add_load_combine(name="荷载组合1",combine_type=1,describe="无",combine_info=[("CS","合计值",1),("CS","恒载",1)])
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if combine_info is None:
            combine_info = []
        qt_model.AddLoadCombine(name=name, loadCombineType=combine_type, describe=describe, caseAndFactor=combine_info)

    @staticmethod
    def remove_load_combine(name: str = ""):
        """
        删除荷载组合
        Args:
             name:指定删除荷载组合名，默认时则删除所有荷载组合
        example:
            mdb.remove_load_combine(name="荷载组合1")
        Returns: 无
        """
        if qt_model.GetApplicationStage() == "首页":
            raise Exception("起始页面下无法修改模型，请切换至前处理")
        if name != "":
            qt_model.DeleteLoadCombine(name=name)
        else:
            qt_model.DeleteAllLoadCombine()

    # endregion
