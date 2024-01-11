from __main__ import qt_model
from .qt_keyword import *
from qtcore import BeamForce


class Odb:
    @staticmethod
    def get_beam_force(beam_id=1, stage_id=1, result_kind=RES_MAIN, increment_type=TOTAL):
        """
        获取梁单元内力
        Args:
            beam_id: 梁单元号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型
            increment_type: 增量和全量

        Returns:

        """
        beam_force_net = qt_model.GetBeamForce(beam_id, stage_id, result_kind, increment_type)
        return BeamForce(beam_id,)
