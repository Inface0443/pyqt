class Node:
    def __init__(self, node_id: int, x: float, y: float, z: float):
        """
        节点编号和位置信息
        Args:
            node_id: 单元类型 支持 BEAM PLATE
            x: 单元节点列表
            y: 单元截面id号或板厚id号
            z: 材料号
        """
        self.node_id = node_id
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class Element:
    def __init__(self, index: int, ele_type: str, node_list: list[int], mat_id: int, sec_id: int, beta: float = 0,
                 initial_type: int = 1, initial_value: float = 0):
        """
        单元详细信息
        Args:
            index: 单元截面id号或板厚id号
            ele_type: 单元类型 支持 BEAM PLATE CABLE LINK
            node_list: 单元节点列表
            mat_id: 材料号
            sec_id: 截面号或板厚号
            beta: 贝塔角
            initial_type: 张拉类型  (仅索单元需要)
            initial_value: 张拉值  (仅索单元需要)
        """
        self.ele_type = ele_type
        self.node_list = node_list
        self.index = index
        self.mat_id = mat_id
        self.sec_id = sec_id
        self.beta = beta
        self.initial_type = initial_type
        self.initial_value = initial_value

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class Material:
    """
    材料信息
    Args:
        mat_id: 材料号
        name: 材料名称
        mat_type: 材料类型
        standard: 规范名
        database: 数据库名称
        data_info: 材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (修改和自定义需要)
        modified: 是否修改材料信息
        construct_factor: 构造系数
        creep_id: 收缩徐变号 默认-1表示不考虑收缩徐变
        f_cuk: 立方体抗压强度标准值 (自定义材料考虑收缩徐变)
    """

    def __init__(self, mat_id: int, name: str, mat_type: str, standard: str, database: str, data_info: list[float] = None,
                 modified: bool = False, construct_factor: float = 1.0, creep_id: int = -1, f_cuk: float = 0):
        self.mat_id = mat_id
        self.name = name
        self.mat_type = mat_type
        self.standard = standard
        self.database = database
        self.construct_factor = construct_factor
        self.modified = modified
        self.data_info = data_info
        self.is_creep = creep_id
        self.f_cuk = f_cuk

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class GeneralSupport:
    """
    一般支承边界信息
    Args:
        support_id: 一般支撑编号
        node_id: 节点号
        boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]  ture-固定 false-自由
        group_name: 边界组名称
        node_system: 0-整体  1-局部 (若节点未定义局部坐标系 则按照整体坐标计算)
    """
    def __init__(self, support_id: int = 1, node_id: int = 1, boundary_info: tuple[bool, bool, bool, bool, bool, bool] = None,
                 group_name: str = "默认边界组", node_system: int = 1):
        self.support_id = support_id
        self.node_id = node_id
        self.fixed_x = False if boundary_info is None else boundary_info[0]
        self.fixed_y = False if boundary_info is None else boundary_info[1]
        self.fixed_z = False if boundary_info is None else boundary_info[2]
        self.fixed_rx = False if boundary_info is None else boundary_info[3]
        self.fixed_ry = False if boundary_info is None else boundary_info[4]
        self.fixed_rz = False if boundary_info is None else boundary_info[5]
        self.group_name = group_name
        self.node_system = node_system

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()