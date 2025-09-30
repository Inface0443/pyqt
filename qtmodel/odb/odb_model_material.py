from ..core.qt_server import QtServer
from ..core.data_helper import QtDataHelper


class OdbModelMaterial:
    """获取材料和板厚"""

    # region 获取材料
    @staticmethod
    def get_concrete_material(ids=None):
        """
        获取混凝土材料信息
        Args:
            ids: 材料号支持XtoYbyN形式字符串,默认时输出全部材料
        Example:
            odb.get_concrete_material() # 获取所有材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_dict("GET-CONCRETE-MATERIAL", payload)

    @staticmethod
    def get_steel_plate_material(ids=None):
        """
        获取钢材材料信息
        Args:
            ids: 材料号支持XtoYbyN形式字符串,默认时输出全部材料
        Example:
            odb.get_steel_plate_material() # 获取所有钢材材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_dict("GET-STEEL-PLATE-MATERIAL", payload)

    @staticmethod
    def get_pre_stress_bar_material(ids=None):
        """
        获取钢材材料信息
        Args:
            ids: 材料号,默认时输出全部材料
        Example:
            odb.get_pre_stress_bar_material() # 获取所有预应力材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_dict("GET-PRE-STRESS-BAR-MATERIAL", payload)

    @staticmethod
    def get_steel_bar_material(ids=None):
        """
        获取钢筋材料信息
        Args:
            ids: 材料号,默认None时输出全部材料
        Example:
            odb.get_steel_bar_material() # 获取所有钢筋材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_dict("GET-STEEL-BAR-MATERIAL", payload)

    @staticmethod
    def get_user_define_material(ids=None):
        """
        获取自定义材料信息
        Args:
            ids: 材料号支持XtoYbyN形式字符串,默认None时输出全部材料
        Example:
            odb.get_user_define_material() # 获取所有自定义材料信息
            odb.get_user_define_material("1to10") # 获取所有自定义材料信息
        Returns:  list[dict]
        """
        payload = {"ids": QtDataHelper.parse_ids_to_array(ids)} if ids is not None else None
        return QtServer.send_dict("GET-USER-DEFINE-MATERIAL", payload)

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
    def get_thickness_data(thick_id: int):
        """
        获取所有板厚信息
        Args:
        Example:
            odb.get_thickness_data(1)
        Returns:
            包含信息为dict
        """
        payload = {"thick_id": thick_id}
        return QtServer.send_dict("GET-THICKNESS-DATA", payload)

    @staticmethod
    def get_all_thickness_data():
        """
        获取所有板厚信息
        Args:
        Example:
            odb.get_all_thickness_data()
        Returns: 包含信息为list[dict]
        """
        return QtServer.send_dict("GET-ALL-THICKNESS-DATA", None)
    # endregion
