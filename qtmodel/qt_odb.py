from __main__ import qt_model
from .res_db import *
from .qt_db import *


class Odb:
    """
    获取模型计算结果和模型信息
    """

    # region 静力结果查看
    @staticmethod
    def get_element_stress(element_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, operation: bool = False, case_name=""):
        """
        获取单元应力,支持单个单元和单元列表
        Args:
            element_id: 单元编号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            operation: 是否为运营阶段
            case_name: 运营阶段所需荷载工况名
        example:
            mdb.get_element_stress(1,stage_id=1)
            mdb.get_element_stress([1,2,3],stage_id=1)
            mdb.get_element_stress(1,operation=True,case_name="工况名")
        Returns:
            list[ElementStress] or ElementStress
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,element_id仅支持 int和 list[int]")
        bf_list = qt_model.GetElementStress(element_id, stage_id, result_kind, increment_type, operation, case_name)
        list_res = []
        for item in bf_list:
            if item.ElementType == "BEAM":
                stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4], item.StressI[5],
                            item.StressI[6], item.StressI[7], item.StressI[8]]
                stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4], item.StressJ[5],
                            item.StressJ[6], item.StressJ[7], item.StressJ[8]]
                list_res.append(BeamElementStress(item.ElementId, stress_i, stress_j))
            elif item.ElementType == "SHELL":
                stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4]]
                stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4]]
                stress_k = [item.StressK[0], item.StressK[1], item.StressK[2], item.StressK[3], item.StressK[4]]
                stress_l = [item.StressL[0], item.StressL[1], item.StressL[2], item.StressL[3], item.StressL[4]]
                stress_i2 = [item.BotIStress[0], item.BotIStress[1], item.BotIStress[2], item.BotIStress[3], item.BotIStress[4]]
                stress_j2 = [item.BotJStress[0], item.BotJStress[1], item.BotJStress[2], item.BotJStress[3], item.BotJStress[4]]
                stress_k2 = [item.BotKStress[0], item.BotKStress[1], item.BotKStress[2], item.BotKStress[3], item.BotKStress[4]]
                stress_l2 = [item.BotLStress[0], item.BotLStress[1], item.BotLStress[2], item.BotLStress[3], item.BotLStress[4]]
                list_res.append(ShellElementStress(item.ElementId, stress_i, stress_j, stress_k, stress_l,
                                                   stress_i2, stress_j2, stress_k2, stress_l2))
            elif item.ElementType == "CABLE" or item.ElementType == "LINK":
                stress_i = [item.StressI[0], item.StressI[1], item.StressI[2], item.StressI[3], item.StressI[4], item.StressI[5],
                            item.StressI[6], item.StressI[7], item.StressI[8]]
                stress_j = [item.StressJ[0], item.StressJ[1], item.StressJ[2], item.StressJ[3], item.StressJ[4], item.StressJ[5],
                            item.StressJ[6], item.StressJ[7], item.StressJ[8]]
                list_res.append(TrussElementStress(item.ElementId, stress_i, stress_j))
            else:
                raise TypeError(f"操作错误，不存在{item.ElementType}类型")
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    @staticmethod
    def get_element_force(element_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, operation: bool = False, case_name=""):
        """
        获取单元内力,支持单个单元和单元列表
        Args:
            element_id: 单元编号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            operation: 是否为运营阶段
            case_name: 运营阶段所需荷载工况名
        example:
            mdb.get_element_force(1,stage_id=1)
            mdb.get_element_force([1,2,3],stage_id=1)
            mdb.get_element_force(1,operation=True,case_name="工况名")
        Returns:
            list[ElementForce] or ElementForce
        """
        if type(element_id) != int and type(element_id) != list:
            raise TypeError("类型错误,element_id仅支持 int和 list[int]")
        bf_list = qt_model.GetElementForce(element_id, stage_id, result_kind, increment_type, operation, case_name)
        list_res = []
        for item in bf_list:
            if item.ElementType == "BEAM":
                force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                list_res.append(BeamElementForce(item.ElementId, force_i, force_j))
            elif item.ElementType == "PLATE":
                force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                force_k = [item.ForceK.Fx, item.ForceK.Fy, item.ForceK.Fz, item.ForceK.Mx, item.ForceK.My, item.ForceK.Mz]
                force_l = [item.ForceL.Fx, item.ForceL.Fy, item.ForceL.Fz, item.ForceL.Mx, item.ForceL.My, item.ForceL.Mz]
                list_res.append(ShellElementForce(item.ElementId, force_i, force_j, force_k, force_l))
            elif item.ElementType == "CABLE" or item.ElementType == "LINK":
                force_i = [item.ForceI.Fx, item.ForceI.Fy, item.ForceI.Fz, item.ForceI.Mx, item.ForceI.My, item.ForceI.Mz]
                force_j = [item.ForceJ.Fx, item.ForceJ.Fy, item.ForceJ.Fz, item.ForceJ.Mx, item.ForceJ.My, item.ForceJ.Mz]
                list_res.append(TrussElementForce(item.ElementId, force_i, force_j))
            else:
                raise TypeError(f"操作错误，不存在{item.ElementType}类型")
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    @staticmethod
    def get_reaction(node_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, operation: bool = False, case_name=""):
        """
        获取节点,支持单个节点和节点列表
        Args:
            node_id: 节点编号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            operation: 是否为运营阶段
            case_name: 运营阶段所需荷载工况名
        example:
            mdb.get_reaction(1,stage_id=1)
            mdb.get_reaction([1,2,3],stage_id=1)
            mdb.get_reaction(1,operation=True,case_name="工况名")
        Returns:
            list[SupportReaction] or SupportReaction
        """
        if type(node_id) != int and type(node_id) != list:
            raise TypeError("类型错误,beam_id int和 list[int]")
        bs_list = qt_model.GetSupportReaction(node_id, stage_id, result_kind, increment_type, operation, case_name)
        list_res = []
        for item in bs_list:
            force = [item.Force.Fx, item.Force.Fy, item.Force.Fz, item.Force.Mx, item.Force.My, item.Force.Mz]
            list_res.append(SupportReaction(item.NodeId, force))
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    @staticmethod
    def get_node_displacement(node_id, stage_id: int = 1, result_kind: int = 1, increment_type: int = 1, operation: bool = False, case_name=""):
        """
        获取节点,支持单个节点和节点列表
        Args:
            node_id: 节点号
            stage_id: 施工极端号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            operation: 是否为运营阶段
            case_name: 运营阶段所需荷载工况名
        example:
            mdb.get_node_displacement(1,stage_id=1)
            mdb.get_node_displacement([1,2,3],stage_id=1)
            mdb.get_node_displacement(1,operation=True,case_name="工况名")
        Returns:
            list[NodeDisplacement] or NodeDisplacement
        """
        if type(node_id) != int and type(node_id) != list:
            raise TypeError("类型错误,node_id仅支持 int和 list[int]")
        bf_list = qt_model.GetNodeDisplacement(node_id, stage_id, result_kind, increment_type, operation, case_name)
        list_res = []
        for item in bf_list:
            displacements = [item.Displacement.Dx, item.Displacement.Dy, item.Displacement.Dz,
                             item.Displacement.Rx, item.Displacement.Ry, item.Displacement.Rz]
            list_res.append(NodeDisplacement(item.NodeId, displacements))
        if len(list_res) == 1:
            return list_res[0]
        return list_res

    # endregion

    # region 获取模型信息
    @staticmethod
    def get_node_data(ids=None):
        """
        获取节点信息 默认获取所有节点信息
        Args: 无
        example:
            mdb.get_node_data()     # 获取所有节点信息
            mdb.get_node_data(1)    # 获取单个节点信息
            mdb.get_node_data([1,2])    # 获取多个节点信息
        Returns:
            list[Node] 或 Node
        """
        if ids is None:
            node_list = qt_model.GetNodeData()
        else:
            node_list = qt_model.GetNodeData(ids)
        res_list = []
        for item in node_list:
            res_list.append(Node(item.Id, item.XCoor, item.YCoor, item.ZCoor))
        if len(res_list) == 1:
            return res_list[0]
        return res_list

    @staticmethod
    def get_element_data(ids=None):
        """
        获取单元信息
        Args: 无
        example:
            mdb.get_element_data() 获取所有单元结果
            mdb.get_element_data(1) 获取指定编号单元信息
        Returns:
            list[Element]
        """
        ele_list = []
        target_ids = []
        if ids is None:
            ele_list.extend(Odb.get_beam_element())
            ele_list.extend(Odb.get_plate_element())
            ele_list.extend(Odb.get_cable_element())
            ele_list.extend(Odb.get_link_element())
            if len(ele_list) == 1:
                return ele_list[0]
            else:
                return ele_list
        if isinstance(ids, int):
            target_ids.append(ids)
        else:
            target_ids.extend(ids)
        for item_id in target_ids:
            ele_type = Odb.get_element_type(item_id)
            if ele_type == "BEAM":
                ele_list.append(Odb.get_beam_element(item_id)[0])
            if ele_type == "PLATE":
                ele_list.append(Odb.get_plate_element(item_id)[0])
            if ele_type == "CABLE":
                ele_list.append(Odb.get_cable_element(item_id)[0])
            if ele_type == "LINK":
                ele_list.append(Odb.get_link_element(item_id)[0])
        return ele_list

    @staticmethod
    def get_element_type(ele_id: int) -> str:
        """
        获取单元类型
        Args:
            ele_id: 单元号
        example:
            mdb.get_element_type(1) 获取所有单元信息
        Returns:
            str类型 返回 BEAM PLATE CABLE LINK
        """
        return qt_model.GetElementType(ele_id)

    @staticmethod
    def get_beam_element(ids=None) -> list[Element]:
        """
        获取梁单元信息
        Args:
            ids: 梁单元号，默认时获取所有梁单元
        example:
            mdb.get_beam_element() 获取所有单元信息
        Returns:
            list[Element]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetBeamElementData()
        else:
            ele_list = qt_model.GetBeamElementData(ids)
        for item in ele_list:
            res_list.append(Element(item.Id, "BEAM", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle))
        return res_list

    @staticmethod
    def get_plate_element(ids=None) -> list[Element]:
        """
        获取板单元信息
        Args:
            ids: 板单元号，默认时获取所有板单元
        example:
            mdb.get_plate_element() 获取所有单元信息
        Returns:
            list[Element]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetPlateElementData()
        else:
            ele_list = qt_model.GetPlateElementData(ids)
        for item in ele_list:
            res_list.append(Element(item.Id, "PLATE", [item.NodeI.Id, item.NodeJ.Id, item.NodeK.Id, item.NodeL.Id],
                                    item.MaterialId, item.ThicknessId, item.BetaAngle))
        return res_list

    @staticmethod
    def get_cable_element(ids=None) -> list[Element]:
        """
        获取索单元信息
        Args:
            ids: 索单元号，默认时获取所有索单元
        example:
            mdb.get_cable_element() 获取所有单元信息
        Returns:
            list[Element]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetCableElementData()
        else:
            ele_list = qt_model.GetCableElementData(ids)
        for item in ele_list:
            res_list.append(Element(item.Id, "CABLE", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle,
                                    int(item.InitialParameterType), item.InitialParameter))
        return res_list

    @staticmethod
    def get_link_element(ids=None) -> list[Element]:
        """
        获取杆单元信息
        Args:
            ids: 杆单元号，默认时输出全部杆单元
        example:
            mdb.get_link_element() 获取所有单元信息
        Returns:
            list[Element]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetLinkElementData()
        else:
            ele_list = qt_model.GetLinkElementData(ids)
        for item in ele_list:
            res_list.append(Element(item.Id, "LINK", [item.StartNode.Id, item.EndNode.Id], item.MaterialId, item.SectionId, item.BetaAngle))
        return res_list

    @staticmethod
    def get_material_data(ids=None):
        """
        获取材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        example:
            mdb.get_material_data() 获取所有材料信息
        Returns:
            list[Material]
        """
        mat_list = []
        # if ids is None:
        #     mat_list.extend(qt_model.GetConcreteMaterialData())
        #     mat_list.extend(qt_model.GeSteelPlateMaterialData())
        #     mat_list.extend(qt_model.GetSteelBarMaterialData())
        #     mat_list.extend(qt_model.GetPreStressedBarMaterialData())
        #     mat_list.extend(qt_model.GetUserDefinedMaterialData())

    @staticmethod
    def get_concrete_material(ids=None) -> list[Material]:
        """
        获取混凝土材料信息
        Args:
            ids: 材料号，默认时输出全部材料
        example:
            mdb.get_concrete_material() 获取所有材料信息
        Returns:
            list[Material]
        """
        res_list = []
        if ids is None:
            ele_list = qt_model.GetConcreteMaterialData()
        else:
            ele_list = qt_model.GetConcreteMaterialData(ids)
        for item in ele_list:
            res_list.append(Material(item.Id, item.Name, "混凝土", item.Standard, item.Database,
                                     [item.ElasticModulus, item.UnitWeight, item.PosiRatio, item.TemperatureCoefficient],
                                     item.Standard, item.IsModifiedByUser))
        return res_list
    # endregion
