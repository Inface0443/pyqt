from qtmodel.core.qt_server import QtServer


class CdbSteelBoxCheck:
    """
    用于钢箱梁结构检查
    """

    # region 钢箱梁检查
    @staticmethod
    def check_steel_box_section():
        """
        检查钢箱梁截面
        Args:无
        Example:
            cdb.check_steel_box_section()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-STEEL-BOX-SECTION")

    @staticmethod
    def check_steel_box_weld():
        """
        检查钢箱梁焊接
        Args:无
        Example:
            cdb.check_steel_box_weld()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-STEEL-BOX-WELD")

    @staticmethod
    def check_steel_box_fatigue():
        """
        检查钢箱梁疲劳
        Args:无
        Example:
            cdb.check_steel_box_fatigue()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-STEEL-BOX-FATIGUE")
    # endregion
