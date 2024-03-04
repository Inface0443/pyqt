from __main__ import qt_model
from .qt_keyword import *
from .res_db import *


class Odb:
    """
    Odb类负责获取后处理信息
    """

    @staticmethod
    def __get_force_i(force_info):
        return [force_info.INodeForce.Fx, force_info.INodeForce.Fy, force_info.INodeForce.Fz,
                force_info.INodeForce.Mx, force_info.INodeForce.My, force_info.INodeForce.Mz]

    @staticmethod
    def __get_force_j(force_info):
        return [force_info.INodeForce.Fx, force_info.INodeForce.Fy, force_info.INodeForce.Fz,
                force_info.INodeForce.Mx, force_info.INodeForce.My, force_info.INodeForce.Mz]

    @staticmethod
    def get_beam_force(beam_id=1, stage_id=1, result_kind=RES_MAIN, increment_type=TYP_TOTAL):
        """
        获取梁单元内力,支持单个节点和节点列表
        Args:
            beam_id: 梁单元号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型
            increment_type: 增量和全量

        Returns:
            FrameForce
        """
        if type(beam_id) == int:
            bf_list = qt_model.GetBeamForce([beam_id], stage_id, result_kind, increment_type)
            return FrameElementForce(beam_id, Odb.__get_force_i(bf_list[0]), Odb.__get_force_j(bf_list[0]))
        elif type(beam_id) == list:
            bf_list = qt_model.GetBeamForce(beam_id, stage_id, result_kind, increment_type)
            list_res = []
            for item in bf_list:
                list_res.append(FrameElementForce(item.ElementId, Odb.__get_force_i(item), Odb.__get_force_j(item)))
            return list_res

    @staticmethod
    def get_cable_force(cable_id=1, stage_id=1, result_kind=RES_MAIN, increment_type=TYP_TOTAL):
        """
        获取索单元内力,支持单个节点和节点列表
        Args:
            cable_id: 索单元号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型
            increment_type: 增量和全量

        Returns:
            FrameForce
        """
        if type(cable_id) == int:
            bf_list = qt_model.GetCableForce([cable_id], stage_id, result_kind, increment_type)
            return FrameElementForce(cable_id, Odb.__get_force_i(bf_list[0]), Odb.__get_force_j(bf_list[0]))
        elif type(cable_id) == list:
            bf_list = qt_model.GetCableForce(cable_id, stage_id, result_kind, increment_type)
            list_res = []
            for item in bf_list:
                list_res.append(FrameElementForce(item.ElementId, Odb.__get_force_i(item), Odb.__get_force_j(item)))
            return list_res

    @staticmethod
    def get_link_force(cable_id=1, stage_id=1, result_kind=RES_MAIN, increment_type=TYP_TOTAL):
        """
        获取桁架单元内力,支持单个节点和节点列表
        Args:
            cable_id: 桁架单元号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型
            increment_type: 增量和全量

        Returns:
            FrameForce
        """
        if type(cable_id) == int:
            bf_list = qt_model.GetLinkForce([cable_id], stage_id, result_kind, increment_type)
            return FrameElementForce(cable_id, Odb.__get_force_i(bf_list[0]), Odb.__get_force_j(bf_list[0]))
        elif type(cable_id) == list:
            bf_list = qt_model.GetLinkForce(cable_id, stage_id, result_kind, increment_type)
            list_res = []
            for item in bf_list:
                list_res.append(FrameElementForce(item.ElementId, Odb.__get_force_i(item), Odb.__get_force_j(item)))
            return list_res
