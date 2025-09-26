from .odb_model import OdbModel
from .odb_model_boundary import OdbModelBoundary
from .odb_model_load import OdbModelLoad
from .odb_model_section import OdbModelSection
from .odb_result import OdbResult
from .odb_result_plot import OdbResultPlot
from .odb_view import OdbView


class Odb(OdbModel,OdbModelSection,
            OdbModelBoundary,
            OdbModelLoad,OdbResultPlot,
            OdbResult,OdbView):
    """聚合所有 Odb 能力的门面类（Facade）。"""
    pass

odb = Odb
__all__ = ["Odb", "odb"]