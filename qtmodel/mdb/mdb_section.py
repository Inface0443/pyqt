import json
from typing import Union

from qtmodel.core.data_helper import QtDataHelper
from qtmodel.core.qt_server import QtServer


class MdbSection:
    """
    用于模型截面创建
    """

    # region 截面
    @staticmethod
    def add_section(
            index: int = 1,
            name: str = "",
            sec_type: str = "矩形",
            sec_info: list[float] = None,
            symmetry: bool = True,
            chamfer_info: list[str] = None,
            sec_right: list[float] = None,
            chamfer_right: list[str] = None,
            box_num: int = 3,
            box_height: float = 2,
            box_other_info: dict[str, list[float]] = None,
            box_other_right: dict[str, list[float]] = None,
            mat_combine: list[float] = None,
            rib_info: dict[str, list[float]] = None,
            rib_place:Union[list[tuple[int, int, float, str, int, str]],list]  = None,
            loop_segments: list[dict] = None,
            sec_lines: Union[list[tuple[float, float, float, float, float]],list]= None,
            secondary_loop_segments: list[dict] = None,
            sec_property: list[float] = None,
            bias_type: str = "中心",
            center_type: str = "质心",
            shear_consider: bool = True,
            bias_x: float = 0,
            bias_y: float = 0):
        """
        添加单一截面信息,如果截面存在则自动覆盖
        Args:
            index: 截面编号,默认自动识别
            name:截面名称
            sec_type:参数截面类型名称(详见UI界面)
            sec_info:截面信息 (必要参数)
            symmetry:混凝土截面是否对称 (仅混凝土箱梁截面需要)
            chamfer_info:混凝土截面倒角信息 (仅混凝土箱梁截面需要)
            sec_right:混凝土截面右半信息 (对称时可忽略，仅混凝土箱梁截面需要)
            chamfer_right:混凝土截面右半倒角信息 (对称时可忽略，仅混凝土箱梁截面需要)
            box_num: 混凝土箱室数 (仅混凝土箱梁截面需要)
            box_height: 混凝土箱梁梁高 (仅混凝土箱梁截面需要)
            box_other_info: 混凝土箱梁额外信息(键包括"i1" "B0" "B4" "T4" 值为列表)
            box_other_right: 混凝土箱梁额外信息(对称时可忽略，键包括"i1" "B0" "B4" "T4" 值为列表)
            mat_combine: 组合截面材料信息 (仅组合材料需要) [弹性模量比s/c、密度比s/c、钢材泊松比、混凝土泊松比、热膨胀系数比s/c]
            rib_info:肋板信息
            rib_place:肋板位置 list[tuple[布置具体部位,参考点0-下/左,距参考点间距,肋板名，加劲肋位置0-上/左 1-下/右 2-两侧,加劲肋名]]
                _布置具体部位(工字钢梁) 1-上左 2-上右 3-腹板 4-下左 5-下右
                _布置具体部位(箱型钢梁) 1-上左 2-上中 3-上右 4-左腹板 5-右腹板 6-下左 7-下中 8-下右
            loop_segments:线圈坐标集合 list[dict] dict示例:{"main":[(x1,y1),(x2,y2)...],"sub1":[(x1,y1),(x2,y2)...],"sub2":[(x1,y1),(x2,y2)...]}
            sec_lines:线宽集合[(x1,y1,x2,y3,thick),]
            secondary_loop_segments:辅材线圈坐标集合 list[dict] (同loop_segments)，建议以左下角为组合截面原点建立截面
            sec_property:截面特性(参考UI界面共计29个参数)，可选参数，指定截面特性时不进行截面计算
            bias_type:偏心类型 默认中心
            center_type:中心类型 默认质心
            shear_consider:考虑剪切 bool 默认考虑剪切变形
            bias_x:自定义偏心点x坐标 (仅自定义类型偏心需要,相对于center_type偏移)
            bias_y:自定义偏心点y坐标 (仅自定义类型偏心需要,相对于center_type偏移)
        Example:
            mdb.add_section(name="截面1",sec_type="矩形",sec_info=[2,4],bias_type="中心")
            mdb.add_section(name="截面2",sec_type="混凝土箱梁",box_height=2,box_num=3,
                sec_info=[0.2,0.4,0.1,0.13,3,1,2,1,0.02,0,12,5,6,0.28,0.3,0.5,0.5,0.5,0.2],
                chamfer_info=["1*0.2,0.1*0.2","0.5*0.15,0.3*0.2","0.4*0.2","0.5*0.2"])
            mdb.add_section(name="钢梁截面1",sec_type="工字钢梁",sec_info=[0,0,0.5,0.5,0.5,0.5,0.7,0.02,0.02,0.02])
            mdb.add_section(name="钢梁截面2",sec_type="箱型钢梁",sec_info=[0,0.15,0.25,0.5,0.25,0.15,0.4,0.15,0.7,0.02,0.02,0.02,0.02],
                rib_info = {"板肋1": [0.1,0.02],"T形肋1":[0.1,0.02,0.02,0.02]},
                rib_place = [(1, 0, 0.1, "板肋1", 2, "默认名称1"),
                            (1, 0, 0.2, "板肋1", 2, "默认名称1")])
        Returns: 无
            """
        if (bias_x, bias_y) != (0, 0):
            bias = f"{bias_x:g},{bias_y:g}"
        else:
            bias = f"{center_type},{bias_type}"
        s = ""
        if sec_property is not None:
            s += "*SEC-PROPERTY\r\n" + f"ID={index},{name},1,{'YES' if shear_consider else 'NO'},{bias}\r\n"
            s += ",".join(f"{x:g}" for x in sec_property) + "\r\n"
        s += "*SEC-INFO\r\n" + f"ID={index},{name},{sec_type},{'YES' if shear_consider else 'NO'},{bias}\r\n"
        s += QtDataHelper.str_section(
            sec_type,
            sec_info,
            symmetry,
            chamfer_info,
            sec_right,
            chamfer_right,
            box_num,
            box_height,
            box_other_info,
            box_other_right,
            mat_combine,
            rib_info,
            rib_place,
            loop_segments,
            sec_lines,
            secondary_loop_segments)
        QtServer.send_command(s, "QDAT")

    @staticmethod
    def add_single_section(index: int = -1, name: str = "", sec_type: str = "矩形", sec_data: dict = None):
        """
        以字典形式添加单一截面
        Args:
            index:截面编号
            name:截面名称
            sec_type:截面类型
            sec_data:截面信息字典，键值参考添加add_section方法参数
        Example:
            mdb.add_single_section(index=1,name="变截面1",sec_type="矩形",
                sec_data={"sec_info":[1,2],"bias_type":"中心"})
        Returns: 无
        """
        shear_consider = sec_data.get("shear_consider", True)
        bias_type = sec_data.get("bias_type", "中心")
        center_type = sec_data.get("center_type", "质心")
        bias_x = sec_data.get("bias_x", 0)
        bias_y = sec_data.get("bias_y", 0)
        if (bias_x, bias_y) != (0, 0):
            bias = f"{bias_x:g},{bias_y:g}"
        else:
            bias = f"{center_type},{bias_type}"
        sec_property: Union[list[float], None] = sec_data.get("sec_property", None)
        s = ""
        if sec_property is not None:
            s += "*SEC-PROPERTY\r\n" + f"ID={index},{name},1,{'YES' if shear_consider else 'NO'},{bias}\r\n"
            s += ",".join(f"{x:g}" for x in sec_property) + "\r\n"
        s += "*SEC-INFO\r\n" + f"ID={index},{name},{sec_type},{'YES' if shear_consider else 'NO'},{bias}\r\n"
        s += QtDataHelper.get_str_by_data(sec_type, sec_data)
        QtServer.send_command(s, "QDAT")

    @staticmethod
    def add_tapper_section(index: int, name: str = "", sec_type: str = "矩形", sec_begin: dict = None,
                           sec_end: dict = None,
                           shear_consider: bool = True, sec_normalize: bool = False):
        """
        添加变截面,字典参数参考单一截面,如果截面存在则自动覆盖
        Args:
            index:截面编号
            name:截面名称
            sec_type:截面类型
            sec_begin:截面始端截面信息字典，键值参考添加add_section方法参数
            sec_end:截面末端截面信息字典，键值参考添加add_section方法参数
            shear_consider:考虑剪切变形
            sec_normalize:变截面线段线圈重新排序
        Example:
            mdb.add_tapper_section(index=1,name="变截面1",sec_type="矩形",
                sec_begin={"sec_info":[1,2],"bias_type":"中心"},
                sec_end={"sec_info":[2,2],"bias_type":"中心"})
        Returns: 无
        """
        bias_type_i = sec_begin.get("bias_type", "中心")
        center_type_i = sec_begin.get("center_type", "质心")
        bias_x_i = sec_begin.get("bias_x", 0)
        bias_y_i = sec_begin.get("bias_y", 0)
        sec_property_i: Union[list[float], None] = sec_begin.get("sec_property", None)
        bias_type_j = sec_end.get("bias_type", "中心")
        center_type_j = sec_end.get("center_type", "质心")
        bias_x_j = sec_end.get("bias_x", 0)
        bias_y_j = sec_end.get("bias_y", 0)
        sec_property_j: Union[list[float], None] = sec_end.get("sec_property", None)

        if (bias_x_i, bias_y_i) != (0, 0):
            bias1 = f"{bias_x_i:g},{bias_y_i:g}"
        else:
            bias1 = f"{center_type_i},{bias_type_i}"
        if (bias_x_j, bias_y_j) != (0, 0):
            bias2 = f"{bias_x_j:g},{bias_y_j:g}"
        else:
            bias2 = f"{center_type_j},{bias_type_j}"
        s = ""
        # 先导入截面特性，以免重复计算截面
        if sec_property_i is not None and sec_property_j is not None:
            s += "*SEC-PROPERTY\r\n" + f"ID={index},{name},2,{'YES' if shear_consider else 'NO'},{bias1},{bias2}\r\n"
            s += ",".join(f"{x:g}" for x in sec_property_i) + "\r\n"
            s += ",".join(f"{x:g}" for x in sec_property_j) + "\r\n"

        # 再导入截面信息
        s += ("*SEC-INFO\r\n" +
              f"ID={index},{name},{sec_type}-变截面,{'YES' if shear_consider else 'NO'},{bias1},{bias2}\r\n")
        # I 端截面
        s += "I=\r\n"
        s += QtDataHelper.get_str_by_data(sec_type, sec_begin)
        # J 端截面
        s += "J=\r\n"
        s += QtDataHelper.get_str_by_data(sec_type, sec_end)
        QtServer.send_command(s, "QDAT")
        if sec_normalize:
            params = {
                "version": QtServer.QT_VERSION,
                "index": index,
            }
            json_string = json.dumps(params, indent=2)
            QtServer.send_command(json_string, "NORMALIZE-SEC")


    @staticmethod
    def calculate_section_property():
        """
        重新计算所有截面特性
        Args: 无
        Example:
            mdb.calculate_section_property()
        Returns: 无
        """
        try:
            QtServer.send_command(header="CALC-SEC")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def remove_unused_sections():
        """
        删除未使用截面
        Args: 无
        Example:
            mdb.remove_unused_sections()
        Returns: 无
        """
        try:
            QtServer.send_command(header="REMOVE-UNUSED-SEC")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_tapper_section_by_id(index: int = -1, name: str = "", begin_id: int = 1, end_id: int = 1,
                                 shear_consider: bool = True, sec_normalize: bool = False):
        """
        添加变截面,需先建立单一截面
        Args:
            index:截面编号
            name:截面名称
            begin_id:截面始端编号
            end_id:截面末端编号
            shear_consider:考虑剪切变形
            sec_normalize: 开启变截面线圈和线宽自适应排序 (避免两端截面绘制顺序导致的渲染和计算失效)
        Example:
            mdb.add_tapper_section_by_id(name="变截面1",begin_id=1,end_id=2)
        Returns: 无
        """
        payload = {
            "index": index,
            "name": name,
            "begin_id": begin_id,
            "end_id": end_id,
            "shear_consider": shear_consider,
            "sec_normalize": sec_normalize,
        }
        return QtServer.send_dict("ADD-TAPPER-SEC-BY-ID", payload)

    @staticmethod
    def update_single_section(index: int, new_id: int = -1, name: str = "", sec_type: str = "矩形", sec_data: dict = None):
        """
        todo 以字典形式添加单一截面
        Args:
            index:截面编号
            new_id:新截面编号，默认为-1时不修改截面编号
            name:截面名称
            sec_type:截面类型
            sec_data:截面信息字典，键值参考添加add_section方法参数
        Example:
            mdb.update_single_section(index=1,name="变截面1",sec_type="矩形",
                sec_data={"sec_info":[1,2],"bias_type":"中心"})
        Returns: 无
        """
        payload = {
            "index": index,
            "new_id": new_id,
            "name": name,
            "sec_type": sec_type,
            "sec_data": sec_data,
        }
        return QtServer.send_dict("UPDATE-SINGLE-SEC", payload)

    @staticmethod
    def update_tapper_section(index: int, new_id: int = -1, name: str = "", sec_type: str = "矩形", sec_begin: dict = None, sec_end: dict = None,
                              shear_consider: bool = True, sec_normalize: bool = False):
        """
        todo 添加变截面,字典参数参考单一截面,如果截面存在则自动覆盖
        Args:
            index:截面编号
            new_id:新截面编号，默认不修改截面编号
            name:截面名称
            sec_type:截面类型
            sec_begin:截面始端编号
            sec_end:截面末端编号
            shear_consider:考虑剪切变形
            sec_normalize:变截面线段线圈重新排序
        Example:
            mdb.add_tapper_section(index=1,name="变截面1",sec_type="矩形",
                sec_begin={"sec_info":[1,2],"bias_type":"中心"},
                sec_end={"sec_info":[2,2],"bias_type":"中心"})
        Returns: 无
        """
        payload = {
            "index": index,
            "new_id": new_id,
            "name": name,
            "sec_type": sec_type,
            "sec_begin": sec_begin,
            "sec_end": sec_end,
            "shear_consider": shear_consider,
            "sec_normalize": sec_normalize,
        }
        return QtServer.send_dict("UPDATE-TAPPER-SEC", payload)

    @staticmethod
    def update_section_bias(index: int = 1, bias_type: str = "中心", center_type: str = "质心", shear_consider: bool = True,
                            bias_point: list[float] = None, side_i: bool = True):
        """
        todo 更新截面偏心
        Args:
             index:截面编号
             bias_type:偏心类型
             center_type:中心类型
             shear_consider:考虑剪切
             bias_point:自定义偏心点(仅自定义类型偏心需要)
             side_i: 是否为截面I,否则为截面J(仅变截面需要)
        Example:
            mdb.update_section_bias(index=1,bias_type="中上",center_type="几何中心")
            mdb.update_section_bias(index=1,bias_type="自定义",bias_point=[0.1,0.2])
        Returns: 无
        """
        payload = {
            "index": index,
            "bias_type": bias_type,
            "center_type": center_type,
            "shear_consider": shear_consider,
            "bias_point": bias_point,
            "side_i": side_i,
        }
        return QtServer.send_dict("UPDATE-SEC-BIAS", payload)

    @staticmethod
    def update_section_property(index: int, sec_property: list[float], side_i: bool = True):
        """
        todo 更新截面特性
        Args:
            index:截面号
            sec_property:截面特性值参考UI共计26个数值
            side_i:是否为I端截面(仅变截面需要)
        Example:
            mdb.update_section_property(index=1,sec_property=[i for i in range(1,27)])
        Returns: 无
        """
        payload = {
            "index": index,
            "sec_property": sec_property,
            "side_i": side_i,
        }
        return QtServer.send_dict("UPDATE-SEC-PROPERTY", payload)

    @staticmethod
    def update_section_id(index: int, new_id: int):
        """
        todo 更新截面编号
        Args:
            index: 原编号
            new_id: 新编号
        Example:
            mdb.update_section_id(index=1,new_id=2)
        Returns:无
        """
        payload = {
            "index": index,
            "new_id": new_id,
        }
        return QtServer.send_dict("UPDATE-SEC-ID", payload)



    @staticmethod
    def remove_section(ids=None):
        """
        删除截面信息,默认则删除所有截面
        Args:
            ids: 截面编号
        Example:
            mdb.remove_section(1)
            mdb.remove_section("1to100")
        Returns: 无
        """
        payload = {"index": QtDataHelper.parse_ids_to_array(ids),}
        return QtServer.send_dict("REMOVE-SEC", payload)

    # endregion

    # region 变截面组
    @staticmethod
    def add_tapper_section_group(ids=None, name: str = "", factor_w: float = 1.0, factor_h: float = 1.0,
                                 ref_w: int = 0, ref_h: int = 0, dis_w: float = 0, dis_h: float = 0,
                                 parameter_info: dict[str, str] = None):
        """
        添加变截面组
        Args:
             ids:变截面组单元号,支持XtoYbyN类型字符串
             name: 变截面组名
             factor_w: 宽度方向变化阶数 线性(1.0) 非线性(!=1.0)
             factor_h: 高度方向变化阶数 线性(1.0) 非线性(!=1.0)
             ref_w: 宽度方向参考点 0-i 1-j
             ref_h: 高度方向参考点 0-i 1-j
             dis_w: 宽度方向距离
             dis_h: 高度方向距离
             parameter_info:参数化变截面组信息,键为参数名(参考UI)值为如下三种类型
                 1(非线性),指数,参考点(I/J),距离
                 2(自定义),变化长1,终点值1,变化长2,终点值2...
                 3(圆弧),半径,参考点(I/J)
        Example:
            mdb.add_tapper_section_group(ids=[1,2,3,4],name="变截面组1")
            mdb.add_tapper_section_group(ids=[1,2,3,4],name="参数化变截面组",parameter_info={"梁高(H)":"1,2,I,0"})
        Returns: 无
        """
        if ids is None:
            id_str = ""
        elif isinstance(ids, list):  # 列表转化为XtoYbyN
            id_str = QtDataHelper.parse_int_list_to_str(ids)
        else:
            id_str = str(ids)
        if parameter_info is None:
            s = "*TSGROUP\r\n" + f"{name},{id_str},{factor_w:g},{ref_w},{dis_w:g},{factor_h:g},{ref_h},{dis_h:g}\r\n"

            QtServer.send_command(s, "QDAT")
        if parameter_info is not None:
            s = "*PARA-TSGROUP\r\n" + f"NAME={name},{id_str}\r\n"
            for key, value in parameter_info.items():
                s += f"{key}={value}\r\n"
            QtServer.send_command(s, "QDAT")


    @staticmethod
    def add_elements_to_tapper_section_group(name: str, ids=None):
        """
        添加单元到变截面组
        Args:
          name:变截面组名称
          ids:新增单元编号
        Example:
          mdb.add_elements_to_tapper_section_group("变截面组1",ids=[1,2,3,4,5,6])
          mdb.add_elements_to_tapper_section_group("变截面组1",ids="1to6")
        Returns:无
        """
        payload = {
            "name": name,
            "ids": QtDataHelper.parse_ids_to_array(ids),
        }
        return QtServer.send_dict("ADD-ELEMENTS-TO-TAPPER-SEC-GROUP", payload)

    @staticmethod
    def add_tapper_section_from_group(name: str = ""):
        """
        将变截面组转为变截面
        Args:
            name: 变截面组名，默认则转化全部变截面组
        Example:
            mdb.add_tapper_section_from_group()
            mdb.add_tapper_section_from_group("变截面组1")
        Returns: 无
        """
        payload = {"name": name}
        return QtServer.send_dict("ADD-TAPPER-SEC-FROM-GROUP", payload)

    @staticmethod
    def update_tapper_section_group(name: str, new_name="", ids=None, factor_w: float = 1.0, factor_h: float = 1.0,
                                    ref_w: int = 0, ref_h: int = 0, dis_w: float = 0, dis_h: float = 0,
                                    parameter_info: dict[str, str] = None):
        """
        todo 更新变截面组
        Args:
             name:变截面组组名
             new_name: 新变截面组名
             ids:变截面组包含的单元号,支持XtoYbyN形式字符串
             factor_w: 宽度方向变化阶数 线性(1.0) 非线性(!=1.0)
             factor_h: 高度方向变化阶数 线性(1.0) 非线性(!=1.0)
             ref_w: 宽度方向参考点 0-i 1-j
             ref_h: 高度方向参考点 0-i 1-j
             dis_w: 宽度方向距离
             dis_h: 高度方向距离
             parameter_info:参数化变截面组信息,键为参数名(参考UI)值为如下三种类型
                 1(非线性),指数,参考点(I/J),距离
                 2(自定义),变化长1,终点值1,变化长2,终点值2...
                 3(圆弧),半径,参考点(I/J)
        Example:
            mdb.update_tapper_section_group(name="变截面组1",ids=[1,2,3,4])
            mdb.update_tapper_section_group(name="变截面组2",ids="1t0100")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "ids": ids,
            "factor_w": factor_w,
            "factor_h": factor_h,
            "ref_w": ref_w,
            "ref_h": ref_h,
            "dis_w": dis_w,
            "dis_h": dis_h,
            "parameter_info": parameter_info,
        }
        return QtServer.send_dict("UPDATE-TAPPER-SEC-GROUP", payload)

    @staticmethod
    def remove_tapper_section_group(name: str = ""):
        """
        todo  删除变截面组，默认删除所有变截面组
        Args:
            name:变截面组名称
        Example:
            mdb.remove_tapper_section_group()
            mdb.remove_tapper_section_group("变截面组1")
        Returns:无
        """
        payload = {"name": name}
        return QtServer.send_dict("REMOVE-TAPPER-SEC-GROUP", payload)
    # endregion
