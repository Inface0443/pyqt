import json
import math
from typing import Union


class NodeDisplacement:
    """
    节点位移
    """

    def __init__(self, node_id, displacements: list[float], time: float = 0):
        self.time = time
        self.node_id = node_id
        if len(displacements) == 6:
            self.dx = displacements[0]
            self.dy = displacements[1]
            self.dz = displacements[2]
            self.rx = displacements[3]
            self.ry = displacements[4]
            self.rz = displacements[5]
        else:
            raise ValueError("操作错误:  'displacements' 列表有误")

    def __str__(self):
        obj_dict = {
            'node_id': self.node_id,
            'time': self.time,
            'dx': self.dx,
            'dy': self.dy,
            'dz': self.dz,
            'rx': self.rx,
            'ry': self.ry,
            'rz': self.rz
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class SupportReaction:
    """
    支座反力
    """

    def __init__(self, node_id: int, force: list[float], time: float = 0):
        self.node_id = node_id
        self.time = time
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
        obj_dict = {
            'node_id': self.node_id,
            'time': self.time,
            'fx': self.fx,
            'fy': self.fy,
            'fz': self.fz,
            'mx': self.mx,
            'my': self.my,
            'mz': self.mz
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class BeamElementForce:
    """
    梁单元内力
    """

    def __init__(self, element_id: int, force_i: list[float], force_j: list[float], time: float = 0):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            time: 时程分析时间
        """
        self.element_id = element_id
        self.time = time
        if len(force_i) == 6 and len(force_j) == 6:
            self.force_i = Force(*force_i)
            self.force_j = Force(*force_j)
        else:
            raise ValueError("操作错误:  'force_i' and 'force_j' 列表有误")

    def __str__(self):
        obj_dict = {
            'element_id': self.element_id,
            'time': self.time,
            'force_i': self.force_i.__str__(),
            'force_j': self.force_j.__str__()
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class TrussElementForce:
    """
    桁架单元内力
    """

    def __init__(self, element_id: int, force_i: list[float], force_j: list[float], time: float = 0):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            time: 时程分析结果时间
        """
        self.element_id = element_id
        self.time = time
        if len(force_i) == 6 and len(force_j) == 6:
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
        obj_dict = {
            'element_id': self.element_id,
            'time': self.time,
            'Ni': self.Ni,
            'Fxi': self.Fxi,
            'Fyi': self.Fyi,
            'Fzi': self.Fzi,
            'Nj': self.Nj,
            'Fxj': self.Fxj,
            'Fyj': self.Fyj,
            'Fzj': self.Fzj
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class ShellElementForce:
    """
    板单元内力
    """

    def __init__(self, element_id: int, force_i: list[float], force_j: list[float],
                 force_k: list[float], force_l: list[float], time: float = 0):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_k: K端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_l: L端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            time: 时程分析时间
        """
        self.element_id = element_id
        self.time = time
        if len(force_i) == 6 and len(force_i) == 6 and len(force_k) == 6 and len(force_l) == 6:
            self.force_i = Force(*force_i)
            self.force_j = Force(*force_j)
            self.force_k = Force(*force_k)
            self.force_l = Force(*force_l)

        else:
            raise ValueError("操作错误:  内力列表有误")

    def __str__(self):
        obj_dict = {
            'element_id': self.element_id,
            'time': self.time,
            'force_i': self.force_i.__str__(),
            'force_j': self.force_j.__str__(),
            'force_k': self.force_k.__str__(),
            'force_l': self.force_l.__str__()
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class CompositeElementForce:
    """
    组合梁单元内力
    """

    def __init__(self, element_id: int, force_i: list[float], force_j: list[float], shear_force: float,
                 main_force_i: list[float], main_force_j: list[float],
                 sub_force_i: list[float], sub_force_j: list[float],
                 is_composite: bool):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            main_force_i: 主材I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            main_force_j: 主材J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            sub_force_i: 辅材I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            sub_force_j: 辅材J端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            is_composite: 是否结合
            shear_force: 接合面剪力
        """
        if len(force_i) == 6 and len(force_j) == 6:
            self.element_id = element_id
            self.force_i = Force(*force_i)
            self.force_j = Force(*force_j)
            self.shear_force = shear_force
            # 运营阶段下述信息全部为0
            self.main_force_i = Force(*main_force_i)
            self.main_force_j = Force(*main_force_j)
            self.sub_force_i = Force(*sub_force_i)
            self.sub_force_j = Force(*sub_force_j)
            self.is_composite = is_composite
        else:
            raise ValueError("操作错误:  'force_i' and 'force_j' 列表有误")

    def __str__(self):
        obj_dict = {
            'element_id': self.element_id,
            'force_i': self.force_i.__str__(),
            'force_j': self.force_j.__str__()
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


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
            self.element_id = element_id
            self.stress_i = BeamStress(*stress_i)
            self.stress_j = BeamStress(*stress_j)
        else:
            raise ValueError("操作错误:  单元应力列表有误")

    def __str__(self):
        obj_dict = {
            'element_id': self.element_id,
            'stress_i': self.stress_i.__str__(),
            'stress_j': self.stress_j.__str__()
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class ShellElementStress:
    """
    板架单元应力
    """

    def __init__(self, element_id: int, stress_i_top: list[float], stress_j_top: list[float],
                 stress_k_top: list[float], stress_l_top: list[float], stress_i_bot: list[float],
                 stress_j_bot: list[float], stress_k_bot: list[float], stress_l_bot: list[float]):
        """
        单元内力构造器
        Args:
            element_id: 单元id
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
            self.element_id = element_id
            self.stress_i_top = ShellStress(*stress_i_top)
            self.stress_j_top = ShellStress(*stress_j_top)
            self.stress_k_top = ShellStress(*stress_k_top)
            self.stress_l_top = ShellStress(*stress_l_top)
            self.stress_i_bot = ShellStress(*stress_i_bot)
            self.stress_j_bot = ShellStress(*stress_j_bot)
            self.stress_k_bot = ShellStress(*stress_k_bot)
            self.stress_l_bot = ShellStress(*stress_l_bot)
        else:
            raise ValueError("操作错误:  单元应力列表有误")

    def __str__(self):
        obj_dict = {
            'element_id': self.element_id,
            'stress_i_top': self.stress_i_top.__str__(),
            'stress_j_top': self.stress_j_top.__str__(),
            'stress_k_top': self.stress_k_top.__str__(),
            'stress_l_top': self.stress_l_top.__str__(),
            'stress_i_bot': self.stress_i_bot.__str__(),
            'stress_j_bot': self.stress_j_bot.__str__(),
            'stress_k_bot': self.stress_k_bot.__str__(),
            'stress_l_bot': self.stress_l_bot.__str__()
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class TrussElementStress:
    """
    桁架单元应力
    """

    def __init__(self, element_id: int, si: float, sj: float):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            si: I端单元应力
            sj: J端单元应力
        """
        self.element_id = element_id
        self.Si = si
        self.Sj = sj

    def __str__(self):
        obj_dict = {
            'element_id': self.element_id,
            'Si': self.Si,
            'Sj': self.Sj
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class CompositeBeamStress:
    """
        梁单元应力
        """

    def __init__(self, element_id: int, main_stress_i: list[float], main_stress_j: list[float],
                 sub_stress_i: list[float], sub_stress_j: list[float]):
        """
        单元内力构造器
        Args:
            element_id: 单元id
            main_stress_i: 主材I端单元应力 [top_left, top_right, bot_left, bot_right, sfx, smz_left, smz_right, smy_top, smy_bot]
            main_stress_j: 主材J端单元应力  [top_left, top_right, bot_left, bot_right, sfx, smz_left, smz_right, smy_top, smy_bot]
            sub_stress_i: 辅材I端单元应力  [top_left, top_right, bot_left, bot_right, sfx, smz_left, smz_right, smy_top, smy_bot]
            sub_stress_j: 辅材J端单元应力  [top_left, top_right, bot_left, bot_right, sfx, smz_left, smz_right, smy_top, smy_bot]
        """
        if len(main_stress_i) == 9 and len(main_stress_j) == 9 and len(sub_stress_i) == 9 and len(sub_stress_j) == 9:
            self.element_id = element_id
            self.main_stress_i = BeamStress(*main_stress_i)
            self.main_stress_j = BeamStress(*main_stress_j)
            self.sub_stress_i = BeamStress(*sub_stress_i)
            self.sub_stress_j = BeamStress(*sub_stress_j)
        else:
            raise ValueError("操作错误:  单元应力列表有误")

    def __str__(self):
        obj_dict = {
            'element_id': self.element_id,
            'main_stress_i': self.main_stress_i.__str__(),
            'main_stress_j': self.main_stress_j.__str__(),
            'sub_stress_i': self.sub_stress_i.__str__(),
            'sub_stress_j': self.sub_stress_j.__str__(),
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


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

    def __repr__(self):
        return self.__str__()


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
        obj_dict = {
            'sx': self.sx,
            'sy': self.sy,
            'sxy': self.sxy,
            's1': self.s1,
            's2': self.s2
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


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

    def __repr__(self):
        return self.__str__()


class ElasticLinkForce:
    """
    弹性连接内力
    """

    def __init__(self, link_id: int, force: list[float]):
        """
        弹性连接内力构造器
        Args:
            link_id: 弹性连接id
            force: 弹性连接内力 [Fx,Fy,Fz,Mx,My,Mz]
        """
        self.link_id = link_id
        if len(force) == 6:
            self.force = Force(*force)
        else:
            raise ValueError("操作错误:  'force' 列表有误")

    def __str__(self):
        obj_dict = {
            'link_id': self.link_id,
            'force': self.force.__str__(),
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class ConstrainEquationForce:
    """
    约束方程内力
    """

    def __init__(self, equation_id: int, force: list[float]):
        """
        约束方程内力构造器
        Args:
            equation_id: 约束方程id
            force: 约束方程内力 [Fx,Fy,Fz,Mx,My,Mz]
        """
        self.equation_id = equation_id
        if len(force) == 6:
            self.force = Force(*force)
        else:
            raise ValueError("操作错误:  'force' 列表有误")

    def __str__(self):
        obj_dict = {
            'equation_id': self.equation_id,
            'force': self.force.__str__(),
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class CableLengthResult:
    """
    用于存储无应力索长及相关几何信息
    """

    def __init__(self, element_id: int, unstressed_length: float,
                 cos_a_xi: float = 0, cos_a_yi: float = 0, cos_a_zi: float = 0,
                 cos_a_xj: float = 0, cos_a_yj: float = 0, cos_a_zj: float = 0,
                 dx: float = 0, dy: float = 0, dz: float = 0):
        """
        构造函数
        Args:
            element_id: 单元号
            unstressed_length: 无应力索长
            cos_a_xi: 索I端沿着x坐标的余弦
            cos_a_yi: 索I端沿着y坐标的余弦
            cos_a_zi: 索I端沿着z坐标的余弦
            cos_a_xj: 索J端沿着x坐标的余弦
            cos_a_yj: 索J端沿着y坐标的余弦
            cos_a_zj: 索J端沿着z坐标的余弦
            dx: 索JI端沿x坐标距离
            dy: 索JI端沿y坐标距离
            dz: 索JI端沿z坐标距离
        """
        self.element_id = element_id
        self.unstressed_length = unstressed_length
        self.cos_a_xi = cos_a_xi
        self.cos_a_yi = cos_a_yi
        self.cos_a_zi = cos_a_zi
        self.cos_a_xj = cos_a_xj
        self.cos_a_yj = cos_a_yj
        self.cos_a_zj = cos_a_zj
        self.dx = dx
        self.dy = dy
        self.dz = dz

    def __str__(self):
        obj_dict = {
            'element_id': self.element_id,
            'unstressed_length': self.unstressed_length,
            'cos_a_xi': self.cos_a_xi,
            'cos_a_yi': self.cos_a_yi,
            'cos_a_zi': self.cos_a_zi,
            'cos_a_xj': self.cos_a_xj,
            'cos_a_yj': self.cos_a_yj,
            'cos_a_zj': self.cos_a_zj,
            'dx': self.dx,
            'dy': self.dy,
            'dz': self.dz
        }
        return str(obj_dict)

    def __repr__(self):
        return self.__str__()


class FreeVibrationResult:
    """
    用于自振周期和频率结果输出
    """

    def __init__(self, mode: int, angel_frequency: float, participate_mass: list[float],
                 sum_participate_mass: list[float],
                 participate_factor: list[float]):
        self.mode = mode
        self.angel_frequency = angel_frequency
        self.engineering_frequency = angel_frequency * 0.159
        self.participate_factor = participate_factor
        self.participate_mass = participate_mass
        self.sum_participate_mass = sum_participate_mass

    def __str__(self):
        obj_dict = {
            'mode': self.mode,
            'angel_frequency': self.angel_frequency,
            'engineering_frequency': self.engineering_frequency,
            'participate_mass': self.participate_mass,
            'sum_participate_mass': self.sum_participate_mass,
            'participate_factor': self.participate_factor,
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class ElasticBucklingResult:
    """
    用于弹性屈曲分析特征值结果
    """

    def __init__(self, mode: int, eigenvalue: float):
        self.mode = mode
        self.eigenvalue = eigenvalue

    def __str__(self):
        obj_dict = {
            'mode': self.mode,
            'eigenvalue': self.eigenvalue,
        }
        return obj_dict

    def __repr__(self):
        return self.__str__()


class TendonLossResult:
    """
    预应力钢筋损失（简化）
    对应 C# PreStressBarLoss:
      - BarId                → bar_id
      - BeamId               → beam_id
      - BeamEndMark          → position
      - EffectiveStress      → effective_s
      - InstantaneousLoss    → instance_s
      - ExceptInstantaneous  → except_s
      - Effective/Instantaneous Ratio → ratio
    """

    def __init__(
            self,
            tendon_name: str,
            beam_id: int,
            position: Union[str, int],
            eff_s: float,
            inst_s: float,
            except_s: float
    ):
        self.tendon_name = tendon_name
        self.beam_id = beam_id
        self.position = position  # 例如: 'I'/'J' 或 1/2
        self.effective_s = float(eff_s)  # 考虑所有损失后的应力
        self.instance_s = float(inst_s)  # 排除瞬时损失后的应力（你的 C# 字段名语义如此）
        self.except_s = float(except_s)  # 弹性变形/收缩徐变/松弛 的合计损失（排除瞬时）

        # 对应 C# 的 EffectiveToInstantaneousLossRatio
        self.ratio = (self.effective_s / self.instance_s) if abs(self.instance_s) > 0.0 else 0.0

    def to_dict(self):
        return {
            "tendon_name": self.tendon_name,
            "beam_id": self.beam_id,
            "position": self.position,
            "effective_s": self.effective_s,
            "instance_s": self.instance_s,
            "except_s": self.except_s,
            "ratio": self.ratio,
        }

    def __str__(self):
        # 保持可读输出，同时兼容中文
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def __repr__(self):
        # 与 __str__ 一致，便于调试打印
        return self.__str__()


class TendonLengthResult:
    """
    预应力伸长量结果
    """
    def __init__(
            self,
            tendon_name: str,
            start_stage: int,
            stress_length: float,
            un_stress_length: float,
            effect_stress_i: float,
            effect_stress_j: float,
            elongation_i: float,
            elongation_j: float,
            elongation: float
    ):
        self.tendon_name = tendon_name
        self.start_stage = start_stage
        self.stress_length = stress_length
        self.un_stress_length = un_stress_length
        self.effect_stress_i = effect_stress_i
        self.effect_stress_j = effect_stress_j
        self.elongation_i = elongation_i
        self.elongation_j = elongation_j
        self.elongation = elongation

    def to_dict(self):
        return {
            "tendon_name": self.tendon_name,
            "start_stage": self.start_stage,
            "stress_length": self.stress_length,
            "un_stress_length": self.un_stress_length,
            "effect_stress_i": self.effect_stress_i,
            "effect_stress_j": self.effect_stress_j,
            "elongation_i": self.elongation_i,
            "elongation_j": self.elongation_j,
            "elongation": self.elongation,
        }

    def __str__(self):
        # 保持可读输出，同时兼容中文
        return json.dumps(self.to_dict(), ensure_ascii=False)

    def __repr__(self):
        # 与 __str__ 一致，便于调试打印
        return self.__str__()
