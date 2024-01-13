from __main__ import qt_model
from .qt_keyword import *
from qtcore import *


class Odb:
    @staticmethod
    def get_beam_force(beam_id=1, stage_id=1, result_kind=RES_MAIN, increment_type=TYP_TOTAL):
        """
        获取梁单元内力
        Args:
            beam_id: 梁单元号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型
            increment_type: 增量和全量

        Returns:

        """
        bf_net = qt_model.GetBeamForce(beam_id, stage_id, result_kind, increment_type)
        force_i = [bf_net.INodeForce.fx, bf_net.INodeForce.fy, bf_net.INodeForce.fz, bf_net.INodeForce.mx, bf_net.INodeForce.my, bf_net.INodeForce.mz]
        force_j = [bf_net.JNodeForce.fx, bf_net.JNodeForce.fy, bf_net.JNodeForce.fz, bf_net.JNodeForce.mx, bf_net.JNodeForce.my, bf_net.JNodeForce.mz]
        return BeamForce(beam_id, force_i, force_j)
