from .odb_model_structure import OdbModelStructure
from .odb_model_material import OdbModelMaterial
from .odb_model_stage import OdbModelStage
from .odb_model_boundary import OdbModelBoundary
from .odb_model_load import OdbModelLoad
from .odb_model_section import OdbModelSection
from .odb_result_data import OdbResultData
from .odb_result_plot import OdbResultPlot
from .odb_view import OdbView


class Odb(OdbModelStructure,OdbModelMaterial,OdbModelSection,
            OdbModelBoundary,OdbModelLoad,OdbModelStage,
            OdbResultData,OdbResultPlot, OdbView):
    """聚合所有 Odb 能力的门面类（Facade）。"""
    pass

odb = Odb
__all__ = ["Odb", "odb"]