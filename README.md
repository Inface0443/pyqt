## 建模操作
### 初始化模型
#### initial
> 初始化模型  

### 节点单元操作
#### add_structure_group
> 添加结构组  
         参数:  
            name: 结构组名  
            index: 结构组编号(非必须参数)，默认自动识别当前编号  
        

#### remove_structure_group
> 可根据结构与组名或结构组编号删除结构组，当组名和组编号均为默认则删除所有结构组  
        参数:  
            name:结构组名称  
            index:结构组编号  
        

#### add_structure_to_group
> 为结构组添加节点和/或单元  
        参数:  
             name: 结构组名  
             node_ids: 节点编号列表(可选参数)  
             element_ids: 单元编号列表(可选参数)  
          

#### remove_structure_in_group
> 为结构组删除节点和/或单元  
        参数:  
             name: 结构组名  
             node_ids: 节点编号列表(可选参数)  
             element_ids: 单元编号列表(可选参数)  
        

#### add_node
> 根据坐标信息和节点编号添加节点，默认自动识别编号  
        参数:  
             x: 节点坐标x  
             y: 节点坐标y  
             z: 节点坐标z
             index: 节点编号，默认自动识别编号 (可选参数)  
          

#### add_nodes
> 添加多个节点，可以选择指定节点编号  
        参数:  
             node_list:节点坐标信息 [[x1,y1,z1],...]或 [[id1,x1,y1,z1]...]  
          

 
#### remove_node
> 删除指定节点
        参数:
            index:节点编号
        

#### add_element
> 根据单元编号和单元类型添加单元  
        参数:  
            index:单元编号  
            ele_type:单元类型 1-梁 2-索 3-杆 4-板  
            node_ids:单元对应的节点列表 [i,j] 或 [i,j,k,l]  
            beta_angle:贝塔角  
            mat_id:材料编号  
            sec_id:截面编号  
          

#### remove_element
> 删除指定编号的单元  
        参数:  
            index: 单元编号,默认时删除所有单元  

### 材料操作
#### add_material
> 添加材料  
        参数:  
            index:材料编号,默认自动识别 (可选参数)   
            name:材料名称  
            material_type: 材料类型  
            standard_name:规范名称  
            database:数据库  
            construct_factor:构造系数  
            modified:是否修改默认材料参数,默认不修改 (可选参数)  
            modify_info:材料参数列表:[弹性模量,容重,泊松比,热膨胀系数] (可选参数)  
          
#### add_time_material
> 添加收缩徐变材料  
        参数:  
            index: 收缩徐变编号,默认自动识别 (可选参数)  
            name: 收缩徐变名  
            code_index: 收缩徐变规范索引  
            time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)  
          
#### update_material_creep
> 将收缩徐变参数连接到材料  
        参数:  
            index: 材料编号  
            creep_id: 收缩徐变编号  
            f_cuk: 材料标准抗压强度,仅自定义材料是需要输入  
          
#### remove_material
> 删除指定材料  
        参数:  
            index:材料编号，默认删除所有材料  

### 截面和板厚操作
#### add_section
> 添加截面信息  
        参数:  
             index: 截面编号,默认自动识别  
             name:截面名称  
             section_type:截面类型  
             sec_info:截面信息  
             bias_type:偏心类型  
             center_type:中心类型  
             shear_consider:考虑剪切  
             bias_point:自定义偏心点(仅自定义类型偏心需要)  
          

#### add_single_box
> 添加单项多室混凝土截面  
        参数:  
             index:截面编号，默认自动识别  
             name:截面名称  
             n:箱室数量  
             h:截面高度  
             section_info:截面信息  
             charm_info:截面倒角  
             section_info2:右半室截面信息  
             charm_info2:右半室截面倒角  
             bias_type:偏心类型  
             center_type:中心类型  
             shear_consider:考虑剪切  
             bias_point:自定义偏心点(仅自定义类型偏心需要)  
          

