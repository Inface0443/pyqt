from typing import Union

from qtmodel.core.qt_server import QtServer


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
        return QtServer.send_dict("GET-ALL-SECTION-SHAPE", None)

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
        return QtServer.send_dict("GET-SECTION-SHAPE", payload)

    @staticmethod
    def get_all_section_data():
        """
        获取所有截面详细信息,截面特性详见UI自定义特性截面
        Args: 无
        Example:
            odb.get_all_section_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-ALL-SECTION-DATA", None)

    @staticmethod
    def get_section_data(sec_id: int, position: int = 0):
        """
        获取截面详细信息,截面特性详见UI自定义特性截面
        Args:
            sec_id: 目标截面编号
            position: 目标截面为变截面时0-首端 1-末端
        Example:
            odb.get_section_data(1)
        Returns: 包含信息为dict
        """
        payload = {"sec_id": sec_id, "position": position}
        return QtServer.send_dict("GET-SECTION-DATA", payload)

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
        return QtServer.send_dict("GET-SECTION-PROPERTY", payload)

    @staticmethod
    def get_section_ids():
        """
        获取模型所有截面号
        Args: 无
        Example:
            odb.get_section_ids()
        Returns: list[int]
        """
        return QtServer.send_dict("GET-SECTION-IDS", None)

    @staticmethod
    def get_section_property_by_loops(loop_segments: list[dict] = None):
        """
        通过多组线圈获取截面特性
        Args:无
        Example:
            dict_item1 = {"main": [[9.25, 0.0], [18.4, 0.0], [18.5, 0.0], [18.5, 2.5], [9.25, 2.5], [0.0, 2.5], [0.0, 0.0], [0.1, 0.0]],
                         "sub1": [[6.35, 0.5], [2.55, 0.5], [2.55, 1.0], [2.55, 2.0], [6.35, 2.0]],
                         "sub2": [[9.25, 0.5], [11.55, 0.5], [11.55, 2.0], [9.25, 2.0], [6.95, 2.0], [6.95, 0.5]],
                         "sub3": [[12.15, 0.5], [15.95, 0.5], [15.95, 1.0], [15.95, 2.0], [12.15, 2.0]]}
            odb.get_section_property_by_loops([dict_item1])
        Returns: dict
        """
        payload = {"loop_segments": loop_segments}
        return QtServer.send_dict("GET-SECTION-PROPERTY-BY-LOOPS", payload)

    @staticmethod
    def get_section_property_by_lines(sec_lines:Union[list[tuple[float, float, float, float, float]],list[list[float]]]  = None):
        """
        通过线宽数据获取截面特性
        Args:无
        Example:
            sec_lines = [[0.0, 2.284, 5.51093, 2.284, 0.016], [0.152479, 2.284, 0.200597, 2.04341, 0.008],
                                   [0.200597, 2.04341, 0.201664, 2.0389, 0.008], [0.201664, 2.0389, 0.203149, 2.03451, 0.008],
                                   [0.203149, 2.03451, 0.205006, 2.03026, 0.008]]
            odb.get_section_property_by_lines(sec_lines)
        Returns: dict
        """
        payload = {"sec_lines": sec_lines}
        return QtServer.send_dict("GET-SECTION-PROPERTY-BY-LINES", payload)
    # endregion
