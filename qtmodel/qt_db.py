class Node:
    """
    用于反应模型节点位置信息
    """
    def __init__(self, node_id: int, x: float, y: float, z: float):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str


# class Element:
#     def __init__(self):