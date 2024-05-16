import math


class NodeDisplacement:
    def __init__(self, node_id, displacements: list[float]):
        if len(displacements) == 6:
            self.id = node_id
            self.dx = displacements[0]
            self.dy = displacements[1]
            self.dz = displacements[2]
            self.rx = displacements[3]
            self.rx = displacements[4]
            self.rz = displacements[5]
        else:
            raise ValueError("操作错误:  'displacements' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str


class FrameElementForce:
    def __init__(self, frame_id: int, force_i: list[float], force_j: list[float]):
        """
        单元内力构造器
        Args:
            frame_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力
        """
        if len(force_i) == 6 and len(force_j) == 6:
            self.id = frame_id
            self.force_i = Force(force_i[0], force_i[1], force_i[2], force_i[3], force_i[4], force_i[5])
            self.force_j = Force(force_j[0], force_j[1], force_j[2], force_j[3], force_j[4], force_j[5])
        else:
            raise ValueError("操作错误:  'force_i' and 'force_j' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str


class FrameElementStress:
    def __init__(self, frame_id: int, stress_i: list[float], stress_j: list[float]):
        """
        单元内力构造器
        Args:
            frame_id: 单元id
            stress_i: I端单元应力 [Fx,Fy,Fz,Mx,My,Mz]
            stress_j: J端单元应力
        """
        if isinstance(frame_id, int) and len(stress_i) == 9 and len(stress_j) == 9:
            self.id = frame_id
            self.stress_i = list(stress_i)
            self.stress_j = list(stress_j)
        else:
            raise ValueError("操作错误:  'stress_i' and 'stress_j' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str


class Force:
    def __init__(self, fx, fy, fz, mx, my, mz):
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.mx = mx
        self.my = my
        self.mz = mz
        self.f_xyz = math.sqrt((self.fx * self.fx + self.fy * self.fy + self.fz * self.fz))
        self.m_xyz = math.sqrt((self.mx * self.mx + self.my * self.my + self.mz * self.mz))

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v:.3f}" for k, v in attrs.items()) + '}'
        return dict_str


class Displacement:
    def __init__(self, dx, dy, dz, rx, ry, rz):
        self.dx = dx
        self.dy = dy
        self.dz = dz
        self.rx = rx
        self.ry = ry
        self.rz = rz

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v:.3f}" for k, v in attrs.items()) + '}'
        return dict_str


class BeamStress:
    def __init__(self, top_left, top_right, bottom_left, bottom_right,
                 s_fx, smy_top, smy_bot, smz_left, smz_right):
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right
        self.s_fx = s_fx
        self.smy_top = smy_top
        self.smy_bot = smy_bot
        self.smz_left = smz_left
        self.smz_right = smz_right

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v:.3f}" for k, v in attrs.items()) + '}'
        return dict_str