#### add_steel_section
> 添加钢梁截面,包括参数型钢梁截面和自定义带肋钢梁截面  
        参数:  
             index:  
             name:  
             section_type:截面类型  
             section_info:截面信息  
             rib_info:肋板信息  
             rib_place:肋板位置  
             bias_type:偏心类型  
             center_type:中心类型  
             shear_consider:考虑剪切  
             bias_point:自定义偏心点(仅自定义类型偏心需要)  
        

#### add_user_section
> 添加自定义截面,目前仅支持特性截面  
        参数:  
             index:截面编号  
             name:截面名称  
             section_type:截面类型  
             property_info: 截面特性列表
          

#### add_tapper_section
> 添加变截面,需先建立单一截面  
        参数:  
             index:截面编号  
             name:截面名称  
             begin_id:截面始端编号  
             end_id:截面末端编号  
             vary_info:截面变化信息  

#### remove_section
> 删除截面信息
        参数:
             index: 截面编号,参数为默认时删除全部截面
        
#### add_thickness
> 添加板厚  
        参数:  
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

#### remove_thickness
> 删除板厚  
        参数:  
             index:板厚编号,默认时删除所有板厚信息  
          

#### add_tapper_section_group
> 添加变截面组  
        参数:  
             ids:变截面组编号  
             name: 变截面组名  
             factor_w: 宽度方向变化阶数 线性(1.0) 非线性(!=1.0)  
             factor_h: 高度方向变化阶数 线性(1.0) 非线性(!=1.0)  
             ref_w: 宽度方向参考点 0-i 1-j   
             ref_h: 高度方向参考点 0-i 1-j  
             dis_w: 宽度方向间距  
             dis_h: 高度方向间距  
          

#### update_section_bias
> 更新截面偏心  
        参数:  
             index:截面编号  
             bias_type:偏心类型  
             center_type:中心类型  
             shear_consider:考虑剪切  
             bias_point:自定义偏心点(仅自定义类型偏心需要)  
          

#### add_boundary_group
> 新建边界组  
        参数:  
             name:边界组名  
             index:边界组编号，默认自动识别当前编号 (可选参数)  
          

#### remove_boundary_group
> 按照名称删除边界组  
         参数：  
            name: 边界组名称，默认删除所有边界组 (非必须参数)  
        Returns: 无  

#### remove_boundary
> 根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息  
         参数：  
            group_name: 边界组名  
            boundary_type: 边界类型  
            index: 边界编号  
        Returns: 无  

#### add_general_support
> 添加一般支承  
         参数：  
             index:边界编号  
             node_id:节点编号  
             boundary_info:边界信息  
             group_name:边界组名  
        Returns: 无

#### add_elastic_support
> 添加弹性支承  
         参数：  
             index:编号  
             node_id:节点编号  
             support_type:支承类型  
             boundary_info:边界信息  
             group_name:边界组  
        Returns: 无  

#### add_master_slave_link
> 添加主从约束  
         参数：  
             index:编号  
             master_id:主节点号  
             slave_id:从节点号  
             boundary_info:边界信息  
             group_name:边界组名  

#### add_elastic_link
> 添加弹性连接  
         参数：  
             index:节点编号  
             link_type:节点类型  
             start_id:起始节点号  
             end_id:终节点号  
             beta_angle:贝塔角  
             boundary_info:边界信息  
             group_name:边界组名  
             dis_ratio:距离比  
             kx:刚度  


#### dd_beam_constraint
> 添加梁端约束  
         参数：  
             index:约束编号,默认自动识别  
             beam_id:梁号  
             info_i:i端约束信息 [IsFreedX,IsFreedY,IsFreedZ,IsFreedRX,IsFreedRY,IsFreedRZ]  
             info_j:j端约束信息 [IsFreedX,IsFreedY,IsFreedZ,IsFreedRX,IsFreedRY,IsFreedRZ]  
             group_name:边界组名  

