# 最新版本 V0.5.54 - 2025-01-03 
> pip install --upgrade qtmodel -i https://pypi.org/simple
- 修改部分接口 
##  项目管理
### update_bim
刷新Bim模型信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.update_bim()
```  
Returns: 无
### update_model
刷新模型信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.update_model()
```  
Returns: 无
### update_app_stage
切换模型前后处理状态
> 参数:  
> num: 1-前处理  2-后处理  
```Python
# 示例代码
from qtmodel import *
mdb.update_app_stage(num=1)
mdb.update_app_stage(num=2)
```  
Returns: 无
### do_solve
运行分析
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.do_solve()
```  
Returns: 无
### initial
初始化模型,新建模型
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.initial()
```  
Returns: 无
### open_file
打开bfmd文件
> 参数:  
> file_path: 文件全路径  
```Python
# 示例代码
from qtmodel import *
mdb.open_file(file_path="a.bfmd")
```  
Returns: 无
### close_project
关闭项目
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.close_project()
```  
Returns: 无
### save_file
保存bfmd文件
> 参数:  
> file_path: 文件全路径  
```Python
# 示例代码
from qtmodel import *
mdb.save_file(file_path="a.bfmd")
```  
Returns: 无
### import_command
导入命令
> 参数:  
> command:命令字符  
> command_type:命令类型,默认桥通命令 1-桥通命令 2-mct命令  
```Python
# 示例代码
from qtmodel import *
mdb.import_command(command="*SECTION")
mdb.import_command(command="*SECTION",command_type=2)
```  
Returns: 无
### import_file
导入文件
> 参数:  
> file_path:导入文件(.mct/.qdat/.dxf/.3dx)  
```Python
# 示例代码
from qtmodel import *
mdb.import_file(file_path="a.mct")
```  
Returns: 无
### export_file
导入命令
> 参数:  
> file_path:导出文件全路径，支持格式(.mct/.qdat/.obj/.txt/.py)  
> convert_sec_group:是否将变截面组转换为变截面  
> type_kind:输出文件类型  1-全部模型文件  2-计算相关文件 (py输出时  2-输出截面特性)  
> group_name:obj与 APDL导出时指定结构组导出  
```Python
# 示例代码
from qtmodel import *
mdb.export_file(file_path="a.mct")
```  
Returns: 无
##  分析设置
### update_global_setting
更新整体设置
> 参数:  
> solver_type:求解器类型 0-稀疏矩阵求解器  1-变带宽求解器  
> calculation_type: 计算设置 0-单线程 1-用户自定义  2-自动设置  
> thread_count: 线程数  
```Python
# 示例代码
from qtmodel import *
mdb.update_global_setting(solver_type=0,calculation_type=2,thread_count=12)
```  
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
```Python
# 示例代码
from qtmodel import *
mdb.update_construction_stage_setting(do_analysis=True, to_end_stage=False, other_stage_id=1,analysis_type=0,
do_creep_analysis=True, cable_tension_position=0, consider_completion_stage=True,shrink_creep_type=2)
```  
Returns: 无
### update_live_load_setting
更新移动荷载分析设置
> 参数:  
> lateral_spacing: 横向加密间距  
> vertical_spacing: 纵向加密间距  
> damper_calc_type: 模拟阻尼器约束方程计算类选项(-1-不考虑 0-全部组 1-部分)  
> displacement_calc_type: 位移计算选项(-1-不考虑 0-全部组 1-部分)  
> force_calc_type: 内力计算选项(-1-不考虑 0-全部组 1-部分)  
> reaction_calc_type: 反力计算选项(-1-不考虑 0-全部组 1-部分)  
> link_calc_type: 连接计算选项(-1-不考虑 0-全部组 1-部分)  
> constrain_calc_type: 约束方程计算选项(-1-不考虑 0-全部组 1-部分)  
> eccentricity: 离心力系数  
> displacement_track: 是否追踪位移  
> force_track: 是否追踪内力  
> reaction_track: 是否追踪反力  
> link_track: 是否追踪连接  
> constrain_track: 是否追踪约束方程  
> damper_groups: 模拟阻尼器约束方程计算类选项为组时边界组名称  
> displacement_groups: 位移计算类选项为组时结构组名称  
> force_groups: 内力计算类选项为组时结构组名称  
> reaction_groups: 反力计算类选项为组时边界组名称  
> link_groups:  弹性连接计算类选项为组时边界组名称  
> constrain_groups: 约束方程计算类选项为组时边界组名称  
```Python
# 示例代码
from qtmodel import *
mdb.update_live_load_setting(lateral_spacing=0.1, vertical_spacing=1, displacement_calc_type=1)
mdb.update_live_load_setting(lateral_spacing=0.1, vertical_spacing=1, displacement_calc_type=2,displacement_track=True,
displacement_groups=["结构组1","结构组2"])
```  
Returns: 无
### update_non_linear_setting
更新非线性设置
> 参数:  
> non_linear_type: 非线性类型 0-部分非线性 1-非线性  
> non_linear_method: 非线性方法 0-修正牛顿法 1-牛顿法  
> max_loading_steps: 最大加载步数  
> max_iteration_times: 最大迭代次数  
> accuracy_of_displacement: 位移相对精度  
> accuracy_of_force: 内力相对精度  
```Python
# 示例代码
from qtmodel import *
mdb.update_non_linear_setting(non_linear_type=-1, non_linear_method=1, max_loading_steps=-1, max_iteration_times=30,
accuracy_of_displacement=0.0001, accuracy_of_force=0.0001)
```  
Returns: 无
### update_operation_stage_setting
更新运营阶段分析设置
> 参数:  
> do_analysis: 是否进行运营阶段分析  
> final_stage: 最终阶段名  
> static_load_cases: 静力工况名列表  
> sink_load_cases: 沉降工况名列表  
> live_load_cases: 活载工况名列表  
```Python
# 示例代码
from qtmodel import *
mdb.update_operation_stage_setting(do_analysis=True, final_stage="上二恒",static_load_cases=None)
```  
Returns: 无
### update_self_vibration_setting
更新自振分析设置
> 参数:  
> do_analysis: 是否进行运营阶段分析  
> method: 计算方法 1-子空间迭代法 2-滤频法  3-多重Ritz法  4-兰索斯法  
> matrix_type: 矩阵类型 0-集中质量矩阵  1-一致质量矩阵  
> mode_num: 振型数量  
```Python
# 示例代码
from qtmodel import *
mdb.update_self_vibration_setting(do_analysis=True,method=1,matrix_type=0,mode_num=3)
```  
Returns: 无
### update_response_spectrum_setting
更新反应谱设置
> 参数:  
> do_analysis:是否进行反应谱分析  
> kind:组合方式 1-SRSS 2-CQC  
> by_mode: 是否按照振型输入阻尼比  
> damping_ratio:常数阻尼比或振型阻尼比列表  
```Python
# 示例代码
from qtmodel import *
mdb.update_response_spectrum_setting(do_analysis=True,kind=1,damping_ratio=0.05)
```  
Returns: 无
##  节点操作
### add_node
根据坐标信息和节点编号添加节点
> 参数:  
> node_data: [id,x,y,z]  或 [x,y,z] 指定节点编号时不进行交叉分割、合并、编号等操作  
> intersected: 是否交叉分割  
> is_merged: 是否忽略位置重复节点  
> merge_error: 合并容许误差  
> numbering_type:编号方式 0-未使用的最小号码 1-最大号码加1 2-用户定义号码  
> start_id:自定义节点起始编号(用户定义号码时使用)  
```Python
# 示例代码
from qtmodel import *
mdb.add_node(node_data=[1,2,3])
mdb.add_node(node_data=[1,1,2,3])
```  
Returns: 无
### add_nodes
根据坐标信息和节点编号添加一组节点，可指定节点号，或不指定节点号
> 参数:  
> node_data: [[id,x,y,z]...]  或[[x,y,z]...]  指定节点编号时不进行交叉分割、合并、编号等操作  
> intersected: 是否交叉分割  
> is_merged: 是否忽略位置重复节点  
> merge_error: 合并容许误差  
> numbering_type:编号方式 0-未使用的最小号码 1-最大号码加1 2-用户定义号码  
> start_id:自定义节点起始编号(用户定义号码时使用)  
```Python
# 示例代码
from qtmodel import *
mdb.add_nodes(node_data=[[1,1,2,3],[1,1,2,3]])
```  
Returns: 无
### update_node
根据节点号修改节点坐标
> 参数:  
> node_id: 旧节点编号  
> new_id: 新节点编号,默认为-1时不改变节点编号  
> x: 更新后x坐标  
> y: 更新后y坐标  
> z: 更新后z坐标  
```Python
# 示例代码
from qtmodel import *
mdb.update_node(node_id=1,new_id=2,x=2,y=2,z=2)
```  
Returns: 无
### update_node_id
修改节点Id
> 参数:  
> node_id: 节点编号  
> new_id: 新节点编号  
```Python
# 示例代码
from qtmodel import *
mdb.update_node_id(node_id=1,new_id=2)
```  
Returns: 无
### merge_nodes
根据坐标信息和节点编号添加节点，默认自动识别编号
> 参数:  
> ids: 合并节点集合  默认全部节点  
> tolerance: 合并容许误差  
```Python
# 示例代码
from qtmodel import *
mdb.merge_nodes()
```  
Returns: 无
### remove_node
删除指定节点,不输入参数时默认删除所有节点
> 参数:  
> ids:节点编号  
```Python
# 示例代码
from qtmodel import *
mdb.remove_node()
mdb.remove_node(ids=1)
mdb.remove_node(ids=[1,2,3])
```  
Returns: 无
### renumber_node
节点编号重拍
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.renumber_node()
```  
Returns: 无
### move_node
移动节点坐标
> 参数:  
> node_id:节点号  
> offset_x:X轴偏移量  
> offset_y:Y轴偏移量  
> offset_z:Z轴偏移量  
```Python
# 示例代码
from qtmodel import *
mdb.move_node(node_id=1,offset_x=1.5,offset_y=1.5,offset_z=1.5)
```  
Returns: 无
### add_structure_group
添加结构组
> 参数:  
> name: 结构组名  
> index: 结构组编号(非必须参数)，默认自动识别当前编号  
> node_ids: 节点编号列表(可选参数)  
> element_ids: 单元编号列表(可选参数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_structure_group(name="新建结构组1")
mdb.add_structure_group(name="新建结构组2",node_ids=[1,2,3,4],element_ids=[1,2])
```  
Returns: 无
### remove_structure_group
可根据结构与组名删除结构组，当组名为默认则删除所有结构组
> 参数:  
> name:结构组名称  
```Python
# 示例代码
from qtmodel import *
mdb.remove_structure_group(name="新建结构组1")
mdb.remove_structure_group()
```  
Returns: 无
### add_structure_to_group
为结构组添加节点和/或单元
> 参数:  
> name: 结构组名  
> node_ids: 节点编号列表(可选参数)  
> element_ids: 单元编号列表(可选参数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_structure_to_group(name="现有结构组1",node_ids=[1,2,3,4],element_ids=[1,2])
```  
Returns: 无
### remove_structure_in_group
为结构组删除节点和/或单元
> 参数:  
> name: 结构组名  
> node_ids: 节点编号列表(可选参数)  
> element_ids: 单元编号列表(可选参数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_structure_to_group(name="现有结构组1",node_ids=[1,2,3,4],element_ids=[1,2])
```  
Returns: 无
##  单元操作
### update_local_orientation
反转杆系单元局部方向
> 参数:  
> ele_id: 杆系单元编号  
```Python
# 示例代码
from qtmodel import *
mdb.update_local_orientation(1)
```  
Returns: 无
### update_element_id
更改单元编号
> 参数:  
> old_id: 单元编号  
> new_id: 新单元编号  
```Python
# 示例代码
from qtmodel import *
mdb.update_element_id(1,2)
```  
Returns: 无
### add_element
根据单元编号和单元类型添加单元
> 参数:  
> index:单元编号  
> ele_type:单元类型 1-梁 2-杆 3-索 4-板  
> node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]  
> beta_angle:贝塔角  
> mat_id:材料编号  
> sec_id:截面编号  
> initial_type:索单元初始参数类型 1-初始拉力 2-初始水平力 3-无应力长度  
> initial_value:索单元初始始参数值  
> plate_type:板单元类型  0-薄板 1-厚板  
```Python
# 示例代码
from qtmodel import *
mdb.add_element(index=1,ele_type=1,node_ids=[1,2],beta_angle=1,mat_id=1,sec_id=1)
```  
Returns: 无
### update_element
根据单元编号和单元类型添加单元
> 参数:  
> old_id:原单元编号  
> new_id:现单元编号，默认不修改原单元Id  
> ele_type:单元类型 1-梁 2-杆 3-索 4-板  
> node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]  
> beta_angle:贝塔角  
> mat_id:材料编号  
> sec_id:截面编号  
> initial_type:索单元初始参数类型 1-初始拉力 2-初始水平力 3-无应力长度  
> initial_value:索单元初始始参数值  
> plate_type:板单元类型  0-薄板 1-厚板  
```Python
# 示例代码
from qtmodel import *
mdb.update_element(old_id=1,ele_type=1,node_ids=[1,2],beta_angle=1,mat_id=1,sec_id=1)
```  
Returns: 无
### add_elements
根据单元编号和单元类型添加单元
> 参数:  
> ele_data:单元信息  
> [编号,类型(1-梁 2-杆),materialId,sectionId,betaAngle,nodeI,nodeJ]  
> [编号,类型(3-索),materialId,sectionId,betaAngle,nodeI,nodeJ,张拉类型(1-初拉力 2-初始水平力 3-无应力长度),张拉值]  
> [编号,类型(4-板),materialId,thicknessId,betaAngle,nodeI,nodeJ,nodeK,nodeL]  
```Python
# 示例代码
from qtmodel import *
mdb.add_elements(ele_data=[
[1,1,1,1,0,1,2],
[2,2,1,1,0,1,2],
[3,3,1,1,0,1,2,1,100],
[4,4,1,1,0,1,2,3,4]])
```  
Returns: 无
### update_element_local_orientation
更新指定单元的单元局部坐标系
> 参数:  
> index: 单元编号  
```Python
# 示例代码
from qtmodel import *
mdb.update_element_local_orientation(index=1)
```  
Returns: 无
### update_element_material
更新指定单元的材料号
> 参数:  
> index: 单元编号  
> mat_id: 材料编号  
```Python
# 示例代码
from qtmodel import *
mdb.update_element_material(index=1,mat_id=2)
```  
Returns: 无
### update_element_beta_angle
更新指定单元的贝塔角
> 参数:  
> index: 单元编号  
> beta_angle: 贝塔角度数  
```Python
# 示例代码
from qtmodel import *
mdb.update_element_beta_angle(index=1,beta_angle=90)
```  
Returns: 无
### update_element_section
更新杆系单元截面或板单元板厚
> 参数:  
> index: 单元编号  
> sec_id: 截面号  
```Python
# 示例代码
from qtmodel import *
mdb.update_element_section(index=1,sec_id=2)
```  
Returns: 无
### update_element_node
更新单元节点
> 参数:  
> index: 单元编号  
> nodes: 杆系单元时为[node_i,node_j] 板单元[i,j,k,l]  
```Python
# 示例代码
from qtmodel import *
mdb.update_element_node(1,[1,2])
mdb.update_element_node(2,[1,2,3,4])
```  
Returns: 无
### remove_element
删除指定编号的单元
> 参数:  
> index: 单元编号,默认时删除所有单元  
```Python
# 示例代码
from qtmodel import *
mdb.remove_element()
mdb.remove_element(index=1)
```  
Returns: 无
##  材料操作
### update_material
添加材料
> 参数:  
> name:旧材料名称  
> new_name:新材料名称,默认不更改名称  
> new_id:新材料Id,默认不更改Id  
> mat_type: 材料类型,1-混凝土 2-钢材 3-预应力 4-钢筋 5-自定义 6-组合材料  
> standard:规范序号,参考UI 默认从1开始  
> database:数据库名称  
> construct_factor:构造系数  
> modified:是否修改默认材料参数,默认不修改 (可选参数)  
> data_info:材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (可选参数)  
> creep_id:徐变材料id (可选参数)  
> f_cuk: 立方体抗压强度标准值 (可选参数)  
> composite_info: 主材名和辅材名 (仅组合材料需要)  
```Python
# 示例代码
from qtmodel import *
mdb.update_material(name="混凝土材料1",mat_type=1,standard=1,database="C50")
mdb.update_material(name="自定义材料1",mat_type=5,data_info=[3.5e10,2.5e4,0.2,1.5e-5])
```  
Returns: 无
### add_material
添加材料
> 参数:  
> index:材料编号,默认为最大Id+1  
> name:材料名称  
> mat_type: 材料类型,1-混凝土 2-钢材 3-预应力 4-钢筋 5-自定义 6-组合材料  
> standard:规范序号,参考UI 默认从1开始  
> database:数据库名称  
> construct_factor:构造系数  
> modified:是否修改默认材料参数,默认不修改 (可选参数)  
> data_info:材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (可选参数)  
> creep_id:徐变材料id (可选参数)  
> f_cuk: 立方体抗压强度标准值 (可选参数)  
> composite_info: 主材名和辅材名 (仅组合材料需要)  
```Python
# 示例代码
from qtmodel import *
mdb.add_material(index=1,name="混凝土材料1",mat_type=1,standard=1,database="C50")
mdb.add_material(index=1,name="自定义材料1",mat_type=5,data_info=[3.5e10,2.5e4,0.2,1.5e-5])
```  
Returns: 无
### add_time_parameter
添加收缩徐变材料
> 参数:  
> name: 收缩徐变名  
> code_index: 收缩徐变规范索引  
> time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)  
> creep_data: 徐变数据 [(函数名,龄期)...]  
> shrink_data: 收缩函数名  
```Python
# 示例代码
from qtmodel import *
mdb.add_time_parameter(name="收缩徐变材料1",code_index=1)
```  
Returns: 无
### update_time_parameter
添加收缩徐变材料
> 参数:  
> name: 收缩徐变名  
> new_name: 新收缩徐变名,默认不改变名称  
> code_index: 收缩徐变规范索引  
> time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)  
> creep_data: 徐变数据 [(函数名,龄期)...]  
> shrink_data: 收缩函数名  
```Python
# 示例代码
from qtmodel import *
mdb.update_time_parameter(name="收缩徐变材料1",new_name="新收缩徐变材料1",code_index=1)
```  
Returns: 无
### add_creep_function
添加徐变函数
> 参数:  
> name:徐变函数名  
> creep_data:徐变数据[(时间,徐变系数)...]  
> scale_factor:缩放系数  
```Python
# 示例代码
from qtmodel import *
mdb.add_creep_function(name="徐变函数名",creep_data=[(5,0.5),(100,0.75)])
```  
Returns: 无
### update_creep_function
添加徐变函数
> 参数:  
> name:徐变函数名  
> new_name: 新徐变函数名，默认不改变函数名  
> creep_data:徐变数据，默认不改变函数名 [(时间,徐变系数)...]  
> scale_factor:缩放系数  
```Python
# 示例代码
from qtmodel import *
mdb.add_creep_function(name="徐变函数名",creep_data=[(5,0.5),(100,0.75)])
```  
Returns: 无
### add_shrink_function
添加收缩函数
> 参数:  
> name:收缩函数名  
> shrink_data:收缩数据[(时间,收缩系数)...]  
> scale_factor:缩放系数  
```Python
# 示例代码
from qtmodel import *
mdb.add_shrink_function(name="收缩函数名",shrink_data=[(5,0.5),(100,0.75)])
mdb.add_shrink_function(name="收缩函数名",scale_factor=1.2)
```  
Returns: 无
### update_shrink_function
添加收缩函数
> 参数:  
> name:收缩函数名  
> new_name:收缩函数名  
> shrink_data:收缩数据,默认不改变数据 [(时间,收缩系数)...]  
> scale_factor:缩放系数  
```Python
# 示例代码
from qtmodel import *
mdb.update_shrink_function(name="收缩函数名",new_name="函数名2")
mdb.update_shrink_function(name="收缩函数名",shrink_data=[(5,0.5),(100,0.75)])
mdb.update_shrink_function(name="收缩函数名",scale_factor=1.2)
```  
Returns: 无
### remove_shrink_function
删除收缩函数
> 参数:  
> name:收缩函数名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_shrink_function(name="收缩函数名")
```  
Returns: 无
### remove_creep_function
删除徐变函数
> 参数:  
> name:徐变函数名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_creep_function(name="徐变函数名")
```  
Returns: 无
### update_material_time_parameter
将收缩徐变参数连接到材料
> 参数:  
> name: 材料名  
> time_parameter_name: 收缩徐变名称  
> f_cuk: 材料标准抗压强度,仅自定义材料是需要输入  
```Python
# 示例代码
from qtmodel import *
mdb.update_material_time_parameter(name="C60",time_parameter_name="收缩徐变1",f_cuk=5e7)
```  
Returns: 无
### update_material_id
更新材料编号
> 参数:  
> name:材料名称  
> new_id:新编号  
```Python
# 示例代码
from qtmodel import *
mdb.update_material_id(name="材料1",new_id=2)
```  
Returns: 无
### remove_material
删除指定材料
> 参数:  
> index:指定材料编号，默认则删除所有材料  
> name: 指定材料名，材料名为空时按照index删除  
```Python
# 示例代码
from qtmodel import *
mdb.remove_material()
mdb.remove_material(index=1)
```  
Returns: 无
### update_material_construction_factor
更新材料构造系数
> 参数:  
> name:指定材料编号，默认则删除所有材料  
> factor:指定材料编号，默认则删除所有材料  
```Python
# 示例代码
from qtmodel import *
mdb.update_material_construction_factor(name="材料1",factor=1.0)
```  
Returns: 无
### remove_time_parameter
删除指定时间依存材料
> 参数:  
> name: 指定收缩徐变材料名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_time_parameter("收缩徐变材料1")
```  
Returns: 无
##  截面板厚操作
### add_section
添加单一截面信息,如果截面存在则自动覆盖
> 参数:  
> index: 截面编号,默认自动识别  
> name:截面名称  
> sec_type:参数截面类型名称(详见UI界面)  
> sec_info:截面信息 (必要参数)  
> symmetry:混凝土截面是否对称 (仅混凝土箱梁截面需要)  
> charm_info:混凝土截面倒角信息 (仅混凝土箱梁截面需要)  
> sec_right:混凝土截面右半信息 (对称时可忽略，仅混凝土箱梁截面需要)  
> charm_right:混凝土截面右半倒角信息 (对称时可忽略，仅混凝土箱梁截面需要)  
> box_num: 混凝土箱室数 (仅混凝土箱梁截面需要)  
> box_height: 混凝土箱梁梁高 (仅混凝土箱梁截面需要)  
> mat_combine: 组合截面材料信息 (仅组合材料需要) [弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c]  
> rib_info:肋板信息  
> rib_place:肋板位置 list[tuple[布置具体部位,参考点0-下/左,距参考点间距,肋板名，加劲肋位置0-上/左 1-下/右 2-两侧,加劲肋名]]  
> 布置具体部位(工字钢梁):1-上左 2-上右 3-腹板 4-下左 5-下右  
> 布置具体部位(箱型钢梁):1-上左 2-上中 3-上右 4-左腹板 5-右腹板 6-下左 7-下中 8-下右  
> sec_info:截面特性列表，共计26个参数参考UI截面  
> loop_segments:线圈坐标集合 list[dict] dict示例:{"main":[(x1,y1),(x2,y2)...],"sub1":[(x1,y1),(x2,y2)...],"sub2":[(x1,y1),(x2,y2)...]}  
> sec_lines:线宽集合[(x1,y1,x2,y3,thick),]  
> secondary_loop_segments:辅材线圈坐标集合 list[dict] (同loop_segments)  
> sec_property:截面特性(参考UI界面共计26个参数)，可选参数，指定截面特性时不进行截面计算  
> bias_type:偏心类型 默认中心  
> center_type:中心类型 默认质心  
> shear_consider:考虑剪切 bool 默认考虑剪切变形  
> bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要,相对于center_type偏移)  
> bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要,相对于center_type偏移)  
```Python
# 示例代码
from qtmodel import *
mdb.add_section(name="截面1",sec_type="矩形",sec_info=[2,4],bias_type="中心")
mdb.add_section(name="截面2",sec_type="混凝土箱梁",box_height=2,box_num=3,
sec_info=[0.02,0,12,3,1,2,1,5,6,0.2,0.4,0.1,0.13,0.28,0.3,0.5,0.5,0.5,0.2],
charm_info=["1*0.2,0.1*0.2","0.5*0.15,0.3*0.2","0.4*0.2","0.5*0.2"])
mdb.add_section(name="钢梁截面1",sec_type="工字钢梁",sec_info=[0,0,0.5,0.5,0.5,0.5,0.7,0.02,0.02,0.02])
mdb.add_section(name="钢梁截面2",sec_type="箱型钢梁",sec_info=[0,0.15,0.25,0.5,0.25,0.15,0.4,0.15,0.7,0.02,0.02,0.02,0.02],
rib_info = {"板肋1": [0.1,0.02],"T形肋1":[0.1,0.02,0.02,0.02]},
rib_place = [(1, 0, 0.1, "板肋1", 2, "默认名称1"),
(1, 0, 0.2, "板肋1", 2, "默认名称1")])
```  
Returns: 无
### add_single_section
以字典形式添加单一截面
> 参数:  
> index:截面编号  
> name:截面名称  
> sec_type:截面类型  
> sec_dict:截面始端编号  
```Python
# 示例代码
from qtmodel import *
mdb.add_single_section(index=1,name="变截面1",sec_type="矩形",
sec_dict={"sec_info":[1,2],"bias_type":"中心"})
```  
Returns: 无
### update_single_section
以字典形式添加单一截面
> 参数:  
> index:截面编号  
> new_id:新截面编号，默认不修改截面编号  
> name:截面名称  
> sec_type:截面类型  
> sec_dict:截面始端编号  
```Python
# 示例代码
from qtmodel import *
mdb.update_single_section(index=1,name="变截面1",sec_type="矩形",
sec_dict={"sec_info":[1,2],"bias_type":"中心"})
```  
Returns: 无
### add_tapper_section
添加变截面,字典参数参考单一截面,如果截面存在则自动覆盖
> 参数:  
> index:截面编号  
> name:截面名称  
> sec_type:截面类型  
> sec_begin:截面始端编号  
> sec_end:截面末端编号  
> shear_consider:考虑剪切变形  
> sec_normalize:变截面线段线圈重新排序  
```Python
# 示例代码
from qtmodel import *
mdb.add_tapper_section(index=1,name="变截面1",sec_type="矩形",
sec_begin={"sec_info":[1,2],"bias_type":"中心"},
sec_end={"sec_info":[2,2],"bias_type":"中心"})
```  
Returns: 无
### update_tapper_section
添加变截面,字典参数参考单一截面,如果截面存在则自动覆盖
> 参数:  
> index:截面编号  
> new_id:新截面编号，默认不修改截面编号  
> name:截面名称  
> sec_type:截面类型  
> sec_begin:截面始端编号  
> sec_end:截面末端编号  
> shear_consider:考虑剪切变形  
> sec_normalize:变截面线段线圈重新排序  
```Python
# 示例代码
from qtmodel import *
mdb.add_tapper_section(index=1,name="变截面1",sec_type="矩形",
sec_begin={"sec_info":[1,2],"bias_type":"中心"},
sec_end={"sec_info":[2,2],"bias_type":"中心"})
```  
Returns: 无
### add_tapper_section_by_id
添加变截面,需先建立单一截面
> 参数:  
> index:截面编号  
> name:截面名称  
> begin_id:截面始端编号  
> end_id:截面末端编号  
> shear_consider:考虑剪切变形  
> sec_normalize: 开启变截面线圈和线宽自适应排序 (避免两端截面绘制顺序导致的渲染和计算失效)  
```Python
# 示例代码
from qtmodel import *
mdb.add_tapper_section_by_id(name="变截面1",begin_id=1,end_id=2)
```  
Returns: 无
### remove_section
删除截面信息
> 参数:  
> index: 截面编号,参数为默认时删除全部截面  
```Python
# 示例代码
from qtmodel import *
mdb.remove_section()
mdb.remove_section(1)
```  
Returns: 无
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
```Python
# 示例代码
from qtmodel import *
mdb.add_thickness(name="厚度1", t=0.2,thick_type=0,bias_info=(0,0.8))
mdb.add_thickness(name="厚度2", t=0.2,thick_type=1,rib_pos=0,dist_v=0.1,rib_v=[1,1,0.02,0.02])
```  
Returns: 无
### remove_thickness
删除板厚
> 参数:  
> index:板厚编号,默认时删除所有板厚信息  
```Python
# 示例代码
from qtmodel import *
mdb.remove_thickness()
mdb.remove_thickness(index=1)
```  
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
```Python
# 示例代码
from qtmodel import *
mdb.add_tapper_section_group(ids=[1,2,3,4],name="变截面组1")
```  
Returns: 无
### update_section_bias
更新截面偏心
> 参数:  
> index:截面编号  
> bias_type:偏心类型  
> center_type:中心类型  
> shear_consider:考虑剪切  
> bias_point:自定义偏心点(仅自定义类型偏心需要)  
```Python
# 示例代码
from qtmodel import *
mdb.update_section_bias(index=1,bias_type="中上",center_type="几何中心")
mdb.update_section_bias(index=1,bias_type="自定义",bias_point=[0.1,0.2])
```  
Returns: 无
##  边界操作
### add_boundary_group
新建边界组
> 参数:  
> name:边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_boundary_group(name="边界组1")
```  
Returns: 无
### update_boundary_group
更改边界组名
> 参数:  
> name:边界组名  
> new_name:新边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.update_boundary_group("旧边界组","新边界组")
```  
Returns: 无
### remove_boundary_group
按照名称删除边界组
> 参数:  
> name: 边界组名称，默认删除所有边界组 (非必须参数)  
```Python
# 示例代码
from qtmodel import *
mdb.remove_boundary_group()
mdb.remove_boundary_group(name="边界组1")
```  
Returns: 无
### remove_all_boundary
根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.remove_all_boundary()
```  
Returns: 无
### remove_boundary
根据节点号删除一般支撑、弹性支承/根据弹性连接I或J端(需指定)节点号删除弹性连接/根据单元号删除梁端约束/根据从节点号和约束方程名删除约束方程/根据从节点号删除主从约束
> 参数:  
> remove_id:节点号 or 单元号  or 从节点号  
> bd_type:边界类型  ["一般支承", "弹性支承","一般弹性支承", "主从约束", "一般/受拉/受压/刚性弹性连接", "约束方程", "梁端约束"]  
> group:边界所处边界组名  
> extra_name:删除弹性连接或约束方程时额外标识,约束方程名或指定删除弹性连接节点类型 I/J  
```Python
# 示例代码
from qtmodel import *
mdb.remove_boundary(remove_id=11, bd_type="一般弹性连接",group="边界组1", extra_name="J")
mdb.remove_boundary(remove_id=12, bd_type="约束方程",group="边界组1", extra_name="约束方程名")
```  
Returns: 无
### add_general_elastic_support_property
添加一般弹性支承特性
> 参数:  
> name:一般弹性支承特性名称  
> data_matrix:一般弹性支承刚度矩阵(数据需按列输入至列表,共计21个参数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_general_elastic_support_property(name = "特性1", data_matrix=[i for i in range(1,22)])
```  
Returns: 无
### update_general_elastic_support_property
添加一般弹性支承特性
> 参数:  
> name:原一般弹性支承特性名称  
> new_name:现一般弹性支承特性名称  
> data_matrix:一般弹性支承刚度矩阵(数据需按列输入至列表,共计21个参数)  
```Python
# 示例代码
from qtmodel import *
mdb.update_general_elastic_support_property(name = "特性1",new_name="特性2", data_matrix=[i for i in range(1,22)])
```  
Returns: 无
### remove_general_elastic_support_property
添加一般弹性支承特性
> 参数:  
> name:一般弹性支承特性名称  
```Python
# 示例代码
from qtmodel import *
mdb.remove_general_elastic_support_property(name = "特性1")
```  
Returns: 无
### add_general_elastic_support
添加一般弹性支承特性
> 参数:  
> node_id:节点号  
> property_name:一般弹性支承特性名  
> group_name:一般弹性支承边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_general_elastic_support(node_id = 1, property_name = "特性1",group_name="边界组1")
```  
Returns: 无
### add_general_support
添加一般支承
> 参数:  
> node_id:节点编号,支持整数或整数型列表  
> boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]  ture-固定 false-自由  
> group_name:边界组名,默认为默认边界组  
```Python
# 示例代码
from qtmodel import *
mdb.add_general_support(node_id=1, boundary_info=[True,True,True,False,False,False])
```  
Returns: 无
### add_elastic_support
添加弹性支承
> 参数:  
> node_id:节点编号,支持数或列表  
> support_type:支承类型 1-线性  2-受拉  3-受压  
> boundary_info:边界信息 受拉和受压时列表长度为2-[direct(1-X 2-Y 3-Z),stiffness]  线性时列表长度为6-[kx,ky,kz,krx,kry,krz]  
> group_name:边界组  
```Python
# 示例代码
from qtmodel import *
mdb.add_elastic_support(node_id=1,support_type=1,boundary_info=[1e6,0,1e6,0,0,0])
mdb.add_elastic_support(node_id=1,support_type=2,boundary_info=[1,1e6])
mdb.add_elastic_support(node_id=1,support_type=3,boundary_info=[1,1e6])
```  
Returns: 无
### add_elastic_link
添加弹性连接，建议指定index(弹性连接编号)
> 参数:  
> index:弹性连接编号,默认自动识别  
> link_type:节点类型 1-一般弹性连接 2-刚性连接 3-受拉弹性连接 4-受压弹性连接  
> start_id:起始节点号  
> end_id:终节点号  
> beta_angle:贝塔角  
> boundary_info:边界信息  
> group_name:边界组名  
> dis_ratio:距i端距离比 (仅一般弹性连接需要)  
> kx:受拉或受压刚度  
```Python
# 示例代码
from qtmodel import *
mdb.add_elastic_link(link_type=1,start_id=1,end_id=2,boundary_info=[1e6,1e6,1e6,0,0,0])
mdb.add_elastic_link(link_type=2,start_id=1,end_id=2)
mdb.add_elastic_link(link_type=3,start_id=1,end_id=2,kx=1e6)
```  
Returns: 无
### add_master_slave_links
添加主从约束
> 参数:  
> node_ids:主节点号和从节点号，主节点号位于首位  
> boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由  
> group_name:边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_master_slave_links(node_ids=[(1,2),(1,3),(4,5),(4,6)],boundary_info=[True,True,True,False,False,False])
```  
Returns: 无
### add_master_slave_link
添加主从约束
> 参数:  
> master_id:主节点号  
> slave_id:从节点号，支持整数或整数型列表  
> boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由  
> group_name:边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_master_slave_link(master_id=1,slave_id=[2,3],boundary_info=[True,True,True,False,False,False])
```  
Returns: 无
### add_beam_constraint
添加梁端约束
> 参数:  
> beam_id:梁号  
> info_i:i端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由  
> info_j:j端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由  
> group_name:边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_beam_constraint(beam_id=2,info_i=[True,True,True,False,False,False],info_j=[True,True,True,False,False,False])
```  
Returns: 无
### add_constraint_equation
添加约束方程
> 参数:  
> name:约束方程名  
> sec_node:从节点号  
> sec_dof: 从节点自由度 1-x 2-y 3-z 4-rx 5-ry 6-rz  
> master_info:主节点约束信息列表  
> group_name:边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_beam_constraint(beam_id=2,info_i=[True,True,True,False,False,False],info_j=[True,True,True,False,False,False])
```  
Returns: 无
### add_node_axis
添加节点坐标
> 参数:  
> node_id:节点号  
> input_type:输入方式 1-角度 2-三点  3-向量  
> coord_info:局部坐标信息 -List<float>(角)  -List<List<float>>(三点 or 向量)  
```Python
# 示例代码
from qtmodel import *
mdb.add_node_axis(input_type=1,node_id=1,coord_info=[45,45,45])
mdb.add_node_axis(input_type=2,node_id=1,coord_info=[[0,0,1],[0,1,0],[1,0,0]])
mdb.add_node_axis(input_type=3,node_id=1,coord_info=[[0,0,1],[0,1,0]])
```  
Returns: 无
### update_node_axis
添加节点坐标
> 参数:  
> node_id:节点号  
> new_id:新节点号  
> input_type:输入方式 1-角度 2-三点  3-向量  
> coord_info:局部坐标信息 -List<float>(角)  -List<List<float>>(三点 or 向量)  
```Python
# 示例代码
from qtmodel import *
mdb.update_node_axis(node_id=1,new_id=1,input_type=1,coord_info=[45,45,45])
mdb.update_node_axis(node_id=2,new_id=2,input_type=2,coord_info=[[0,0,1],[0,1,0],[1,0,0]])
mdb.update_node_axis(node_id=3,new_id=3,input_type=3,coord_info=[[0,0,1],[0,1,0]])
```  
Returns: 无
### remove_node_axis
添加节点坐标
> 参数:  
> node_id:节点号  
```Python
# 示例代码
from qtmodel import *
mdb.remove_node_axis(node_id=1)
```  
Returns: 无
##  移动荷载操作
### add_standard_vehicle
添加标准车辆
> 参数:  
> name: 车辆荷载名称  
> standard_code: 荷载规范  
> _1-中国铁路桥涵规范(TB10002-2017)_  
> _2-城市桥梁设计规范(CJJ11-2019)_  
> _3-公路工程技术标准(JTJ 001-97)_  
> _4-公路桥涵设计通规(JTG D60-2004)_  
> _5-公路桥涵设计通规(JTG D60-2015)_  
> _6-城市轨道交通桥梁设计规范(GB/T51234-2017)_  
> _7-市域铁路设计规范2017(T/CRS C0101-2017)  
> load_type: 荷载类型,支持类型参考软件内界面  
> load_length: 默认为0即不限制荷载长度  (铁路桥涵规范2017 所需参数)  
> factor: 默认为1.0(铁路桥涵规范2017 ZH荷载所需参数)  
> n:车厢数: 默认6节车厢 (城市轨道交通桥梁规范2017 所需参数)  
> calc_fatigue:计算公路疲劳 (公路桥涵设计通规2015 所需参数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_standard_vehicle("高速铁路",standard_code=1,load_type="高速铁路")
```  
Returns: 无
### add_user_vehicle
添加标准车辆
> 参数:  
> name: 车辆荷载名称  
> load_type: 荷载类型,支持类型 -车辆/车道荷载 列车普通活载 城市轻轨活载 旧公路人群荷载 轮重集合  
> p: 荷载Pk或Pi列表  
> q: 均布荷载Qk或荷载集度dW  
> dis:荷载距离Li列表  
> load_length: 荷载长度  (列车普通活载 所需参数)  
> n:车厢数: 默认6节车厢 (列车普通活载 所需参数)  
> empty_load:空载 (列车普通活载、城市轻轨活载 所需参数)  
> width:宽度 (旧公路人群荷载 所需参数)  
> wheelbase:轮间距 (轮重集合 所需参数)  
> min_dis:车轮距影响面最小距离 (轮重集合 所需参数))  
> unit_force:荷载单位 默认为"N"  
> unit_length:长度单位 默认为"M"  
```Python
# 示例代码
from qtmodel import *
mdb.add_user_vehicle(name="车道荷载",load_type="车道荷载",p=270000,q=10500)
```  
Returns: 无
### add_node_tandem
添加节点纵列
> 参数:  
> name:节点纵列名  
> start_id:起始节点号  
> node_ids:节点列表  
```Python
# 示例代码
from qtmodel import *
mdb.add_node_tandem(name="节点纵列1",start_id=1,node_ids=[i+1 for i in range(12)])
```  
Returns: 无
### add_influence_plane
添加影响面
> 参数:  
> name:影响面名称  
> tandem_names:节点纵列名称组  
```Python
# 示例代码
from qtmodel import *
mdb.add_influence_plane(name="影响面1",tandem_names=["节点纵列1","节点纵列2"])
```  
Returns: 无
### add_lane_line
添加车道线
> 参数:  
> name:车道线名称  
> influence_name:影响面名称  
> tandem_name:节点纵列名  
> offset:偏移  
> lane_width:车道宽度  
```Python
# 示例代码
from qtmodel import *
mdb.add_lane_line(name="车道1",influence_name="影响面1",tandem_name="节点纵列1",offset=0,lane_width=3.1)
```  
Returns: 无
### add_live_load_case
添加移动荷载工况
> 参数:  
> name:活载工况名  
> influence_plane:影响线名  
> span:跨度  
> sub_case:子工况信息 [(车辆名称,系数,["车道1","车道2"])...]  
> trailer_code:考虑挂车时挂车车辆名  
> special_code:考虑特载时特载车辆名  
```Python
# 示例代码
from qtmodel import *
mdb.add_live_load_case(name="活载工况1",influence_plane="影响面1",span=100,sub_case=[("车辆名称",1.0,["车道1","车道2"]),])
```  
Returns: 无
### add_car_relative_factor
添加移动荷载工况汽车折减
> 参数:  
> name:活载工况名  
> code_index: 汽车折减规范编号  1-公规2015 2-公规2004 3-无  
> cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取  
> longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取  
> impact_factor:冲击系数大于1时为自定义，否则按照规范自动选取  
> frequency:桥梁基频  
```Python
# 示例代码
from qtmodel import *
mdb.add_car_relative_factor(name="活载工况1",code_index=1,cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5])
```  
Returns: 无
### add_train_relative_factor
添加移动荷载工况汽车折减
> 参数:  
> name:活载工况名  
> code_index: 火车折减规范编号  1-铁规2017_ZK_ZC 2-铁规2017_ZKH_ZH 3-无  
> cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取  
> calc_fatigue:是否计算疲劳  
> line_count: 疲劳加载线路数  
> longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取  
> impact_factor:强度冲击系数大于1时为自定义，否则按照规范自动选取  
> fatigue_factor:疲劳系数  
> bridge_kind:桥梁类型 0-无 1-简支 2-结合 3-涵洞 4-空腹式  
> fill_thick:填土厚度 (规ZKH ZH钢筋/素混凝土、石砌桥跨结构以及涵洞所需参数)  
> rise:拱高 (规ZKH ZH活载-空腹式拱桥所需参数)  
> calc_length:计算跨度(铁规ZKH ZH活载-空腹式拱桥所需参数)或计算长度(铁规ZK ZC活载所需参数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_train_relative_factor(name="活载工况1",code_index=1,cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5],calc_length=50)
```  
Returns: 无
### add_metro_relative_factor
添加移动荷载工况汽车折减
> 参数:  
> name:活载工况名  
> cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取  
> longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取  
> impact_factor:强度冲击系数大于1时为自定义，否则按照规范自动选取  
```Python
# 示例代码
from qtmodel import *
mdb.add_metro_relative_factor(name="活载工况1",cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5],
longitude_factor=1,impact_factor=1)
```  
Returns: 无
### remove_vehicle
删除车辆信息
> 参数:  
> name:车辆名称  
```Python
# 示例代码
from qtmodel import *
mdb.remove_vehicle(name="车辆名称")
```  
Returns: 无
### remove_node_tandem
按照 节点纵列编号/节点纵列名 删除节点纵列
> 参数:  
> index:节点纵列编号  
> name:节点纵列名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_node_tandem(index=1)
mdb.remove_node_tandem(name="节点纵列1")
```  
Returns: 无
### remove_influence_plane
按照 影响面编号/影响面名称 删除影响面
> 参数:  
> index:影响面编号  
> name:影响面名称  
```Python
# 示例代码
from qtmodel import *
mdb.remove_influence_plane(index=1)
mdb.remove_influence_plane(name="影响面1")
```  
Returns: 无
### remove_lane_line
按照 车道线编号/车道线名称 删除车道线
> 参数:  
> name:车道线名称  
> index:车道线编号  
```Python
# 示例代码
from qtmodel import *
mdb.remove_lane_line(index=1)
mdb.remove_lane_line(name="车道线1")
```  
Returns: 无
### remove_live_load_case
删除移动荷载工况
> 参数:  
> name:移动荷载工况名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_live_load_case(name="活载工况1")
```  
Returns: 无
##  动力荷载操作
### add_load_to_mass
添加荷载转为质量
> 参数:  
> name: 荷载工况名称  
> factor: 系数  
```Python
# 示例代码
from qtmodel import *
mdb.add_load_to_mass(name="荷载工况",factor=1)
```  
Returns: 无
### add_nodal_mass
添加节点质量
> 参数:  
> node_id:节点编号，支持单个编号和编号列表  
> mass_info:[m,rmX,rmY,rmZ]  
```Python
# 示例代码
from qtmodel import *
mdb.add_nodal_mass(node_id=1,mass_info=(100,0,0,0))
```  
Returns: 无
### remove_nodal_mass
删除节点质量
> 参数:  
> node_id:节点号，默认删除所有节点质量  
```Python
# 示例代码
from qtmodel import *
mdb.remove_nodal_mass(node_id=1)
```  
Returns: 无
### remove_load_to_mass
删除荷载转为质量
> 参数:  
> name:荷载工况名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_load_to_mass(name="荷载工况")
```  
Returns: 无
### add_spectrum_function
添加反应谱函数
> 参数:  
> name:反应谱函数名  
> factor:反应谱调整系数  
> kind:反应谱类型 0-无量纲 1-加速度 2-位移  
> function_info:反应谱函数信息  
```Python
# 示例代码
from qtmodel import *
mdb.add_spectrum_function(name="反应谱函数1",factor=1.0,function_info=[(0,0.02),(1,0.03)])
```  
Returns: 无
### add_spectrum_case
添加反应谱工况
> 参数:  
> name:荷载工况名  
> description:说明  
> kind:组合方式 1-求模 2-求和  
> info_x: 反应谱X向信息 (X方向函数名,系数)  
> info_y: 反应谱Y向信息 (Y方向函数名,系数)  
> info_z: 反应谱Z向信息 (Z方向函数名,系数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_spectrum_case(name="反应谱工况",info_x=("函数1",1.0))
```  
Returns: 无
##  钢束操作
### add_tendon_group
按照名称添加钢束组，添加时可指定钢束组id
> 参数:  
> name: 钢束组名称  
> index: 钢束组编号(非必须参数)，默认自动识别  
```Python
# 示例代码
from qtmodel import *
mdb.add_tendon_group(name="钢束组1")
```  
Returns: 无
### remove_tendon_group
按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组
> 参数:  
> name:钢束组名称,默认自动识别 (可选参数)  
```Python
# 示例代码
from qtmodel import *
mdb.remove_tendon_group(name="钢束组1")
```  
Returns: 无
### add_tendon_property
添加钢束特性
> 参数:  
> name:钢束特性名  
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
```Python
# 示例代码
from qtmodel import *
mdb.add_tendon_property(name="钢束1",tendon_type=0,material_id=1,duct_type=1,steel_type=1,
steel_detail=[0.00014,0.10,0.25,0.0015],loos_detail=(1,1,1))
```  
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
```Python
# 示例代码
from qtmodel import *
mdb.add_tendon_3d("BB1",property_name="22-15",num=2,position_type=1,
control_points=[(0,0,-1,0),(10,0,-1,0)],point_insert=(0,0,0))
mdb.add_tendon_3d("BB1",property_name="22-15",num=2,position_type=2,
control_points=[(0,0,-1,0),(10,0,-1,0)],point_insert=(1,1,1),track_group="轨迹线结构组1")
```  
Returns: 无
### add_tendon_2d
添加三维钢束
> 参数:  
> name:钢束名称  
> property_name:钢束特性名称  
> group_name:默认钢束组  
> num:根数  
> line_type:1-导线点  2-折线点  
> position_type: 定位方式 1-直线  2-轨迹线  
> symmetry: 对称点 0-左端点 1-右端点 2-不对称  
> control_points: 控制点信息[(x1,z1,r1),(x2,z2,r2)....]  
> control_points_lateral: 控制点横弯信息[(x1,y1,r1),(x2,y2,r2)....]，无横弯时不必输入  
> point_insert: 定位方式  
> _直线: 插入点坐标[x,y,z]_  
> _轨迹线:  [插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id]_  
> tendon_direction:直线钢束X方向向量  默认为[1,0,0] (轨迹线不用赋值)  
> _x轴-[1,0,0] y轴-[0,1,0] z轴-[0,0,1]_  
> rotation_angle:绕钢束旋转角度  
> track_group:轨迹线结构组名  (直线时不用赋值)  
> projection:直线钢束投影 (默认为true)  
```Python
# 示例代码
from qtmodel import *
mdb.add_tendon_2d(name="BB1",property_name="22-15",num=2,position_type=1,
control_points=[(0,-1,0),(10,-1,0)],point_insert=(0,0,0))
mdb.add_tendon_2d(name="BB1",property_name="22-15",num=2,position_type=2,
control_points=[(0,-1,0),(10,-1,0)],point_insert=(1,1,1),track_group="轨迹线结构组1")
```  
Returns: 无
### update_tendon_element
赋予钢束构件
> 参数:  
> ids: 钢束构件所在单元编号集合  
```Python
# 示例代码
from qtmodel import *
mdb.update_tendon_element(ids=[1,2,3,4])
```  
Returns: 无
### remove_tendon
按照名称或编号删除钢束,默认时删除所有钢束
> 参数:  
> name:钢束名称  
> index:钢束编号  
```Python
# 示例代码
from qtmodel import *
mdb.remove_tendon(name="钢束1")
mdb.remove_tendon(index=1)
mdb.remove_tendon()
```  
Returns: 无
### remove_tendon_property
按照名称或编号删除钢束组,默认时删除所有钢束组
> 参数:  
> name:钢束组名称  
> index:钢束组编号  
```Python
# 示例代码
from qtmodel import *
mdb.remove_tendon_property(name="钢束特性1")
mdb.remove_tendon_property(index=1)
mdb.remove_tendon_property()
```  
Returns: 无
##  静力荷载操作
### add_load_group
根据荷载组名称添加荷载组
> 参数:  
> name: 荷载组名称  
```Python
# 示例代码
from qtmodel import *
mdb.add_load_group(name="荷载组1")
```  
Returns: 无
### remove_load_group
根据荷载组名称删除荷载组,参数为默认时删除所有荷载组
> 参数:  
> name: 荷载组名称  
```Python
# 示例代码
from qtmodel import *
mdb.remove_load_group(name="荷载组1")
```  
Returns: 无
### add_pre_stress
添加预应力
> 参数:  
> case_name:荷载工况名  
> tendon_name:钢束名,支持钢束名或钢束名列表  
> tension_type:预应力类型  
> _0-始端 1-末端 2-两端_  
> force:预应力  
> group_name:边界组  
```Python
# 示例代码
from qtmodel import *
mdb.add_pre_stress(case_name="荷载工况名",tendon_name="钢束1",force=1390000)
```  
Returns: 无
### remove_pre_stress
删除预应力
> 参数:  
> case_name:荷载工况  
> tendon_name:钢束组  
```Python
# 示例代码
from qtmodel import *
mdb.remove_pre_stress(case_name="工况1",tendon_name="钢束1")
```  
Returns: 无
### add_nodal_force
添加节点荷载
> 参数:  
> node_id:节点编号  
> case_name:荷载工况名  
> load_info:荷载信息列表 [Fx,Fy,Fz,Mx,My,Mz]  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_nodal_force(case_name="荷载工况1",node_id=1,load_info=[1,1,1,1,1,1],group_name="默认结构组")
```  
Returns: 无
### remove_nodal_force
删除节点荷载
> 参数:  
> case_name:荷载工况名  
> node_id:节点编号  
```Python
# 示例代码
from qtmodel import *
mdb.remove_nodal_force(case_name="荷载工况1",node_id=1)
```  
Returns: 无
### add_node_displacement
添加节点位移
> 参数:  
> node_id:节点编号,支持整型或整数型列表  
> case_name:荷载工况名  
> load_info:节点位移列表 [Dx,Dy,Dz,Rx,Ry,Rz]  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_node_displacement(case_name="荷载工况1",node_id=1,load_info=(1,0,0,0,0,0),group_name="默认荷载组")
mdb.add_node_displacement(case_name="荷载工况1",node_id=[1,2,3],load_info=(1,0,0,0,0,0),group_name="默认荷载组")
```  
Returns: 无
### remove_nodal_displacement
删除节点位移
> 参数:  
> node_id:节点编号,支持数或列表  
> case_name:荷载工况名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_nodal_displacement(case_name="荷载工况1",node_id=1)
```  
Returns: 无
### add_beam_element_load
添加梁单元荷载
> 参数:  
> element_id:单元编号,支持数或列表  
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
```Python
# 示例代码
from qtmodel import *
mdb.add_beam_element_load(case_name="荷载工况1",element_id=1,load_type=1,list_x=[0.1,0.5,0.8],list_load=[100,100,100])
mdb.add_beam_element_load(case_name="荷载工况1",element_id=1,load_type=3,list_x=[0.4,0.8],list_load=[100,200])
```  
Returns: 无
### remove_beam_element_load
删除梁单元荷载
> 参数:  
> element_id:单元号支持数或列表  
> case_name:荷载工况名  
> load_type:荷载类型  
> _1-集中力   2-集中弯矩  3-分布力   4-分布弯矩_  
```Python
# 示例代码
from qtmodel import *
mdb.remove_beam_element_load(case_name="工况1",element_id=1,load_type=1)
```  
Returns: 无
### add_initial_tension_load
添加初始拉力
> 参数:  
> element_id:单元编号支持数或列表  
> case_name:荷载工况名  
> tension:初始拉力  
> tension_type:张拉类型  0-增量 1-全量  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_initial_tension_load(element_id=1,case_name="工况1",tension=100,tension_type=1)
```  
Returns: 无
### remove_initial_tension_load
删除初始拉力
> 参数:  
> element_id:单元编号支持数或列表  
> case_name:荷载工况名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_initial_tension_load(case_name="工况1",element_id=1)
```  
Returns: 无
### add_cable_length_load
添加索长张拉
> 参数:  
> element_id:单元编号支持数或列表  
> case_name:荷载工况名  
> length:长度  
> tension_type:张拉类型  0-增量 1-全量  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_cable_length_load(element_id=1,case_name="工况1",length=1,tension_type=1)
```  
Returns: 无
### remove_cable_length_load
删除索长张拉
> 参数:  
> element_id:单元号支持数或列表  
> case_name:荷载工况名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_cable_length_load(case_name="工况1",element_id=1)
```  
Returns: 无
### add_plate_element_load
添加版单元荷载
> 参数:  
> element_id:单元编号支持数或列表  
> case_name:荷载工况名  
> load_type:荷载类型  
> _1-集中力  2-集中弯矩  3-分布力  4-分布弯矩_  
> load_place:荷载位置  
> _0-面IJKL 1-边IJ  2-边JK  3-边KL  4-边LI  (仅分布荷载需要)_  
> coord_system:坐标系  (默认3)  
> _1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z_  
> group_name:荷载组名  
> list_load:荷载列表  
> list_xy:荷载位置信息 [IJ方向绝对距离x,IL方向绝对距离y]  (仅集中荷载需要)  
```Python
# 示例代码
from qtmodel import *
mdb.add_plate_element_load(element_id=1,case_name="工况1",load_type=1,group_name="默认荷载组",list_load=[1000],list_xy=(0.2,0.5))
```  
Returns: 无
### remove_plate_element_load
删除指定荷载工况下指定单元的板单元荷载
> 参数:  
> element_id:单元编号，支持数或列表  
> case_name:荷载工况名  
> load_type: 板单元类型 1集中力   2-集中弯矩  3-分布线力  4-分布线弯矩  5-分布面力  6-分布面弯矩  
```Python
# 示例代码
from qtmodel import *
mdb.remove_plate_element_load(case_name="工况1",element_id=1,load_type=1)
```  
Returns: 无
### add_deviation_parameter
添加制造误差
> 参数:  
> name:名称  
> element_type:单元类型  1-梁单元  2-板单元  
> parameters:参数列表  
> _梁杆单元:[轴向,I端X向转角,I端Y向转角,I端Z向转角,J端X向转角,J端Y向转角,J端Z向转角]_  
> _板单元:[X向位移,Y向位移,Z向位移,X向转角,Y向转角]_  
```Python
# 示例代码
from qtmodel import *
mdb.add_deviation_parameter(name="梁端制造误差",element_type=1,parameters=[1,0,0,0,0,0,0])
mdb.add_deviation_parameter(name="板端制造误差",element_type=1,parameters=[1,0,0,0,0])
```  
Returns: 无
### remove_deviation_parameter
删除指定制造偏差参数
> 参数:  
> name:制造偏差参数名  
> para_type:制造偏差类型 1-梁单元  2-板单元  
```Python
# 示例代码
from qtmodel import *
mdb.remove_deviation_parameter(name="参数1",para_type=1)
```  
Returns: 无
### add_deviation_load
添加制造误差荷载
> 参数:  
> element_id:单元编号，支持数或列表  
> case_name:荷载工况名  
> parameters:参数名列表  
> _梁杆单元时:制造误差参数名称_  
> _板单元时: [I端误差名,J端误差名,K端误差名,L端误差名]_  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_deviation_load(element_id=1,case_name="工况1",parameters="梁端误差")
mdb.add_deviation_load(element_id=2,case_name="工况1",parameters=["板端误差1","板端误差2","板端误差3","板端误差4"])
```  
Returns: 无
### remove_deviation_load
删除指定制造偏差荷载
> 参数:  
> case_name:荷载工况名  
> element_id:单元编号，支持数或列表  
```Python
# 示例代码
from qtmodel import *
mdb.remove_deviation_load(case_name="工况1",element_id=1)
```  
Returns: 无
### add_element_temperature
添加单元温度
> 参数:  
> element_id:单元编号，支持数或列表  
> case_name:荷载工况名  
> temperature:最终温度  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_element_temperature(element_id=1,case_name="自重",temperature=1,group_name="默认荷载组")
```  
Returns: 无
### remove_element_temperature
删除指定单元温度
> 参数:  
> case_name:荷载工况名  
> element_id:单元编号，支持数或列表  
> group_name:指定荷载组,后续升级开放指定荷载组删除功能  
```Python
# 示例代码
from qtmodel import *
mdb.remove_element_temperature(case_name="荷载工况1",element_id=1)
```  
Returns: 无
### add_gradient_temperature
添加梯度温度
```Python
# 示例代码
from qtmodel import *
mdb.add_gradient_temperature(element_id=1,case_name="荷载工况1",group_name="荷载组名1",temperature=10)
mdb.add_gradient_temperature(element_id=2,case_name="荷载工况2",group_name="荷载组名2",temperature=10,element_type=2)
```  
Returns: 无
### remove_gradient_temperature
删除梁或板单元梯度温度
> 参数:  
> case_name:荷载工况名  
> element_id:单元编号，支持数或列表  
> group_name:指定荷载组,后续升级开放指定荷载组删除功能  
```Python
# 示例代码
from qtmodel import *
mdb.remove_gradient_temperature(case_name="工况1",element_id=1)
```  
Returns: 无
### add_beam_section_temperature
添加梁截面温度
> 参数:  
> element_id:单元编号，支持整数或整数型列表  
> case_name:荷载工况名  
> code_index:规范编号  (1-公路规范2015  2-AASHTO2017)  
> paving_thick:铺设厚度(m)  
> temperature_type:温度类型,默认升温  (1-升温 2-降温)  
> paving_type:铺设类型，默认为1 (1-沥青混凝土(默认)  2-水泥混凝土)  
> zone_index: 区域号 (仅规范二需要)  
> group_name:荷载组名  
> modify:是否修改规范温度  
> temp_list:温度列表[T1,T2,T3,t]or[T1,T2]  (仅修改时需要)  
```Python
# 示例代码
from qtmodel import *
mdb.add_beam_section_temperature(element_id=1,case_name="工况1",paving_thick=0.1)
```  
Returns: 无
### remove_beam_section_temperature
删除指定梁或板单元梁截面温度
> 参数:  
> case_name:荷载工况名  
> element_id:单元编号，支持数或列表  
> group_name:指定荷载组,后续升级开放指定荷载组删除功能  
```Python
# 示例代码
from qtmodel import *
mdb.remove_beam_section_temperature(case_name="工况1",element_id=1)
```  
Returns: 无
### add_index_temperature
添加指数温度
> 参数:  
> element_id:单元编号，支持数或列表  
> case_name:荷载工况名  
> temperature:温差  
> index:指数  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_index_temperature(element_id=1,case_name="工况1",temperature=20,index=2)
```  
Returns: 无
### remove_index_temperature
删除梁单元指数温度
> 参数:  
> case_name:荷载工况名  
> element_id:单元编号，支持数或列表  
> group_name:指定荷载组,后续升级开放指定荷载组删除功能  
```Python
# 示例代码
from qtmodel import *
mdb.remove_index_temperature(case_name="工况1",element_id=1)
```  
Returns: 无
### add_top_plate_temperature
添加顶板温度
> 参数:  
> element_id:单元编号  
> case_name:荷载  
> temperature:温差，最终温度于初始温度之差  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_top_plate_temperature(element_id=1,case_name="工况1",temperature=40,group_name="默认荷载组")
```  
Returns: 无
### remove_top_plate_temperature
删除梁单元顶板温度
> 参数:  
> case_name:荷载工况名  
> element_id:单元编号，支持数或列表  
> group_name:指定荷载组,后续升级开放指定荷载组删除功能  
```Python
# 示例代码
from qtmodel import *
mdb.remove_top_plate_temperature(case_name="荷载工况1",element_id=1,group_name="默认荷载组")
```  
Returns: 无
### add_custom_temperature
添加梁自定义温度
> 参数:  
> case_name:荷载工况名  
> element_id:单元编号，支持数或列表  
> group_name:指定荷载组,后续升级开放指定荷载组删除功能  
> orientation: 1-局部坐标z 2-局部坐标y  
> temperature_data:自定义数据[(参考位置1-顶 2-底,高度,温度)...]  
```Python
# 示例代码
from qtmodel import *
mdb.add_custom_temperature(case_name="荷载工况1",element_id=1,orientation=1,temperature_data=[(1,1,20),(1,2,10)])
```  
Returns: 无
### remove_custom_temperature
删除梁单元自定义温度
> 参数:  
> case_name:荷载工况名  
> element_id:单元编号，支持数或列表  
> group_name:指定荷载组,后续升级开放指定荷载组删除功能  
```Python
# 示例代码
from qtmodel import *
mdb.remove_custom_temperature(case_name="工况1",element_id=1,group_name="默认荷载组")
```  
Returns: 无
### add_plane_load_type
添加分配面荷载类型
> 参数:  
> name:荷载类型名称  
> load_type:荷载类型  1-集中荷载 2-线荷载 3-面荷载  
> point_list:点列表，集中力时为列表内元素为 [x,y,force] 线荷载与面荷载时为 [x,y]  
> load:荷载值,仅线荷载与面荷载需要  
> copy_x:复制到x轴距离，与UI一致，支持3@2形式字符串，逗号分隔  
> copy_y:复制到y轴距离，与UI一致，支持3@2形式字符串，逗号分隔  
> describe:描述  
```Python
# 示例代码
from qtmodel import *
mdb.remove_custom_temperature(case_name="工况1",element_id=1,group_name="默认荷载组")
```  
Returns: 无
### add_plane_load
添加分配面荷载类型
> 参数:  
> case_name:工况名  
> type_name:荷载类型  1-集中荷载 2-线荷载 3-面荷载  
> point1:第一点(原点)  
> point2:第一点(在x轴上)  
> point3:第一点(在y轴上)  
> plate_ids:指定板单元。默认时为全部板单元  
> coord_system:描述  
> group_name:描述  
```Python
# 示例代码
from qtmodel import *
mdb.remove_custom_temperature(case_name="工况1",element_id=1,group_name="默认荷载组")
```  
Returns: 无
##  沉降操作
### add_sink_group
添加沉降组
> 参数:  
> name: 沉降组名  
> sink: 沉降值  
> node_ids: 节点编号，支持数或列表  
```Python
# 示例代码
from qtmodel import *
mdb.add_sink_group(name="沉降1",sink=0.1,node_ids=[1,2,3])
```  
Returns: 无
### remove_sink_group
按照名称删除沉降组
> 参数:  
> name:沉降组名,默认删除所有沉降组  
```Python
# 示例代码
from qtmodel import *
mdb.remove_sink_group()
mdb.remove_sink_group(name="沉降1")
```  
Returns: 无
### add_sink_case
添加沉降工况
> 参数:  
> name:荷载工况名  
> sink_groups:沉降组名，支持字符串或列表  
```Python
# 示例代码
from qtmodel import *
mdb.add_sink_case(name="沉降工况1",sink_groups=["沉降1","沉降2"])
```  
Returns: 无
### remove_sink_case
按照名称删除沉降工况,不输入名称时默认删除所有沉降工况
> 参数:  
> name:沉降工况名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_sink_case()
mdb.remove_sink_case(name="沉降1")
```  
Returns: 无
### add_concurrent_reaction
添加并发反力组
> 参数:  
> names: 结构组名称集合  
```Python
# 示例代码
from qtmodel import *
mdb.add_concurrent_reaction(names=["默认结构组"])
```  
Returns: 无
### remove_concurrent_reaction
删除所有并发反力组
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.remove_concurrent_reaction()
```  
Returns: 无
### add_concurrent_force
创建并发内力组
> 参数:  
> names: 结构组名称集合  
```Python
# 示例代码
from qtmodel import *
mdb.add_concurrent_force(names=["默认结构组"])
```  
Returns: 无
### remove_concurrent_force
删除所有并发内力组
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.remove_concurrent_force()
```  
Returns: 无
### add_load_case
添加荷载工况
> 参数:  
> name:沉降名  
> case_type:荷载工况类型  
> -"施工阶段荷载", "恒载", "活载", "制动力", "风荷载","体系温度荷载","梯度温度荷载",  
> -"长轨伸缩挠曲力荷载", "脱轨荷载", "船舶撞击荷载","汽车撞击荷载","长轨断轨力荷载", "用户定义荷载"  
```Python
# 示例代码
from qtmodel import *
mdb.add_load_case(name="工况1",case_type="施工阶段荷载")
```  
Returns: 无
### remove_load_case
删除荷载工况,参数均为默认时删除全部荷载工况
> 参数:  
> index:荷载编号  
> name:荷载名  
```Python
# 示例代码
from qtmodel import *
mdb.remove_load_case(index=1)
mdb.remove_load_case(name="工况1")
mdb.remove_load_case()
```  
Returns: 无
##  施工阶段操作
### add_construction_stage
添加施工阶段信息
> 参数:  
> name:施工阶段信息  
> duration:时长  
> active_structures:激活结构组信息 [(结构组名,龄期,安装方法,计自重施工阶段id),...]  
> _计自重施工阶段id: 0-不计自重,1-本阶段 n-第n阶段)_  
> _安装方法：1-变形法 2-无应力法 3-接线法 4-切线法  
> delete_structures:钝化结构组信息 [结构组1，结构组2,...]  
> active_boundaries:激活边界组信息 [(边界组1，位置),...]  
> _位置:  0-变形前 1-变形后_  
> delete_boundaries:钝化边界组信息 [边界组1，边界组2,...]  
> active_loads:激活荷载组信息 [(荷载组1,时间),...]  
> _时间: 0-开始 1-结束_  
> delete_loads:钝化荷载组信息 [(荷载组1,时间),...]  
> _时间: 0-开始 1-结束_  
> temp_loads:临时荷载信息 [荷载组1，荷载组2,..]  
> index:施工阶段插入位置,从0开始,默认添加到最后  
```Python
# 示例代码
from qtmodel import *
mdb.add_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
```  
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
```Python
# 示例代码
from qtmodel import *
mdb.update_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
```  
Returns: 无
### update_weight_stage
更新施工阶段自重
> 参数:  
> name:施工阶段信息  
> structure_group_name:结构组名  
> weight_stage_id: 计自重阶段号 (0-不计自重,1-本阶段 n-第n阶段)  
```Python
# 示例代码
from qtmodel import *
mdb.update_weight_stage(name="施工阶段1",structure_group_name="默认结构组",weight_stage_id=1)
```  
Returns: 无
### update_all_stage_setting_type
更新施工阶段安装方式
> 参数:  
> setting_type:安装方式 (1-接线法 2-无应力法 3-变形法 4-切线法)  
```Python
# 示例代码
from qtmodel import *
mdb.update_all_stage_setting_type(setting_type=1)
```  
Returns: 无
### remove_construction_stage
按照施工阶段名删除施工阶段,默认删除所有施工阶段
> 参数:  
> name:所删除施工阶段名称  
```Python
# 示例代码
from qtmodel import *
mdb.remove_construction_stage(name="施工阶段1")
```  
Returns: 无
##  荷载组合操作
### add_load_combine
添加荷载组合
> 参数:  
> name:荷载组合名  
> combine_type:荷载组合类型 1-叠加  2-判别  3-包络 4-SRss 5-AbsSum  
> describe:描述  
> combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下  
> _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合_  
> _"MV"-移动荷载工况  "SM"-沉降荷载工况_ "RS"-反应谱工况_  
```Python
# 示例代码
from qtmodel import *
mdb.add_load_combine(name="荷载组合1",combine_type=1,describe="无",combine_info=[("CS","合计值",1),("CS","恒载",1)])
```  
Returns: 无
### update_load_combine
更新荷载组合
> 参数:  
> name:荷载组合名  
> combine_type:荷载组合类型 (1-叠加  2-判别  3-包络)  
> describe:描述  
> combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下  
> _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合_  
> _"MV"-移动荷载工况  "SM"-沉降荷载工况_  
```Python
# 示例代码
from qtmodel import *
mdb.update_load_combine(name="荷载组合1",combine_type=1,describe="无",combine_info=[("CS","合计值",1),("CS","恒载",1)])
```  
Returns: 无
### remove_load_combine
删除荷载组合
> 参数:  
> name:指定删除荷载组合名，默认时则删除所有荷载组合  
```Python
# 示例代码
from qtmodel import *
mdb.remove_load_combine(name="荷载组合1")
```  
Returns: 无
##  视图控制
### set_view_camera
更改三维显示相机设置
> 参数:  
> camera_point: 相机坐标点  
> focus_point: 相机焦点  
> camera_rotate:相机绕XYZ旋转角度  
> scale: 缩放系数  
```Python
# 示例代码
from qtmodel import *
odb.set_view_camera(camera_point=(-100,-100,100),focus_point=(0,0,0))
```  
Returns: 无
### set_view_direction
更改三维显示默认视图
> 参数:  
> direction: 1-空间视图1 2-前视图 3-三维视图2 4-左视图  5-顶视图 6-右视图 7-空间视图3 8-后视图 9-空间视图4 10-底视图  
> horizontal_degree:水平向旋转角度  
> vertical_degree:竖向旋转角度  
> scale:缩放系数  
```Python
# 示例代码
from qtmodel import *
odb.set_view_direction(direction=1,scale=1.2)
```  
Returns: 无
### activate_structure
激活指定阶段和单元,默认激活所有
> 参数:  
> node_ids: 节点集合  
> element_ids: 单元集合  
```Python
# 示例代码
from qtmodel import *
odb.activate_structure(node_ids=[1,2,3],element_ids=[1,2,3])
```  
Returns: 无
### set_unit
修改视图显示时单位制,不影响建模
> 参数:  
> unit_force: 支持 N KN TONF KIPS LBF  
> unit_length: 支持 M MM CM IN FT  
```Python
# 示例代码
from qtmodel import *
odb.set_unit(unit_force="N",unit_length="M")
```  
Returns: 无
### remove_display
删除当前所有显示,包括边界荷载钢束等全部显示
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.remove_display()
```  
Returns: 无
### save_png
保存当前模型窗口图形信息
> 参数:  
> file_path: 文件全路径  
```Python
# 示例代码
from qtmodel import *
odb.save_png(file_path=r"D:\\QT\\aa.png")
```  
Returns: 无
### set_render
消隐设置开关
> 参数:  
> flag: 默认设置打开消隐  
```Python
# 示例代码
from qtmodel import *
odb.set_render(flag=True)
```  
Returns: 无
### change_construct_stage
消隐设置开关
> 参数:  
> stage: 施工阶段名称或施工阶段号  0-基本  
```Python
# 示例代码
from qtmodel import *
odb.change_construct_stage(0)
odb.change_construct_stage(stage=1)
```  
Returns: 无
##  静力结果查看
### get_element_stress
获取单元应力,支持单个单元和单元列表
> 参数:  
> element_id: 单元编号,支持整数或整数型列表  
> stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载  
> increment_type: 1-全量    2-增量  
> case_name: 运营阶段所需荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_element_stress(element_id=1,stage_id=1)
odb.get_element_stress(element_id=[1,2,3],stage_id=1)
odb.get_element_stress(element_id=1,stage_id=-1,case_name="工况名")
```  
Returns: json字符串,包含信息为list[dict] or dict
### get_element_force
获取单元内力,支持单个单元和单元列表
> 参数:  
> element_id: 单元编号  
> stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载  
> increment_type: 1-全量    2-增量  
> case_name: 运营阶段所需荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_element_force(element_id=1,stage_id=1)
odb.get_element_force(element_id=[1,2,3],stage_id=1)
odb.get_element_force(element_id=1,stage_id=-1,case_name="工况名")
```  
Returns: json字符串,包含信息为list[dict] or dict
### get_reaction
获取节点反力
> 参数:  
> node_id: 节点编号,支持整数或整数型列表  
> stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载  
> increment_type: 1-全量    2-增量  
> case_name: 运营阶段所需荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_reaction(node_id=1,stage_id=1)
odb.get_reaction(node_id=[1,2,3],stage_id=1)
odb.get_reaction(node_id=1,stage_id=-1,case_name="工况名")
```  
Returns: json字符串,包含信息为list[dict] or dict
### get_node_displacement
获取节点,支持单个节点和节点列表
> 参数:  
> node_id: 节点号  
> stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载  
> increment_type: 1-全量    2-增量  
> case_name: 运营阶段所需荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_node_displacement(node_id=1,stage_id=1)
odb.get_node_displacement(node_id=[1,2,3],stage_id=1)
odb.get_node_displacement(node_id=1,stage_id=-1,case_name="工况名")
```  
Returns: json字符串,包含信息为list[dict] or dict
##  绘制模型结果
### plot_reaction_result
保存结果图片到指定文件甲
> 参数:  
> file_path: 保存路径名  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)  
> show_increment: 是否显示增量结果  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> component: 分量编号 0-Fx 1-Fy 2-Fz 3-Fxyz 4-Mx 5-My 6-Mz 7-Mxyz  
> show_number: 数值选项卡开启  
> show_legend: 图例选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> arrow_scale:箭头大小  
```Python
# 示例代码
from qtmodel import *
odb.plot_reaction_result(file_path=r"D:\\图片\\反力图.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
### plot_displacement_result
保存结果图片到指定文件甲
> 参数:  
> file_path: 保存路径名  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)  
> show_increment: 是否显示增量结果  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> component: 分量编号 0-Dx 1-Dy 2-Dz 3-Rx 4-Ry 5-Rz 6-Dxy 7-Dyz 8-Dxz 9-Dxyz  
> show_deformed: 变形选项卡开启  
> deformed_scale:变形比例  
> deformed_actual:是否显示实际变形  
> show_number: 数值选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> show_legend: 图例选项卡开启  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> show_pre_deformed: 显示变形前  
```Python
# 示例代码
from qtmodel import *
odb.plot_displacement_result(file_path=r"D:\\图片\\变形图.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
### plot_beam_element_force
绘制梁单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)  
> show_increment: 是否显示增量结果  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> component: 分量编号 0-Dx 1-Dy 2-Dz 3-Rx 4-Ry 5-Rz 6-Dxy 7-Dyz 8-Dxz 9-Dxyz  
> show_line_chart: 折线图选项卡开启  
> line_scale:折线图比例  
> flip_plot:反向绘制  
> show_deformed: 变形选项卡开启  
> deformed_scale:变形比例  
> deformed_actual:是否显示实际变形  
> show_number: 数值选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> show_legend: 图例选项卡开启  
> show_pre_deformed: 显示变形前  
> position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部  
```Python
# 示例代码
from qtmodel import *
odb.plot_beam_element_force(file_path=r"D:\\图片\\梁内力.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
### plot_truss_element_force
绘制杆单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)  
> show_increment: 是否显示增量结果  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> component: 分量编号 0-N 1-Fx 2-Fy 3-Fz  
> show_line_chart: 折线图选项卡开启  
> line_scale:折线图比例  
> flip_plot:反向绘制  
> show_deformed: 变形选项卡开启  
> deformed_scale:变形比例  
> deformed_actual:是否显示实际变形  
> show_number: 数值选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> show_legend: 图例选项卡开启  
> show_pre_deformed: 显示变形前  
> position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部  
```Python
# 示例代码
from qtmodel import *
odb.plot_truss_element_force(file_path=r"D:\\图片\\杆内力.png",load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
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
```Python
# 示例代码
from qtmodel import *
odb.plot_plate_element_force(file_path=r"D:\\图片\\板内力.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
### plot_composite_beam_force
绘制组合梁单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)  
> show_increment: 是否显示增量结果  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> mat_type: 材料类型 0-主材 1-辅材 2-主材+辅材  
> component: 分量编号 0-Fx 1-Fy 2-Fz 3-Mx 4-My 5-Mz  
> show_line_chart: 折线图选项卡开启  
> line_scale:折线图比例  
> flip_plot:反向绘制  
> show_deformed: 变形选项卡开启  
> deformed_scale:变形比例  
> deformed_actual:是否显示实际变形  
> show_number: 数值选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> show_legend: 图例选项卡开启  
> show_pre_deformed: 显示变形前  
> position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部  
```Python
# 示例代码
from qtmodel import *
odb.plot_composite_beam_force(file_path=r"D:\\图片\\组合梁内力.png",mat_type=0,component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
### plot_beam_element_stress
绘制梁单元应力结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)  
> show_increment: 是否显示增量结果  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> component: 分量编号 0-轴力分量 1-Mz分量 2-My分量 3-组合包络 4-左上 5-右上 6-右下 7-左下  
> show_line_chart: 折线图选项卡开启  
> line_scale:折线图比例  
> flip_plot:反向绘制  
> show_deformed: 变形选项卡开启  
> deformed_scale:变形比例  
> deformed_actual:是否显示实际变形  
> show_number: 数值选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> show_legend: 图例选项卡开启  
> show_pre_deformed: 显示变形前  
> position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部  
```Python
# 示例代码
from qtmodel import *
odb.plot_beam_element_stress(file_path=r"D:\\图片\\梁应力.png",show_line_chart=False,component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
### plot_truss_element_stress
绘制杆单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)  
> show_increment: 是否显示增量结果  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> show_line_chart: 折线图选项卡开启  
> line_scale:折线图比例  
> flip_plot:反向绘制  
> show_deformed: 变形选项卡开启  
> deformed_scale:变形比例  
> deformed_actual:是否显示实际变形  
> show_number: 数值选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> show_legend: 图例选项卡开启  
> show_pre_deformed: 显示变形前  
> position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部  
```Python
# 示例代码
from qtmodel import *
odb.plot_truss_element_stress(file_path=r"D:\\图片\\杆应力.png",load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
### plot_composite_beam_stress
绘制组合梁单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> stage_id: -1-运营阶段  0-施工阶段包络 n-施工阶段号  
> load_case_name: 详细荷载工况名,参考桥通结果输出,例如： CQ:成桥(合计)  
> show_increment: 是否显示增量结果  
> envelope_type: 施工阶段包络类型 1-最大 2-最小  
> mat_type: 材料类型 0-主材 1-辅材  
> component: 分量编号 0-轴力分量 1-Mz分量 2-My分量 3-包络 4-左上 5-右上 6-左下 7-右下  
> show_line_chart: 折线图选项卡开启  
> line_scale:折线图比例  
> flip_plot:反向绘制  
> show_deformed: 变形选项卡开启  
> deformed_scale:变形比例  
> deformed_actual:是否显示实际变形  
> show_number: 数值选项卡开启  
> text_rotation: 数值选项卡内文字旋转角度  
> digital_count: 小数点位数  
> show_exponential: 指数显示开启  
> max_min_kind: 数值选项卡内最大最小值显示 -1-不显示最大最小值  0-显示最大值和最小值  1-最大绝对值 2-最大值 3-最小值  
> show_legend: 图例选项卡开启  
> show_pre_deformed: 显示变形前  
> position: 位置编号 0-始端 1-末端 2-绝对最大 4-全部  
```Python
# 示例代码
from qtmodel import *
odb.plot_composite_beam_stress(file_path=r"D:\\图片\\组合梁应力.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
### plot_plate_element_stress
绘制板单元结果图并保存到指定文件
> 参数:  
> file_path: 保存路径名  
> component: 分量编号 0-Fxx 1-Fyy 2-Fxy 3-Mxx 4-Myy 5-Mxy  
> stress_kind: 力类型 0-单元 1-节点平均  
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
> position: 位置 0-板顶 1-板底 2-绝对值最大  
```Python
# 示例代码
from qtmodel import *
odb.plot_plate_element_stress(file_path=r"D:\\图片\\板应力.png",component=0,load_case_name="CQ:成桥(合计)",stage_id=-1)
```  
Returns: 无
##  获取模型信息
### get_element_by_point
获取某一点指定范围内单元集合,单元中心点为节点平均值
> 参数:  
> x: 坐标x  
> y: 坐标y  
> z: 坐标z  
> tolerance:容许范围,默认为1  
```Python
# 示例代码
from qtmodel import *
odb.get_element_by_point(0.5,0.5,0.5,tolerance=1)
```  
Returns: json字符串,包含信息为list[int]
### get_element_by_material
获取某一材料相应的单元
> 参数:  
> name:材料名称  
```Python
# 示例代码
from qtmodel import *
odb.get_element_by_material("材料1")
```  
Returns: json字符串,包含信息为list[int]
### get_overlap_nodes
获取重合节点
> 参数:  
> round_num: 判断精度，默认小数点后四位  
```Python
# 示例代码
from qtmodel import *
odb.get_overlap_nodes()
```  
Returns: json字符串,包含信息为list[list[int]]
### get_overlap_elements
获取重合节点
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_overlap_elements()
```  
Returns: json字符串,包含信息为list[list[int]]
### get_structure_group_names
获取结构组名称
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_structure_group_names()
```  
Returns: json字符串,包含信息为list[str]
### get_thickness_data
获取所有板厚信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_thickness_data(1)
```  
Returns: json字符串,包含信息为dict
### get_all_thickness_data
获取所有板厚信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_all_thickness_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_all_section_shape
获取所有截面形状信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_all_section_shape()
```  
Returns: json字符串,包含信息为list[dict]
### get_section_shape
获取截面形状信息
> 参数:  
> sec_id: 目标截面编号  
```Python
# 示例代码
from qtmodel import *
odb.get_section_shape(1)
```  
Returns: json字符串,包含信息为dict
### get_all_section_data
获取所有截面详细信息,截面特性详见UI自定义特性截面
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_all_section_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_section_data
获取截面详细信息,截面特性详见UI自定义特性截面
> 参数:  
> sec_id: 目标截面编号  
```Python
# 示例代码
from qtmodel import *
odb.get_section_data(1)
```  
Returns: json字符串,包含信息为dict
### get_section_property
获取指定截面特性
> 参数:  
> index:截面号  
```Python
# 示例代码
from qtmodel import *
odb.get_section_property(1)
```  
Returns: dict
### get_section_ids
获取模型所有截面号
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_section_ids()
```  
Returns: list[int]
### get_node_id
获取节点编号,结果为-1时则表示未找到该坐标节点
> 参数:  
> x: 目标点X轴坐标  
> y: 目标点Y轴坐标  
> z: 目标点Z轴坐标  
> tolerance: 距离容许误差  
```Python
# 示例代码
from qtmodel import *
odb.get_node_id(x=1,y=1,z=1)
```  
Returns: int
### get_group_elements
获取结构组单元编号
> 参数:  
> group_name: 结构组名  
```Python
# 示例代码
from qtmodel import *
odb.get_group_elements(group_name="默认结构组")
```  
Returns: list[int]
### get_group_nodes
获取结构组节点编号
> 参数:  
> group_name: 结构组名  
```Python
# 示例代码
from qtmodel import *
odb.get_group_nodes(group_name="默认结构组")
```  
Returns: list[int]
### get_node_data
获取节点信息 默认获取所有节点信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_node_data()     # 获取所有节点信息
odb.get_node_data(ids=1)    # 获取单个节点信息
odb.get_node_data(ids=[1,2])    # 获取多个节点信息
```  
Returns:  json字符串,包含信息为list[dict] or dict
### get_element_data
获取单元信息
> 参数:  
> ids:单元号,支持整数或整数型列表,默认为None时获取所有单元信息  
```Python
# 示例代码
from qtmodel import *
odb.get_element_data() # 获取所有单元结果
odb.get_element_data(ids=1) # 获取指定编号单元信息
```  
Returns:  json字符串,包含信息为list[dict] or dict
### get_element_type
获取单元类型
> 参数:  
> ele_id: 单元号  
```Python
# 示例代码
from qtmodel import *
odb.get_element_type(ele_id=1) # 获取1号单元类型
```  
Returns: str
### get_beam_element
获取梁单元信息
> 参数:  
> ids: 梁单元号,默认时获取所有梁单元  
```Python
# 示例代码
from qtmodel import *
odb.get_beam_element() # 获取所有单元信息
```  
Returns:  list[str] 其中str为json格式
### get_plate_element
获取板单元信息
> 参数:  
> ids: 板单元号,默认时获取所有板单元  
```Python
# 示例代码
from qtmodel import *
odb.get_plate_element() # 获取所有单元信息
```  
Returns:  list[str] 其中str为json格式
### get_cable_element
获取索单元信息
> 参数:  
> ids: 索单元号,默认时获取所有索单元  
```Python
# 示例代码
from qtmodel import *
odb.get_cable_element() # 获取所有单元信息
```  
Returns:  list[str] 其中str为json格式
### get_link_element
获取杆单元信息
> 参数:  
> ids: 杆单元号,默认时输出全部杆单元  
```Python
# 示例代码
from qtmodel import *
odb.get_link_element() # 获取所有单元信息
```  
Returns:  list[str] 其中str为json格式
### get_material_data
获取材料信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_material_data() # 获取所有材料信息
```  
Returns: json字符串,包含信息为list[dict]
### get_concrete_material
获取混凝土材料信息
> 参数:  
> ids: 材料号,默认时输出全部材料  
```Python
# 示例代码
from qtmodel import *
odb.get_concrete_material() # 获取所有材料信息
```  
Returns:  list[str] 其中str为json格式
### get_steel_plate_material
获取钢材材料信息
> 参数:  
> ids: 材料号,默认时输出全部材料  
```Python
# 示例代码
from qtmodel import *
odb.get_steel_plate_material() # 获取所有钢材材料信息
```  
Returns:  list[str] 其中str为json格式
### get_pre_stress_bar_material
获取钢材材料信息
> 参数:  
> ids: 材料号,默认时输出全部材料  
```Python
# 示例代码
from qtmodel import *
odb.get_pre_stress_bar_material() # 获取所有预应力材料信息
```  
Returns:  list[str] 其中str为json格式
### get_steel_bar_material
获取钢筋材料信息
> 参数:  
> ids: 材料号,默认时输出全部材料  
```Python
# 示例代码
from qtmodel import *
odb.get_steel_bar_material() # 获取所有钢筋材料信息
```  
Returns:  list[str] 其中str为json格式
### get_user_###ine_material
获取自定义材料信息
> 参数:  
> ids: 材料号,默认时输出全部材料  
```Python
# 示例代码
from qtmodel import *
odb.get_user_define_material() # 获取所有自定义材料信息
```  
Returns:  list[str] 其中str为json格式
##  获取模型边界信息
### get_boundary_group_names
获取自边界组名称
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_boundary_group_names()
```  
Returns: json字符串,包含信息为list[str]
### get_general_support_data
获取一般支承信息
> 参数:  
> group_name:默认输出所有边界组信息  
```Python
# 示例代码
from qtmodel import *
odb.get_general_support_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_elastic_link_data
获取弹性连接信息
> 参数:  
> group_name:默认输出所有边界组信息  
```Python
# 示例代码
from qtmodel import *
odb.get_elastic_link_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_elastic_support_data
获取弹性支承信息
> 参数:  
> group_name:默认输出所有边界组信息  
```Python
# 示例代码
from qtmodel import *
odb.get_elastic_support_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_master_slave_link_data
获取主从连接信息
> 参数:  
> group_name:默认输出所有边界组信息  
```Python
# 示例代码
from qtmodel import *
odb.get_master_slave_link_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_node_local_axis_data
获取节点坐标信息
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_node_local_axis_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_beam_constraint_data
获取节点坐标信息
> 参数:  
> group_name:默认输出所有边界组信息  
```Python
# 示例代码
from qtmodel import *
odb.get_beam_constraint_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_constraint_equation_data
获取约束方程信息
> 参数:  
> group_name:默认输出所有边界组信息  
```Python
# 示例代码
from qtmodel import *
odb.get_constraint_equation_data()
```  
Returns: json字符串,包含信息为list[dict]
##  获取施工阶段信息
### get_stage_name
获取所有施工阶段名称
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_stage_name()
```  
Returns: json字符串,包含信息为list[int]
### get_elements_of_stage
获取指定施工阶段单元编号信息
> 参数:  
> stage_id: 施工阶段编号  
```Python
# 示例代码
from qtmodel import *
odb.get_elements_of_stage(stage_id=1)
```  
Returns: json字符串,包含信息为list[int]
### get_nodes_of_stage
获取指定施工阶段节点编号信息
> 参数:  
> stage_id: 施工阶段编号  
```Python
# 示例代码
from qtmodel import *
odb.get_nodes_of_stage(stage_id=1)
```  
Returns: json字符串,包含信息为list[int]
### get_groups_of_stage
获取施工阶段结构组、边界组、荷载组名集合
> 参数:  
> stage_id: 施工阶段编号  
```Python
# 示例代码
from qtmodel import *
odb.get_groups_of_stage(stage_id=1)
```  
Returns: json字符串,包含信息为dict
##  荷载信息
### get_load_case_names
获取荷载工况名
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_load_case_names()
```  
Returns: json字符串,包含信息为list[str]
### get_pre_stress_load
获取预应力荷载
> 参数:  
> case_name: 荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_pre_stress_load(case_name="荷载工况1")
```  
Returns: json字符串,包含信息为list[dict]
### get_node_mass_data
获取节点质量
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_node_mass_data()
```  
Returns: json字符串,包含信息为list[dict]
### get_nodal_force_load
获取节点力荷载
> 参数:  
> case_name: 荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_nodal_force_load(case_name="荷载工况1")
```  
Returns: json字符串,包含信息为list[dict]
### get_nodal_displacement_load
获取节点位移荷载
> 参数:  
> case_name: 荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_nodal_displacement_load(case_name="荷载工况1")
```  
Returns: json字符串,包含信息为list[dict]
### get_beam_element_load
获取梁单元荷载
> 参数:  
> case_name: 荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_beam_element_load(case_name="荷载工况1")
```  
Returns: json字符串,包含信息为list[dict]
### get_plate_element_load
获取梁单元荷载
> 参数:  
> case_name: 荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_beam_element_load(case_name="荷载工况1")
```  
Returns: json字符串,包含信息为list[dict]
### get_initial_tension_load
获取初拉力荷载数据
> 参数:  
> case_name: 荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_initial_tension_load(case_name="荷载工况1")
```  
Returns: json字符串,包含信息为list[dict]
### get_cable_length_load
获取指定荷载工况的初拉力荷载数据
> 参数:  
> case_name: 荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_cable_length_load(case_name="荷载工况1")
```  
Returns: json字符串,包含信息为list[dict]
### get_deviation_parameter
获取制造偏差参数
> 参数:  
```Python
# 示例代码
from qtmodel import *
odb.get_deviation_parameter()
```  
Returns: json字符串,包含信息为list[dict]
### get_deviation_load
获取指定荷载工况的制造偏差荷载
> 参数:  
> case_name:荷载工况名  
```Python
# 示例代码
from qtmodel import *
odb.get_deviation_load(case_name="荷载工况1")
```  
Returns: json字符串,包含信息为list[dict]
