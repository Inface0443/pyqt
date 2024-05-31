import math
import json


class NodeDisplacement:
    """
    节点位移
    """

    def __init__(self, node_id, displacements: list[float]):
        if len(displacements) == 6:
            self.id = node_id
            self.dx = displacements[0]
            self.dy = displacements[1]
            self.dz = displacements[2]
            self.rx = displacements[3]
            self.ry = displacements[4]
            self.rz = displacements[5]
        else:
            raise ValueError("操作错误:  'displacements' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'id': self.id,
            'dx': self.dx,
            'dy': self.dy,
            'dz': self.dz,
            'rx': self.rx,
            'ry': self.ry,
            'rz': self.rz
        }
        return json.dumps(obj_dict)


class SupportReaction:
    """
    支座反力
    """

    def __init__(self, support_id: int, force: list[float]):
        self.support_id = support_id
        if len(force) == 6:
            self.fx = force[0]
            self.fy = force[1]
            self.fz = force[2]
            self.mx = force[3]
            self.my = force[4]
            self.mz = force[5]
        else:
            raise ValueError("操作错误:  'force' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'support_id': self.support_id,
            'fx': self.fx,
            'fy': self.fy,
            'fz': self.fz,
            'mx': self.mx,
            'my': self.my,
            'mz': self.mz
        }
        return json.dumps(obj_dict)


class BeamElementForce:
    """
    梁单元内力
    """

    def __init__(self, element_id: int, force_i: list[float], force_j: list[float]):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
        """
        if len(force_i) == 6 and len(force_j) == 6:
            self.id = element_id
            self.force_i = Force(*force_i)
            self.force_j = Force(*force_j)
        else:
            raise ValueError("操作错误:  'force_i' and 'force_j' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将 BeamElementForce 对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'id': self.id,
            'force_i': self.force_i.to_json(),
            'force_j': self.force_j.to_json()
        }
        return json.dumps(obj_dict)


class TrussElementForce:
    """
    桁架单元内力
    """

    def __init__(self, element_id: int, force_i: list[float], force_j: list[float]):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
        """
        if len(force_i) == 6 and len(force_j) == 6:
            self.id = element_id
            self.Ni = force_i[3]
            self.Fxi = force_i[0]
            self.Fyi = force_i[1]
            self.Fzi = force_i[2]
            self.Nj = force_j[3]
            self.Fxj = force_j[0]
            self.Fyj = force_j[1]
            self.Fzj = force_j[2]
        else:
            raise ValueError("操作错误:  'stress_i' and 'stress_j' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'id': self.id,
            'Ni': self.Ni,
            'Fxi': self.Fxi,
            'Fyi': self.Fyi,
            'Fzi': self.Fzi,
            'Nj': self.Nj,
            'Fxj': self.Fxj,
            'Fyj': self.Fyj,
            'Fzj': self.Fzj
        }
        return json.dumps(obj_dict)


class ShellElementForce:
    """
    板单元内力
    """

    def __init__(self, element_id: int, force_i: list[float], force_j: list[float], force_k: list[float], force_l: list[float]):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_k: K端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_l: J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
        """
        if len(force_i) == 6 and len(force_i) == 6 and len(force_k) == 6 and len(force_l) == 6:
            self.id = element_id
            self.force_i = Force(*force_i)
            self.force_j = Force(*force_j)
            self.force_k = Force(*force_k)
            self.force_l = Force(*force_l)

        else:
            raise ValueError("操作错误:  内力列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将 ShellElementForce 对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'id': self.id,
            'force_i': self.force_i.to_json(),
            'force_j': self.force_j.to_json(),
            'force_k': self.force_k.to_json(),
            'force_l': self.force_l.to_json()
        }
        return json.dumps(obj_dict)


class BeamElementStress:
    """
    梁单元应力
    """

    def __init__(self, element_id: int, stress_i: list[float], stress_j: list[float]):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            stress_i: I端单元应力 [top_left, top_right, bot_left, bot_right, sfx, smz_left, smz_right, smy_top, smy_bot]
            stress_j: J端单元应力  [top_left, top_right, bot_left, bot_right, sfx, smz_left, smz_right, smy_top, smy_bot]
        """
        if len(stress_i) == 9 and len(stress_i) == 9:
            self.id = element_id
            self.stress_i = BeamStress(*stress_i)
            self.stress_j = BeamStress(*stress_j)
        else:
            raise ValueError("操作错误:  'stress_i' or 'stress_j' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将 BeamElementStress 对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'id': self.id,
            'stress_i': self.stress_i.to_json(),
            'stress_j': self.stress_j.to_json()
        }
        return json.dumps(obj_dict)


