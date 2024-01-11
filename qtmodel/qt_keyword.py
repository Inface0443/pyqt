# qt_model 此命名变量为软件内置,请勿重复赋值
# 坐标系  -coordinate_system
GLOBAL_X = 1
GLOBAL_Y = 2
GLOBAL_Z = 3
LOCAL_X = 4
LOCAL_Y = 5
LOCAL_Z = 6
# 钢束定位方式 -position_type
STRAIGHT = 1
TRACK = 2
# 荷载组合
CS = "施工阶段荷载"
ST = "ST"
SM = "SM"
MV = "MV"
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
PRE = 0  # 先张
POST = 1  # 后张
# 施工阶段数据的类型
RES_MAIN = 1    # 合计
RES_CREEP = 2   # 收缩徐变效应
RES_PRE = 3     # 预应力效应
RES_DLOAD = 4   # 恒载
# 增量和全量
TOTAL = 1
INCREMENT = 2
