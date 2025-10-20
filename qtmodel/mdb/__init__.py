from .mdb_analysis_setting import MdbAnalysisSetting
from .mdb_assistant import MdbAssistant
from .mdb_boundary import MdbBoundary
from .mdb_construction_stage import MdbConstructionStage
from .mdb_dynamic_load import MdbDynamicLoad
from .mdb_live_load import MdbLiveLoad
from .mdb_project import MdbProject
from .mdb_property import MdbProperty
from .mdb_section import MdbSection
from .mdb_static_load import MdbStaticLoad
from .mdb_structure import MdbStructure
from .mdb_sink_load import MdbSinkLoad
from .mdb_temperature_load import MdbTemperatureLoad
from .mdb_tendon import MdbTendon
from .mdb_load import MdbLoad

# version 1.1.11

class Mdb(MdbProject, MdbStructure,MdbProperty, MdbSection,
          MdbBoundary,  MdbDynamicLoad,MdbConstructionStage,
          MdbLoad,
          MdbStaticLoad, MdbTendon, MdbAssistant,MdbSinkLoad,
          MdbTemperatureLoad,MdbLiveLoad,MdbAnalysisSetting):
    """聚合所有 Mdb 能力的门面类（Facade）。"""
    pass


mdb = Mdb
__all__ = ["Mdb", "mdb"]
