from qtmodel.core.qt_server import QtServer
from qtmodel.core.data_helper import QtDataHelper


class OdbModelMaterial:
    """获取材料和板厚"""

    # region 获取材料
    @staticmethod
    def get_material_data():
        """
        获取材料信息
        Args: 无
        Example:
            odb.get_material_data() # 获取所有材料信息
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-MATERIAL-DATA", None)

    @staticmethod
    def get_thickness_data():
        """
        获取所有板厚信息
        Args:
        Example:
            odb.get_thickness_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-THICKNESS-DATA", None)
    # endregion
