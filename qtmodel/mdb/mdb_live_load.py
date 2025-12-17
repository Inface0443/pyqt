from qtmodel.core.qt_server import QtServer
from typing import Union, List, Optional
from qtmodel.core.data_helper import QtDataHelper


class MdbLiveLoad:
    # region 移动荷载操作
    @staticmethod
    def add_standard_vehicle(name: str, standard_code: int = 1, load_type: str = "公路I级车道",
                             load_length: float = 0, factor: float = 1.0, n: int = 6,
                             calc_fatigue: (Union[bool, List[bool]]) = None):
        """
        添加标准车辆
        Args:
             name: 车辆荷载名称
             standard_code: 荷载规范
                _1-中国铁路桥涵规范(TB10002-2017)
                _2-城市桥梁设计规范(CJJ11-2019)
                _3-公路工程技术标准(JTJ 001-97)
                _4-公路桥涵设计通规(JTG D60-2004
                _5-公路桥涵设计通规(JTG D60-2015)
                _6-城市轨道交通桥梁设计规范(GB/T51234-2017)
                _7-市域铁路设计规范2017(T/CRS C0101-2017)
             load_type: 荷载类型,支持类型参考软件内界面
             load_length: 默认为0即不限制荷载长度  (铁路桥涵规范2017 所需参数)
             factor: 默认为1.0(铁路桥涵规范2017 ZH荷载所需参数)
             n:车厢数: 默认6节车厢 (城市轨道交通桥梁规范2017 所需参数)
             calc_fatigue:疲劳荷载模式是否计算三种类型疲劳荷载 (公路桥涵设计通规2015 所需参数)
        Example:
            mdb.add_standard_vehicle("高速铁路",standard_code=1,load_type="高速铁路")
        Returns: 无
        """
        if calc_fatigue is None:
            calc_fatigue = [False, False, False]
        if isinstance(calc_fatigue,bool):
            calc_fatigue = [calc_fatigue]
        payload = {
            "name": name,
            "standard_code": standard_code,
            "load_type": load_type,
            "load_length": load_length,
            "factor": factor,
            "n": n,
            "calc_fatigue": calc_fatigue,
        }
        return QtServer.send_dict("ADD-STANDARD-VEHICLE", payload)

    @staticmethod
    def add_user_vehicle(name: str, load_type: str = "车辆荷载", p: (Union[float, List[float]]) = 270000,
                         q: float = 10500, dis: list[float] = None, load_length: float = 500, n: int = 6,
                         empty_load: float = 90000, width: float = 1.5, wheelbase: float = 1.8, min_dis: float = 1.5):
        """
            添加用户定义车辆
        Args:
             name: 车辆荷载名称
             load_type: 荷载类型,支持类型 -车辆/车道荷载 列车普通活载 城市轻轨活载 旧公路人群荷载 轮重集合
             p: 荷载Pk或Pi列表
             q: 均布荷载Qk或荷载集度dW
             dis:荷载距离Li列表
             load_length: 荷载长度  (列车普通活载 所需参数)
             n:车厢数: 默认6节车厢 (列车普通活载 所需参数)
             empty_load:空载 (列车普通活载、城市轻轨活载 所需参数)
             width:宽度 (旧公路人群荷载 所需参数)
             wheelbase:轮间距 (轮重集合 所需参数)
             min_dis:车轮距影响面最小距离 (轮重集合 所需参数))
        Example:
            mdb.add_user_vehicle(name="车道荷载",load_type="车道荷载",p=270000,q=10500)
        Returns: 无
        """
        if dis is None:
            dis = []
        if  isinstance(p, int):
            p = [p]
        payload = {
            "name": name,
            "load_type": load_type,
            "p": p,
            "q": q,
            "dis": dis,
            "load_length": load_length,
            "n": n,
            "empty_load": empty_load,
            "width": width,
            "wheelbase": wheelbase,
            "min_dis": min_dis,
        }
        return QtServer.send_dict("ADD-USER-VEHICLE", payload)

    @staticmethod
    def add_node_tandem(name: str, node_ids: (Union[str, List[int]]), order_by_x: bool = True):
        """
        添加节点纵列,默认以最小X对应节点作为纵列起点
        Args:
             name:节点纵列名
             node_ids:节点列表，支持XToYbyN字符串
             order_by_x:是否开启自动排序，按照X坐标从小到大排序
        Example:
            mdb.add_node_tandem(name="节点纵列1",node_ids=[1,2,3,4,5,6,7])
            mdb.add_node_tandem(name="节点纵列1",node_ids="1to7")
        Returns: 无
        """
        try:
            params = {
                "name": name,
                "node_ids": QtDataHelper.parse_ids_to_array(node_ids),
                "order_by_x": order_by_x,
            }
            QtServer.send_dict(header="ADD-NODE-TANDEM", payload=params)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_influence_plane(name: str, tandem_names: list[str]):
        """
        添加影响面
        Args:
             name:影响面名称
             tandem_names:节点纵列名称组
        Example:
            mdb.add_influence_plane(name="影响面1",tandem_names=["节点纵列1","节点纵列2"])
        Returns: 无
        """
        payload = {
            "name": name,
            "tandem_names": tandem_names,
        }
        return QtServer.send_dict("ADD-INFLUENCE-PLANE", payload)

    @staticmethod
    def add_lane_line(name: str, influence_name: str, tandem_name: str, offset: float = 0, lane_width: float = 0,
                      optimize: bool = False, direction: int = 0):
        """
        添加车道线
        Args:
             name:车道线名称
             influence_name:影响面名称
             tandem_name:节点纵列名
             offset:偏移
             lane_width:车道宽度
             optimize:是否允许车辆摆动
             direction:0-向前  1-向后
        Example:
            mdb.add_lane_line(name="车道1",influence_name="影响面1",tandem_name="节点纵列1",offset=0,lane_width=3.1)
        Returns: 无
        """
        payload = {
            "name": name,
            "influence_name": influence_name,
            "tandem_name": tandem_name,
            "offset": offset,
            "lane_width": lane_width,
            "optimize": optimize,
            "direction": direction,
        }
        return QtServer.send_dict("ADD-LANE-LINE", payload)

    @staticmethod
    def add_live_load_case(name: str, influence_plane: str, span: float,
                           sub_case: list[tuple[str, float, list[str]]] = None,
                           trailer_code: str = "", special_code: str = "", is_save: bool = True):
        """
        添加移动荷载工况
        Args:
             name:活载工况名
             influence_plane:影响线名
             span:跨度
             sub_case:子工况信息 [(车辆名称,系数,["车道1","车道2"])...]
             trailer_code:考虑挂车时挂车车辆名
             special_code:考虑特载时特载车辆名
             is_save:是否保存子工况结果
        Example:
            mdb.add_live_load_case(name="活载工况1",influence_plane="影响面1",span=100,sub_case=[("车辆名称",1.0,["车道1","车道2"]),])
        Returns: 无
        """
        payload = {
            "name": name,
            "influence_plane": influence_plane,
            "span": span,
            "sub_case": sub_case,
            "trailer_code": trailer_code,
            "special_code": special_code,
            "is_save": is_save,
        }
        return QtServer.send_dict("ADD-LIVE-LOAD-CASE", payload)

    @staticmethod
    def add_car_relative_factor(name: str, code_index: int, cross_factors: list[float] = None,
                                longitude_factor: float = -1,
                                impact_factor: float = -1, frequency: float = 14):
        """
        添加移动荷载工况汽车折减
        Args:
             name:活载工况名
             code_index: 汽车折减规范编号  0-无 1-公规2015 2-公规2004
             cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取
             longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取
             impact_factor:冲击系数大于1时为自定义，否则按照规范自动选取
             frequency:桥梁基频
        Example:
            mdb.add_car_relative_factor(name="活载工况1",code_index=1,cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5])
        Returns: 无
        """
        if cross_factors is None:
            cross_factors = []
        payload = {
            "name": name,
            "code_index": code_index,
            "cross_factors": cross_factors,
            "longitude_factor": longitude_factor,
            "impact_factor": impact_factor,
            "frequency": frequency,
        }
        return QtServer.send_dict("ADD-CAR-RELATIVE-FACTOR", payload)

    @staticmethod
    def add_train_relative_factor(name: str, code_index: int = 1, cross_factors: Optional[list[float]] = None,
                                  calc_fatigue: bool = False,
                                  line_count: int = 0, longitude_factor: float = -1, impact_factor: float = -1,
                                  fatigue_factor: float = -1, bridge_kind: int = 0, fill_thick: float = 0.5,
                                  rise: float = 1.5, calc_length: float = 50):
        """
        添加移动荷载工况汽车折减
        Args:
            name:活载工况名
            code_index: 火车折减规范编号  0-无 1-铁规ZK 2-铁规ZKH
            cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取
            calc_fatigue:是否计算疲劳
            line_count: 疲劳加载线路数
            longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取
            impact_factor:强度冲击系数大于1时为自定义，否则按照规范自动选取
            fatigue_factor:疲劳系数
            bridge_kind:桥梁类型 0-无 1-简支 2-结合 3-涵洞 4-空腹式
            fill_thick:填土厚度 (规ZKH ZH钢筋/素混凝土、石砌桥跨结构以及涵洞所需参数)
            rise:拱高 (规ZKH ZH活载-空腹式拱桥所需参数)
            calc_length:计算跨度(铁规ZKH ZH活载-空腹式拱桥所需参数)或计算长度(铁规ZK ZC活载所需参数)
        Example:
            mdb.add_train_relative_factor(name="活载工况1",code_index=1,cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5],calc_length=50)
        Returns: 无
        """
        if cross_factors is None:
            cross_factors = []

        payload = {
            "name": name,
            "code_index": code_index,
            "cross_factors": cross_factors,
            "calc_fatigue": calc_fatigue,
            "line_count": line_count,
            "longitude_factor": longitude_factor,
            "impact_factor": impact_factor,
            "fatigue_factor": fatigue_factor,
            "bridge_kind": bridge_kind,
            "fill_thick": fill_thick,
            "rise": rise,
            "calc_length": calc_length,
        }
        return QtServer.send_dict("ADD-TRAIN-RELATIVE-FACTOR", payload)

    @staticmethod
    def add_metro_relative_factor(name: str, cross_factors: list[float] = None, longitude_factor: float = -1,
                                  impact_factor: float = -1):
        """
        添加移动荷载工况汽车折减
        Args:
             name:活载工况名
             cross_factors:横向折减系数列表,自定义时要求长度为8,否则按照规范选取
             longitude_factor:纵向折减系数，大于0时为自定义，否则为规范自动选取
             impact_factor:强度冲击系数大于1时为自定义，否则按照规范自动选取
        Example:
            mdb.add_metro_relative_factor(name="活载工况1",cross_factors=[1.2,1,0.78,0.67,0.6,0.55,0.52,0.5],
                longitude_factor=1,impact_factor=1)
        Returns: 无
        """
        if cross_factors is None:
            cross_factors = []

        payload = {
            "name": name,
            "cross_factors": cross_factors,
            "longitude_factor": longitude_factor,
            "impact_factor": impact_factor,
        }
        return QtServer.send_dict("ADD-METRO-RELATIVE-FACTOR", payload)

    @staticmethod
    def update_vehicle_name(name: str, new_name: str = ""):
        """
        更新标准车辆
        Args:
             name: 车辆荷载名称
             new_name: 新车辆荷载名称,默认不修改
        Example:
            mdb.update_vehicle_name(name ="高速铁路1",new_name = "高速铁路2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-VEHICLE-NAME", payload)


    @staticmethod
    def update_influence_plane_name(name: str, new_name: str = ""):
        """
        更新影响面
        Args:
             name:影响面名称
             new_name:更改后影响面名称，若无更改则默认
        Example:
            mdb.update_influence_plane_name(name="影响面1",new_name="影响面2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-INFLUENCE-PLANE-NAME", payload)

    @staticmethod
    def update_lane_line_name(name: str, new_name: str = ""):
        """
        更新车道线
        Args:
             name:车道线名称
             new_name:更改后车道名,默认为不更改
        Example:
            mdb.update_lane_line(name="车道1",new_name="车道2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-LANE-LINE-NAME", payload)

    @staticmethod
    def update_node_tandem_name(name: str, new_name: str = ""):
        """
        更新节点纵列,默认以最小X对应节点作为纵列起点
        Args:
             name:节点纵列名
             new_name: 新节点纵列名，默认不修改
        Example:
            mdb.update_node_tandem_name(name="节点纵列1",new_name="节点纵列2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-NODE-TANDEM-NAME", payload)

    @staticmethod
    def update_live_load_case_name(name: str, new_name: str = ""):
        """
        更新移动荷载工况
        Args:
             name:活载工况名
             new_name:新移动荷载名
        Example:
            mdb.update_live_load_case_name(name="活载工况1",new_name="活载工况2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-LIVE-LOAD-CASE-NAME", payload)

    @staticmethod
    def remove_vehicle(index: int = -1, name: str = ""):
        """
        删除车辆信息
        Args:
            index:车辆编号
            name:车辆名称
        Example:
            mdb.remove_vehicle(name="车辆名称")
            mdb.remove_vehicle(index=1)
        Returns: 无
        """
        payload = {"index": index, "name": name}
        return QtServer.send_dict("REMOVE-VEHICLE", payload)

    @staticmethod
    def remove_node_tandem(index: int = -1, name: str = ""):
        """
        按照节点纵列编号/节点纵列名 删除节点纵列
        Args:
             index:节点纵列编号
             name:节点纵列名
        Example:
            mdb.remove_node_tandem(index=1)
            mdb.remove_node_tandem(name="节点纵列1")
        Returns: 无
        """
        payload = {"index": index, "name": name}
        return QtServer.send_dict("REMOVE-NODE-TANDEM", payload)

    @staticmethod
    def remove_influence_plane(index: int = -1, name: str = ""):
        """
        按照影响面编号/影响面名称 删除影响面
        Args:
             index:影响面编号
             name:影响面名称
        Example:
            mdb.remove_influence_plane(index=1)
            mdb.remove_influence_plane(name="影响面1")
        Returns: 无
        """
        payload = {"index": index, "name": name}
        return QtServer.send_dict("REMOVE-INFLUENCE-PLANE", payload)

    @staticmethod
    def remove_lane_line(index: int = -1, name: str = ""):
        """
        按照车道线编号或车道线名称 删除车道线
        Args:
             index:车道线编号，默认时则按照名称删除车道线
             name:车道线名称
        Example:
            mdb.remove_lane_line(index=1)
            mdb.remove_lane_line(name="车道线1")
        Returns: 无
        """
        payload = {"index": index, "name": name}
        return QtServer.send_dict("REMOVE-LANE-LINE", payload)

    @staticmethod
    def remove_live_load_case(index: int = -1, name: str = ""):
        """
        删除移动荷载工况，默认值时则按照工况名删除
        Args:
             index:移动荷载工况编号
             name:移动荷载工况名
        Example:
            mdb.remove_live_load_case(name="活载工况1")
            mdb.remove_live_load_case(index=1)
        Returns: 无
        """
        payload = {"index": index, "name": name}
        return QtServer.send_dict("REMOVE-LIVE-LOAD-CASE", payload)

    # endregion
