from qtmodel.core.qt_server import QtServer


class CdbAntiOverturnCheck:
    """
    用于抗倾覆检查
    """

    # region 抗倾覆检查
    @staticmethod
    def check_anti_overturn_criteria():
        """
        检查抗倾覆标准
        Args:无
        Example:
            cdb.check_anti_overturn_criteria()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-ANTI-OVERTURN-CRITERIA")

    @staticmethod
    def check_anti_overturn_stability():
        """
        检查抗倾覆稳定性
        Args:无
        Example:
            cdb.check_anti_overturn_stability()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-ANTI-OVERTURN-STABILITY")

    @staticmethod
    def check_anti_overturn_safety_factor():
        """
        检查抗倾覆安全系数
        Args:无
        Example:
            cdb.check_anti_overturn_safety_factor()
        Returns: 无
        """
        QtServer.send_dict(header="CHECK-ANTI-OVERTURN-SAFETY-FACTOR")
    # endregion
