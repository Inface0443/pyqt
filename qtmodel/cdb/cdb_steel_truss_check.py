from qtmodel.core.qt_server import QtServer


class CdbSteelTrussCheck:
    """
    用于钢桁架结构检查
    """

    # region 钢桁架检查
    @staticmethod
    def check_steel_truss_member():
        """
        检查钢桁架杆件
        Args:无
        Example:
            cdb.check_steel_truss_member()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-STEEL-TRUSS-MEMBER")

    @staticmethod
    def check_steel_truss_joint():
        """
        检查钢桁架节点
        Args:无
        Example:
            cdb.check_steel_truss_joint()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-STEEL-TRUSS-JOINT")

    @staticmethod
    def check_steel_truss_stability():
        """
        检查钢桁架稳定性
        Args:无
        Example:
            cdb.check_steel_truss_stability()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-STEEL-TRUSS-STABILITY")
    # endregion