#### add_node_axis
> 添加节点坐标  
         参数：  
             index:默认自动识别  
             input_type:输入方式  
             node_id:节点号  
             coord_info:局部坐标信息 -List<float>(角度x,y,z)  -List<List<float>>(三点/向量)  

### 移动荷载
#### add_standard_vehicle
> 添加标准车辆  
         参数：  
             name:车辆荷载名称  
             standard_code:荷载规范  
             load_type:荷载类型  
             load_length:荷载长度  
             n:车厢数  

#### add_node_tandem
>添加节点纵列  
         参数：  
             name:节点纵列名  
             start_id:起始节点号  
             node_ids:节点列表   

#### add_influence_plane
>添加影响面  
         参数：  
             name:影响面名称  
             tandem_names:节点纵列名称组  

#### add_lane_line
>添加车道线  
         参数：  
             name:车道线名称  
             influence_name:影响面名称  
             tandem_name:节点纵列名  
             offset:偏移  
             direction:方向  

#### add_live_load_case
>添加移动荷载工况  
         参数：  
             name:荷载工况名  
             influence_plane:影响线名  
             span:跨度  
             sub_case:子工况信息  

#### remove_vehicle 
>删除车辆信息  
         参数：  
             index:车辆荷载编号  

#### remove_node_tandem 
>按照 节点纵列编号/节点纵列名 删除节点纵列   
         参数：    
             index:节点纵列编号   
             name:节点纵列名   

#### remove_influence_plane 
>按照 影响面编号/影响面名称 删除影响面  
         参数：  
             index:影响面编号  
             name:影响面名称  

#### remove_lane_line 
>按照 车道线编号/车道线名称 删除车道线  
         参数：
             name:车道线名称
             index:车道线编号
        Returns: 无

#### remove_live_load_case 
>删除移动荷载工况  
         参数：  
             name:移动荷载工况名   

### 钢束操作

#### add_tendon_group 
        按照名称添加钢束组，添加时可指定钢束组id  
         参数：  
            name: 钢束组名称  
            index: 钢束组编号(非必须参数)，默认自动识别  



#### remove_tendon_group 
>按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组  
         参数：  
             name:钢束组名称,默认自动识别 (可选参数)  
             index:钢束组编号,默认自动识别 (可选参数)  



#### add_tendon_property
>添加钢束特性
         参数：  
             name:钢束特性名  
             index:钢束编号,默认自动识别 (可选参数)  
             tendon_type: 0-PRE 1-POST   
             material_id: 钢材材料编号  
             duct_type: 1-金属波纹管  2-塑料波纹管  3-铁皮管  4-钢管  5-抽芯成型  
             steel_type: 1-钢绞线  2-螺纹钢筋  
             steel_detail: 钢绞线[钢束面积,孔道直径,摩阻,偏差]  螺纹钢筋[钢筋直径,钢束面积,孔道直径,摩阻,偏差,张拉方式]  
             loos_detail: 松弛信息[规范(1-公规 2-铁规),张拉方式,松弛(1-一般松弛 2-低松弛)] (仅钢绞线需要)  
             slip_info: 滑移信息[始端距离,末端距离]  


#### add_tendon_3d
>添加三维钢束  
         参数：  
             name:钢束名称  
             property_name:钢束特性名称  
             group_name:默认钢束组  
             num:根数  
             line_type:1-导线点  2-折线点  
             position_type: 定位方式 1-直线  2-轨迹线  
             control_info: 控制点信息[[x1,y1,z1,r1],[x2,y2,z2,r2]....]    
             point_insert: 直线-[x,y,z], 轨迹线-[插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id]  
             tendon_direction:直线钢束方向向量 x轴-[1,0,0] y轴-[0,1,0] (轨迹线时不用赋值)  
             rotation_angle:绕钢束旋转角度  
             track_group:轨迹线结构组名  (直线时不用赋值)  


#### remove_tendon  
>按照名称或编号删除钢束,默认时删除所有钢束  
         参数：   
             name:钢束名称    
             index:钢束编号  


