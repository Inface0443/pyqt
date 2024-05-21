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


class Element:
    def __init__(self, ele_type: str = "BEAM", node_list: list[int] = None, sec_id: int = 1, mat_id: int = 1, beta: float = 0,
                 initial_type: int = 1, initial_value: float = 0):
        """
        单元详细信息
        Args:
            ele_type: 单元类型 支持 BEAM PLATE
            node_list: 单元节点列表
            sec_id: 单元截面id号或板厚id号
            mat_id: 材料号
            beta: 贝塔角
            initial_type: 张拉类型  (仅索单元需要)
            initial_value: 张拉值  (仅索单元需要)
        """
        self.ele_type = ele_type
        self.node_list = node_list
        self.sec_id = sec_id
        self.mat_id = mat_id
        self.beta = beta
        self.initial_type = 1
        self.initial_value = 0
        self.initial_type = 1
        self.initial_value = 0

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str
