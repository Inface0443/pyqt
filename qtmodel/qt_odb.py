from __main__ import qt_model
from .res_db import *


class Odb:
    """
    Odb类负责获取后处理信息
    """

    @staticmethod
    def _get_displacement(displacement_info):
        return [displacement_info.Dx, displacement_info.Dy, displacement_info.Dz,
                displacement_info.Rx, displacement_info.Ry, displacement_info.Rz]

    @staticmethod
    def _get_force(force_info):
        return [force_info.Fx, force_info.Fy, force_info.Fz, force_info.Mx, force_info.My, force_info.Mz]

    @staticmethod
    def _get_stress(stress_info):
        return [stress_info.TopLeft, stress_info.TopRight, stress_info.BottomLeft, stress_info.BottomRight,
                stress_info.Sfx, stress_info.SmyTop, stress_info.SmyBot, stress_info.SmzLeft, stress_info.SmzRight]

    @staticmethod
    def get_beam_force(element_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1):
        """
        获取梁单元内力,支支持单个单元和单元列表
        Args:
            element_id: 梁单元号,支持 int和 list[int]
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
        Returns:
            FrameForce
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,beam_id仅支持 int和 list[int]")
        bf_list = qt_model.GetBeamForce(element_id, stage_id, result_kind, increment_type)
        list_res = []
        for item in bf_list:
            list_res.append(FrameElementForce(item.ElementId, Odb._get_force(item.INodeForce), Odb._get_force(item.JNodeForce)))
        return list_res

    @staticmethod
    def get_cable_force(element_id, stage_id=1, result_kind=1, increment_type=1):
        """
        获取索单元内力,支持单个单元和单元列表
        Args:
            element_id: 索单元号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type:  1-全量    2-增量

        Returns:
            FrameForce
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,cable_id仅支持 int和 list[int]")
        bf_list = qt_model.GetCableForce(element_id, stage_id, result_kind, increment_type)
        list_res = []
        for item in bf_list:
            list_res.append(FrameElementForce(item.ElementId, Odb._get_force(item.INodeForce), Odb._get_force(item.JNodeForce)))
        return list_res

    @staticmethod
    def get_link_force(element_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1):
        """
        获取桁架单元内力,支持单个单元和单元列表
        Args:
            element_id: 桁架单元号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量

        Returns:
            FrameForce
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,link_id仅支持 int和 list[int]")
        bf_list = qt_model.GetLinkForce(element_id, stage_id, result_kind, increment_type)
        list_res = []
        for item in bf_list:
            list_res.append(FrameElementForce(item.ElementId, Odb._get_force(item.INodeForce), Odb._get_force(item.JNodeForce)))
        return list_res

    @staticmethod
    def get_node_displacement(node_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1):
        """
        获取节点,支持单个节点和节点列表
        Args:
            node_id: 节点号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量

        Returns:
            FrameForce
        """
        if type(node_id) != int and type(node_id) != list:
            raise TypeError("类型错误,node_id仅支持 int和 list[int]")
        bf_list = qt_model.GetNodeDisplacement(node_id, stage_id, result_kind, increment_type)
        list_res = []
        for item in bf_list:
            list_res.append(NodeDisplacement(item.ElementId, Odb._get_displacement(item.Displacement)))
        return list_res

    @staticmethod
    def get_beam_stress(element_id, stage_id: int, result_kind: int = 1, increment_type: int = 1):
        """
        获取节点,支持单个节点和节点列表
        Args:
            element_id: 单元号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量

        Returns:
            FrameForce
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,beam_id int和 list[int]")
        bs_list = qt_model.GetBeamStress(element_id, stage_id, result_kind, increment_type)
        list_res = []
        for item in bs_list:
            list_res.append(FrameElementStress(item.ElementId, Odb._get_stress(item.IBeamStress), Odb._get_stress(item.JBeamStress)))
        return list_res
