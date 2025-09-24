> 最新版本 V1.1.1 - 2025-09-24 
> pip install --upgrade qtmodel -i https://pypi.org/simple
- 新增更新结构组接口 
# 建模操作 
##  节点操作
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
mdb.add_nodes(node_data=[[1,1,2,3],[2,1,2,3]])
```  
Returns: 无
##  单元操作
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
### add_elements
根据单元编号和单元类型添加单元
> 参数:  
> ele_data:单元信息  
> [编号,类型(1-梁 2-杆),materialId,sectionId,betaAngle,nodeI,nodeJ]  
> [编号,类型(3-索),materialId,sectionId,betaAngle,nodeI,nodeJ,张拉类型(1-初拉力 2-初始水平力 3-无应力长度),张拉值]  
> [编号,类型(4-板),materialId,thicknessId,betaAngle,nodeI,nodeJ,nodeK,nodeL,plate_type(0-薄板 1-厚板)]  
```Python
# 示例代码
from qtmodel import *
mdb.add_elements(ele_data=[
[1,1,1,1,0,1,2],
[2,2,1,1,0,1,2],
[3,3,1,1,0,1,2,1,100],
[4,4,1,1,0,1,2,3,4,0]])
```  
Returns: 无
##  结构组操作
### add_structure_group
添加结构组
> 参数:  
> name: 结构组名  
> node_ids: 节点编号列表,支持XtoYbyN类型字符串(可选参数)  
> element_ids: 单元编号列表,支持XtoYbyN类型字符串(可选参数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_structure_group(name="新建结构组1")
mdb.add_structure_group(name="新建结构组2",node_ids=[1,2,3,4],element_ids=[1,2])
mdb.add_structure_group(name="新建结构组2",node_ids="1to10 11to21by2",element_ids=[1,2])
```  
Returns: 无
### update_structure_group_name
更新结构组名
> 参数:  
> name: 结构组名  
> new_name: 新结构组名(可选参数)  
```Python
# 示例代码
from qtmodel import *
mdb.update_structure_group_name(name="结构组1",new_name="新结构组")
```  
Returns: 无
### update_structure_group
更新结构组信息
> 参数:  
> name: 结构组名  
> new_name: 新结构组名  
> node_ids: 节点编号列表,支持XtoYbyN类型字符串(可选参数)  
> element_ids: 单元编号列表,支持XtoYbyN类型字符串(可选参数)  
```Python
# 示例代码
from qtmodel import *
mdb.update_structure_group(name="结构组",new_name="新建结构组",node_ids=[1,2,3,4],element_ids=[1,2])
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
### remove_structure_from_group
为结构组删除节点、单元
> 参数:  
> name: 结构组名  
> node_ids: 节点编号列表(可选参数)  
> element_ids: 单元编号列表(可选参数)  
```Python
# 示例代码
from qtmodel import *
mdb.remove_structure_from_group(name="现有结构组1",node_ids=[1,2,3,4],element_ids=[1,2])
```  
Returns: 无
##  材料
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
> index:材料编号,默认为最大Id+1  
> name: 收缩徐变名  
> code_index: 1-公规JTG3362-2018  2-公规JTGD62-2004 3-公规JTJ023-85 4-铁规TB10092-2017 5-地铁GB50157-2013  6-老化理论  7-BS5400_4_1990  8-AASHTO_LRFD_2017    1000-AASHTO_LRFD_2017  
> time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)  
> creep_data: 徐变数据 [(函数名,龄期)...]  
> shrink_data: 收缩函数名  
```Python
# 示例代码
from qtmodel import *
mdb.add_time_parameter(name="收缩徐变材料1",code_index=1)
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
##  板厚
### add_thickness
添加板厚
> 参数:  
> index: 板厚id  
> name: 板厚名称  
> t: 板厚度  
> thick_type: 板厚类型 0-普通板 1-加劲肋板  
> bias_info: 默认不偏心,偏心时输入列表[type(0-厚度比 1-数值),value]  
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
##  截面
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
> box_other_info: 混凝土箱梁额外信息(键包括"i1" "B0" "B4" "T4" 值为列表)  
> box_other_right: 混凝土箱梁额外信息(对称时可忽略，键包括"i1" "B0" "B4" "T4" 值为列表)  
> mat_combine: 组合截面材料信息 (仅组合材料需要) [弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c]  
> rib_info:肋板信息  
> rib_place:肋板位置 list[tuple[布置具体部位,参考点0-下/左,距参考点间距,肋板名，加劲肋位置0-上/左 1-下/右 2-两侧,加劲肋名]]  
> _布置具体部位(工字钢梁) 1-上左 2-上右 3-腹板 4-下左 5-下右  
> _布置具体部位(箱型钢梁) 1-上左 2-上中 3-上右 4-左腹板 5-右腹板 6-下左 7-下中 8-下右  
> loop_segments:线圈坐标集合 list[dict] dict示例:{"main":[(x1,y1),(x2,y2)...],"sub1":[(x1,y1),(x2,y2)...],"sub2":[(x1,y1),(x2,y2)...]}  
> sec_lines:线宽集合[(x1,y1,x2,y3,thick),]  
> secondary_loop_segments:辅材线圈坐标集合 list[dict] (同loop_segments)  
> sec_property:截面特性(参考UI界面共计29个参数)，可选参数，指定截面特性时不进行截面计算  
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
sec_info=[0.2,0.4,0.1,0.13,3,1,2,1,0.02,0,12,5,6,0.28,0.3,0.5,0.5,0.5,0.2],
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
> sec_data:截面信息字典，键值参考添加add_section方法参数  
```Python
# 示例代码
from qtmodel import *
mdb.add_single_section(index=1,name="变截面1",sec_type="矩形",
sec_data={"sec_info":[1,2],"bias_type":"中心"})
```  
Returns: 无
### add_tapper_section
添加变截面,字典参数参考单一截面,如果截面存在则自动覆盖
> 参数:  
> index:截面编号  
> name:截面名称  
> sec_type:截面类型  
> sec_begin:截面始端截面信息字典，键值参考添加add_section方法参数  
> sec_end:截面末端截面信息字典，键值参考添加add_section方法参数  
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
### calculate_section_property
重新计算所有截面特性
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.calculate_section_property()
```  
Returns: 无
### remove_unused_sections
删除未使用截面
> 参数:  
```Python
# 示例代码
from qtmodel import *
mdb.remove_unused_sections()
```  
Returns: 无
##  变截面组
### add_tapper_section_group
添加变截面组
> 参数:  
> ids:变截面组单元号,支持XtoYbyN类型字符串  
> name: 变截面组名  
> factor_w: 宽度方向变化阶数 线性(1.0) 非线性(!=1.0)  
> factor_h: 高度方向变化阶数 线性(1.0) 非线性(!=1.0)  
> ref_w: 宽度方向参考点 0-i 1-j  
> ref_h: 高度方向参考点 0-i 1-j  
> dis_w: 宽度方向距离  
> dis_h: 高度方向距离  
> parameter_info:参数化变截面组信息,键为参数名(参考UI)值为如下三种类型  
> 1(非线性),指数,参考点(I/J),距离  
> 2(自定义),变化长1,终点值1,变化长2,终点值2...  
> 3(圆弧),半径,参考点(I/J)  
```Python
# 示例代码
from qtmodel import *
mdb.add_tapper_section_group(ids=[1,2,3,4],name="变截面组1")
mdb.add_tapper_section_group(ids=[1,2,3,4],name="参数化变截面组",parameter_info={"梁高(H)":"1,2,I,0"})
```  
Returns: 无
##  边界操作
### add_effective_width
添加有效宽度系数
> 参数:  
> element_ids:边界单元号支持整形和整形列表且支持XtoYbyN形式  
> factor_i:I端截面Iy折减系数  
> factor_j:J端截面Iy折减系数  
> dz_i:I端截面形心变换量  
> dz_j:J端截面形心变换量  
> group_name:边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_effective_width(element_ids=[1,2,3,4],factor_i=0.1,factor_j=0.1,dz_i=0.1,dz_j=0.1)
mdb.add_effective_width(element_ids="1to4",factor_i=0.1,factor_j=0.1,dz_i=0.1,dz_j=0.1)
```  
Returns: 无
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
### add_general_elastic_support
添加一般弹性支承特性
> 参数:  
> node_id:节点号,支持整数或整数型列表且支持XtoYbyN形式字符串  
> property_name:一般弹性支承特性名  
> group_name:一般弹性支承边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_general_elastic_support(node_id=1, property_name = "特性1",group_name="边界组1")
```  
Returns: 无
### add_general_support
添加一般支承
> 参数:  
> node_id:节点编号,支持整数或整数型列表且支持XtoYbyN形式字符串  
> boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]  ture-固定 false-自由  
> group_name:边界组名,默认为默认边界组  
```Python
# 示例代码
from qtmodel import *
mdb.add_general_support(node_id=1, boundary_info=[True,True,True,False,False,False])
mdb.add_general_support(node_id="1to100", boundary_info=[True,True,True,False,False,False])
```  
Returns: 无
### add_elastic_support
添加弹性支承
> 参数:  
> node_id:节点编号,支持数或列表且支持XtoYbyN形式字符串  
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
批量添加主从约束，不指定编号默认为最大编号加1
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
> slave_id:从节点号，支持整数或整数型列表且支持XtoYbyN形式字符串  
> boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由  
> group_name:边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_master_slave_link(master_id=1,slave_id=[2,3],boundary_info=[True,True,True,False,False,False])
mdb.add_master_slave_link(master_id=1,slave_id="2to3",boundary_info=[True,True,True,False,False,False])
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
### remove_elastic_link
根据弹性连接号删除弹性连接
> 参数:  
> index:弹性连接号  
```Python
# 示例代码
from qtmodel import *
mdb.remove_elastic_link(index=1)
```  
Returns: 无
### update_elastic_link
更新弹性连接，根据指定的index
> 参数:  
> index:弹性连接号  
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
mdb.update_elastic_link(index=1,link_type=1,start_id=1,end_id=2,boundary_info=[1e6,1e6,1e6,0,0,0])
mdb.update_elastic_link(index=2,link_type=2,start_id=1,end_id=2)
mdb.update_elastic_link(index=3,link_type=3,start_id=1,end_id=2,kx=1e6)
```  
Returns: 无
##  钢束操作
### add_tendon_group
按照名称添加钢束组，添加时可指定钢束组id
> 参数:  
> name: 钢束组名称  
```Python
# 示例代码
from qtmodel import *
mdb.add_tendon_group(name="钢束组1")
```  
Returns: 无
### add_tendon_property
添加钢束特性
> 参数:  
> name:钢束特性名  
> tendon_type: 0-PRE 1-POST  
> material_name: 钢材材料所属名称  
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
mdb.add_tendon_property(name="钢束1",tendon_type=0,material_name="预应力材料",duct_type=1,steel_type=1,
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
> point_insert: 定位方式 (直线时为插入点坐标[x,y,z]  轨迹线时[插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id])  
> tendon_direction:直线钢束X方向向量  默认为x轴即[1,0,0] (轨迹线不用赋值)  
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
> control_points: 控制点信息[(x1,z1,r1),(x2,z2,r2)....] 三维[(x1,y1,z1,r1),(x2,y2,z2,r2)....]  
> control_points_lateral: 控制点横弯信息[(x1,y1,r1),(x2,y2,r2)....]，无横弯时不必输入  
> point_insert: 定位方式 (直线时为插入点坐标[x,y,z]  轨迹线时[插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id])  
> tendon_direction:直线钢束X方向向量  默认为x轴即[1,0,0] (轨迹线不用赋值)  
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
### add_tendon_elements
添加预应力单元
> 参数:  
> ids:单元编号支持数或列表且支持XtoYbyN形式字符串  
```Python
# 示例代码
from qtmodel import *
mdb.add_tendon_elements(ids=[1,2,4,6])
```  
Returns: 无
##  静力荷载操作
### add_nodal_force
添加节点荷载
> 参数:  
> node_id:节点编号且支持XtoYbyN形式字符串  
> case_name:荷载工况名  
> load_info:荷载信息列表 [Fx,Fy,Fz,Mx,My,Mz]  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_nodal_force(node_id=1,case_name="荷载工况1",load_info=[1,1,1,1,1,1],group_name="默认结构组")
mdb.add_nodal_force(node_id="1to100",case_name="荷载工况1",load_info=[1,1,1,1,1,1],group_name="默认结构组")
```  
Returns: 无
### add_node_displacement
添加节点位移
> 参数:  
> node_id:节点编号,支持整型或整数型列表且支持XtoYbyN形式字符串  
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
### add_beam_element_load
添加梁单元荷载
> 参数:  
> element_id:单元编号,支持数或列表且支持XtoYbyN形式字符串  
> case_name:荷载工况名  
> load_type:荷载类型 (1-集中力 2-集中弯矩 3-分布力 4-分布弯矩)  
> coord_system:坐标系 (1-整体X  2-整体Y 3-整体Z  4-局部X  5-局部Y  6-局部Z)  
> is_abs: 荷载位置输入方式，True-绝对值   False-相对值  
> list_x:荷载位置信息 ,荷载距离单元I端的距离，可输入绝对距离或相对距离  
> list_load:荷载数值信息  
> group_name:荷载组名  
> load_bias:偏心荷载 (是否偏心,0-中心 1-偏心,偏心坐标系-int,偏心距离)  
> projected:荷载是否投影  
```Python
# 示例代码
from qtmodel import *
mdb.add_beam_element_load(element_id=1,case_name="荷载工况1",load_type=1,list_x=0.5,list_load=100)
mdb.add_beam_element_load(element_id="1to100",case_name="荷载工况1",load_type=3,list_x=[0.4,0.8],list_load=[100,200])
```  
Returns: 无
### add_pre_stress
添加预应力
> 参数:  
> case_name:荷载工况名  
> tendon_name:钢束名,支持钢束名或钢束名列表  
> tension_type:预应力类型 (0-始端 1-末端 2-两端)  
> force:预应力  
> group_name:荷载组  
```Python
# 示例代码
from qtmodel import *
mdb.add_pre_stress(case_name="荷载工况名",tendon_name="钢束1",force=1390000)
```  
Returns: 无
### add_initial_tension_load
添加初始拉力
> 参数:  
> element_id:单元编号支持数或列表且支持XtoYbyN形式字符串  
> case_name:荷载工况名  
> tension:初始拉力  
> tension_type:张拉类型  0-增量 1-全量  
> group_name:荷载组名  
> application_type:计算方式 1-体外力 2-体内力 3-转为索长张拉  
> stiffness:索刚度参与系数  
```Python
# 示例代码
from qtmodel import *
mdb.add_initial_tension_load(element_id=1,case_name="工况1",tension=100,tension_type=1)
```  
Returns: 无
### add_cable_length_load
添加索长张拉
> 参数:  
> element_id:单元编号支持数或列表且支持XtoYbyN形式字符串  
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
### add_plate_element_load
添加版单元荷载
> 参数:  
> element_id:单元编号支持数或列表  
> case_name:荷载工况名  
> load_type:荷载类型 (1-集中力  2-集中弯矩  3-分布力  4-分布弯矩)  
> load_place:荷载位置 (0-面IJKL 1-边IJ  2-边JK  3-边KL  4-边LI ) (仅分布荷载需要)  
> coord_system:坐标系  (1-整体X  2-整体Y 3-整体Z  4-局部X  5-局部Y  6-局部Z)  
> group_name:荷载组名  
> list_load:荷载列表  
> list_xy:荷载位置信息 [IJ方向绝对距离x,IL方向绝对距离y]  (仅集中荷载需要)  
```Python
# 示例代码
from qtmodel import *
mdb.add_plate_element_load(element_id=1,case_name="工况1",load_type=1,group_name="默认荷载组",list_load=[1000],list_xy=(0.2,0.5))
```  
Returns: 无
##  移动荷载操作
### add_standard_vehicle
添加标准车辆
> 参数:  
> name: 车辆荷载名称  
> standard_code: 荷载规范  
> _1-中国铁路桥涵规范(TB10002-2017)  
> _2-城市桥梁设计规范(CJJ11-2019)  
> _3-公路工程技术标准(JTJ 001-97)  
> _4-公路桥涵设计通规(JTG D60-2004  
> _5-公路桥涵设计通规(JTG D60-2015)  
> _6-城市轨道交通桥梁设计规范(GB/T51234-2017)  
> _7-市域铁路设计规范2017(T/CRS C0101-2017)  
> load_type: 荷载类型,支持类型参考软件内界面  
> load_length: 默认为0即不限制荷载长度  (铁路桥涵规范2017 所需参数)  
> factor: 默认为1.0(铁路桥涵规范2017 ZH荷载所需参数)  
> n:车厢数: 默认6节车厢 (城市轨道交通桥梁规范2017 所需参数)  
> calc_fatigue:疲劳荷载模式是否计算三种类型疲劳荷载 (公路桥涵设计通规2015 所需参数)  
```Python
# 示例代码
from qtmodel import *
mdb.add_standard_vehicle("高速铁路",standard_code=1,load_type="高速铁路")
```  
Returns: 无
### add_user_vehicle
添加用户定义车辆
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
```Python
# 示例代码
from qtmodel import *
mdb.add_user_vehicle(name="车道荷载",load_type="车道荷载",p=270000,q=10500)
```  
Returns: 无
### add_node_tandem
添加节点纵列,默认以最小X对应节点作为纵列起点
> 参数:  
> name:节点纵列名  
> node_ids:节点列表，支持XToYbyN字符串  
> order_by_x:是否开启自动排序，按照X坐标从小到大排序  
```Python
# 示例代码
from qtmodel import *
mdb.add_node_tandem(name="节点纵列1",node_ids=[1,2,3,4,5,6,7])
mdb.add_node_tandem(name="节点纵列1",node_ids="1to7")
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
> optimize:是否允许车辆摆动  
> direction:0-向前  1-向后  
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
> is_save:是否保存子工况结果  
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
> code_index: 汽车折减规范编号  0-无 1-公规2015 2-公规2004  
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
> code_index: 火车折减规范编号  0-无 1-铁规ZK 2-铁规ZKH  
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
### add_spectrum_function
添加反应谱函数
> 参数:  
> name:反应谱函数名  
> factor:反应谱调整系数  
> kind:反应谱类型 0-无量纲 1-加速度 2-位移  
> function_info:反应谱函数信息[(时间1,数值1),[时间2,数值2]]  
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
### add_boundary_element_property
添加边界单元特性
> 参数:  
> index: 边界单元特性编号,默认自动识别  
> name: 边界单元特性名称  
> kind: 类型名，支持:粘滞阻尼器、支座摩阻、滑动摩擦摆(具体参考界面数据名)  
> info_x: 自由度X信息(参考界面数据，例如粘滞阻尼器为[阻尼系数,速度指数]，支座摩阻为[安装方向0/1,弹性刚度/摩擦系数,恒载支承力N])  
> info_y: 自由度Y信息,默认则不考虑该自由度  
> info_z: 自由度Z信息  
> weight: 重量（单位N）  
> pin_stiffness: 剪力销刚度  
> pin_yield: 剪力销屈服力  
> description: 说明  
```Python
# 示例代码
from qtmodel import *
mdb.add_boundary_element_property(name="边界单元特性",kind="粘滞阻尼器",info_x=[0.05,1])
```  
Returns: 无
### add_boundary_element_link
添加边界单元连接
> 参数:  
> index: 边界单元连接号  
> property_name: 边界单元特性名称  
> node_i: 起始节点  
> node_j: 终止节点  
> beta: 角度  
> node_system: 参考坐标系0-单元 1-整体  
> group_name: 边界组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_boundary_element_link(property_name="边界单元特性",node_i=1,node_j=2,group_name="边界组1")
```  
Returns: 无
### add_nodal_dynamic_load
添加节点动力荷载
> 参数:  
> index: 节点动力荷载编号,默认自动识别  
> node_id: 节点号  
> case_name: 时程工况名  
> function_name: 函数名称  
> force_type: 荷载类型 1-X 2-Y 3-Z 4-负X 5-负Y 6-负Z  
> factor: 系数  
> time: 到达时间  
```Python
# 示例代码
from qtmodel import *
mdb.add_nodal_dynamic_load(node_id=1,case_name="时程工况1",function_name="函数1",time=10)
```  
Returns: 无
### add_ground_motion
添加地面加速度
> 参数:  
> case_name: 工况名称  
> info_x: X方向时程分析函数信息列表(函数名,系数,到达时间)  
> info_y: Y方向时程分析函数信息列表  
> info_z: Z方向时程分析函数信息列表  
```Python
# 示例代码
from qtmodel import *
mdb.add_ground_motion(case_name="时程工况1",info_x=("函数名",1,10))
```  
Returns: 无
### add_time_history_case
添加时程工况
> 参数:  
> index: 时程工况编号,默认自动识别  
> name: 时程工况名  
> description: 描述  
> analysis_kind: 分析类型(0-线性 1-边界非线性)  
> nonlinear_groups: 非线性结构组列表  
> duration: 分析时间  
> time_step: 分析时间步长  
> min_step: 最小收敛步长  
> tolerance: 收敛容限  
> damp_type: 组阻尼类型(0-不计阻尼 1-单一阻尼 2-组阻尼)  
> single_damping: 单一阻尼信息列表(周期1,阻尼比1,周期2,阻尼比2)  
> group_damping: 组阻尼信息列表[(材料名1,周期1,周期2,阻尼比),(材料名2,周期1,周期2,阻尼比)...]  
```Python
# 示例代码
from qtmodel import *
mdb.add_time_history_case(name="时程工况1",analysis_kind=0,duration=10,time_step=0.02,damp_type=2,
group_damping=[("材料1",8,1,0.05),("材料2",8,1,0.05),("材料3",8,1,0.02)])
```  
Returns: 无
### add_time_history_function
添加时程函数
> 参数:  
> name: 名称  
> factor: 放大系数  
> kind: 0-无量纲 1-加速度 2-力 3-力矩  
> function_info: 函数信息[(时间1,数值1),(时间2,数值2)]  
```Python
# 示例代码
from qtmodel import *
mdb.add_time_history_function(name="时程函数1",factor=1,function_info=[(0,0),(0.02,0.1),[0.04,0.3]])
```  
Returns: 无
##  温度与制造偏差荷载
### add_deviation_parameter
添加制造误差
> 参数:  
> name:名称  
> parameters:参数列表  
> _梁杆单元为[轴向,I端X向转角,I端Y向转角,I端Z向转角,J端X向转角,J端Y向转角,J端Z向转角]  
> _板单元为[X向位移,Y向位移,Z向位移,X向转角,Y向转角]  
```Python
# 示例代码
from qtmodel import *
mdb.add_deviation_parameter(name="梁端制造误差",parameters=[1,0,0,0,0,0,0])
mdb.add_deviation_parameter(name="板端制造误差",parameters=[1,0,0,0,0])
```  
Returns: 无
### add_deviation_load
添加制造误差荷载
> 参数:  
> element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串  
> case_name:荷载工况名  
> parameters:参数名列表  
> _梁杆单元为制造误差参数名称  
> _板单元为[I端误差名,J端误差名,K端误差名,L端误差名]  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_deviation_load(element_id=1,case_name="工况1",parameters="梁端误差")
mdb.add_deviation_load(element_id=2,case_name="工况1",parameters=["板端误差1","板端误差2","板端误差3","板端误差4"])
```  
Returns: 无
### add_custom_temperature
添加梁自定义温度
> 参数:  
> element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串  
> case_name:荷载工况名  
> group_name:指定荷载组,后续升级开放指定荷载组删除功能  
> orientation: 1-局部坐标z 2-局部坐标y  
> temperature_data:自定义数据[(参考位置1-顶 2-底,高度,温度)...]  
```Python
# 示例代码
from qtmodel import *
mdb.add_custom_temperature(case_name="荷载工况1",element_id=1,orientation=1,temperature_data=[(1,1,20),(1,2,10)])
```  
Returns: 无
### add_element_temperature
添加单元温度
> 参数:  
> element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串  
> case_name:荷载工况名  
> temperature:最终温度  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_element_temperature(element_id=1,case_name="自重",temperature=1,group_name="默认荷载组")
```  
Returns: 无
### add_system_temperature
添加系统温度
> 参数:  
> case_name:荷载工况名  
> temperature:最终温度  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_system_temperature(case_name="荷载工况",temperature=20,group_name="默认荷载组")
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
### add_beam_section_temperature
添加梁截面温度
> 参数:  
> element_id:单元编号，支持整数或整数型列表且支持XtoYbyN形式字符串  
> case_name:荷载工况名  
> code_index:规范编号  (1-公路规范2015  2-美规2017)  
> sec_type:截面类型(1-混凝土 2-组合梁)  
> t1:温度1  
> t2:温度2  
> t3:温度3  
> t4:温度4  
> thick:厚度  
> group_name:荷载组名  
```Python
# 示例代码
from qtmodel import *
mdb.add_beam_section_temperature(element_id=1,case_name="工况1",code_index=1,sec_type=1,t1=-4.2,t2=-1)
```  
Returns: 无
### add_index_temperature
添加指数温度
> 参数:  
> element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串  
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
##  施工阶段操作
### add_construction_stage
添加施工阶段信息
> 参数:  
> name:施工阶段信息  
> duration:时长  
> active_structures:激活结构组信息 [(结构组名,龄期,安装方法,计自重施工阶段id),...]  
> _计自重施工阶段id 0-不计自重,1-本阶段 n-第n阶段(可能用到尚未添加的施工阶段请先添加)  
> _安装方法 1-变形法 2-无应力法 3-接线法 4-切线法  
> delete_structures:钝化结构组信息 [结构组1，结构组2,...]  
> active_boundaries:激活边界组信息 [(边界组1，位置),...]  
> _位置 0-变形前 1-变形后  
> delete_boundaries:钝化边界组信息 [边界组1，边界组2,...]  
> active_loads:激活荷载组信息 [(荷载组1,时间),...]  
> _时间 0-开始 1-结束  
> delete_loads:钝化荷载组信息 [(荷载组1,时间),...]  
> _时间 0-开始 1-结束  
> temp_loads:临时荷载信息 [荷载组1，荷载组2,..]  
> index:施工阶段插入位置,从0开始,默认添加到最后  
> tendon_cancel_loss:钝化预应力单元后预应力损失  
> constraint_cancel_type:钝化梁端约束释放计算方法1-变形法 2-无应力法  
```Python
# 示例代码
from qtmodel import *
mdb.add_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
```  
Returns: 无
##  荷载组合操作
### add_load_combine
添加荷载组合
> 参数:  
> index:荷载组合编号  
> name:荷载组合名  
> combine_type:荷载组合类型 1-叠加  2-判别  3-包络 4-SRss 5-AbsSum  
> describe:描述  
> combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下  
> _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合  
> _"MV"-移动荷载工况  "SM"-沉降荷载工况_ "RS"-反应谱工况 "TH"-时程分析  
```Python
# 示例代码
from qtmodel import *
mdb.add_load_combine(name="荷载组合1",combine_type=1,describe="无",combine_info=[("CS","合计值",1),("CS","恒载",1)])
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
##  荷载工况操作
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
### add_load_case
添加荷载工况
> 参数:  
> name:工况名  
> case_type:荷载工况类型  
> _"施工阶段荷载", "恒载", "活载", "制动力", "风荷载","体系温度荷载","梯度温度荷载",  
> _"长轨伸缩挠曲力荷载", "脱轨荷载", "船舶撞击荷载","汽车撞击荷载","长轨断轨力荷载", "用户定义荷载"  
```Python
# 示例代码
from qtmodel import *
mdb.add_load_case(name="工况1",case_type="施工阶段荷载")
```  
Returns: 无
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
##  分析设置
### update_project_setting
更新总体设置
> 参数:  
> project: 项目名  
> company: 公司名  
> designer: 设计人员  
> reviewer: 复核人员  
> date_time: 时间  
> gravity: 重力加速度 (m/s²)  
> temperature: 设计温度 (摄氏度)  
> description: 说明  
```Python
# 示例代码
from qtmodel import *
mdb.update_project_setting(project="项目名",gravity=9.8,temperature=20)
```  
Returns: 无
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
> other_stage_name: 计算至其他阶段时名称  
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
mdb.update_construction_stage_setting(do_analysis=True, to_end_stage=False, other_stage_name="1",analysis_type=0,
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
### update_time_history_setting
更新时程分析设置
> 参数:  
> do_analysis:是否进行反应谱分析  
> output_all:是否输出所有结构组  
> groups: 结构组列表  
```Python
# 示例代码
from qtmodel import *
mdb.update_time_history_setting(do_analysis=True,output_all=True)
```  
Returns: 无
### update_bulking_setting
更新屈曲分析设置
> 参数:  
> do_analysis:是否进行反应谱分析  
> mode_count:模态数量  
> stage_id: 指定施工阶段号(默认选取最后一个施工阶段)  
> calculate_kind: 1-计为不变荷载 2-计为可变荷载  
> stressed:是否指定施工阶段末的受力状态  
> constant_cases: 不变荷载工况名称集合  
> variable_cases: 可变荷载工况名称集合(必要参数)  
```Python
# 示例代码
from qtmodel import *
mdb.update_bulking_setting(do_analysis=True,mode_count=3,variable_cases=["工况1","工况2"])
```  
Returns: 无
