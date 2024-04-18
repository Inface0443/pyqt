import math


class FrameElementForce:
    def __init__(self, frame_id, force_i, force_j):
        """
        单元内力构造器
        Args:
            frame_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力
        """
        if isinstance(frame_id, int) and len(force_i) == 6 and len(force_j) == 6:
            self.id = frame_id
            self.force_i = Force(force_i[0], force_i[1], force_i[2], force_i[3], force_i[4], force_i[5])
            self.force_j = Force(force_j[0], force_j[1], force_j[2], force_j[3], force_j[4], force_j[5])
        else:
            raise ValueError("Invalid input: 'id' must be an integer, and 'force_i' and 'force_j' must be lists of length 6.")

    def __str__(self):
        return f"BeamId:{self.id}\nforce_i: {self.force_i}\nforce_j: {self.force_j}"


class FrameElementStress:
    def __init__(self, frame_id, force_i, force_j):
        """
        单元内力构造器
        Args:
            frame_id: 单元id
            force_i: I端单元内力 [Fx,Fy,Fz,Mx,My,Mz]
            force_j: J端单元内力
        """
        if isinstance(frame_id, int) and len(force_i) == 6 and len(force_j) == 6:
            self.id = frame_id
            self.force_i = list(force_i)
            self.force_j = list(force_j)
        else:
            raise ValueError("Invalid input: 'id' must be an integer, and 'force_i' and 'force_j' must be lists of length 6.")

    def __str__(self):
        return f"FrameId:{self.id}\nForceI: {self.force_i}\nForceJ: {self.force_j}"


class Force:
    def __init__(self, fx, fy, fz, mx, my, mz):
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.mx = mx
        self.my = my
        self.mz = mz
        self.fxyz = math.sqrt((self.fx * self.fx + self.fy * self.fy + self.fz * self.fz))
        self.mxyz = math.sqrt((self.mx * self.mx + self.my * self.my + self.mz * self.mz))

    def __str__(self):
        return (f"(fx={self.fx:.3f}, fy={self.fy:.3f}, fz={self.fz:.3f}, "
                f"mx={self.mx:.3f}, my={self.my:.3f}, mz={self.mz:.3f}, "
                f"f_xyz={self.fxyz:.3f}, "
                f"m_xyz={self.mxyz:.3f})")


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
        return (f"BeamStress:\n"
                f"  Force Top Left: {self.top_left:.3f}\n"
                f"  Force Top Right: {self.top_right:.3f}\n"
                f"  Force Bottom Left: {self.bottom_left:.3f}\n"
                f"  Force Bottom Right: {self.bottom_right:.3f}\n"
                f"  Force X: {self.s_fx:.3f}\n"
                f"  Moment Y Top: {self.smy_top:.3f}\n"
                f"  Moment Y Bottom: {self.smy_bot:.3f}\n"
                f"  Moment Z Left: {self.smz_left:.3f}\n"
                f"  Moment Z Right: {self.smz_right:.3f}")

    @staticmethod
    def test_print():
        print("yes")
