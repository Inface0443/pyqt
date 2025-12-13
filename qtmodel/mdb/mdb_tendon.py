from typing import Optional, Union

from qtmodel.core.data_helper import QtDataHelper
from qtmodel.core.qt_server import QtServer


class MdbTendon:
    """
    用于钢束操作
    """

    # region 钢束操作
    @staticmethod
    def add_tendon_group(name: str = ""):
        """
        按照名称添加钢束组，添加时可指定钢束组id
        Args:
            name: 钢束组名称
        Example:
            mdb.add_tendon_group(name="钢束组1")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        return QtServer.send_dict("ADD-TENDON-GROUP", payload)

    @staticmethod
    def add_tendon_property(name: str = "", tendon_type: int = 0, material_name: str = "", duct_type: int = 1,
                            steel_type: int = 1, steel_detail: list[float] = None,
                            loos_detail: Optional[Union[list,tuple]] = None,
                            slip_info: Optional[tuple[float, float]] = None):
        """
        添加钢束特性
        Args:
             name:钢束特性名
             tendon_type: 0-PRE 1-POST 2-体外
             material_name: 钢材材料所属名称
             duct_type: 1-金属波纹管  2-塑料波纹管  3-铁皮管  4-钢管  5-抽芯成型
             steel_type: 1-钢绞线  2-螺纹钢筋
             steel_detail: 钢束详细信息
                _钢绞线[钢束面积,孔道直径,摩阻系数,偏差系数]_
                _螺纹钢筋[钢筋直径,钢束面积,孔道直径,摩阻系数,偏差系数,张拉方式(1-一次张拉 2-超张拉)]_
             loos_detail: 松弛信息[公规,张拉,松弛]/[铁规，松弛]/[英规,Kp,松弛天数]/[美规,KL] (仅钢绞线需要,默认为[1,1,1])
                _规范:1-公规 2-铁规_ 3-不考虑松弛 4-英规 5-美规
                _张拉方式:1-一次张拉 2-超张拉_
                _松弛类型：1-一般松弛 2-低松弛_
             slip_info: 滑移信息[始端距离,末端距离] 默认为[0.006, 0.006]
        Example:
            mdb.add_tendon_property(name="钢束1",tendon_type=0,material_name="预应力材料",duct_type=1,steel_type=1,
                                    steel_detail=[0.00014,0.10,0.25,0.0015],loos_detail=[1,1,1])
        Returns: 无
        """
        payload = {
            "name": name,
            "tendon_type": tendon_type,
            "material_name": material_name,
            "duct_type": duct_type,
            "steel_type": steel_type,
            "steel_detail": steel_detail,
            "loos_detail": loos_detail,
            "slip_info": slip_info,
        }
        return QtServer.send_dict("ADD-TENDON-PROPERTY", payload)

    @staticmethod
    def add_tendon_3d(name: str, property_name: str = "", group_name: str = "默认钢束组",
                      num: int = 1, line_type: int = 1, position_type=1,
                      control_points: Optional[list[tuple[float, float, float, float]]] = None,
                      point_insert: tuple[float, float, float] = None,
                      tendon_direction: Optional[tuple[float, float, float]] = None,
                      rotation_angle: float = 0, rotate_bias: tuple[float, float] = None,
                      track_group: str = "默认结构组", projection: bool = True):
        """
        添加三维钢束，支持覆盖添加
        Args:
             name:钢束名称
             property_name:钢束特性名称
             group_name:默认钢束组
             num:根数
             line_type:1-导线点  2-折线点
             position_type: 定位方式 1-直线  2-轨迹线
             control_points: 控制点信息[(x1,y1,z1,r1),(x2,y2,z2,r2)....]
             point_insert: 定位方式 (直线时为插入点坐标[x,y,z]  轨迹线时[插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id])
             tendon_direction:直线钢束X方向向量  默认为x轴即[1,0,0] (轨迹线不用赋值)
             rotation_angle:绕钢束旋转角度
             rotate_bias:绕钢束旋转偏心X、Y
             track_group:轨迹线结构组名  (直线时不用赋值)
             projection:直线钢束投影 (默认为true)
        Example:
            mdb.add_tendon_3d("BB1",property_name="22-15",num=2,position_type=1,
                    control_points=[(0,0,-1,0),(10,0,-1,0)],point_insert=(0,0,0))
            mdb.add_tendon_3d("BB1",property_name="22-15",num=2,position_type=2,
                    control_points=[(0,0,-1,0),(10,0,-1,0)],point_insert=(1,1,1),track_group="轨迹线结构组1")
        Returns: 无
        """
        payload = {
            "name": name,
            "property_name": property_name,
            "group_name": group_name,
            "num": num,
            "line_type": line_type,
            "position_type": position_type,
            "control_points": control_points,
            "point_insert": point_insert,
            "tendon_direction": tendon_direction,
            "rotation_angle": rotation_angle,
            "rotate_bias": rotate_bias,
            "track_group": track_group,
            "projection": projection,
        }
        return QtServer.send_dict("ADD-TENDON-3D", payload)

    @staticmethod
    def add_tendon_2d(name: str, property_name: str = "", group_name: str = "默认钢束组",
                      num: int = 1, line_type: int = 1, position_type: int = 1,
                      symmetry: int = 2, control_points: list[tuple[float, float, float]] = None,
                      control_points_lateral: Optional[list[tuple[float, float, float]]] = None,
                      point_insert: tuple[float, float, float] = None,
                      tendon_direction: Optional[tuple[float, float, float]] = None,
                      rotation_angle: float = 0, rotate_bias: tuple[float, float] = None,
                      track_group: str = "默认结构组", projection: bool = True):
        """
        添加三维钢束，支持覆盖添加
        Args:
             name:钢束名称
             property_name:钢束特性名称
             group_name:默认钢束组
             num:根数
             line_type:1-导线点  2-折线点
             position_type: 定位方式 1-直线  2-轨迹线
             symmetry: 对称点 0-左端点 1-右端点 2-不对称
             control_points: 控制点信息[(x1,z1,r1),(x2,z2,r2)....]
             control_points_lateral: 控制点横弯信息[(x1,y1,r1),(x2,y2,r2)....]，无横弯时不必输入
             point_insert: 定位方式 (直线时为插入点坐标[x,y,z]  轨迹线时[插入端(1-I 2-J),插入方向(1-ij 2-ji),插入单元id])
             tendon_direction:直线钢束X方向向量  默认为x轴即[1,0,0] (轨迹线不用赋值)
             rotation_angle:绕钢束旋转角度
             rotate_bias:绕钢束旋转偏心X、Y
             track_group:轨迹线结构组名  (直线时不用赋值)
             projection:直线钢束投影 (默认为true)
        Example:
            mdb.add_tendon_2d(name="BB1",property_name="22-15",num=2,position_type=1,
                    control_points=[(0,-1,0),(10,-1,0)],point_insert=(0,0,0))
            mdb.add_tendon_2d(name="BB1",property_name="22-15",num=2,position_type=2,
                    control_points=[(0,-1,0),(10,-1,0)],point_insert=(1,1,1),track_group="轨迹线结构组1")
        Returns: 无
        """
        payload = {
            "name": name,
            "property_name": property_name,
            "group_name": group_name,
            "num": num,
            "line_type": line_type,
            "position_type": position_type,
            "symmetry": symmetry,
            "control_points": control_points,
            "control_points_lateral": control_points_lateral,
            "point_insert": point_insert,
            "tendon_direction": tendon_direction,
            "rotation_angle": rotation_angle,
            "rotate_bias": rotate_bias,
            "track_group": track_group,
            "projection": projection,
        }
        return QtServer.send_dict("ADD-TENDON-2D", payload)

    @staticmethod
    def add_tendon_elements(ids):
        """
        添加预应力单元
        Args:
             ids:单元编号支持数或列表且支持XtoYbyN形式字符串
        Example:
            mdb.add_tendon_elements(ids=[1,2,4,6])
        Returns: 无
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
        }
        return QtServer.send_dict("ADD-TENDON-ELEMENTS", payload)

    @staticmethod
    def update_tendon_property_material(name: str, material_name: str):
        """
        更新钢束特性材料
        Args:
            name:钢束特性名
            material_name:材料名
        Example:
            mdb.update_tendon_property_material("特性1",material_name="材料1")
        Returns:无
        """
        payload = {
            "name": name,
            "material_name": material_name,
        }
        return QtServer.send_dict("UPDATE-TENDON-PROPERTY-MATERIAL", payload)

    @staticmethod
    def update_tendon_property(name: str, new_name: str = "", tendon_type: int = 0, material_name: str = "", duct_type: int = 1,
                               steel_type: int = 1, steel_detail: list[float] = None, loos_detail: tuple[int, int, int] = None,
                               slip_info: tuple[float, float] = None):
        """
        更新钢束特性
        Args:
            name:钢束特性名
            new_name:新钢束特性名,默认不修改
            tendon_type: 0-PRE 1-POST 2-体外
            material_name: 钢材材料名
            duct_type: 1-金属波纹管  2-塑料波纹管  3-铁皮管  4-钢管  5-抽芯成型
            steel_type: 1-钢绞线  2-螺纹钢筋
            steel_detail: 钢束详细信息
                _钢绞线[钢束面积,孔道直径,摩阻系数,偏差系数]
                _螺纹钢筋[钢筋直径,钢束面积,孔道直径,摩阻系数,偏差系数,张拉方式(1-一次张拉 2-超张拉)]
            loos_detail: 松弛信息[规范(1-公规 2-铁规),张拉(1-一次张拉 2-超张拉),松弛(1-一般松弛 2-低松弛)] (仅钢绞线需要,默认为[1,1,1])
            slip_info: 滑移信息[始端距离,末端距离] 默认为[0.006, 0.006]
        Example:
            mdb.update_tendon_property(name="钢束1",tendon_type=0,material_name="材料1",duct_type=1,steel_type=1,
                                    steel_detail=[0.00014,0.10,0.25,0.0015],loos_detail=(1,1,1))
        Returns:无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "tendon_type": tendon_type,
            "material_name": material_name,
            "duct_type": duct_type,
            "steel_type": steel_type,
            "steel_detail": steel_detail,
            "loos_detail": loos_detail,
            "slip_info": slip_info,
        }
        return QtServer.send_dict("UPDATE-TENDON-PROPERTY", payload)

    @staticmethod
    def update_tendon_name(name: str, new_name: str = ""):
        """
        更新钢束名称
        Args:
            name:原钢束名
            new_name:新钢束名
        Example:
            mdb.update_tendon_name("钢束1","钢束2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-TENDON-NAME", payload)

    @staticmethod
    def update_element_component_type(ids=None, component_type: int = 2):
        """
        赋予单元构件类型
        Args:
            ids: 钢束构件所在单元编号集合且支持XtoYbyN形式字符串
            component_type:0-钢结构构件 1-钢筋混凝土构件 2-预应力混凝土构件
        Example:
           mdb.update_element_component_type(ids=[1,2,3,4],component_type=2)
        Returns: 无
        """
        payload = {
            "ids": QtDataHelper.parse_ids_to_array(ids),
            "component_type": component_type,
        }
        return QtServer.send_dict("UPDATE-ELEMENT-COMPONENT-TYPE", payload)

    @staticmethod
    def update_tendon_group(name: str, new_name: str = ""):
        """
        更新钢束组名
        Args:
            name:原钢束组名
            new_name:新钢束组名
        Example:
            mdb.update_tendon_group("钢束组1","钢束组2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-TENDON-GROUP", payload)

    @staticmethod
    def remove_tendon(name: str = "", index: int = -1):
        """
        按照名称或编号删除钢束,默认时删除所有钢束
        Args:
             name:钢束名称
             index:钢束编号
        Example:
            mdb.remove_tendon(name="钢束1")
            mdb.remove_tendon(index=1)
            mdb.remove_tendon()
        Returns: 无
        """
        payload = {
            "name": name,
            "index": index,
        }
        return QtServer.send_dict("REMOVE-TENDON", payload)

    @staticmethod
    def remove_tendon_property(name: str = "", index: int = -1):
        """
        按照名称或编号删除钢束组,默认时删除所有钢束组
        Args:
             name:钢束组名称
             index:钢束组编号
        Example:
            mdb.remove_tendon_property(name="钢束特性1")
            mdb.remove_tendon_property(index=1)
            mdb.remove_tendon_property()
        Returns: 无
        """
        payload = {
            "name": name,
            "index": index,
        }
        return QtServer.send_dict("REMOVE-TENDON-PROPERTY", payload)

    @staticmethod
    def remove_pre_stress(tendon_name: str = ""):
        """
        删除预应力
        Args:
             tendon_name:钢束组,默认则删除所有预应力荷载
        Example:
            mdb.remove_pre_stress(tendon_name="钢束1")
            mdb.remove_pre_stress()
        Returns: 无
        """
        payload = {"tendon_name": tendon_name} if tendon_name != "" else None
        return QtServer.send_dict("REMOVE-PRE-STRESS", payload)

    @staticmethod
    def remove_tendon_group(name: str = ""):
        """
        按照钢束组名称或钢束组编号删除钢束组，两参数均为默认时删除所有钢束组
        Args:
             name:钢束组名称,默认自动识别 (可选参数)
        Example:
            mdb.remove_tendon_group(name="钢束组1")
        Returns: 无
        """
        payload = {"name": name} if name != "" else None
        return QtServer.send_dict("REMOVE-TENDON-GROUP", payload)
    # endregion
