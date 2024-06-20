# 最新版本 V0.4.8 - 2024.06.20
> pip install --upgrade qtmodel -i https://pypi.org/simple
- 增加分析设置接口

##  视图控制
### remove_display
删除当前所有显示，包括边界荷载钢束等全部显示
> 参数:  
Returns: 无
### save_png
保存当前模型窗口图形信息
> 参数:  
> file_path: 文件全路径  
Returns: 无
### set_render
消隐设置开关
> 参数:  
> flag: 默认设置打开消隐  
Returns: 无
### change_construct_stage
消隐设置开关
> 参数:  
> stage: 施工阶段名称或施工阶段号  0-基本  
Returns: 无
##  项目管理
### update_bim
刷新Bim模型信息
> 参数:  
Returns: 无
### update_model
刷新模型信息
> 参数:  
Returns: 无
### update_app_stage
切换模型前后处理状态
> 参数:  
> num: 1-前处理  2-后处理  
Returns: 无
### do_solve
运行分析
> 参数:  
Returns: 无
### initial
初始化模型,新建模型
> 参数:  
Returns: 无
### open_file
打开bfmd文件
> 参数:  
> file_path: 文件全路径  
Returns: 无
### close_project
关闭项目
> 参数:  
Returns: 无
### save_file
保存bfmd文件
> 参数:  
> file_path: 文件全路径  
Returns: 无
### import_command
导入命令
> 参数:  
> command:命令字符  
> command_type:命令类型 1-桥通命令 目前仅支持桥通命令  
Returns: 无
### import_file
导入文件
> 参数:  
> file_path:导入文件(.mct/.qdat/.dxf/.3dx)  
Returns: 无
### export_file
导入命令
> 参数:  
> file_path:导出文件全路径，支持格式(.mct/.qdat/.PGF/.3dx)  
Returns: 无
##  分析设置
### update_global_setting
更新整体设置
> 参数:  
> solver_type:求解器类型 0-稀疏矩阵求解器  1-变带宽求解器  
> calculation_type: 计算设置 0-单线程 1-用户自定义  2-自动设置  
> thread_count: 线程数  
Returns: 无
### update_construction_stage_setting
更新施工阶段设置
> 参数:  
> do_analysis: 是否进行分析  
> to_end_stage: 是否计算至最终阶段  
> other_stage_id: 计算至其他阶段时ID  
> analysis_type: 分析类型 (0-线性 1-非线性 2-部分非线性)  
> do_creep_analysis: 是否进行徐变分析  
> cable_tension_position: 索力张力位置 (0-I端 1-J端 2-平均索力)  
> consider_completion_stage: 是否考虑成桥内力对运营阶段影响  
> shrink_creep_type: 收缩徐变类型 (0-仅徐变 1-仅收缩 2-收缩徐变)  
> creep_load_type: 徐变荷载类型  (1-开始  2-中间  3-结束)  
> sub_step_info: 子步信息 [是否开启子部划分设置,10天步数,100天步数,1000天步数,5000天步数,10000天步数] None时为UI默认值  
Returns: 无
### update_non_linear_setting
更新非线性设置
> 参数:  
> non_linear_type: 非线性类型 0-部分非线性 1-非线性  
> non_linear_method: 非线性方法 0-修正牛顿法 1-牛顿法  
> max_loading_steps: 最大加载步数  
> max_iteration_times: 最大迭代次数  
> relative_accuracy_of_displacement: 位移相对精度  
> relative_accuracy_of_force: 内力相对精度  
Returns: 无
### update_operation_stage_setting
更新运营阶段分析设置
> 参数:  
> do_analysis: 是否进行运营阶段分析  
> final_stage: 最终阶段名  
> do_static_load_analysis: 是否进行静力工况分析  
> static_load_cases: 静力工况名列表  
> do_sink_analysis: 是否进行沉降工况分析  
> sink_cases: 沉降工况名列表  
> do_live_load_analysis: 是否进行活载工况分析  
> live_load_cases: 活载工况名列表  
> live_load_analytical_type: 移动荷载分析类型  
Returns: 无
##  节点单元操作
### add_nodes
添加多个节点，可以选择指定节点编号
> 参数:  
> node_list:节点坐标信息 [[x1,y1,z1],...]或 [[id1,x1,y1,z1]...]  
Returns: 无
### add_node
根据坐标信息和节点编号添加节点，默认自动识别编号
> 参数:  
> x: 节点坐标x  
> y: 节点坐标y  
> z: 节点坐标z  
> index: 节点编号，默认自动识别编号 (可选参数)  
Returns: 无
### update_node_id
根据坐标信息和节点编号添加节点，默认自动识别编号
> 参数:  
> node_id: 节点编号  
> new_id: 新节点编号  
Returns: 无
### merge_nodes
根据坐标信息和节点编号添加节点，默认自动识别编号
> 参数:  
> ids: 合并节点集合  默认全部节点  
> tolerance: 合并容许误差  
Returns: 无
### remove_node
删除指定节点,不输入参数时默认删除所有节点
> 参数:  
> ids:节点编号  
Returns: 无
### renumber_node
节点编号重拍
> 参数:  
Returns: 无
### move_node
移动节点坐标
> 参数:  
> node_id：节点号  
> offset_x:X轴偏移量  
> offset_y:Y轴偏移量  
> offset_z:Z轴偏移量  
Returns: 无
### add_structure_group
添加结构组
> 参数:  
> name: 结构组名  
> index: 结构组编号(非必须参数)，默认自动识别当前编号  
Returns: 无
### remove_structure_group
可根据结构与组名或结构组编号删除结构组，当组名和组编号均为默认则删除所有结构组
> 参数:  
> name:结构组名称  
> index:结构组编号  
Returns: 无
### add_structure_to_group
为结构组添加节点和/或单元
> 参数:  
> name: 结构组名  
> node_ids: 节点编号列表(可选参数)  
> element_ids: 单元编号列表(可选参数)  
Returns: 无
### remove_structure_in_group
为结构组删除节点和/或单元
> 参数:  
> name: 结构组名  
> node_ids: 节点编号列表(可选参数)  
> element_ids: 单元编号列表(可选参数)  
Returns: 无
### add_element
根据单元编号和单元类型添加单元
> 参数:  
> index:单元编号  
> ele_type:单元类型 1-梁 2-索 3-杆 4-板  
> node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]  
> beta_angle:贝塔角  
> mat_id:材料编号  
> sec_id:截面编号  
Returns: 无
### remove_element
删除指定编号的单元
> 参数:  
> index: 单元编号,默认时删除所有单元  
Returns: 无
##  材料操作
### add_material
添加材料
> 参数:  
> index:材料编号,默认自动识别 (可选参数)  
> name:材料名称  
> mat_type: 材料类型  
> standard:规范名称  
> database:数据库  
> construct_factor:构造系数  
> modified:是否修改默认材料参数,默认不修改 (可选参数)  
> data_info:材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (可选参数)  
> creep_id:徐变材料id (可选参数)  
> f_cuk: 立方体抗压强度标准值 (可选参数)  
Returns: 无
### add_time_material
添加收缩徐变材料
> 参数:  
> index: 指定收缩徐变编号,默认则自动识别 (可选参数)  
> name: 收缩徐变名  
> code_index: 收缩徐变规范索引  
> time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)  
Returns: 无
### update_material_creep
将收缩徐变参数连接到材料
> 参数:  
> index: 材料编号  
> creep_id: 收缩徐变编号  
> f_cuk: 材料标准抗压强度,仅自定义材料是需要输入  
Returns: 无
### remove_material
删除指定材料
> 参数:  
> index:指定材料编号，默认则删除所有材料  
Returns: 无
##  截面操作
### add_parameter_section
添加截面信息
> 参数:  
> index: 截面编号,默认自动识别  
> name:截面名称  
> sec_type:参数截面类型名称,支持以下类型  
> _"矩形", "圆形", "圆管", "箱型", "实腹八边形",_  
> _"空腹八边形", "内八角形", "实腹圆端型", "T形", "倒T形",_  
> _"I字形", "马蹄T形", "I字形混凝土", "混凝土箱梁", "带肋钢箱",_  
> _"带肋H截面", "钢桁箱梁1", "钢桁箱梁2", "钢桁箱梁3",_  
> _"钢工字型带肋", "钢管砼", "钢箱砼"_  
> sec_info:截面信息 (必要参数)  
> symmetry:混凝土截面是否对称 (仅混凝土箱梁截面需要)  
> charm_info:混凝土截面倒角信息 (仅混凝土箱梁截面需要)  
> sec_right:混凝土截面右半信息 (对称时可忽略，仅混凝土箱梁截面需要)  
> charm_right:混凝土截面右半倒角信息 (对称时可忽略，仅混凝土箱梁截面需要)  
> box_number: 混凝土箱室数 (仅混凝土箱梁截面需要)  
> box_height: 混凝土箱梁梁高 (仅混凝土箱梁截面需要)  
> mat_combine: 组合截面材料信息 (仅组合材料需要)  
> _[弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c]_  
> bias_type:偏心类型 默认中心  
> center_type:中心类型 默认质心  
> shear_consider:考虑剪切 bool 默认考虑剪切变形  
> bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要)  
> bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要)  
Returns: 无
### add_steel_section
添加钢梁截面,包括参数型钢梁截面和自定义带肋钢梁截面
> 参数:  
> index:  
> name:  
> sec_type:截面类型 1-工字钢梁  2-箱型钢梁  
> sec_info:截面信息  
> _工字钢梁[topDis,botDis,b1,b2,b3,b4,h,t1,t2,tw]_  
> _箱型钢梁[topDis,botDis,b1,b2,b3,b4,b5,b6,h,t1,t2,tw1,tw2]_  
> rib_info:肋板信息  
> rib_place:肋板位置 list[tuple[布置位置,具体位置,参考点位置,肋板间隔列表]]  
> _肋板间隔列表: list[tuple[间隔,肋板名，加劲肋位置,加劲肋名]]_  
> _布置位置: 0-上...  具体位置 0-桥面1..._  
> _参考点位置:0-左  加劲肋位置 0-上/左 1-下/右 2-两侧_  
> bias_type:偏心类型  
> center_type:中心类型  
> shear_consider:考虑剪切  
> bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要,相对形心)  
> bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要)  
Returns: 无
### add_user_section
添加自定义截面,目前仅支持特性截面
> 参数:  
> index:截面编号  
> name:截面名称  
> sec_type:截面类型  
> property_info:截面特性列表，共计25个参数  
> - [Area, AreaY, AreaZ, InertialX, InertialY, InertialZ, InertialYz,  
> Cyp, Cym, Czp, Czm, Peri0, PeriI, CentY, CentZ,  
> Y1, Z1, Y2, Z2, Y3, Z3, Y4, Z4, ShearCenterY, ShearCenterZ]  
> main_loop:主线圈坐标集合 [(-1,-1),(5,0),(5,5),(-1,5)] 目前只支持单一线圈  
> sub_loops:次线圈坐标集合 [[(0,0),(0,1),(1,1,)], [(2,2),(3,2),(3,3)]]  
> sec_lines:线宽集合[(x1,y1,x2,y3,thick),]  
Returns: 无
### add_tapper_section
添加变截面,需先建立单一截面
> 参数:  
> index:截面编号  
> name:截面名称  
> begin_id:截面始端编号  
> end_id:截面末端编号  
Returns: 无
### remove_section
删除截面信息
> 参数:  
> index: 截面编号,参数为默认时删除全部截面  
Returns: 无
##  板厚操作
### add_thickness
添加板厚
> 参数:  
> index: 板厚id  
> name: 板厚名称  
> t:   板厚度  
> thick_type: 板厚类型 0-普通板 1-加劲肋板  
> bias_info: 默认不偏心,偏心时输入列表[type,value]  
> _type:0-厚度比 1-数值_  
> rib_pos: 肋板位置 0-下部 1-上部  
> dist_v: 纵向截面肋板间距  
> dist_l: 横向截面肋板间距  
> rib_v: 纵向肋板信息  
> rib_l: 横向肋板信息  
Returns: 无
### remove_thickness
删除板厚
> 参数:  
> index:板厚编号,默认时删除所有板厚信息  
Returns: 无
### add_tapper_section_group
添加变截面组
> 参数:  
> ids:变截面组编号  
> name: 变截面组名  
> factor_w: 宽度方向变化阶数 线性(1.0) 非线性(!=1.0)  
> factor_h: 高度方向变化阶数 线性(1.0) 非线性(!=1.0)  
> ref_w: 宽度方向参考点 0-i 1-j  
> ref_h: 高度方向参考点 0-i 1-j  
> dis_w: 宽度方向距离  
> dis_h: 高度方向距离  
Returns: 无
### update_section_bias
更新截面偏心
> 参数:  
> index:截面编号  
> bias_type:偏心类型  
> center_type:中心类型  
> shear_consider:考虑剪切  
> bias_point:自定义偏心点(仅自定义类型偏心需要)  
Returns: 无
##  边界操作
### add_boundary_group
新建边界组
> 参数:  
> name:边界组名  
> index:边界组编号，默认自动识别当前编号 (可选参数)  
Returns: 无
### remove_boundary_group
按照名称删除边界组
> 参数:  
> name: 边界组名称，默认删除所有边界组 (非必须参数)  
Returns: 无
### remove_all_boundary
根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息
> 参数:  
Returns: 无
### remove_boundary
根据节点号删除一般支撑、弹性支承/根据单元号删除梁端约束/根据主节点号删除主从约束/根据从节点号删除约束方程
> 参数:  
> remove_id:节点号 or 单元号 or主节点号  or 从节点号  
> bd_type:边界类型  
> _1-一般支承 2-弹性支承 3-主从约束 4-弹性连接 5-约束方程 6-梁端约束_  
> group:边界所处边界组名  
Returns: 无
### add_general_support
添加一般支承
> 参数:  
> node_id:节点编号  
> boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]  ture-固定 false-自由  
> group_name:边界组名,默认为默认边界组  
Returns: 无
### add_elastic_support
添加弹性支承
> 参数:  
> node_id:节点编号  
> support_type:支承类型 1-线性  2-受拉  3-受压  
> boundary_info:边界信息 受拉和受压时列表长度为2-[direct(1-X 2-Y 3-Z),stiffness]  线性时列表长度为6-[kx,ky,kz,krx,kry,krz]  
> group_name:边界组  
Returns: 无
### add_elastic_link
添加弹性连接
> 参数:  
> link_type:节点类型 1-一般弹性连接 2-刚性连接 3-受拉弹性连接 4-受压弹性连接  
> start_id:起始节点号  
> end_id:终节点号  
> beta_angle:贝塔角  
> boundary_info:边界信息  
> group_name:边界组名  
> dis_ratio:距i端距离比 (仅一般弹性连接需要)  
> kx:受拉或受压刚度  
Returns: 无
### add_master_slave_link
添加主从约束
> 参数:  
> master_id:主节点号  
> slave_id:从节点号  
> boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由  
> group_name:边界组名  
Returns: 无
### add_node_axis
添加节点坐标
> 参数:  
> input_type:输入方式 1-角度 2-三点  3-向量  
> node_id:节点号  
> coord_info:局部坐标信息 -List<float>(角)  -List<List<float>>(三点 or 向量)  
Returns: 无
### add_beam_constraint
添加梁端约束
> 参数:  
> beam_id:梁号  
> info_i:i端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由  
> info_j:j端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由  
> group_name:边界组名  
Returns: 无
### add_constraint_equation
添加约束方程
> 参数:  
> name:约束方程名  
> sec_node:从节点号  
> sec_dof: 从节点自由度 1-x 2-y 3-z 4-rx 5-ry 6-rz  
> master_info:主节点约束信息列表  
> group_name:边界组名  
Returns: 无
##  移动荷载操作
### add_standard_vehicle
添加标准车辆
> 参数:  
> name: 车辆荷载名称  
> standard_code: 荷载规范  
> _1-中国铁路桥涵规范(Q/CR 9300-2017)_  
> _2-城市桥梁设计规范(CJJ11-2019)_  
> _3-公路工程技术标准(JTJ 001-97)_  
> _4-公路桥涵设计通规(JTG D60-2004)_  
> _5-公路桥涵设计通规(JTG D60-2015)_  
> _6-城市轨道交通桥梁规范(GB/T51234-2017)_  
> load_type: 荷载类型,支持类型如下  
> _"公路I级","公路II级","城A车道","城B车道"_  
> _"地铁A型车","地铁B型车","地铁C型车","汽10"_  
> _"汽15","汽20","汽超20","特载","挂80"_  
> _"挂100","挂120","公路疲劳荷载1","公路疲劳荷载2"_  
> _"公路疲劳荷载3","汽36轻", "汽38重","高速铁路"_  
> _"城际铁路","客货共线铁路","重载铁路","中活载","长大货物车检算荷载"_  
> load_length: 默认为0即不限制荷载长度  (铁路桥涵规范2017 所需参数)  
> n:车厢数: 默认6节车厢 (城市轨道交通桥梁规范2017 所需参数)  
Returns: 无
### add_node_tandem
添加节点纵列
> 参数:  
> name:节点纵列名  
> start_id:起始节点号  
> node_ids:节点列表  
Returns: 无
### add_influence_plane
添加影响面
> 参数:  
> name:影响面名称  
> tandem_names:节点纵列名称组  
Returns: 无
### add_lane_line
添加车道线
> 参数:  
> name:车道线名称  
> influence_name:影响面名称  
> tandem_name:节点纵列名  
> offset:偏移  
> lane_width:车道宽度  
Returns: 无
### add_live_load_case
添加移动荷载工况
> 参数:  
> name:荷载工况名  
> influence_plane:影响线名  
> span:跨度  
> car_detail: 汽车相关系数 (横向折减列表float[8],纵向折减系数,冲击强度)  
> train_detail: 火车相关系数 (横向折减列表float[8],纵向折减系数,强度冲击,疲劳冲击)  
> metro_detail: 轻轨相关系数 (横向折减列表float[8],纵向折减系数,冲击强度)  
> sub_case:子工况信息 [(车辆名称,系数,["车道1","车道2"])...]  
Returns: 无
### remove_vehicle
删除车辆信息
> 参数:  
> index:车辆荷载编号  
> name:车辆名称  
Returns: 无
### remove_node_tandem
按照 节点纵列编号/节点纵列名 删除节点纵列
> 参数:  
> index:节点纵列编号  
> name:节点纵列名  
Returns: 无
### remove_influence_plane
按照 影响面编号/影响面名称 删除影响面
> 参数:  
> index:影响面编号  
> name:影响面名称  
Returns: 无
### remove_lane_line
按照 车道线编号/车道线名称 删除车道线
> 参数:  
> name:车道线名称  
> index:车道线编号  
Returns: 无
### remove_live_load_case
删除移动荷载工况
> 参数:  
> name:移动荷载工况名  
Returns: 无
##  钢束操作
### add_tendon_group
按照名称添加钢束组，添加时可指定钢束组id
> 参数:  
> name: 钢束组名称  
> index: 钢束组编号(非必须参数)，默认自动识别  
Returns: 无
### remove_tendon_group
按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组
> 参数:  
> name:钢束组名称,默认自动识别 (可选参数)  
> index:钢束组编号,默认自动识别 (可选参数)  
Returns: 无
### add_tendon_property
添加钢束特性
> 参数:  
> name:钢束特性名  
> index:钢束编号,默认自动识别 (可选参数)  
> tendon_type: 0-PRE 1-POST  
> material_id: 钢材材料编号  
> duct_type: 1-金属波纹管  2-塑料波纹管  3-铁皮管  4-钢管  5-抽芯成型  
> steel_type: 1-钢绞线  2-螺纹钢筋  
> steel_detail: 钢束详细信息  
> _钢绞线[钢束面积,孔道直径,摩阻系数,偏差系数]_  
> _螺纹钢筋[钢筋直径,钢束面积,孔道直径,摩阻系数,偏差系数,张拉方式(1-一次张拉 2-超张拉)]_  
> loos_detail: 松弛信息[规范,张拉,松弛] (仅钢绞线需要,默认为[1,1,1])  
> _规范:1-公规 2-铁规_  
> _张拉方式:1-一次张拉 2-超张拉_  
> _松弛类型：1-一般松弛 2-低松弛_  
> slip_info: 滑移信息[始端距离,末端距离] 默认为[0.006, 0.006]  
Returns: 无
### add_tendon_3d
添加三维钢束
> 参数:  
> name:钢束名称  
> property_name:钢束特性名称  
> group_name:默认钢束组  
> num:根数  
> line_type:1-导线点  2-折线点  
> position_type: 定位方式 1-直线  2-轨迹线  
> control_points: 控制点信息[(x1,y1,z1,r1),(x2,y2,z2,r2)....]  
> point_insert: 定位方式  
> _直线: 插入点坐标[x,y,z]_  
> _轨迹线:  [插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id]_  
> tendon_direction:直线钢束X方向向量  默认为[1,0,0] (轨迹线不用赋值)  
> _x轴-[1,0,0] y轴-[0,1,0] z轴-[0,0,1]_  
> rotation_angle:绕钢束旋转角度  
> track_group:轨迹线结构组名  (直线时不用赋值)  
> projection:直线钢束投影 (默认为true)  
Returns: 无
### update_tendon_element
赋予钢束构件
> 参数:  
> ids: 钢束构件所在单元编号集合  
Returns: 无
### remove_tendon
按照名称或编号删除钢束,默认时删除所有钢束
> 参数:  
> name:钢束名称  
> index:钢束编号  
Returns: 无
### remove_tendon_property
按照名称或编号删除钢束组,默认时删除所有钢束组
> 参数:  
> name:钢束组名称  
> index:钢束组编号  
Returns: 无
##  荷载操作
### add_load_group
根据荷载组名称添加荷载组
> 参数:  
> name: 荷载组名称  
Returns: 无
### remove_load_group
根据荷载组名称或荷载组id删除荷载组,参数为默认时删除所有荷载组
> 参数:  
> name: 荷载组名称  
> index: 荷载组编号  
Returns: 无
### add_nodal_mass
添加节点质量
> 参数:  
> node_id:节点编号  
> mass_info:[m,rmX,rmY,rmZ]  
Returns: 无
### remove_nodal_mass
删除节点质量
> 参数:  
> node_id:节点号  
Returns: 无
### add_pre_stress
添加预应力
> 参数:  
> case_name:荷载工况名  
> tendon_name:钢束名  
> tension_type:预应力类型  
> _0-始端 1-末端 2-两端_  
> force:预应力  
> group_name:边界组  
Returns: 无
### remove_pre_stress
删除预应力
> 参数:  
> case_name:荷载工况  
> tendon_name:钢束组  
> group_name:边界组名  
Returns: 无
### add_nodal_force
添加节点荷载
> 参数:  
> node_id:节点编号  
> case_name:荷载工况名  
> load_info:荷载信息列表 [Fx,Fy,Fz,Mx,My,Mz]  
> group_name:荷载组名  
Returns: 无
### remove_nodal_force
删除节点荷载
> 参数:  
> case_name:荷载工况名  
> node_id:节点编号  
Returns: 无
### add_node_displacement
添加节点位移
> 参数:  
> node_id:节点编号  
> case_name:荷载工况名  
> load_info:节点位移列表 [Dx,Dy,Dz,Rx,Ry,Rz]  
> group_name:荷载组名  
Returns: 无
### remove_nodal_displacement
删除节点位移
> 参数:  
> node_id:节点编号  
> case_name:荷载工况名  
Returns: 无
### add_beam_load
添加梁单元荷载
> 参数:  
> beam_id:单元编号  
> case_name:荷载工况名  
> load_type:荷载类型  
> _ 1-集中力 2-集中弯矩 3-分布力 4-分布弯矩  
> coord_system:坐标系  
> _1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z_  
> is_abs: 荷载位置输入方式，True-绝对值   False-相对值  
> list_x:荷载位置信息 ,荷载距离单元I端的距离，可输入绝对距离或相对距离  
> list_load:荷载数值信息  
> group_name:荷载组名  
> load_bias:偏心荷载 (是否偏心,0-中心 1-偏心,偏心坐标系-int,偏心距离)  
> projected:荷载是否投影  
Returns: 无
### remove_beam_load
删除梁单元荷载
> 参数:  
> element_id:单元号  
> case_name:荷载工况名  
> load_type:荷载类型  
> _1-集中力   2-集中弯矩  3-分布力   4-分布弯矩_  
> group_name:边界组名  
Returns: 无
### add_initial_tension
添加初始拉力
> 参数:  
> element_id:单元编号  
> case_name:荷载工况名  
> tension:初始拉力  
> tension_type:张拉类型  0-增量 1-全量  
> group_name:荷载组名  
Returns: 无
### add_cable_length_load
添加索长张拉
> 参数:  
> element_id:单元类型  
> case_name:荷载工况名  
> length:长度  
> tension_type:张拉类型  0-增量 1-全量  
> group_name:荷载组名  
Returns: 无
### add_plate_element_load
添加版单元荷载
> 参数:  
> element_id:单元id  
> case_name:荷载工况名  
> load_type:荷载类型  
> _1-集中力  2-集中弯矩  3-分布力  4-分布弯矩_  
> load_place:荷载位置  
> _0-面IJKL 1-边IJ  2-边JK  3-边KL  4-边LI  (仅分布荷载需要)_  
> coord_system:坐标系  (默认3)  
> _1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z_  
> group_name:荷载组名  
> load_list:荷载列表  
> xy_list:荷载位置信息 [IJ方向绝对距离x,IL方向绝对距离y]  (仅集中荷载需要)  
Returns: 无
### add_deviation_parameter
添加制造误差
> 参数:  
> name:名称  
> element_type:单元类型  1-梁单元  2-板单元  
> parameters:参数列表  
> _梁杆单元:[轴向,I端X向转角,I端Y向转角,I端Z向转角,J端X向转角,J端Y向转角,J端Z向转角]_  
> _板单元:[X向位移,Y向位移,Z向位移,X向转角,Y向转角]_  
Returns: 无
### add_deviation_load
添加制造误差荷载
> 参数:  
> element_id:单元编号  
> case_name:荷载工况名  
> parameters:参数名列表  
> _梁杆单元时-[制造误差参数名称]_  
> _板单元时-[I端误差名,J端误差名,K端误差名,L端误差名]_  
> group_name:荷载组名  
Returns: 无
### add_element_temperature
添加单元温度
> 参数:  
> element_id:单元编号  
> case_name:荷载工况名  
> temperature:最终温度  
> group_name:荷载组名  
Returns: 无
### add_gradient_temperature
添加梯度温度
Returns: 无
### add_beam_section_temperature
添加梁截面温度
> 参数:  
> element_id:单元编号  
> case_name:荷载工况名  
> paving_thick:铺设厚度(m)  
> temperature_type:温度类型  1-升温(默认) 2-降温  
> paving_type:铺设类型  
> _1-沥青混凝土(默认)  2-水泥混凝土_  
> group_name:荷载组名  
> modify:是否修改规范温度  
> temp_list:温度列表[T1,T2]  (仅修改时需要)  
Returns: 无
### add_index_temperature
添加指数温度
> 参数:  
> element_id:单元编号  
> case_name:荷载工况名  
> temperature:温差  
> index:指数  
> group_name:荷载组名  
Returns: 无
### add_top_plate_temperature
添加顶板温度
> 参数:  
> element_id:单元编号  
> case_name:荷载  
> temperature:最终温度  
> group_name:荷载组名  
Returns: 无
##  沉降操作
### add_sink_group
添加沉降组
> 参数:  
> name: 沉降组名  
> sink: 沉降值  
> node_ids: 节点编号  
Returns: 无
### remove_sink_group
按照名称删除沉降组
> 参数:  
> name:沉降组名,默认删除所有沉降组  
Returns: 无
### add_sink_case
添加沉降工况
> 参数:  
> name:荷载工况名  
> sink_groups:沉降组名  
Returns: 无
### remove_sink_case
按照名称删除沉降工况,不输入名称时默认删除所有沉降工况
> 参数:  
> name:沉降工况名  
Returns: 无
### add_concurrent_reaction
添加并发反力组
> 参数:  
> names: 结构组名称集合  
Returns: 无
### remove_concurrent_reaction
删除所有并发反力组
> 参数:  
Returns: 无
### add_concurrent_force
创建并发内力组
> 参数:  
> names: 结构组名称集合  
Returns: 无
### remove_concurrent_force
删除所有并发内力组
> 参数:  
Returns: 无
### add_load_case
添加荷载工况
> 参数:  
> name:沉降名  
> case_type:荷载工况类型  
Returns: 无
### remove_load_case
删除荷载工况,参数均为默认时删除全部荷载工况
> 参数:  
> index:荷载编号  
> name:荷载名  
Returns: 无
##  施工阶段操作
### add_construction_stage
添加施工阶段信息
> 参数:  
> name:施工阶段信息  
> duration:时长  
> active_structures:激活结构组信息 [(结构组名,龄期,安装方法,计自重施工阶段id),...]  
> _计自重施工阶段id: 0-不计自重,1-本阶段 n-第n阶段)_  
> _安装方法：1-变形法 2-接线法 3-无应力法_  
> delete_structures:钝化结构组信息 [结构组1，结构组2,...]  
> active_boundaries:激活边界组信息 [(边界组1，位置),...]  
> _位置:  0-变形前 1-变形后_  
> delete_boundaries:钝化边界组信息 [边界组1，结构组2,...]  
> active_loads:激活荷载组信息 [(荷载组1,时间),...]  
> _时间: 0-开始 1-结束_  
> delete_loads:钝化荷载组信息 [(荷载组1,时间),...]  
> _时间: 0-开始 1-结束_  
> temp_loads:临时荷载信息 [荷载组1，荷载组2,..]  
> index:施工阶段编号，默认自动添加  
Returns: 无
### update_construction_stage
添加施工阶段信息
> 参数:  
> name:施工阶段信息  
> duration:时长  
> active_structures:激活结构组信息 [(结构组名,龄期,安装方法,计自重施工阶段id),...]  
> _计自重施工阶段id: 0-不计自重,1-本阶段 n-第n阶段)_  
> _安装方法：1-变形法 2-接线法 3-无应力法_  
> delete_structures:钝化结构组信息 [结构组1，结构组2,...]  
> active_boundaries:激活边界组信息 [(边界组1，位置),...]  
> _位置:  0-变形前 1-变形后_  
> delete_boundaries:钝化边界组信息 [边界组1，结构组2,...]  
> active_loads:激活荷载组信息 [(荷载组1,时间),...]  
> _时间: 0-开始 1-结束_  
> delete_loads:钝化荷载组信息 [(荷载组1,时间),...]  
> _时间: 0-开始 1-结束_  
> temp_loads:临时荷载信息 [荷载组1，荷载组2,..]  
Returns: 无
### update_weight_stage
添加施工阶段信息
> 参数:  
> stage_name:施工阶段信息  
> structure_group_name:结构组名  
> weight_stage_id: 计自重阶段号  
> _0-不计自重,1-本阶段 n-第n阶段_  
Returns: 无
### remove_construction_stage
按照施工阶段名删除施工阶段,默认删除所有施工阶段
> 参数:  
> name:所删除施工阶段名称  
Returns: 无
##  荷载组合操作
### add_load_combine
添加荷载组合
> 参数:  
> name:荷载组合名  
> combine_type:荷载组合类型 1-叠加  2-判别  3-包络  
> describe:描述  
> combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下  
> _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合_  
> _"MV"-移动荷载工况  "SM"-沉降荷载工况_  
Returns: 无
### update_load_combine
更新荷载组合
> 参数:  
> name:荷载组合名  
> combine_type:荷载组合类型 1-叠加  2-判别  3-包络  
> describe:描述  
> combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下  
> _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合_  
> _"MV"-移动荷载工况  "SM"-沉降荷载工况_  
Returns: 无
### remove_load_combine
删除荷载组合
> 参数:  
> name:指定删除荷载组合名，默认时则删除所有荷载组合  
Returns: 无


