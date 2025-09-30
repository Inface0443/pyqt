# -*- coding: utf-8 -*-
from qtmodel import *
mdb.set_url("http://10.33.176.44:61076/")
mdb.set_version("1.2.3")
mdb.initial()
# 收缩徐变材料
# 材料数据
mdb.add_material(index=1,name="S355(纵梁计重)",mat_type=5,construct_factor=1,data_info=[205000000000,0,0.3,1.2E-05],creep_id=-1,f_cuk=0)
mdb.add_material(index=2,name="Strand1860",mat_type=3,standard=2,database="钢绞线1860",construct_factor=1,modified=False,data_info=[195000000000,78500,0.3,1.2E-5])
mdb.add_material(index=3,name="支座垫石",mat_type=5,construct_factor=1,data_info=[36000000000,25000,0.2,1.2E-05],creep_id=-1,f_cuk=0)
mdb.add_material(index=4,name="斜拉索",mat_type=5,construct_factor=1,data_info=[195000000000,85000,0.3,1.2E-05],creep_id=-1,f_cuk=0)
mdb.add_material(index=6,name="索塔G60",mat_type=5,construct_factor=1,data_info=[36000000000,29200,0.2,1.2E-05],creep_id=-1,f_cuk=0)
mdb.add_material(index=11,name="刚臂",mat_type=5,construct_factor=1,data_info=[2.1E+18,0,0.3,1.2E-05],creep_id=-1,f_cuk=0)
mdb.add_material(index=12,name="桩基G40",mat_type=5,construct_factor=1,data_info=[31000000000,25000,0.2,1.2E-05],creep_id=-1,f_cuk=0)
mdb.update_model()  # 刷新材料数据
# 截面数据
sec_begin={"sec_info":[6.15,4.0,0.6,0.5],"sec_property":[24.00000239999963,20.08921662927783,19.522330544220292,77.29484485908813,30.775003067600508,72.56475724399439,0.0,3.075,3.075,2.0,2.0,19.0241,0.0,3.075,2.0,-2.475,2.0,2.475,2.0,2.475,-2.0,-2.475,-2.0,-0.0,-0.0,6.15,3.9999999999999996,11.75000117504849,18.04892505540068],"shear_consider":True,"bias_type":"中心"}
sec_end={"sec_info":[5.92,4.0,0.6,0.5],"sec_property":[23.080002308000477,19.321198424070555,18.839882203653257,72.55301744789581,29.54833627897534,64.57567578733622,0.0,2.96,2.96,2.0,2.0,18.5641,0.0,2.96,2.0,-2.36,2.0,2.36,2.0,2.36,-2.0,-2.36,-2.0,0.0,0.0,5.92,4.000000000000001,11.290001129055787,16.69520167021937],"shear_consider":False,"bias_type":"中心"}
mdb.add_tapper_section(index=2,name="变截面1插值变截面-2",sec_type="实腹八边形",sec_begin=sec_begin,sec_end=sec_end,shear_consider=True)