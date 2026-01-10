from .cdb_concrete_check import CdbConcreteCheck
from .cdb_steel_box_check import CdbSteelBoxCheck
from .cdb_steel_truss_check import CdbSteelTrussCheck
from .cdb_anti_overturn_check import CdbAntiOverturnCheck

class Cdb(CdbConcreteCheck, CdbSteelBoxCheck, CdbSteelTrussCheck, CdbAntiOverturnCheck):
    """聚合所有 Cdb 能力的门面类（Facade）。"""
    pass


cdb = Cdb
__all__ = ["Cdb", "cdb"]