#### remove_tendon_property 
>按照名称或编号删除钢束组,默认时删除所有钢束组  
         参数：  
             name:钢束组名称   
             index:钢束组编号  

#### add_nodal_mass 
>添加节点质量  
         参数：  
             node_id:节点编号  
             mass_info:[m,rmX,rmY,rmZ]  
        Returns: 无  


#### remove_nodal_mass
>删除节点质量
         参数：
             node_id:节点号
        Returns: 无


#### add_pre_stress
>添加预应力  
         参数：  
             index:编号  
             case_name:荷载工况名  
             tendon_name:钢束名  
             pre_type:预应力类型  
             force:预应力   
             group_name:边界组  

#### remove_pre_stress
>删除预应力  
         参数：  
             case_name:荷载工况  
             tendon_name:钢束组  
             group_name:边界组名  

### 荷载操作
#### add_load_group
>根据荷载组名称添加荷载组  
         参数：  
             name: 荷载组名称  
             index: 荷载组编号，默认自动识别 (可选参数)  


#### remove_load_group
>根据荷载组名称或荷载组id删除荷载组,参数为默认时删除所有荷载组  
         参数：  
             name: 荷载组名称  
             index: 荷载组编号  


#### add_nodal_force 
>添加节点荷载  
             case_name:荷载工况名  
             node_id:节点编号  
             load_info:[Fx,Fy,Fz,Mx,My,Mz]  
             group_name:荷载组名  

#### remove_nodal_force 
>删除节点荷载  
         参数：  
             case_name:荷载工况名  
             node_id:节点编号  

#### add_node_displacement 
>添加节点位移  
         参数：  
             case_name:荷载工况名  
             node_id:节点编号  
             load_info:[Dx,Dy,Dz,Rx,Ry,Rz]  
             group_name:荷载组名  


#### remove_nodal_displacement 
>删除节点位移  
         参数：  
             case_name:荷载工况名  
             node_id:节点编号  

#### add_beam_load
>添加梁单元荷载  
         参数：  
             case_name:荷载工况名  
             beam_id:单元编号  
             load_type:荷载类型  
             coordinate_system:坐标系  
             load_info:荷载信息  
             group_name:荷载组名  

#### remove_beam_load
>删除梁单元荷载  
         参数：  
             case_name:荷载工况名  
             element_id:单元号  
             load_type:荷载类型  
             group_name:边界组名  

#### add_initial_tension
>添加初始拉力  
         参数：  
             element_id:单元编号  
             case_name:荷载工况名  
             group_name:荷载组名  
             tension:初始拉力  
             tension_type:张拉类型  

#### add_cable_length_load
>添加索长张拉  
         参数：  
             element_id:单元类型  
             case_name:荷载工况名  
             group_name:荷载组名  
             length:长度  
             tension_type:张拉类型  

#### add_plate_element_load
>添加版单元荷载  
         参数：  
             element_id:单元id  
             case_name:荷载工况名  
             load_type:荷载类型   
             load_place:荷载位置  
             coord_system:坐标系  
             group_name:荷载组名  
             load_info:荷载信息  

#### add_deviation_parameter
>添加制造误差  
         参数：  
             name:名称  
             element_type:单元类型  
             parameter_info:参数列表  

#### add_deviation_load
>添加制造误差荷载  
         参数：  
             element_id:单元编号  
             case_name:荷载工况名  
             parameter_name:参数名  
             group_name:荷载组名  


#### add_element_temperature
>添加单元温度  
         参数：  
             element_id:单元编号  
             case_name:荷载工况名  
             temperature:温度  
             group_name:荷载组名  

#### add_gradient_temperature
>添加梯度温度  
             element_id:单元编号  
             case_name:荷载工况名  
             temperature:温度  
             section_oriental:截面方向  
             element_type:单元类型  
             group_name:荷载组名  

