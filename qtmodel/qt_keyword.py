# qt_model 此命名变量为桥通内置,请勿重复赋值
# 坐标系  -coordinate_system
GLB_X = 1  # 整体坐标X
GLB_Y = 2  # 整体坐标Y
GLB_Z = 3  # 整体坐标Z
LOC_X = 4  # 局部坐标X
LOC_Y = 5  # 局部坐标Y
LOC_Z = 6  # 局部坐标Z
# 钢束定位方式 -position_type
TYP_STRAIGHT = 1  # 直线
TYP_TRACK = 2  # 轨迹线
# 荷载工况类型
LD_CS = "施工阶段荷载"  # ConstructionStage
LD_DL = "恒载"  # DeadLoad
LD_LL = "活载"  # LiveLoad
LD_BF = "制动力"  # BrakingForce
LD_WL = "风荷载"  # WindLoad
LD_ST = "体系温度荷载"  # SystemTemperature
LD_GT = "梯度温度荷载"  # GradientTemperature
LD_RD = "长轨伸缩挠曲力荷载"  # RailDeformation
LD_DE = "脱轨荷载"  # Derailment
LD_SC = "船舶撞击荷载"  # ShipCollision
LD_VC = "汽车撞击荷载"  # VehicleCollision
LD_RB = "长轨断轨力荷载"  # RailBreakingForce
LD_UD = "用户定义荷载"  # UserDefine
# 截面类型 -section_type
SEC_JX = "矩形"  # [W,H]
SEC_YX = "圆形"  # [D]
SEC_YG = "圆管"  # [D,t]
SEC_XX = "箱型"  # [W,H,dw,tw,tt,tb]
SEC_SFB = "实腹八边形"  # [a,b,W,H]
SEC_KFB = "空腹八边形"  # [W,H,tw,tt,tb,a,b]
SEC_NBJ = "内八角形"  # [W,H,tw,tt,tb,a,b]
SEC_SFY = "实腹圆端形"  # [W,H]
SEC_KFY = "空腹圆端形"  # [H,W,tw,tt]
SEC_TX = "T形"  # [H,W,tw,tt]
SEC_DTX = "倒T形"  # [H,W,tw,tb]
SEC_IX = "I字形"  # [Wt,Wb,H,tw,tt,tb]
SEC_MTX = "马蹄T形"  # [H,tb,b2,b1,tt,tw,W,a2,a1]
SEC_IXH = "I字型混凝土"  # [tb,Wb,H,b2,b1,tt,Wt,tw,a2,a1]
SEC_GT = "钢管砼"  # [D,t,Es/Ec,Ds/Dc,Ts/Tc,poissonConcrete,poissonSteel]
SEC_XT = "钢箱砼"  # [W,H,dw,tw,tt,tb,Es/Ec,Ds/Dc,Ts/Tc,vC,νS]
SEC_DLG = "带肋钢箱"
SEC_DLH = "带肋H截面"
SEC_GHX1 = "钢桁箱梁1"
SEC_GHX2 = "钢桁箱梁2"
SEC_GHX3 = "钢桁箱梁3"
SEC_GZL = "钢工字型带肋"
SEC_GGL = "工字钢梁"
SEC_XGL = "箱型钢梁"
SEC_GZZ = "工字组合梁"
SEC_GXZ = "钢箱组合梁"

SEC_HXL = "混凝土箱梁"  # 参数列表(float)-[i1,i2,B0,B1,B1a,B1b,B2,B3,B4,H1,H2,H2a,H2b,T1,T2,T3,T4,R1,R2] 倒角列表(str)-[C1,C2,C3,C4]

# 钢束特性
MET_PRE = 0  # 先张
MET_POST = 1  # 后张
# 增量和全量
MET_TOTAL = 1
MET_INCREMENT = 2
# 施工阶段数据的类型
RES_MAIN = 1  # 合计
RES_CREEP = 2  # 收缩徐变效应
RES_PRE = 3  # 预应力效应
RES_DLOAD = 4  # 恒载
# 荷载组合类型
TYP_ADD = 0  # 叠加
TYP_JUDGE = 1  # 判别
TYP_ENVELOPE = 2  # 包络