##  静力结果查看
### get_element_stress
获取单元应力,支持单个单元和单元列表
> 参数:  
> element_id: 单元编号  
> stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载  
> increment_type: 1-全量    2-增量  
> case_name: 运营阶段所需荷载工况名  
Returns: list[ElementStress] or ElementStress
### get_element_force
获取单元内力,支持单个单元和单元列表
> 参数:  
> element_id: 单元编号  
> stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载  
> increment_type: 1-全量    2-增量  
> case_name: 运营阶段所需荷载工况名  
Returns: list[ElementForce] or ElementForce
### get_reaction
获取节点,支持单个节点和节点列表
> 参数:  
> node_id: 节点编号  
> stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载  
> increment_type: 1-全量    2-增量  
> case_name: 运营阶段所需荷载工况名  
Returns: list[SupportReaction] or SupportReaction
### get_node_displacement
获取节点,支持单个节点和节点列表
> 参数:  
> node_id: 节点号  
> stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载  
> increment_type: 1-全量    2-增量  
> case_name: 运营阶段所需荷载工况名  
Returns: list[NodeDisplacement] or NodeDisplacement
##  绘制模型结果
### plot_reaction_result
保存结果图片到指定文件甲
> 参数:  
> file_path: 保存路径名  
> component: 分量编号 0-Fx 1-Fy 2-Fz 3-Fxyz 4-Mx 5-My 6-Mz 7-Mxyz  
> load_case_name: 详细荷载工况名，参考桥通结果输出，例如： CQ:成桥(合计)  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> show_number: 数值选项卡开启  
> show_legend: 图例选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> show_increment: 是否显示增量结果  
Returns: 无
### plot_displacement_result
保存结果图片到指定文件甲
> 参数:  
> file_path: 保存路径名  
> component: 分量编号 0-Dx 1-Dy 2-Dz 3-Rx 4-Ry 5-Rz 6-Dxy 7-Dyz 8-Dxz 9-Dxyz  
> load_case_name: 详细荷载工况名，参考桥通结果输出，例如： CQ:成桥(合计)  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> show_deformed: 变形选项卡开启  
> show_pre_deformed: 显示变形前  
> deformed_scale:变形比例  
> actual_deformed:是否显示实际变形  
> show_number: 数值选项卡开启  
> show_legend: 图例选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> show_increment: 是否显示增量结果  
Returns: 无
### plot_beam_element_force
绘制梁单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> component: 分量编号 0-Fx 1-Fy 2-Fz 3-Mx 4-My 5-Mz  
> load_case_name: 详细荷载工况名  
> stage_id: 阶段编号  
> envelope_type: 包络类型  
> show_line_chart: 是否显示线图  
> show_number: 是否显示数值  
> position: 位置编号  
> flip_plot: 是否翻转绘图  
> line_scale: 线的比例  
> show_deformed: 是否显示变形形状  
> show_pre_deformed: 是否显示未变形形状  
> deformed_actual: 是否显示实际变形  
> deformed_scale: 变形比例  
> show_legend: 是否显示图例  
> text_rotation: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_exponential: 是否以指数形式显示  
> max_min_kind: 最大最小值显示类型  
> show_increment: 是否显示增量结果  
Returns: 无
### plot_truss_element_force
绘制杆单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> load_case_name: 详细荷载工况名  
> stage_id: 阶段编号  
> envelope_type: 包络类型  
> show_line_chart: 是否显示线图  
> show_number: 是否显示数值  
> position: 位置编号  
> flip_plot: 是否翻转绘图  
> line_scale: 线的比例  
> show_deformed: 是否显示变形形状  
> show_pre_deformed: 是否显示未变形形状  
> deformed_actual: 是否显示实际变形  
> deformed_scale: 变形比例  
> show_legend: 是否显示图例  
> text_rotation_angle: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_as_exponential: 是否以指数形式显示  
> max_min_kind: 最大最小值显示类型  
> show_increment:是否显示增量结果  
Returns: 无
### plot_plate_element_force
绘制板单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> component: 分量编号 0-Fxx 1-Fyy 2-Fxy 3-Mxx 4-Myy 5-Mxy  
> force_kind: 力类型  
> load_case_name: 详细荷载工况名  
> stage_id: 阶段编号  
> envelope_type: 包络类型  
> show_number: 是否显示数值  
> show_deformed: 是否显示变形形状  
> show_pre_deformed: 是否显示未变形形状  
> deformed_actual: 是否显示实际变形  
> deformed_scale: 变形比例  
> show_legend: 是否显示图例  
> text_rotation_angle: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_as_exponential: 是否以指数形式显示  
> max_min_kind: 最大最小值显示类型  
> show_increment: 是否显示增量结果  
Returns: 无
##  获取模型信息
### get_section_data
获取截面详细信息，截面特性详见UI自定义特性截面
> 参数:  
> sec_id: 目标截面编号  
Returns: dict
### get_section_ids
获取模型所有截面号
> 参数:  
Returns: list[int]
### get_node_id
获取节点编号，为-1时则表示未找到该坐标节点
> 参数:  
> x: 目标点X轴坐标  
> y: 目标点Y轴坐标  
> z: 目标点Z轴坐标  
> tolerance: 距离容许误差  
Returns: int
### get_group_elements
获取结构组单元编号
> 参数:  
> group_name: 结构组名  
Returns: list[int]
### get_group_nodes
获取结构组节点编号
> 参数:  
> group_name: 结构组名  
Returns: list[int]
### get_node_data
获取节点信息 默认获取所有节点信息
> 参数:  
Returns: list[Node] 或 Node
### get_element_data
获取单元信息
> 参数:  
Returns: list[Element]
### get_element_type
获取单元类型
> 参数:  
> ele_id: 单元号  
Returns: str类型 返回 BEAM PLATE CABLE LINK
### get_beam_element
获取梁单元信息
> 参数:  
> ids: 梁单元号，默认时获取所有梁单元  
Returns: list[Element]
### get_plate_element
获取板单元信息
> 参数:  
> ids: 板单元号，默认时获取所有板单元  
Returns: list[Element]
### get_cable_element
获取索单元信息
> 参数:  
> ids: 索单元号，默认时获取所有索单元  
Returns: list[Element]
### get_link_element
获取杆单元信息
> 参数:  
> ids: 杆单元号，默认时输出全部杆单元  
Returns: list[Element]
### get_material_data
获取材料信息
> 参数:  
> ids: 材料号，默认时输出全部材料  
Returns: list[Material]
### get_concrete_material
获取混凝土材料信息
> 参数:  
> ids: 材料号，默认时输出全部材料  
Returns: list[Material]
### get_steel_plate_material
获取钢材材料信息
> 参数:  
> ids: 材料号，默认时输出全部材料  
Returns: list[Material]
### get_pre_stress_bar_material
获取钢材材料信息
> 参数:  
> ids: 材料号，默认时输出全部材料  
Returns: list[Material]
### get_steel_bar_material
获取钢筋材料信息
> 参数:  
> ids: 材料号，默认时输出全部材料  
Returns: list[Material]
### get_user_###ine_material
获取自定义材料信息
> 参数:  
> ids: 材料号，默认时输出全部材料  
Returns: list[Material]
##  获取模型边界信息
### get_boundary_group_names
获取自边界组名称
> 参数:  
Returns: list[str]
### get_general_support_data
获取一般支承信息
> 参数:  
> group_name:默认输出所有边界组信息  
Returns: list[GeneralSupport]
### get_elastic_link_data
获取弹性连接信息
> 参数:  
> group_name:默认输出所有边界组信息  
Returns: list[ElasticLink]
### get_elastic_support_data
获取弹性支承信息
> 参数:  
> group_name:默认输出所有边界组信息  
Returns: list[ElasticSupport]
### get_master_slave_link_data
获取主从连接信息
> 参数:  
> group_name:默认输出所有边界组信息  
Returns: list[MasterSlaveLink]
### get_node_local_axis_data
获取节点坐标信息
> 参数:  
Returns: list[NodalLocalAxis]
### get_beam_constraint_data
获取节点坐标信息
> 参数:  
> group_name:默认输出所有边界组信息  
Returns: list[BeamConstraint]
### get_constraint_equation_data
获取约束方程信息
> 参数:  
> group_name:默认输出所有边界组信息  
Returns: list[ConstraintEquation]
##  获取施工阶段信息
### get_elements_of_stage
获取指定施工阶段单元编号信息
> 参数:  
> stage_id: 施工阶段编号  
Returns: list[int]
### get_nodes_of_stage
获取指定施工阶段节点编号信息
> 参数:  
> stage_id: 施工阶段编号  
Returns: list[int]
### get_groups_of_stage
获取施工阶段结构组、边界组、荷载组名集合
> 参数:  
> stage_id: 施工阶段编号  
Returns: dict
##  荷载信息
### get_load_case_names
获取荷载工况名
> 参数:  
Returns: list[str]
### get_pre_stress_load
获取预应力荷载
> 参数:  
> case_name: 荷载工况名  
Returns: list[PreStressLoad]
### get_node_mass_data
获取节点质量
> 参数:  
Returns: list[NodalMass]
### get_nodal_force_load
获取节点力荷载
> 参数:  
> case_name: 荷载工况名  
Returns: list[NodalForce]
### get_nodal_displacement_load
获取节点位移荷载
> 参数:  
> case_name: 荷载工况名  
Returns: list[NodalForceDisplacement]
### get_beam_element_load
获取梁单元荷载
> 参数:  
> case_name: 荷载工况名  
Returns: list[BeamElementLoad]
### get_plate_element_load
获取梁单元荷载
> 参数:  
> case_name: 荷载工况名  
Returns: list[BeamElementLoad]
### get_initial_tension_load
获取初拉力荷载数据
> 参数:  
> case_name: 荷载工况名  
Returns: list[InitialTension]
### get_cable_length_load
获取初拉力荷载数据
> 参数:  
> case_name: 荷载工况名  
Returns: list[CableLengthLoad]
### get_deviation_parameter
获取制造偏差参数
> 参数:  
Returns: list[DeviationParameter]
### get_deviation_load
获取制造偏差荷载
> 参数:  
> case_name:荷载工况名  
Returns: list[DeviationLoad]