#### add_beam_section_temperature
>添加梁截面温度  
         参数：  
             element_id:单元编号  
             case_name:荷载工况名  
             paving_thick:铺设厚度  
             temperature_type:温度类型  
             paving_type:铺设类型  
             group_name:荷载组名  

#### add_index_temperature
>添加指数温度  
         参数：  
             element_id:单元编号  
             case_name:荷载工况名  
             temperature:单元类型  
             index:指数  
             group_name:荷载组名  


#### add_plate_temperature
>添加顶板温度  
         参数：  
             element_id:单元编号  
             case_name:荷载工况  
             temperature:温度  
             group_name:荷载组名  

### 沉降操作

#### add_sink_group
>添加沉降组  
         参数：  
             name: 沉降组名  
             sink: 沉降值  
             node_ids: 节点编号  

#### remove_sink_group
>按照名称删除沉降组  
         参数：  
             name:沉降组名,默认删除所有沉降组  


#### add_sink_case
>添加沉降工况  
         参数：  
             name:荷载工况名  
             sink_groups:沉降组名  


#### remove_sink_case
>按照名称删除沉降工况,不输入名称时默认删除所有沉降工况  
         参数：  
             name:沉降工况名  


#### add_concurrent_reaction
>添加并发反力组  
         参数：  
            name:结构组名


#### remove_concurrent_reaction
>删除并发反力组  


#### add_concurrent_force
>添加并发内力  


#### remove_concurrent_force
>删除并发内力  


#### add_load_case
>添加荷载工况  
         参数：  
            index:沉降工况编号  
            name:沉降名  
            load_case_type:荷载工况类型  

#### remove_load_case
>删除荷载工况,参数均为默认时删除全部荷载工况  
         参数：  
            index:荷载编号  
            name:荷载名  

### 施工阶段和荷载组合

#### add_construction_stage
>添加施工阶段信息  
         参数：  
            name:施工阶段信息  
            duration:时长  
            active_structures:激活结构组信息  
            delete_structures:钝化结构组信息  
            active_boundaries:激活边界组信息  
            delete_boundaries:钝化边界组信息  
            active_loads:激活荷载组信息  
            delete_loads:钝化荷载组信息  
            temp_loads:临时荷载信息  
            index:施工阶段编号，默认自动添加  


#### remove_construction_stage
>按照施工阶段名删除施工阶段  
         参数：  
            name:所删除施工阶段名称  


#### remove_all_construction_stage
>删除所有施工阶段  


#### add_load_combine
>添加荷载组合  
         参数：  
            name:荷载组合名  
            combine_type:荷载组合类型  
            describe:描述  
            combine_info:荷载组合信息  

#### remove_load_combine 
>删除荷载组合,参数默认时删除所有荷载组合  
         参数：  
             name:所删除荷载组合名  

### 参数说明

#### 混凝土箱梁相关参数
> 顶板坡度(i1)	0.02    -float类型  
底板坡度(i2)	0  
顶板宽(B0)	12  
悬臂宽度(B1)	3  
悬臂宽度(B1a)	1
悬臂宽度(B1b)	2  
左边腹板水平投影(B2)	1  
边室底宽(B3)	5  
中室底宽(B4)	6  
悬臂端部高(H1)	0.2  
悬臂下缘高(H2)	0.4  
悬臂下缘高(H2a)	0.1  
悬臂下缘高(H2b)	0.13  
顶板厚(T1)	0.28  
底板厚(T2)	0.3  
边腹板厚(T3)	0.5  
中腹板厚(T4)	0.5   
悬臂根部倒角(R1)	0.5  
边腹板外部下倒角(R2)	0.2  
边腹板顶部倒角(C1)	1\*0.2,0.1\*0.2   -str类型  
边腹板底部倒角(C2)	0.5\*0.15,0.3\*0.2  
中腹板顶部倒角(C3)	0.4\*0.2  
中腹板底部倒角(C4)	0.5\*0.2  

