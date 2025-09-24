from .odb_model import OdbModel
from .odb_result import OdbResult
from .odb_result_plot import OdbResultPlot
from .odb_view import OdbView


class Odb(OdbView,OdbModel,OdbResultPlot,OdbResult):
    """聚合所有 Odb 能力的门面类（Facade）。"""
    pass

odb = Odb
__all__ = ["Odb", "odb"]