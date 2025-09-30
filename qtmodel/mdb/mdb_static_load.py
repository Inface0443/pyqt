import json
from ..core.qt_server import QtServer
from typing import Union, List
from qtmodel.core.data_helper import QtDataHelper


class MdbStaticLoad:
    """
    用于静力荷载添加
    """

    # region 静力荷载操作
    @staticmethod
    def add_nodal_force(node_id, case_name: str = "", load_info: list[float] = None,
                        group_name: str = "默认荷载组"):
        """
        添加节点荷载
        Args:
            node_id:节点编号且支持XtoYbyN形式字符串
            case_name:荷载工况名
            load_info:荷载信息列表 [Fx,Fy,Fz,Mx,My,Mz]
            group_name:荷载组名
        Example:
            mdb.add_nodal_force(node_id=1,case_name="荷载工况1",load_info=[1,1,1,1,1,1],group_name="默认结构组")
            mdb.add_nodal_force(node_id="1to100",case_name="荷载工况1",load_info=[1,1,1,1,1,1],group_name="默认结构组")
        Returns: 无
        """
        try:
            if load_info is None or len(load_info) != 6:
                raise Exception("操作错误，节点荷载列表信息不能为空，且其长度必须为6")
            if node_id is None:
                node_str = ""
            elif isinstance(node_id, list):  # 列表转化为XtoYbyN
                node_str = QtDataHelper.parse_int_list_to_str(node_id)
            else:
                node_str = str(node_id)
            s = "*NODALLOAD\r\n" + f"{node_str},{case_name},{group_name}," + ",".join(
                f"{x:g}" for x in load_info) + "\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_node_displacement(node_id, case_name: str = "",
                              load_info: tuple[float, float, float, float, float, float] = None,
                              group_name: str = "默认荷载组"):
        """
        添加节点位移
        Args:
            node_id:节点编号,支持整型或整数型列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            load_info:节点位移列表 [Dx,Dy,Dz,Rx,Ry,Rz]
            group_name:荷载组名
        Example:
            mdb.add_node_displacement(case_name="荷载工况1",node_id=1,load_info=(1,0,0,0,0,0),group_name="默认荷载组")
            mdb.add_node_displacement(case_name="荷载工况1",node_id=[1,2,3],load_info=(1,0,0,0,0,0),group_name="默认荷载组")
        Returns: 无
        """
        try:
            if load_info is None or len(load_info) != 6:
                raise Exception("操作错误，节点位移列表信息不能为空，且其长度必须为6")
            if node_id is None:
                node_str = ""
            elif isinstance(node_id, list):  # 列表转化为XtoYbyN
                node_str = QtDataHelper.parse_int_list_to_str(node_id)
            else:
                node_str = str(node_id)
            s = "*NODALDISP\r\n" + f"{node_str},{case_name},{group_name}," + ",".join(
                f"{x:g}" for x in load_info) + "\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_beam_element_load(element_id, case_name: str = "", load_type: int = 1, coord_system: int = 3,
                              is_abs=False, list_x: (Union[float, List[float]]) = None,
                              list_load: (Union[float, List[float]]) = None,
                              group_name="默认荷载组", load_bias: tuple[bool, int, int, float] = (False, 1, 1, 0.1),
                              projected: bool = False):
        """
        添加梁单元荷载
        Args:
            element_id:单元编号,支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            load_type:荷载类型 (1-集中力 2-集中弯矩 3-分布力 4-分布弯矩)
            coord_system:坐标系 (1-整体X  2-整体Y 3-整体Z  4-局部X  5-局部Y  6-局部Z)
            is_abs: 荷载位置输入方式，True-绝对值   False-相对值
            list_x:荷载位置信息 ,荷载距离单元I端的距离，可输入绝对距离或相对距离
            list_load:荷载数值信息
            group_name:荷载组名
            load_bias:偏心荷载 (是否偏心,0-中心 1-偏心,偏心坐标系-int,偏心距离)
            projected:荷载是否投影
        Example:
            mdb.add_beam_element_load(element_id=1,case_name="荷载工况1",load_type=1,list_x=0.5,list_load=100)
            mdb.add_beam_element_load(element_id="1to100",case_name="荷载工况1",load_type=3,list_x=[0.4,0.8],list_load=[100,200])
        Returns: 无
        """
        try:
            if element_id is None:
                elem_ids = []
            elif isinstance(element_id, int):
                elem_ids = [element_id]
            elif isinstance(element_id, list):
                elem_ids = element_id
            elif isinstance(element_id, str):
                parsed = QtDataHelper.parse_number_string(element_id)
                elem_ids = parsed if parsed is not None else []
            else:
                raise ValueError(f"Unsupported element_id type: {type(element_id)}")
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "element_id": elem_ids,
                "case_name": case_name,
                "load_type": load_type,
                "coord_system": coord_system,
                "is_abs": is_abs,
                "list_x": list_x if isinstance(list_x, list) else ([list_x] if list_x is not None else []),
                "list_load": list_load if isinstance(list_load, list) else ([list_load] if list_load is not None else []),
                "group_name": group_name,
                "load_bias": list(load_bias),
                "projected": projected,
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.send_command(header="ADD-BEAM-ELEMENT-LOAD", command=json_string)
            # s = "*BEAMLOAD\r\n" + f"{elem_str},{case_name},{group_name},{load_type},{coord_system},"
            # if load_type in (1, 2):
            #     s += f"{list_x:g},{list_load:g}"
            # elif load_type in (3, 4):
            #     s += ",".join(f"{x:g}" for x in list_x) + "," + ",".join(f"{load:g}" for load in list_load)
            # bias_str = "YES" if load_bias[0] else "NO"
            # s += f",{bias_str},{load_bias[1]},{load_bias[2]},{load_bias[3]:g}\r\n"
            # # print(s)
            # QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_pre_stress(case_name: str = "", tendon_name: (Union[str, List[str]]) = "", tension_type: int = 2,
                       force: float = 1395000, group_name: str = "默认荷载组"):
        """
        添加预应力
        Args:
             case_name:荷载工况名
             tendon_name:钢束名,支持钢束名或钢束名列表
             tension_type:预应力类型 (0-始端 1-末端 2-两端)
             force:预应力
             group_name:荷载组
        Example:
            mdb.add_pre_stress(case_name="荷载工况名",tendon_name="钢束1",force=1390000)
        Returns: 无
        """
        try:
            tend_list = []
            if isinstance(tendon_name, str):
                tend_list.append(tendon_name)
            else:
                tend_list = tendon_name
            s = "*PRESTRESS\r\n" + "\r\n".join(
                f"{tend},{case_name},{group_name},{tension_type},{force}" for tend in tend_list) + "\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_initial_tension_load(element_id, case_name: str = "", group_name: str = "默认荷载组", tension: float = 0,
                                 tension_type: int = 1, application_type: int = 1, stiffness: float = 0):
        """
        添加初始拉力
        Args:
             element_id:单元编号支持数或列表且支持XtoYbyN形式字符串
             case_name:荷载工况名
             tension:初始拉力
             tension_type:张拉类型  0-增量 1-全量
             group_name:荷载组名
             application_type:计算方式 1-体外力 2-体内力 3-转为索长张拉
             stiffness:索刚度参与系数
        Example:
            mdb.add_initial_tension_load(element_id=1,case_name="工况1",tension=100,tension_type=1)
        Returns: 无
        """
        try:
            if element_id is None:
                elem_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                elem_str = QtDataHelper.parse_int_list_to_str(element_id)
            else:
                elem_str = str(element_id)
            s = "*INITTENSION\r\n" + f"{elem_str},{case_name},{group_name},{tension:g},{tension_type},{application_type},{stiffness:g}\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_cable_length_load(element_id, case_name: str = "", group_name: str = "默认荷载组", length: float = 0,
                              tension_type: int = 1):
        """
        添加索长张拉
        Args:
            element_id:单元编号支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            length:长度
            tension_type:张拉类型  0-增量 1-全量
            group_name:荷载组名
        Example:
            mdb.add_cable_length_load(element_id=1,case_name="工况1",length=1,tension_type=1)
        Returns: 无
        """
        try:
            if element_id is None:
                elem_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                elem_str = QtDataHelper.parse_int_list_to_str(element_id)
            else:
                elem_str = str(element_id)
            s = "*CABLELENLOAD\r\n" + f"{elem_str},{case_name},{group_name},{length},{tension_type}\r\n"
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_plate_element_load(element_id, case_name: str = "",
                               load_type: int = 1, load_place: int = 1, coord_system: int = 3,
                               group_name: str = "默认荷载组", list_load: (Union[float, List[float]]) = None,
                               list_xy: tuple[float, float] = None):
        """
        添加版单元荷载
        Args:
             element_id:单元编号支持数或列表
             case_name:荷载工况名
             load_type:荷载类型 (1-集中力  2-集中弯矩  3-分布力  4-分布弯矩)
             load_place:荷载位置 (0-面IJKL 1-边IJ  2-边JK  3-边KL  4-边LI ) (仅分布荷载需要)
             coord_system:坐标系  (1-整体X  2-整体Y 3-整体Z  4-局部X  5-局部Y  6-局部Z)
             group_name:荷载组名
             list_load:荷载列表
             list_xy:荷载位置信息 [IJ方向绝对距离x,IL方向绝对距离y]  (仅集中荷载需要)
        Example:
            mdb.add_plate_element_load(element_id=1,case_name="工况1",load_type=1,group_name="默认荷载组",list_load=[1000],list_xy=(0.2,0.5))
        Returns: 无
        """
        try:
            if element_id is None:
                elem_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                elem_str = QtDataHelper.parse_int_list_to_str(element_id)
            else:
                elem_str = str(element_id)
            if isinstance(list_load, float):
                list_load = [list_load]
            s = "*PLATELOAD\r\n" + f"{elem_str},{case_name},{group_name},"
            if load_type == 2 or load_type == 4 or load_type == 6:
                raise Exception("操作错误，板单元暂不支持弯矩荷载")
            elif load_type == 1:
                s += f"{load_type},{coord_system},{list_xy[0]:g},{list_xy[1]:g},{list_load[0]:g}\r\n"
            elif (load_type == 3) and (load_place != 0):
                s += f"{load_type},{coord_system},{load_place},{list_load[0]:g},{list_load[1]:g}\r\n"
            elif (load_type == 3 and load_place == 0) or (load_type == 5):
                load_type = 5
                s += f"{load_type},{coord_system},{list_load[0]:g},{list_load[1]:g},{list_load[2]:g},{list_load[3]:g}\r\n"
            else:
                raise Exception("操作错误，板单元暂不支持该类型荷载")
            # print(s)
            QtServer.send_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_distribute_plane_load_type(name: str, load_type: int, point_list: list[list[float]], load: float = 0, copy_x: str = None,
                                       copy_y: str = None,
                                       describe: str = ""):
        """
        添加分配面荷载类型
        Args:
            name:荷载类型名称
            load_type:荷载类型  1-集中荷载 2-线荷载 3-面荷载
            point_list:点列表，集中力时为列表内元素为 [x,y,force] 线荷载与面荷载时为 [x,y]
            load:荷载值,仅线荷载与面荷载需要
            copy_x:复制到x轴距离，与UI一致，支持3@2形式字符串，逗号分隔
            copy_y:复制到y轴距离，与UI一致，支持3@2形式字符串，逗号分隔
            describe:描述
        Example:
            mdb.add_distribute_plane_load_type(name="荷载类型1",load_type=1,point_list=[[1,0,10],[1,1,10],[1,2,10]])
            mdb.add_distribute_plane_load_type(name="荷载类型2",load_type=2,point_list=[[1,0],[1,1]],load=10)
        Returns: 无
        """
        payload = {
            "name": name,
            "load_type": load_type,
            "point_list": point_list,
            "load": load,
            "copy_x": copy_x,
            "copy_y": copy_y,
            "describe": describe,
        }
        return QtServer.send_dict("ADD-DISTRIBUTE-PLANE-LOAD-TYPE", payload)

    @staticmethod
    def add_distribute_plane_load(index: int = -1, case_name: str = "", type_name: str = "",
                                  point1: tuple[float, float, float] = None, point2: tuple[float, float, float] = None,
                                  point3: tuple[float, float, float] = None,
                                  plate_ids: list[int] = None, coord_system: int = 3, group_name: str = "默认荷载组"):
        """
        添加分配面荷载类型
        Args:
            index:荷载编号,默认自动识别
            case_name:工况名
            type_name:荷载类型名称
            point1:第一点(原点)
            point2:第一点(在x轴上)
            point3:第一点(在y轴上)
            plate_ids:指定板单元。默认时为全部板单元
            coord_system:描述
            group_name:描述
        Example:
            mdb.add_distribute_plane_load(index=1,case_name="工况1",type_name="荷载类型1",point1=(0,0,0),
                point2=(1,0,0),point3=(0,1,0),group_name="默认荷载组")
        Returns: 无
        """
        payload = {
            "id": index,
            "case_name": case_name,
            "type_name": type_name,
            "point1": point1,
            "point2": point2,
            "point3": point3,
            "coord_system": coord_system,
            "plate_ids": plate_ids,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-DISTRIBUTE-PLANE-LOAD", payload)

    @staticmethod
    def update_distribute_plane_load_type(name: str = "", new_name: str = "", load_type: int = 1, point_list: list[list[float]] = None,
                                          load: float = 0, copy_x: str = None, copy_y: str = None, describe: str = ""):
        """
        todo  更新板单元类型
        Args:
            name:荷载类型名称
            new_name:新名称，默认不修改名称
            load_type:荷载类型  1-集中荷载 2-线荷载 3-面荷载
            point_list:点列表，集中力时为列表内元素为 [x,y,force] 线荷载与面荷载时为 [x,y]
            load:荷载值,仅线荷载与面荷载需要
            copy_x:复制到x轴距离，与UI一致，支持3@2形式字符串，逗号分隔
            copy_y:复制到y轴距离，与UI一致，支持3@2形式字符串，逗号分隔
            describe:描述
        Example:
            mdb.update_distribute_plane_load_type(name="荷载类型1",load_type=1,point_list=[[1,0,10],[1,1,10],[1,2,10]])
            mdb.update_distribute_plane_load_type(name="荷载类型2",load_type=2,point_list=[[1,0],[1,1]],load=10)
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "load_type": load_type,
            "point_list": point_list,
            "load": load,
            "copy_x": copy_x,
            "copy_y": copy_y,
            "describe": describe,
        }
        return QtServer.send_dict("UPDATE-DISTRIBUTE-PLANE-LOAD-TYPE", payload)

    @staticmethod
    def remove_nodal_force(node_id, case_name: str = "", group_name="默认荷载组"):
        """
        todo 删除节点荷载
        Args:
             node_id:节点编号且支持XtoYbyN形式字符串
             case_name:荷载工况名
             group_name:指定荷载组
        Example:
            mdb.remove_nodal_force(case_name="荷载工况1",node_id=1,group_name="默认荷载组")
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "node_id": node_id,
            "group_name": group_name,
        }
        return QtServer.send_dict("REMOVE-NODAL-FORCE", payload)

    @staticmethod
    def remove_nodal_displacement(node_id, case_name: str = "", group_name="默认荷载组"):
        """
        todo 删除节点位移荷载
        Args:
            node_id:节点编号,支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            group_name:指定荷载组
        Example:
            mdb.remove_nodal_displacement(case_name="荷载工况1",node_id=1,group_name="默认荷载组")
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "node_id": node_id,
            "group_name": group_name,
        }
        return QtServer.send_dict("REMOVE-NODAL-DISPLACEMENT", payload)

    @staticmethod
    def remove_initial_tension_load(element_id, case_name: str, group_name: str = "默认荷载组"):
        """
        todo 删除初始拉力
        Args:
            element_id:单元编号支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            group_name:荷载组名
        Example:
            mdb.remove_initial_tension_load(element_id=1,case_name="工况1",group_name="默认荷载组")
        Returns: 无
        """
        payload = {
            "element_id": element_id,
            "case_name": case_name,
            "group_name": group_name,
        }
        return QtServer.send_dict("REMOVE-INITIAL-TENSION-LOAD", payload)

    @staticmethod
    def remove_beam_element_load(element_id, case_name: str = "", load_type: int = 1, group_name="默认荷载组"):
        """
        todo 删除梁单元荷载
        Args:
            element_id:单元号支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            load_type:荷载类型 (1-集中力   2-集中弯矩  3-分布力   4-分布弯矩)
            group_name:荷载组名称
        Example:
            mdb.remove_beam_element_load(case_name="工况1",element_id=1,load_type=1,group_name="默认荷载组")
        Returns: 无
        """
        payload = {
            "element_id": element_id,
            "case_name": case_name,
            "load_type": load_type,
            "group_name": group_name,
        }
        return QtServer.send_dict("REMOVE-BEAM-ELEMENT-LOAD", payload)

    @staticmethod
    def remove_plate_element_load(element_id, case_name: str, load_type: int, group_name="默认荷载组"):
        """
        todo 删除指定荷载工况下指定单元的板单元荷载
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            load_type: 板单元类型 1集中力   2-集中弯矩  3-分布线力  4-分布线弯矩  5-分布面力  6-分布面弯矩
            group_name:荷载组名
        Example:
            mdb.remove_plate_element_load(case_name="工况1",element_id=1,load_type=1,group_name="默认荷载组")
        Returns: 无
        """
        payload = {
            "element_id": element_id,
            "case_name": case_name,
            "load_type": load_type,
            "group_name": group_name,
        }
        return QtServer.send_dict("REMOVE-PLATE-ELEMENT-LOAD", payload)

    @staticmethod
    def remove_cable_length_load(element_id, case_name: str, group_name: str = "默认荷载组"):
        """
        todo 删除索长张拉
        Args:
            element_id:单元号支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            group_name:荷载组名
        Example:
            mdb.remove_cable_length_load(case_name="工况1",element_id=1, group_name= "默认荷载组")
        Returns: 无
        """
        payload = {
            "element_id": element_id,
            "case_name": case_name,
            "group_name": group_name,
        }
        return QtServer.send_dict("REMOVE-CABLE-LENGTH-LOAD", payload)

    @staticmethod
    def remove_plane_load(index: int = -1):
        """
        todo 根据荷载编号删除分配面荷载
        Args:
            index: 指定荷载编号，默认则删除所有分配面荷载
        Example:
            mdb.remove_plane_load()
            mdb.remove_plane_load(index=1)
        Returns: 无
        """
        payload = {
            "id": index,
        }
        return QtServer.send_dict("REMOVE-PLANE-LOAD", payload)

    @staticmethod
    def remove_distribute_plane_load_type(name: str = -1):
        """
        todo 删除分配面荷载类型
        Args:
            name: 指定荷载类型，默认则删除所有分配面荷载
        Example:
            mdb.remove_distribute_plane_load_type("类型1")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        return QtServer.send_dict("REMOVE-DISTRIBUTE-PLANE-LOAD-TYPE", payload)
    # endregion
