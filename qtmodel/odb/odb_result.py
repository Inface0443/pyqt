from ..core.qt_server import QtServer
from ..core.data_helper import QtDataHelper


class OdbResult:
    """
    用于获取结果数据，统一返回json字符串
    """

    # region 结果表格
    @staticmethod
    def get_reaction(ids, envelop_type=1, stage_id: int = 1, result_kind: int = 1,
                     increment_type: int = 1, case_name="", is_time_history: bool = False) -> str:
        """
        获取制作反力
        Args:
            ids: 节点编号,支持整数或整数型列表支持XtoYbyN形式字符串
            envelop_type: 施工阶段包络类型 1-最大 2-最小
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
            is_time_history: 运营阶段所需荷载工况名是否为时程分析
        Example:
            odb.get_reaction(ids=1,stage_id=1)
            odb.get_reaction(ids=[1,2,3],stage_id=1)
            odb.get_reaction(ids="1to3",stage_id=1)
            odb.get_reaction(ids=1,stage_id=-1,case_name="工况名")
        Returns: 返回json字符串， 内部为list[dict]
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "envelop_type": envelop_type,
            "stage_id": stage_id,
            "result_kind": result_kind,
            "increment_type": increment_type,
            "case_name": case_name,
            "is_time_history": is_time_history,
        }
        return QtServer.send_get("GET-REACTION", payload)

    @staticmethod
    def get_deformation(ids, envelop_type=1,
                        stage_id: int = 1, result_kind: int = 1, increment_type: int = 1,
                        case_name="", is_time_history: bool = False) -> str:
        """
        获取节点变形结果,支持单个节点和节点列表
        Args:
            ids: 查询结果的节点号支持XtoYbyN形式字符串
            envelop_type: 施工阶段包络类型 1-最大 2-最小
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型(1-合计 2-收缩徐变效应 3-预应力效应 4-恒载) 时程分析类型(1-位移 2-速度 3-加速度)
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
            is_time_history: 是否为时程分析
        Example:
            odb.get_deformation(ids=1,stage_id=1)
            odb.get_deformation(ids=[1,2,3],stage_id=1)
            odb.get_deformation(ids="1to3",stage_id=1)
            odb.get_deformation(ids=1,stage_id=-1,case_name="工况名")
        Returns: 返回json字符串， 内部为list[dict]
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "envelop_type": envelop_type,
            "stage_id": stage_id,
            "result_kind": result_kind,
            "increment_type": increment_type,
            "case_name": case_name,
            "is_time_history": is_time_history,
        }
        return QtServer.send_get("GET-DEFORMATION", payload)

    @staticmethod
    def get_element_stress(ids, envelop_type: int = 1, stage_id: int = 1, result_kind: int = 1,
                           increment_type: int = 1, case_name="") -> str:
        """
        获取单元应力,支持单个单元和单元列表
        Args:
            ids: 单元编号,支持整数或整数型列表
            envelop_type:施工阶段包络类型 1-最大 2-最小 3-包络
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
        Example:
            odb.get_element_stress(ids=1,stage_id=1)
            odb.get_element_stress(ids=[1,2,3],stage_id=1)
            odb.get_element_stress(ids=1,stage_id=-1,case_name="工况名")
        Returns: 返回json字符串， 内部为list[dict]
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "envelop_type": envelop_type,
            "stage_id": stage_id,
            "result_kind": result_kind,
            "increment_type": increment_type,
            "case_name": case_name,
        }
        return QtServer.send_get("GET-ELEMENT-STRESS", payload)

    @staticmethod
    def get_element_force(ids, stage_id: int = 1, envelop_type: int = 1,
                          result_kind: int = 1, increment_type: int = 1, case_name="",
                          is_time_history: bool = False, is_boundary_element: bool = False) -> str:
        """
        获取单元内力,支持单个单元和单元列表
        Args:
            ids: 单元编号支持整数或整数列表且支持XtoYbyN形式字符串
            stage_id: 施工阶段号 -1-运营阶段  0-施工阶段包络 n-施工阶段号
            envelop_type: 1-最大 2-最小 3-包络
            result_kind: 施工阶段数据的类型 1-合计 2-收缩徐变效应 3-预应力效应 4-恒载
            increment_type: 1-全量    2-增量
            case_name: 运营阶段所需荷载工况名
            is_time_history: 是否为时程分析
            is_boundary_element: 是否为时程分析边界单元连接
        Example:
            odb.get_element_force(ids=1,stage_id=1)
            odb.get_element_force(ids=[1,2,3],stage_id=1)
            odb.get_element_force(ids=1,stage_id=-1,case_name="工况名")
        Returns: 返回json字符串， 内部为list[dict]
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "stage_id": stage_id,
            "envelop_type": envelop_type,
            "result_kind": result_kind,
            "increment_type": increment_type,
            "case_name": case_name,
            "is_time_history": is_time_history,
            "is_boundary_element": is_boundary_element,
        }
        return QtServer.send_get("GET-ELEMENT-FORCE", payload)

    @staticmethod
    def get_self_concurrent_reaction(node_id: int, case_name: str) -> str:
        """
        获取自并发反力
        Args:
          node_id:单个节点号
          case_name:工况号
        Example:
          odb.get_self_concurrent_reaction(node_id=1,case_name="工况1_Fx最大")
        Returns: 返回json字符串， 内部为list[dict]
        """
        payload = {
            "node_id": node_id,
            "case_name": case_name,
        }
        return QtServer.send_get("GET-SELF-CONCURRENT-REACTION", payload)

    @staticmethod
    def get_all_concurrent_reaction(node_id: int, case_name: str) -> str:
        """
        获取完全并发反力
        Args:
          node_id:单个节点号
          case_name:工况号
        Example:
          odb.get_all_concurrent_reaction(node_id=1,case_name="工况1_Fx最大")
        Returns: 返回json字符串， 包含信息为list[dict]
        """
        payload = {
            "node_id": node_id,
            "case_name": case_name,
        }
        return QtServer.send_get("GET-ALL-CONCURRENT-REACTION", payload)

    @staticmethod
    def get_concurrent_force(ids=None, case_name: str = "") -> str:
        """
        获取单元并发内力
        Args:
          ids:单元号支持XtoYbyN形式字符串
          case_name:工况号
        Example:
          odb.get_concurrent_force(ids=1,case_name="工况1_Fx最大")
          odb.get_concurrent_force(ids="1to19",case_name="工况1_Fx最大")
        Returns: 返回json字符串， 包含信息为list[dict]
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "case_name": case_name,
        }
        return QtServer.send_get("GET-CONCURRENT-FORCE", payload)

    @staticmethod
    def get_elastic_link_force(ids, result_kind=1, stage_id=-1, envelop_type=0, increment_type=1, case_name="") -> str:
        """
        获取弹性连接内力
        Args:
            ids: 弹性连接ID集合,支持整数和整数列表且支持XtoYbyN字符串
            result_kind: 施工阶段荷载类型1-合计 2-预应力 3-收缩徐变 4-恒载
            stage_id: -1为运营阶段 0-施工阶段包络 n-施工阶段
            envelop_type: 包络类型，1-最大 2-最小
            increment_type: 增量类型，1-全量 2-增量
            case_name: 工况名称，默认为空
        Example:
            odb.get_elastic_link_force(ids=[1,2,3], result_kind=1, stage_id=1)
        Returns: 返回json字符串， 内部为list[dict]
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "result_kind": result_kind,
            "stage_id": stage_id,
            "envelop_type": envelop_type,
            "increment_type": increment_type,
            "case_name": case_name,
        }
        return QtServer.send_get("GET-ELASTIC-LINK-FORCE", payload)

    @staticmethod
    def get_constrain_equation_force(ids, result_kind=1, stage_id=1, envelop_type=0, increment_type=1, case_name="") -> str:
        """
        查询约束方程内力
        Args:
            ids: 约束方程ID列表支持整数和整数列表且支持XtoYbyN字符串
            result_kind: 施工阶段荷载类型1-合计 2-预应力 3-收缩徐变 4-恒载
            stage_id: -1为运营阶段 0-施工阶段包络 n-施工阶段
            envelop_type: 包络类型，1-最大 2-最小
            increment_type: 增量类型，1-全量 2-增量
            case_name: 工况名称
        Example:
            odb.get_constrain_equation_force(ids=[1,2,3], result_kind=1, stage_id=1)
        Returns: 返回json字符串， 内部为list[dict]
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "result_kind": result_kind,
            "stage_id": stage_id,
            "envelop_type": envelop_type,
            "increment_type": increment_type,
            "case_name": case_name,
        }
        return QtServer.send_get("GET-CONSTRAIN-EQUATION-FORCE", payload)

    @staticmethod
    def get_cable_element_length(ids, stage_id=-1, increment_type=1) -> str:
        """
        查询无应力索长
        Args:
            ids: 索单元ID集合，支持整数和整数列表且支持XtoYbyN字符串
            stage_id: 施工阶段ID,默认为运营阶段
            increment_type: 增量类型，默认为1
        Example:
            odb.get_cable_element_length(ids=[1,2,3], stage_id=1)
        Returns: 返回json字符串， 内部为list[dict]
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "stage_id": stage_id,
            "increment_type": increment_type,
        }
        return QtServer.send_get("GET-CABLE-ELEMENT-LENGTH", payload)

    @staticmethod
    def get_period_and_vibration_results() -> str:
        """
        获取自振分析角频率和振型参与质量等结果
        Args: 无
        Example:
          odb.get_period_and_vibration_results()
        Returns: 返回json字符串，list[dict]包含各模态周期和频率的列表
        """
        return QtServer.send_get("GET-PERIOD-AND-VIBRATION-RESULTS", None)

    @staticmethod
    def get_vibration_modal_results(mode: int = 1) -> str:
        """
        获取自振分析振型向量
        Args:
            mode: 模态号. 默认为1
        Example:
            odb.get_vibration_modal_results(mode=1)
        Returns: 返回json字符串，list[dict]包含该模态下节点位移向量列表
        """
        payload = {
            "mode": mode
        }
        return QtServer.send_get("GET-VIBRATION-MODAL-RESULTS", payload)

    @staticmethod
    def get_buckling_eigenvalue() -> str:
        """
        获取屈曲分析特征值
        Args: 无
        Example:
            odb.get_buckling_eigenvalue()
        Returns: 返回json字符串， list[dict]包含各模态下特征值
        """
        return QtServer.send_get("GET-BUCKLING-EIGENVALUE", None)

    @staticmethod
    def get_buckling_modal_results(mode: int = 1) -> str:
        """
        获取屈曲模态向量
        Args:
            mode:模态号. 默认为1
        Example:
            odb.get_buckling_modal_results(mode=1)
        Returns: 返回json字符串，list[dict]包含该模态下屈曲模态向量列表
        """
        payload = {
            "mode": mode
        }
        return QtServer.send_get("GET-BUCKLING-MODAL-RESULTS", payload)
# endregion
