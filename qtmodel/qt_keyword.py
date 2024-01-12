# qt_model 此命名变量为桥通内置,请勿重复赋值
# 坐标系  -coordinate_system
GLB_X = 1
GLB_Y = 2
GLB_Z = 3
LOC_X = 4
LOC_Y = 5
LOC_Z = 6
# 钢束定位方式 -position_type
TYP_STRAIGHT = 1
TYP_TRACK = 2
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
SEC_JX = "矩形"
SEC_YX = "圆形"
SEC_YG = "圆管"
SEC_XX = "箱型"
SEC_SFB = "实腹八边形"
SEC_KFB = "空腹八边形"
SEC_NBJ = "内八角形"
SEC_SFY = "实腹圆端形"
SEC_KFY = "空腹圆端形"
SEC_TX = "T形"
SEC_DTX = "倒T形"
SEC_IX = "I字形"
SEC_MTX = "马蹄T形"
SEC_IXH = "I字型混凝土"
SEC_HXL = "混凝土箱梁"
SEC_DLG = "带肋钢箱"
SEC_DLH = "带肋H截面"
SEC_GHX1 = "钢桁箱梁1"
SEC_GHX2 = "钢桁箱梁2"
SEC_GHX3 = "钢桁箱梁3"
SEC_GZL = "钢工字型带肋"
SEC_GGL = "工字钢梁"
SEC_XGL = "箱型钢梁"
SEC_GT = "钢管砼"
SEC_XT = "钢箱砼"
SEC_GZZ = "工字组合梁"
SEC_GXZ = "钢箱组合梁"
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
