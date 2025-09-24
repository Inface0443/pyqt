import json
from .data_helper import MdbDataHelper
from ..core.qt_server import QtServer
from typing import Union, List


class MdbDynamicLoad:
    # region 动力荷载操作
    @staticmethod
    def add_load_to_mass(name: str, factor: float = 1):
        """
        添加荷载转为质量
        Args:
            name: 荷载工况名称
            factor: 系数
        Example:
            mdb.add_load_to_mass(name="荷载工况",factor=1)
        Returns: 无
        """
        try:
            s = "*LOADTOMASS\r\n" + f"{name},{factor}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_nodal_mass(node_id: (Union[int, List[int], str]) = 1, mass_info: tuple[float, float, float, float] = None):
        """
        添加节点质量
        Args:
             node_id:节点编号，支持单个编号和编号列表
             mass_info:[m,rmX,rmY,rmZ]
        Example:
            mdb.add_nodal_mass(node_id=1,mass_info=(100,0,0,0))
        Returns: 无
        """
        try:
            if mass_info is None:
                raise Exception("操作错误，节点质量信息列表不能为空")
            if isinstance(node_id, list):    # 列表转化为XtoYbyN
                node_str = MdbDataHelper.parse_int_list_to_str(node_id)
            else:
                node_str = str(node_id)
            s = "*NODALMASS\r\n" + f"{node_str},{mass_info[0]:g},{mass_info[1]:g},{mass_info[2]:g},{mass_info[3]:g}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_spectrum_function( name: str = "", factor: float = 1.0, kind: int = 0,
                              function_info: list[tuple[float, float]] = None):
        """
        添加反应谱函数
        Args:
            name:反应谱函数名
            factor:反应谱调整系数
            kind:反应谱类型 0-无量纲 1-加速度 2-位移
            function_info:反应谱函数信息[(时间1,数值1),[时间2,数值2]]
        Example:
            mdb.add_spectrum_function(name="反应谱函数1",factor=1.0,function_info=[(0,0.02),(1,0.03)])
        Returns: 无
        """
        try:
            s = "*SPFUNC\r\n" + f"NAME={name},{factor:g},{kind}\r\n"
            if function_info is not None:
                s += ",".join(f"{time:g},{y:g}" for time,y in function_info) + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_spectrum_case(name: str = "", description: str = "", kind: int = 1, info_x: tuple[str, float] = None,
                          info_y: tuple[str, float] = None, info_z: tuple[str, float] = None):
        """
        添加反应谱工况
        Args:
             name:荷载工况名
             description:说明
             kind:组合方式 1-求模 2-求和
             info_x: 反应谱X向信息 (X方向函数名,系数)
             info_y: 反应谱Y向信息 (Y方向函数名,系数)
             info_z: 反应谱Z向信息 (Z方向函数名,系数)
        Example:
            mdb.add_spectrum_case(name="反应谱工况",info_x=("函数1",1.0))
        Returns: 无
        """
        try:
            if info_x is None and info_y is None and info_z is None:
                raise Exception("添加反应谱函数错误,无反应谱分项信息")
            s = "*SPLDCASE\r\n" + f"NAME={name},{kind},{description}\r\n"
            if info_x is not None:
                s += f"X={info_x[0]},{info_x[1]:g}\r\n"
            if info_y is not None:
                s += f"Y={info_y[0]},{info_y[1]:g}\r\n"
            if info_z is not None:
                s += f"Z={info_z[0]},{info_z[1]:g}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_boundary_element_property(index: int = -1, name: str = "", kind: str = "钩",
                                      info_x: list[float] = None, info_y: list[float] = None, info_z: list[float] = None,
                                      weight: float = 0, pin_stiffness: float = 0, pin_yield: float = 0, description: str = ""):
        """
        添加边界单元特性
        Args:
            index: 边界单元特性编号,默认自动识别
            name: 边界单元特性名称
            kind: 类型名，支持:粘滞阻尼器、支座摩阻、滑动摩擦摆(具体参考界面数据名)
            info_x: 自由度X信息(参考界面数据，例如粘滞阻尼器为[阻尼系数,速度指数]，支座摩阻为[安装方向0/1,弹性刚度/摩擦系数,恒载支承力N])
            info_y: 自由度Y信息,默认则不考虑该自由度
            info_z: 自由度Z信息
            weight: 重量（单位N）
            pin_stiffness: 剪力销刚度
            pin_yield: 剪力销屈服力
            description: 说明
        Example:
            mdb.add_boundary_element_property(name="边界单元特性",kind="粘滞阻尼器",info_x=[0.05,1])
        Returns: 无
        """
        try:
            # s = "*BDPROP\r\n" + f"NAME={name},{kind},{weight},{pin_yield},{description}\r\n"
            # if info_x is not None:
            #     s += "X=" + ",".join(f"{x:g}" for x in info_x) + "\r\n"
            # if info_y is not None:
            #     s += "Y=" + ",".join(f"{y:g}" for y in info_y) + "\r\n"
            # if info_z is not None:
            #     s += "Z=" + ",".join(f"{z:g}" for z in info_z) + "\r\n"
            # # print(s)
            # QtServer.post_command(s, "QDAT")
            params = {
                "version": QtServer.QT_VERSION,
                "index": index,
                "name": name,
                "kind": kind,
                "info_x": info_x,
                "info_y": info_y,
                "info_z": info_z,
                "weight": weight,
                "pin_stiffness": pin_stiffness,
                "pin_yield": pin_yield,
                "description": description
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.get_command(header="ADD-BOUNDARY-ELEMENT-PROPERTY", command=json_string)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_boundary_element_link(index: int = -1, property_name: str = "", node_i: int = 1, node_j: int = 2,
                                  beta: float = 0, node_system: int = 0, group_name: str = "默认边界组"):
        """
        添加边界单元连接
        Args:
            index: 边界单元连接号
            property_name: 边界单元特性名称
            node_i: 起始节点
            node_j: 终止节点
            beta: 角度
            node_system: 参考坐标系0-单元 1-整体
            group_name: 边界组名
        Example:
            mdb.add_boundary_element_link(property_name="边界单元特性",node_i=1,node_j=2,group_name="边界组1")
        Returns: 无
        """
        try:
            s = "*BDLINK\r\n" + f"{index},{property_name},{node_i},{node_j},{beta},{node_system},{group_name}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_nodal_dynamic_load(index: int = -1, node_id: int = 1, case_name: str = "",
                               function_name: str = "", force_type: int = 1, factor: float = 1, time: float = 1):
        """
        添加节点动力荷载
        Args:
            index: 节点动力荷载编号,默认自动识别
            node_id: 节点号
            case_name: 时程工况名
            function_name: 函数名称
            force_type: 荷载类型 1-X 2-Y 3-Z 4-负X 5-负Y 6-负Z
            factor: 系数
            time: 到达时间
        Example:
            mdb.add_nodal_dynamic_load(node_id=1,case_name="时程工况1",function_name="函数1",time=10)
        Returns: 无
        """
        try:
            # s = "*DMCLOAD\r\n" + f"{node_id},{case_name},{function_name},{force_type},{factor},{time}\r\n"
            # # print(s)
            # QtServer.post_command(s, "QDAT")
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "index": index,
                "node_id": node_id,
                "case_name": case_name,
                "function_name": function_name,
                "force_type": force_type,
                "factor": factor,
                "time": time
            }
            json_string = json.dumps(params, indent=2)
            QtServer.get_command(header="ADD-NODAL-DYNAMIC-LOAD", command=json_string)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_ground_motion(case_name: str = "", info_x: tuple[str, float, float] = None,
                          info_y: tuple[str, float, float] = None, info_z: tuple[str, float, float] = None):
        """
        添加地面加速度
        Args:
            case_name: 工况名称
            info_x: X方向时程分析函数信息列表(函数名,系数,到达时间)
            info_y: Y方向时程分析函数信息列表
            info_z: Z方向时程分析函数信息列表
        Example:
            mdb.add_ground_motion(case_name="时程工况1",info_x=("函数名",1,10))
        Returns: 无
        """
        try:
            s = "*GDMOTION\r\n" + f"NAME={case_name}\r\n"
            if info_x is not None:
                s += f"X={info_x[0]},{info_x[1]:g},{info_x[2]:g}\r\n"
            if info_y is not None:
                s += f"Y={info_y[0]},{info_y[1]:g},{info_y[2]:g}\r\n"
            if info_z is not None:
                s += f"Z={info_z[0]},{info_z[1]:g},{info_z[2]:g}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_time_history_case(
            index: int = -1,
            name: str = "",
            description: str = "",
            analysis_kind: int = 0,
            nonlinear_groups: list = None,
            duration: float = 1,
            time_step: float = 0.01,
            min_step: float = 1e-4,
            tolerance: float = 1e-4,
            damp_type: int = 0,
            single_damping: tuple[float, float, float, float] = None,
            group_damping: list[tuple[str, float, float, float]] = None
    ):
        """
        添加时程工况
        Args:
            index: 时程工况编号,默认自动识别
            name: 时程工况名
            description: 描述
            analysis_kind: 分析类型(0-线性 1-边界非线性)
            nonlinear_groups: 非线性结构组列表
            duration: 分析时间
            time_step: 分析时间步长
            min_step: 最小收敛步长
            tolerance: 收敛容限
            damp_type: 组阻尼类型(0-不计阻尼 1-单一阻尼 2-组阻尼)
            single_damping: 单一阻尼信息列表(周期1,阻尼比1,周期2,阻尼比2)
            group_damping: 组阻尼信息列表[(材料名1,周期1,周期2,阻尼比),(材料名2,周期1,周期2,阻尼比)...]
        Example:
            mdb.add_time_history_case(name="时程工况1",analysis_kind=0,duration=10,time_step=0.02,damp_type=2,
                group_damping=[("材料1",8,1,0.05),("材料2",8,1,0.05),("材料3",8,1,0.02)])
        Returns: 无
        """
        try:
            # s = "*THCASE\r\n" + f"NAME={name},{analysis_kind},{duration:g},{time_step:g},{min_step:g},{tolerance:g},{damp_type},{description}\r\n"
            # if analysis_kind == 1:
            #     s += "GROUP=" + ",".join(f"{x}" for x in nonlinear_groups) + "\r\n"
            # if damp_type == 1:
            #     s += f"DAMPING={single_damping[0]:g},{single_damping[1]:g},{single_damping[2]:g},{single_damping[3]:g}\r\n"
            # elif  damp_type == 2:
            #     s += "DAMPING=" + ",".join(f"{m1},{t1:g},{t2:g},{d:g}" for m1,t1,t2,d in group_damping) + "\r\n"
            # # print(s)
            # QtServer.post_command(s, "QDAT")
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "index": index,
                "name": name,
                "description": description,
                "analysis_kind": analysis_kind,
                "nonlinear_groups": nonlinear_groups or [],
                "duration": duration,
                "time_step": time_step,
                "min_step": min_step,
                "tolerance": tolerance,
                "damp_type": damp_type,
                "single_damping": list(single_damping) if single_damping else [],
                "group_damping": [list(x) for x in (group_damping or [])],
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.get_command(header="ADD-TIME-HISTORY-CASE", command=json_string)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_time_history_function(name: str = "", factor: float = 1.0, kind: int = 0, function_info: list = None):
        """
        添加时程函数
        Args:
            name: 名称
            factor: 放大系数
            kind: 0-无量纲 1-加速度 2-力 3-力矩
            function_info: 函数信息[(时间1,数值1),(时间2,数值2)]
        Example:
            mdb.add_time_history_function(name="时程函数1",factor=1,function_info=[(0,0),(0.02,0.1),[0.04,0.3]])
        Returns: 无
        """
        try:
            s = "*THFUNC\r\n" + f"NAME={name},{factor},{kind}\r\n"
            if function_info is not None:
                s += ",".join(f"{time:g},{y:g}" for time,y in function_info) + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)
    # endregion