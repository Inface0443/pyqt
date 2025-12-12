from typing import Optional

from qtmodel.core.qt_server import QtServer


class MdbProperty:
    """
    用于模型特性定义，包括材料和板厚
    """

    # region 材料
    @staticmethod
    def add_material(index: int = -1, name: str = "", mat_type: int = 1, standard: int = 1, database: str = "C50",
                     construct_factor: float = 1, modified: bool = False, data_info: list[float] = None,
                     creep_id: int = -1, f_cuk: float = 0, composite_info: Optional[tuple[str, str]] = None):
        """
        添加材料
        Args:
            index:材料编号,默认为最大Id+1
            name:材料名称，默认覆盖添加
            mat_type: 材料类型,1-混凝土 2-钢材 3-预应力 4-钢筋 5-自定义 6-组合材料
            standard:规范序号,参考UI 默认从1开始
            database:数据库名称
            construct_factor:构造系数
            modified:是否修改默认材料参数,默认不修改 (可选参数)
            data_info:材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (可选参数)
            creep_id:徐变材料id (可选参数)
            f_cuk: 立方体抗压强度标准值 (可选参数)
            composite_info: 主材名和辅材名 (仅组合材料需要)
        Example:
            mdb.add_material(index=1,name="混凝土材料1",mat_type=1,standard=1,database="C50")
            mdb.add_material(index=1,name="自定义材料1",mat_type=5,data_info=[3.5e10,2.5e4,0.2,1.5e-5])
        Returns: 无
        """
        if mat_type == 5:
            modified = True
        if modified and len(data_info) != 4:
            raise Exception("操作错误,modify_info数据无效!")
        payload = {
            "index": index,
            "name": name,
            "mat_type": mat_type,
            "standard": standard,
            "database": database,
            "construct_factor": construct_factor,
            "modified": modified,
            "data_info": data_info,
            "creep_id": creep_id,
            "f_cuk": f_cuk,
            "composite_info": composite_info,
        }
        return QtServer.send_dict("ADD-MATERIAL", payload)


    @staticmethod
    def add_time_parameter(index: int = -1, name: str = "", code_index: int = 1, time_parameter: list[float] = None,
                           creep_data: list[tuple[str, float]] = None, shrink_data: str = ""):
        """
        添加收缩徐变材料
        Args:
            index:材料编号,默认为最大Id+1
            name: 收缩徐变名
            code_index: 1-公规JTG3362-2018  2-公规JTGD62-2004 3-公规JTJ023-85 4-铁规TB10092-2017
                5-地铁GB50157-2013  6-老化理论  7-BS5400_4_1990  8-AASHTO_LRFD_2017    1000-AASHTO_LRFD_2017
            time_parameter: 对应规范的收缩徐变参数列表,默认不改变规范中信息 (可选参数)
            creep_data: 徐变数据 [(函数名,龄期)...]
            shrink_data: 收缩函数名
        Example:
            mdb.add_time_parameter(name="收缩徐变材料1",code_index=1)
        Returns: 无
        """
        payload = {
            "index": index,
            "name": name,
            "code_index": code_index,
            "time_parameter": time_parameter,
            "creep_data": creep_data,
            "shrink_data": shrink_data,
        }
        return QtServer.send_dict("ADD-TIME-PARAMETER", payload)

    @staticmethod
    def add_creep_function(name: str, creep_data: list[tuple[float, float]], scale_factor: float = 1):
        """
        添加徐变函数
        Args:
            name:徐变函数名
            creep_data:徐变数据[(时间,徐变系数)...]
            scale_factor:缩放系数
        Example:
            mdb.add_creep_function(name="徐变函数名",creep_data=[(5,0.5),(100,0.75)])
        Returns: 无
        """
        payload = {
            "name": name,
            "creep_data": creep_data,
            "scale_factor": scale_factor,
        }
        return QtServer.send_dict("ADD-CREEP-FUNCTION", payload)


    @staticmethod
    def add_shrink_function(name: str, shrink_data: list[tuple[float, float]] = None, scale_factor: float = 1):
        """
        添加收缩函数
        Args:
            name:收缩函数名
            shrink_data:收缩数据[(时间,收缩系数)...]
            scale_factor:缩放系数
        Example:
            mdb.add_shrink_function(name="收缩函数名",shrink_data=[(5,0.5),(100,0.75)])
            mdb.add_shrink_function(name="收缩函数名",scale_factor=1.2)
        Returns: 无
        """
        payload = {
            "name": name,
            "shrink_data": shrink_data,
            "scale_factor": scale_factor,
        }
        return QtServer.send_dict("ADD-SHRINK-FUNCTION", payload)

    @staticmethod
    def remove_shrink_function(name: str = ""):
        """
        删除收缩函数
        Args:
            name:收缩函数名
        Example:
            mdb.remove_shrink_function(name="收缩函数名")
        Returns: 无
        """
        payload = {"name": name} if name else None
        return QtServer.send_dict("REMOVE-SHRINK-FUNCTION", payload)

    @staticmethod
    def remove_creep_function(name: str = ""):
        """
        删除徐变函数
        Args:
            name:徐变函数名
        Example:
            mdb.remove_creep_function(name="徐变函数名")
        Returns: 无
        """
        payload = {"name": name} if name else None
        return QtServer.send_dict("REMOVE-CREEP-FUNCTION", payload)

    @staticmethod
    def update_material_time_parameter(name: str = "", time_parameter_name: str = "", f_cuk: float = 0):
        """
        将收缩徐变参数连接到材料
        Args:
            name: 材料名
            time_parameter_name: 收缩徐变名称
            f_cuk: 材料标准抗压强度,仅自定义材料是需要输入
        Example:
            mdb.update_material_time_parameter(name="C60",time_parameter_name="收缩徐变1",f_cuk=5e7)
        Returns: 无
        """
        payload = {
            "name": name,
            "time_parameter_name": time_parameter_name,
            "f_cuk": f_cuk,
        }
        return QtServer.send_dict("UPDATE-MATERIAL-TIME-PARAMETER", payload)

    @staticmethod
    def update_material_id(name: str, new_id: int):
        """
        更新材料编号
        Args:
            name:材料名称
            new_id:新编号
        Example:
            mdb.update_material_id(name="材料1",new_id=2)
        Returns: 无
        """
        payload = {
            "name": name,
            "new_id": new_id,
        }
        return QtServer.send_dict("UPDATE-MATERIAL-ID", payload)

    @staticmethod
    def update_time_parameter_id(name: str, new_id: int):
        """
        更新时间依存材料编号
        Args:
            name:时间依存材名称
            new_id:新时间依存材编号
        Example:
            mdb.update_time_parameter_id(name="时间依存材料1",new_id=2)
        Returns: 无
        """
        payload = {
            "name": name,
            "new_id": new_id,
        }
        return QtServer.send_dict("UPDATE-TIME-PARAMETER-ID", payload)

    @staticmethod
    def remove_material(index: int = -1, name: str = ""):
        """
        删除指定材料
        Args:
            index:指定材料编号，默认则删除所有材料
            name: 指定材料名，材料名为空时按照index删除
        Example:
            mdb.remove_material()
            mdb.remove_material(index=1)
        Returns: 无
        """
        # 两者均为默认值 -> 视作删除全部，按需仅发 Header
        if index == -1 and not name:
            return QtServer.send_dict("REMOVE-MATERIAL", None)
        payload = {
            "index": index,
            "name": name,
        }
        return QtServer.send_dict("REMOVE-MATERIAL", payload)

    @staticmethod
    def update_material_construction_factor(name: str, factor: float = 1):
        """
        更新材料构造系数
        Args:
            name:指定材料编号，默认则删除所有材料
            factor:指定材料编号，默认则删除所有材料
        Example:
            mdb.update_material_construction_factor(name="材料1",factor=1.0)
        Returns: 无
        """
        payload = {
            "name": name,
            "factor": factor,
        }
        return QtServer.send_dict("UPDATE-MATERIAL-CONSTRUCTION-FACTOR", payload)

    @staticmethod
    def remove_time_parameter(name: str = ""):
        """
        删除指定时间依存材料
        Args:
            name: 指定收缩徐变材料名
        Example:
            mdb.remove_time_parameter("收缩徐变材料1")
        Returns: 无
        """
        payload = {"name": name} if name else None
        return QtServer.send_dict("REMOVE-TIME-PARAMETER", payload)

    # endregion

    # region 板厚
    @staticmethod
    def add_thickness(index: int = -1, name: str = "", t: float = 0,
                      thick_type: int = 0, bias_info: tuple[int, float] = None,
                      rib_pos: int = 0, dist_v: float = 0, dist_l: float = 0,
                      rib_v:list[float]=None, rib_l:list[float]=None):
        """
        添加板厚
        Args:
            index: 板厚id
            name: 板厚名称
            t: 板厚度
            thick_type: 板厚类型 0-普通板 1-加劲肋板
            bias_info: 默认不偏心,偏心时输入列表[type(0-厚度比 1-数值),value]
            rib_pos: 肋板位置 0-下部 1-上部
            dist_v: 纵向截面肋板间距
            dist_l: 横向截面肋板间距
            rib_v: 纵向肋板信息
            rib_l: 横向肋板信息
        Example:
            mdb.add_thickness(name="厚度1", t=0.2,thick_type=0,bias_info=(0,0.8))
            mdb.add_thickness(name="厚度2", t=0.2,thick_type=1,rib_pos=0,dist_v=0.1,rib_v=[1,1,0.02,0.02])
        Returns: 无
        """
        payload = {
            "index": index,
            "name": name,
            "t": t,
            "thick_type": thick_type,
            "bias_info": bias_info,
            "rib_pos": rib_pos,
            "dist_v": dist_v,
            "dist_l": dist_l,
            "rib_v": rib_v,
            "rib_l": rib_l,
        }
        return QtServer.send_dict("ADD-THICKNESS", payload)

    @staticmethod
    def update_thickness_id(index: int, new_id: int):
        """
        更新板厚编号
        Args:
            index: 板厚id
            new_id: 新板厚id
        Example:
            mdb.update_thickness_id(1,2)
        Returns: 无
        """
        payload = {
            "index": index,
            "new_id": new_id,
        }
        return QtServer.send_dict("UPDATE-THICKNESS-ID", payload)

    @staticmethod
    def remove_thickness(index: int = -1, name: str = ""):
        """
        删除板厚
        Args:
             index:板厚编号,默认时删除所有板厚信息
             name:默认按照编号删除,如果不为空则按照名称删除
        Example:
            mdb.remove_thickness()
            mdb.remove_thickness(index=1)
            mdb.remove_thickness(name="板厚1")
        Returns: 无
        """
        # 按你原有逻辑：优先按名称删除；index==-1 视为删除全部；否则按编号删除
        if name:
            payload = {"name": name}
        elif index == -1:
            payload = None  # 仅发 Header，表示“删除全部”
        else:
            payload = {"index": index}
        return QtServer.send_dict("REMOVE-THICKNESS", payload)

    # endregion
