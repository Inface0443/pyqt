from .mdb_analysis_setting import MdbAnalysisSetting
from .mdb_boundary import MdbBoundary
from .mdb_construction_stage import MdbConstructionStage
from .mdb_dynamic_load import MdbDynamicLoad
from .mdb_live_load import MdbLiveLoad
from .mdb_project import MdbProject
from .mdb_property import MdbProperty
from .mdb_section import MdbSection
from .mdb_static_load import MdbStaticLoad
from .mdb_structure import MdbStructure
from .mdb_temperature_load import MdbTemperatureLoad
from .mdb_tendon import MdbTendon


class Mdb(MdbBoundary, MdbConstructionStage, MdbDynamicLoad,
          MdbProject, MdbProperty, MdbSection,MdbStaticLoad, MdbTendon,
          MdbStructure,MdbTemperatureLoad,MdbLiveLoad,MdbAnalysisSetting):
    """聚合所有 Mdb 能力的门面类（Facade）。"""
    pass


mdb = Mdb
__all__ = ["Mdb", "mdb"]
