# -*- coding: utf-8 -*-
import sys
module_path = r'C:\Users\Robert\Desktop\MyWork\Python建模'
sys.path.append(rf"{module_path}")
from qtmodel import *
mdb.set_url("http://10.33.176.44:61076/")
mdb.set_version("1.2.4")
mdb.initial()
# 收缩徐变材料
# 截面数据
mdb.add_section(index=1,name="新建混凝土箱梁1",box_num=3,box_height=2,sec_type="混凝土箱梁",sec_info=[0.2,0.4,0.1,0.13,3,1,2,1,0.02,0,12,5,6,0.28,0.3,0.5,0.5,0.5,0.2],symmetry=True,chamfer_info = ["1,0.2,0.1,0.2","0.4,0.2","0.5,0.15,0.3,0.2","0.5,0.2"],shear_consider=True,bias_type="中心")
mdb.add_section(index=2,name="新建边腹板截面2",sec_type="箱梁边腹板",sec_info=[8,3,4,-1,2,0,0,0.2,0.4,0.28,0.5,0.3,0.5],chamfer_info=["0.5*0.3","1*0.2,0.1*0.2","0.5*0.15,0.3*0.2"],shear_consider=True,bias_type="中心")
mdb.add_section(index=3,name="新建中腹板截面3",sec_type="箱梁中腹板",sec_info=[2,2,2,2,2,0,0,0,0,0.2,0.2,0.2],chamfer_info=["1*0.2,0.1*0.2","1*0.2,0.1*0.2","0.5*0.2","0.5*0.2"],shear_consider=True,bias_type="中心")
mdb.update_model()  # 刷新截面数据
# 节点数据
mdb.update_model()  # 刷新节点数据
# 单元数据
mdb.update_model()  # 刷新单元数据
# 边界数据
mdb.update_model()  # 刷新边界数据
mdb.add_load_group("默认荷载组")
# 沉降数据
mdb.update_model()  # 刷新沉降数据
# 分析设置
mdb.update_project_setting(project="",company="",designer="",reviewer="",date_time="",gravity=9.8,temperature=0,description="")
mdb.update_global_setting(solver_type=1,calculation_type=2,thread_count=1)
mdb.update_operation_stage_setting(final_stage="")
mdb.update_non_linear_setting(non_linear_type=1,non_linear_method=1,max_loading_steps=1,max_iteration_times=30,accuracy_of_displacement=0.0001,accuracy_of_force=0.0001)
mdb.update_live_load_setting(lateral_spacing=0.1,vertical_spacing=1,eccentricity=0,displacement_calc_type=0,force_calc_type=0,reaction_calc_type=0,link_calc_type=0,constrain_calc_type=0)
mdb.update_model()  # 刷新分析设置
