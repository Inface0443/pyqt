from ..core.qt_server import QtServer


class OdbModelStage:
    # region 获取施工阶段信息
    @staticmethod
    def get_stage_name():
        """
        获取所有施工阶段名称
        Args: 无
        Example:
            odb.get_stage_name()
        Returns: 包含信息为list[int]
        """
        return QtServer.send_dict("GET-STAGE-NAMES", None)

    @staticmethod
    def get_elements_of_stage(stage_id: int):
        """
        获取指定施工阶段单元编号信息
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_elements_of_stage(stage_id=1)
        Returns: 包含信息为list[int]
        """
        payload = {"stage_id": stage_id}
        return QtServer.send_dict("GET-ELEMENTS-OF-STAGE", payload)

    @staticmethod
    def get_nodes_of_stage(stage_id: int):
        """
        获取指定施工阶段节点编号信息
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_nodes_of_stage(stage_id=1)
        Returns: 包含信息为list[int]
        """
        payload = {"stage_id": stage_id}
        return QtServer.send_dict("GET-NODES-OF-STAGE", payload)

    @staticmethod
    def get_groups_of_stage(stage_id: int):
        """
        获取施工阶段结构组、边界组、荷载组名集合
        Args:
            stage_id: 施工阶段编号
        Example:
            odb.get_groups_of_stage(stage_id=1)
        Returns: 包含信息为dict
        """
        payload = {"stage_id": stage_id}
        return QtServer.send_dict("GET-GROUPS-OF-STAGE", payload)
    # endregion
