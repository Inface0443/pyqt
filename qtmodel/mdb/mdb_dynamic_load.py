import json
from qtmodel.core.data_helper import QtDataHelper
from ..core.qt_server import QtServer
from typing import Union, List, Optional


class MdbDynamicLoad:
    """
    用于添加动力荷载操作
    """

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
    def add_nodal_mass(node_id, mass_info: tuple[float, float, float, float] = None):
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
            if isinstance(node_id, list):  # 列表转化为XtoYbyN
                node_str = QtDataHelper.parse_int_list_to_str(node_id)
            else:
                node_str = str(node_id)
            s = "*NODALMASS\r\n" + f"{node_str},{mass_info[0]:g},{mass_info[1]:g},{mass_info[2]:g},{mass_info[3]:g}\r\n"
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
    def add_ground_motion(case_name: str = "",
                          info_x: Optional[tuple[str, float, float]] = None,
                          info_y: Optional[tuple[str, float, float]] = None,
                          info_z: Optional[tuple[str, float, float]] = None):
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
            single_damping: Optional[tuple[float, float, float, float]] = None,
            group_damping: Optional[list[tuple[str, float, float, float]]] = None
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
                s += ",".join(f"{time:g},{y:g}" for time, y in function_info) + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_vehicle_dynamic_load(node_ids=None, function_name: str = "", case_name: str = "", kind: int = 1,
                                 speed_kmh: float = 120, braking: bool = False, braking_a: float = 0.8,
                                 braking_d: float = 0, time: float = 0, direction: int = 6, gap: float = 14,
                                 factor: float = 1, vehicle_info_kn: list[float] = None) -> None:
        """
        添加列车动力荷载
        Args:
            node_ids: 节点纵列节点编号集合，支持XtoYbyN形式字符串
            function_name: 函数名
            case_name: 工况名
            kind: 类型 1-ZK型车辆 2-动车组
            speed_kmh: 列车速度(km/h)
            braking: 是否考虑制动
            braking_a: 制动加速度(m/s²)
            braking_d: 制动时车头位置(m)
            time: 上桥时间(s)
            direction: 荷载方向 1-X 2-Y 3-Z 4-负X 5-负Y 6-负Z
            gap: 加载间距(m)
            factor: 放大系数
            vehicle_info_kn: 车辆参数,参数为空时则选取界面默认值,注意单位输入单位为KN
                ZK型车辆: [dW1,dW2,P1,P2,P3,P4,dD1,dD2,D1,D2,D3,LoadLength]
                动力组: [L1,L2,L3,P,N]
        Example:
            mdb.add_vehicle_dynamic_load("1to100",function_name="时程函数名",case_name="时程工况名",kind=1,speed_kmh=120,time=10)
            mdb.add_vehicle_dynamic_load([1,2,3,4,5,6,7],function_name="时程函数名",case_name="时程工况名",kind=1,speed_kmh=120,time=10)
        Returns:无
        """
        payload = {
            "node_ids": node_ids,
            "function_name": function_name,
            "case_name": case_name,
            "kind": kind,
            "speed_kmh": speed_kmh,
            "braking": braking,
            "braking_a": braking_a,
            "braking_d": braking_d,
            "time": time,
            "direction": direction,
            "gap": gap,
            "factor": factor,
            "vehicle_info_kn": vehicle_info_kn,
        }
        return QtServer.send_post("ADD-VEHICLE-DYNAMIC-LOAD", payload)

    @staticmethod
    def update_load_to_mass(name: str = "", factor: float = 1):
        """
        更新荷载转为质量
        Args:
            name:荷载工况名称
            factor:荷载工况系数
        Example:
            mdb.update_load_to_mass(name="工况1",factor=1)
        Returns: 无
        """
        payload = {
            "name": name,
            "factor": factor,
        }
        return QtServer.send_post("UPDATE-LOAD-TO-MASS", payload)

    @staticmethod
    def update_nodal_mass(node_id: int, new_node_id: int = -1, mass_info: tuple[float, float, float, float] = None):
        """
        更新节点质量
        Args:
            node_id:节点编号
            new_node_id:新节点编号，默认不改变节点
            mass_info:[m,rmX,rmY,rmZ]
        Example:
            mdb.add_nodal_mass(node_id=1,mass_info=(100,0,0,0))
        Returns: 无
        """
        payload = {
            "node_id": node_id,
            "new_node_id": new_node_id,
            "mass_info": mass_info,
        }
        return QtServer.send_post("UPDATE-NODAL-MASS", payload)

    @staticmethod
    def update_boundary_element_property(name: str = "", new_name: str = "", kind: str = "钩",
                                         info_x: Optional[list[float]] = None,
                                         info_y: Optional[list[float]] = None,
                                         info_z: Optional[list[float]] = None,
                                         weight: float = 0, pin_stiffness: float = 0, pin_yield: float = 0, description: str = "") -> None:
        """
        todo 更新边界单元特性，输入参数单位默认为N、m
        Args:
            name: 原边界单元特性名称
            new_name: 更新后边界单元特性名称，默认时不修改
            kind: 类型名，支持:粘滞阻尼器、支座摩阻、滑动摩擦摆(具体参考界面数据名)
            info_x: 自由度X信息(参考界面数据，例如粘滞阻尼器为[阻尼系数,速度指数]，支座摩阻为[安装方向0/1,弹性刚度/摩擦系数,恒载支承力N])
            info_y: 自由度Y信息
            info_z: 自由度Z信息
            weight: 重量（单位N）
            pin_stiffness: 剪力销刚度
            pin_yield: 剪力销屈服力
            description: 说明
        Example:
            mdb.update_boundary_element_property(name="old_prop",kind="粘滞阻尼器",info_x=[0.5, 0.5],weight=1000.0)
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "kind": kind,
            "info_x": info_x,
            "info_y": info_y,
            "info_z": info_z,
            "is_dx": info_x is not None,
            "is_dy": info_y is not None,
            "is_dz": info_z is not None,
            "weight": weight,
            "pin_stiffness": pin_stiffness,
            "pin_yield": pin_yield,
            "description": description,
        }
        return QtServer.send_post("UPDATE-BOUNDARY-ELEMENT-PROPERTY", payload)

    @staticmethod
    def update_boundary_element_link(index: int, property_name: str = "", node_i: int = 1, node_j: int = 2,
                                     beta: float = 0, node_system: int = 0, group_name: str = "默认边界组") -> None:
        """
        todo 更新边界单元连接
        Args:
            index: 根据边界单元连接id选择待更新对象
            property_name: 边界单元特性名
            node_i: 起始节点点
            node_j: 终点节点号
            beta: 角度参数
            node_system: 0-单元坐标系 1-整体坐标系
            group_name: 边界组名称
        Example:
            mdb.update_boundary_element_link(index=1,property_name="边界单元特性名",node_i=101,node_j=102,beta=30.0)
        Returns: 无
        """
        payload = {
            "index": index,
            "property_name": property_name,
            "node_i": node_i,
            "node_j": node_j,
            "beta": beta,
            "node_system": node_system,
            "group_name": group_name,
        }
        return QtServer.send_post("UPDATE-BOUNDARY-ELEMENT-LINK", payload)

    @staticmethod
    def update_time_history_case(name: str = "", new_name: str = "", description: str = "", analysis_kind: int = 0,
                                 nonlinear_groups: list[str] = None, duration: float = 1, time_step: float = 0.01, min_step: float = 1e-4,
                                 tolerance: float = 1e-4, damp_type: int = 0, single_damping: list[float] = None,
                                 group_damping: list[tuple[str, float, float, float]] = None) -> None:
        """
        todo 添加时程工况
        Args:
            name: 时程工况号
            new_name: 时程工况名
            description: 描述
            analysis_kind: 分析类型(0-线性 1-边界非线性)
            nonlinear_groups: 非线性结构组列表
            duration: 分析时间
            time_step: 分析时间步长
            min_step: 最小收敛步长
            tolerance: 收敛容限
            damp_type: 组阻尼类型(0-不计阻尼 1-单一阻尼 2-组阻尼)
            single_damping: 单一阻尼信息列表(周期1,周期2,频率1,频率2)
            group_damping: 组阻尼信息列表[(材料名1,周期1,周期2,阻尼比),(材料名2,周期1,周期2,阻尼比)...]
        Example:
            mdb.update_time_history_case(name="TH1",analysis_kind=1,
                nonlinear_groups=["结构组1", "结构组2"],duration=30.0,time_step=0.02,damp_type=2,
                group_damping=[("concrete", 0.1, 0.5, 0.05), ("steel", 0.1, 0.5, 0.02)])
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "description": description,
            "analysis_kind": analysis_kind,
            "nonlinear_groups": nonlinear_groups or [],
            "duration": duration,
            "time_step": time_step,
            "min_step": min_step,
            "tolerance": tolerance,
            "damp_type": damp_type,
            "single_damping": single_damping or [],
            "group_damping": group_damping or [],
        }
        return QtServer.send_post("UPDATE-TIME-HISTORY-CASE", payload)

    @staticmethod
    def update_time_history_function(name: str, new_name: str = "", factor: float = 1.0, kind: int = 0,
                                     function_info: list[tuple[float, float]] = None) -> None:
        """
        todo 更新时程函数
        Args:
            name: 更新前函数名
            new_name: 更新后函数名，默认不更新名称
            factor: 放大系数
            kind: 0-无量纲 1-加速度 2-力 3-力矩
            function_info: 函数信息[(时间1,数值1),(时间2,数值2)]
        Example:
            mdb.update_time_history_function(name="old_func",factor=1.5,kind=1,function_info=[(0.0, 0.0), (0.1, 0.5)])
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "factor": factor,
            "kind": kind,
            "function_info": function_info,
        }
        return QtServer.send_post("UPDATE-TIME-HISTORY-FUNCTION", payload)

    @staticmethod
    def update_nodal_dynamic_load(index: int = -1, node_id: int = 1, case_name: str = "", function_name: str = "",
                                  direction: int = 1, factor: float = 1, time: float = 1) -> None:
        """
        todo 更新节点动力荷载
        Args:
            index: 待修改荷载编号
            node_id: 节点号
            case_name: 时程工况名
            function_name: 函数名称
            direction: 荷载类型 1-X 2-Y 3-Z 4-负X 5-负Y 6-负Z
            factor: 系数
            time: 到达时间
        Example:
            mdb.update_nodal_dynamic_load(index=1,node_id=101,case_name="Earthquake_X",function_name="EQ_function",direction=1,factor=1.2,time=0.0 )
        Returns: 无
        """
        payload = {
            "index": index,
            "node_id": node_id,
            "case_name": case_name,
            "function_name": function_name,
            "direction": direction,
            "factor": factor,
            "time": time,
        }
        return QtServer.send_post("UPDATE-NODAL-DYNAMIC-LOAD", payload)

    @staticmethod
    def update_ground_motion(index: int, case_name: str = "",
                             info_x: Optional[tuple[str, float, float]] = None,
                             info_y: Optional[tuple[str, float, float]] = None,
                             info_z: Optional[tuple[str, float, float]] = None) -> None:
        """
        todo 更新地面加速度
        Args:
            index: 地面加速度编号
            case_name: 时程工况名
            info_x: X方向时程分析函数信息数据(函数名,系数,到达时间)
            info_y: Y方向信息
            info_z: Z方向信息
        Example:
            mdb.update_ground_motion(index=1,case_name="Earthquake_X",
                info_x=("EQ_X_func", 1.0, 0.0),info_y=("EQ_Y_func", 0.8, 0.0),info_z=("EQ_Z_func", 0.6, 0.0) )
        Returns: 无
        """
        payload = {
            "index": index,
            "case_name": case_name,
            "info_x": info_x,
            "info_y": info_y,
            "info_z": info_z,
        }
        return QtServer.send_post("UPDATE-GROUND-MOTION", payload)

    @staticmethod
    def remove_time_history_load_case(name: str) -> None:
        """
        todo 通过时程工况名删除时程工况
        Args:
            name: 时程工况名
        Example:
            mdb.remove_time_history_load_case("工况名")
        Returns: 无
        """
        payload = {"name": name}
        return QtServer.send_post("REMOVE-TIME-HISTORY-LOAD-CASE", payload)

    @staticmethod
    def remove_time_history_function(ids=None, name: str = "") -> None:
        """
        todo 通过函数编号删除时程函数
        Args:
            ids: 删除时程函数编号集合支持XtoYbyN形式，默认为空时则按照名称删除
            name: 编号集合为空时则按照名称删除
        Example:
            mdb.remove_time_history_function(ids=[1,2,3])
            mdb.remove_time_history_function(ids="1to3")
            mdb.remove_time_history_function(name="函数名")
        Returns: 无
        """
        payload = {
            "ids": ids,
            "name": name,
        }
        return QtServer.send_post("REMOVE-TIME-HISTORY-FUNCTION", payload)

    @staticmethod
    def remove_load_to_mass(name: str = ""):
        """
        todo 删除荷载转为质量,默认删除所有荷载转质量
        Args:
            name:荷载工况名
        Example:
            mdb.remove_load_to_mass(name="荷载工况")
        Returns: 无
        """
        payload = {"name": name} if name else None
        return QtServer.send_post("REMOVE-LOAD-TO-MASS", payload)

    @staticmethod
    def remove_nodal_mass(node_id=None):
        """
        todo 删除节点质量
        Args:
             node_id:节点号,自动忽略不存在的节点质量
        Example:
            mdb.remove_nodal_mass(node_id=1)
            mdb.remove_nodal_mass(node_id=[1,2,3,4])
            mdb.remove_nodal_mass(node_id="1to5")
        Returns: 无
        """
        payload = None if node_id is None else {"node_id": node_id}
        return QtServer.send_post("REMOVE-NODAL-MASS", payload)

    @staticmethod
    def remove_boundary_element_property(name: str) -> None:
        """
        todo 删除边界单元特性
        Args: 无
        Example:
            mdb.remove_boundary_element_property(name="特性名")
        Returns: 无
        """
        payload = {"name": name}
        return QtServer.send_post("REMOVE-BOUNDARY-ELEMENT-PROPERTY", payload)

    @staticmethod
    def remove_boundary_element_link(ids=None) -> None:
        """
        todo 删除边界单元连接
        Args:
            ids:所删除的边界单元连接号且支持XtoYbyN形式字符串
        Example:
            mdb.remove_boundary_element_link(ids=1)
            mdb.remove_boundary_element_link(ids=[1,2,3,4])
        Returns: 无
        """
        payload = {"ids": ids}
        return QtServer.send_post("REMOVE-BOUNDARY-ELEMENT-LINK", payload)

    @staticmethod
    def remove_ground_motion(name: str) -> None:
        """
        todo 删除地面加速度
        Args:
            name: 工况名称
        Example:
            mdb.remove_ground_motion("时程工况名")
        Returns: 无
        """
        payload = {"name": name}
        return QtServer.send_post("REMOVE-GROUND-MOTION", payload)

    @staticmethod
    def remove_nodal_dynamic_load(ids=None) -> None:
        """
        todo 删除节点动力荷载
        Args:
            ids:所删除的节点动力荷载编号且支持XtoYbyN形式字符串
        Example:
            mdb.remove_nodal_dynamic_load(ids=1)
            mdb.remove_nodal_dynamic_load(ids=[1,2,3,4])
        Returns: 无
        """
        payload = {"ids": ids}
        return QtServer.send_post("REMOVE-NODAL-DYNAMIC-LOAD", payload)

    # endregion

    # region 反应谱分析
    @staticmethod
    @staticmethod
    def add_spectrum_function(name: str = "", factor: float = 1.0, kind: int = 0,
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
                s += ",".join(f"{time:g},{y:g}" for time, y in function_info) + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_spectrum_case(name: str = "", description: str = "", kind: int = 1, info_x: Optional[tuple[str, float]] = None,
                          info_y: Optional[tuple[str, float]] = None, info_z: Optional[tuple[str, float]] = None):
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

    def update_spectrum_function(name: str = "", new_name: str = "", factor: float = 1.0, kind: int = 0,
                                 function_info: list[tuple[float, float]] = None) -> None:
        """
        todo 更新反应谱函数
        Args:
            name: 函数名称
            new_name: 新函数名称
            factor: 反应谱调整系数
            kind: 0-无量纲 1-加速度 2-位移
            function_info: 函数信息[(时间1,数值1),(时间2,数值2)]
        Example:
            mdb.update_spectrum_function( name="函数名称", factor=1.2, kind=1, function_info=[(0.0, 0.0), (0.5, 0.8), (1.0, 1.2)])
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "factor": factor,
            "kind": kind,
            "function_info": function_info or [],
        }
        return QtServer.send_post("UPDATE-SPECTRUM-FUNCTION", payload)

    @staticmethod
    def update_spectrum_case(name: str, new_name: str = "", description: str = "", kind: int = 1,
                             info_x: Optional[tuple[str, float]] = None,
                             info_y: Optional[tuple[str, float]] = None,
                             info_z: Optional[tuple[str, float]] = None) -> None:
        """
        todo 更新反应谱工况
        Args:
            name: 工况名称
            new_name: 新工况名称
            description: 描述
            kind: 组合方式 1-求模 2-求和
            info_x: 反应谱X向信息 (X方向函数名,系数)
            info_y: Y向信息
            info_z: Z向信息
        Example:
            mdb.update_spectrum_case(name="RS1",kind=1,info_x=("函数X", 1.0),info_y=("函数Y", 0.85) )
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "description": description,
            "kind": kind,
            "info_x": info_x,
            "info_y": info_y,
            "info_z": info_z,
        }
        return QtServer.send_post("UPDATE-SPECTRUM-CASE", payload)

    @staticmethod
    def remove_spectrum_case(name: str) -> None:
        """
        todo 删除反应谱工况
        Args:
            name: 工况名称
        Example:
            mdb.remove_spectrum_case("工况名")
        Returns: 无
        """
        payload = {"name": name}
        return QtServer.send_post("REMOVE-SPECTRUM-CASE", payload)

    @staticmethod
    def remove_spectrum_function(ids=None, name: str = "") -> None:
        """
        todo 删除反应谱函数
        Args:
            ids: 删除反应谱工况函数编号集合支持XtoYbyN形式，默认为空时则按照名称删除
            name: 编号集合为空时则按照名称删除
        Example:
            mdb.remove_spectrum_function(name="工况名")
        Returns: 无
        """
        payload = {
            "ids": ids,
            "name": name,
        }
        return QtServer.send_post("REMOVE-SPECTRUM-FUNCTION", payload)

    # endregion