class ShellElementStress:
    """
    板架单元应力
    """

    def __init__(self, frame_id: int, stress_i_top: list[float], stress_j_top: list[float], stress_k_top: list[float], stress_l_top: list[float]
                 , stress_i_bot: list[float], stress_j_bot: list[float], stress_k_bot: list[float], stress_l_bot: list[float]):
        """
        单元内力构造器
        Args:
            frame_id: 单元id
            stress_i_top: I端单元上部应力 [sx,sy,sxy,s1,s2]
            stress_j_top: J端单元上部应力 [sx,sy,sxy,s1,s2]
            stress_k_top: K端单元上部应力 [sx,sy,sxy,s1,s2]
            stress_l_top: L端单元上部应力 [sx,sy,sxy,s1,s2]
            stress_i_bot: I端单元下部应力 [sx,sy,sxy,s1,s2]
            stress_j_bot: J端单元下部应力 [sx,sy,sxy,s1,s2]
            stress_k_bot: K端单元下部应力 [sx,sy,sxy,s1,s2]
            stress_l_bot: L端单元下部应力 [sx,sy,sxy,s1,s2]
        """
        if len(stress_i_top) == 5 and len(stress_j_top) == 5 \
                and len(stress_k_top) == 5 and len(stress_l_top) == 5 \
                and len(stress_i_bot) == 5 and len(stress_j_bot) == 5 \
                and len(stress_k_bot) == 5 and len(stress_l_bot) == 5:
            self.id = frame_id
            self.stress_i_top = ShellStress(*stress_i_top)
            self.stress_j_top = ShellStress(*stress_j_top)
            self.stress_k_top = ShellStress(*stress_k_top)
            self.stress_l_top = ShellStress(*stress_l_top)
            self.stress_i_bot = ShellStress(*stress_i_bot)
            self.stress_j_bot = ShellStress(*stress_j_bot)
            self.stress_k_bot = ShellStress(*stress_k_bot)
            self.stress_l_bot = ShellStress(*stress_l_bot)
        else:
            raise ValueError("操作错误:  'stress' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将 ShellElementStress 对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'id': self.id,
            'stress_i_top': self.stress_i_top.to_json(),
            'stress_j_top': self.stress_j_top.to_json(),
            'stress_k_top': self.stress_k_top.to_json(),
            'stress_l_top': self.stress_l_top.to_json(),
            'stress_i_bot': self.stress_i_bot.to_json(),
            'stress_j_bot': self.stress_j_bot.to_json(),
            'stress_k_bot': self.stress_k_bot.to_json(),
            'stress_l_bot': self.stress_l_bot.to_json()
        }
        return json.dumps(obj_dict)


class TrussElementStress:
    """
    桁架单元应力
    """

    def __init__(self, frame_id: int, stress_i: list[float], stress_j: list[float]):
        """
        单元内力构造器
        Args:
            frame_id: 单元id
            stress_i: I端单元应力
            stress_j: J端单元应力
        """
        if len(stress_i) == 9 and len(stress_j) == 9:
            self.id = frame_id
            self.Si = stress_i[0]
            self.Sj = stress_j[0]
        else:
            raise ValueError("操作错误:  'stress_i' and 'stress_j' 列表有误")

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将 TrussElementStress 对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'id': self.id,
            'Si': self.Si,
            'Sj': self.Sj
        }
        return json.dumps(obj_dict)


class Force:
    """
    用于梁单元内力和板单元内力
    """

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

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将 Force 对象转换为 JSON 格式的字典
        """
        obj_dict = {
            'fx': self.fx,
            'fy': self.fy,
            'fz': self.fz,
            'mx': self.mx,
            'my': self.my,
            'mz': self.mz,
            'f_xyz': self.f_xyz,
            'm_xyz': self.m_xyz
        }
        return obj_dict


class ShellStress:
    """
    用于板单元应力分量
    """

    def __init__(self, sx, sy, sxy, s1, s2):
        self.sx = sx
        self.sy = sy
        self.sxy = sxy
        self.s1 = s1
        self.s2 = s2

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v:.3f}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将 ShellStress 对象转换为 JSON 格式的字符串
        """
        obj_dict = {
            'sx': self.sx,
            'sy': self.sy,
            'sxy': self.sxy,
            's1': self.s1,
            's2': self.s2
        }
        return json.dumps(obj_dict)


class BeamStress:
    """
    用于梁单元应力分量
    """

    def __init__(self, top_left, top_right, bot_left, bot_right, sfx, smz_left, smz_right, smy_top, smy_bot):
        self.top_left = top_left  # 左上角应力
        self.top_right = top_right  # 右上角应力
        self.bot_left = bot_left  # 左下角应力
        self.bot_right = bot_right  # 右下角应力
        self.sfx = sfx  # 轴向应力
        self.smz_left = smz_left  # Mz引起的+y轴应力
        self.smz_right = smz_right  # Mz引起的-y轴应力
        self.smy_top = smy_top  # My引起的+z轴应力
        self.smy_bot = smy_bot  # My引起的-z轴应力

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v:.3f}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        """
        将 BeamStress 对象转换为 JSON 格式的字典
        """
        obj_dict = {
            'top_left': self.top_left,
            'top_right': self.top_right,
            'bot_left': self.bot_left,
            'bot_right': self.bot_right,
            'sfx': self.sfx,
            'smz_left': self.smz_left,
            'smz_right': self.smz_right,
            'smy_top': self.smy_top,
            'smy_bot': self.smy_bot
        }
        return obj_dict
