from ..core.qt_server import QtServer


class OdbModelSection:
    """获取模型截面数据"""

    # region 获取截面信息
    @staticmethod
    def get_all_section_shape():
        """
        获取所有截面形状信息
        Args:
        Example:
            odb.get_all_section_shape()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_get("GET-ALL-SECTION-SHAPE", None)

    @staticmethod
    def get_section_shape(sec_id: int):
        """
        获取截面形状信息
        Args:
            sec_id: 目标截面编号
        Example:
            odb.get_section_shape(1)
        Returns:
            包含信息为dict
        """
        payload = {"sec_id": sec_id}
        return QtServer.send_get("GET-SECTION-SHAPE", payload)

    @staticmethod
    def get_all_section_data():
        """
        获取所有截面详细信息,截面特性详见UI自定义特性截面
        Args: 无
        Example:
            odb.get_all_section_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_get("GET-ALL-SECTION-DATA", None)

    @staticmethod
    def get_section_data(sec_id: int):
        """
        获取截面详细信息,截面特性详见UI自定义特性截面
        Args:
            sec_id: 目标截面编号
        Example:
            odb.get_section_data(1)
        Returns: 包含信息为dict
        """
        payload = {"sec_id": sec_id}
        return QtServer.send_get("GET-SECTION-DATA", payload)

    @staticmethod
    def get_section_property(index: int):
        """
        获取指定截面特性
        Args:
            index:截面号
        Example:
            odb.get_section_property(1)
        Returns: dict
        """
        payload = {"index": index}
        return QtServer.send_get("GET-SECTION-PROPERTY", payload)

    @staticmethod
    def get_section_ids():
        """
        获取模型所有截面号
        Args: 无
        Example:
            odb.get_section_ids()
        Returns: list[int]
        """
        return QtServer.send_get("GET-SECTION-IDS", None)

    # endregion
