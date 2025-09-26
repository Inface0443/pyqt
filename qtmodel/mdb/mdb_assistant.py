from ..core.qt_server import QtServer


class MdbAssistant:
    """
    用于建模助手创建
    """
    @staticmethod
    def create_cantilever_bridge(span_len: list[float], span_seg: list[float], bearing_spacing: list[float],
                                 top_width: float = 20.0, bottom_width: float = 12.5, box_num: int = 1, material: str = "C50"):
        """
        悬浇桥快速建模
        Args:
            span_len:桥跨分段
            span_seg:各桥跨内节段基准长度
            bearing_spacing:支座间距
            top_width:主梁顶板宽度
            bottom_width:主梁顶板宽度
            box_num:主梁箱室长度
            material:主梁材料类型
        Example:
           mdb.create_cantilever_bridge(span_len=[6,70,70,6],span_seg=[2,3.5,3.5,2],bearing_spacing=[5.6,5.6])
        Returns: 无
        """
        payload = {
            "span_len": span_len,
            "span_seg": span_seg,
            "bearing_spacing": bearing_spacing,
            "top_width": top_width,
            "bottom_width": bottom_width,
            "box_num": box_num,
            "material": material,
        }
        return QtServer.send_post("CREATE-CANTILEVER-BRIDGE", payload)
