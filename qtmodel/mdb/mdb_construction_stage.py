import json

from ..core.qt_server import QtServer
from typing import Union, List
from .data_helper import MdbDataHelper


class MdbConstructionStage:
    # region 施工阶段操作
    @staticmethod
    def add_construction_stage(name: str = "", duration: int = 0,
                               active_structures: list[tuple[str, float, int, int]] = None,
                               delete_structures: list[str] = None,
                               active_boundaries: list[tuple[str, int]] = None,
                               delete_boundaries: list[str] = None,
                               active_loads: list[tuple[str, int]] = None,
                               delete_loads: list[tuple[str, int]] = None,
                               temp_loads: list[str] = None, index=-1,
                               tendon_cancel_loss: float = 0,
                               constraint_cancel_type: int = 2):
        """
        添加施工阶段信息
        Args:
           name:施工阶段信息
           duration:时长
           active_structures:激活结构组信息 [(结构组名,龄期,安装方法,计自重施工阶段id),...]
                               _计自重施工阶段id 0-不计自重,1-本阶段 n-第n阶段(可能用到尚未添加的施工阶段请先添加)
                               _安装方法 1-变形法 2-无应力法 3-接线法 4-切线法
           delete_structures:钝化结构组信息 [结构组1，结构组2,...]
           active_boundaries:激活边界组信息 [(边界组1，位置),...]
                               _位置 0-变形前 1-变形后
           delete_boundaries:钝化边界组信息 [边界组1，边界组2,...]
           active_loads:激活荷载组信息 [(荷载组1,时间),...]
                               _时间 0-开始 1-结束
           delete_loads:钝化荷载组信息 [(荷载组1,时间),...]
                               _时间 0-开始 1-结束
           temp_loads:临时荷载信息 [荷载组1，荷载组2,..]
           index:施工阶段插入位置,从0开始,默认添加到最后
           tendon_cancel_loss:钝化预应力单元后预应力损失
           constraint_cancel_type:钝化梁端约束释放计算方法1-变形法 2-无应力法
        Example:
           mdb.add_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
                active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
        Returns: 无
        """
        try:
            s = "*STAGE\r\n"
            s += f"ID={index},{name},{duration},{tendon_cancel_loss:g},{constraint_cancel_type}\r\n"
            if active_structures is not None:
                s += f"AELEM={','.join(f'{','.join(f'{x:g}' if isinstance(x, (int, float)) else str(x) for x in row)}' for row in active_structures)}" + "\r\n"
            if delete_structures is not None:
                s += f"DELEM={','.join(f'{x}' for x in delete_structures)}\r\n"
            if active_boundaries is not None:
                s += f"ABNDR={','.join(f'{','.join(f'{x}' for x in row)}' for row in active_boundaries)}" + "\r\n"
            if delete_boundaries is not None:
                s += f"DBNDR={','.join(f'{x}' for x in delete_boundaries)}\r\n"
            if active_loads is not None:
                s += f"ALOAD={','.join(f'{','.join(f'{x}' for x in row)}' for row in active_loads)}" + "\r\n"
            if delete_loads is not None:
                s += f"DLOAD={','.join(f'{','.join(f'{x}' for x in row)}' for row in delete_loads)}" + "\r\n"
            if temp_loads is not None:
                s += f"TEPLOAD={str.join(',', temp_loads)}" + "\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(f"添加施工阶段:{name}错误,{ex}")

    # endregion

    # region 荷载组合操作
    @staticmethod
    def add_load_combine(index: int = -1, name: str = "", combine_type: int = 1, describe: str = "",
                         combine_info: list[tuple[str, str, float]] = None):
        """
        添加荷载组合
        Args:
            index:荷载组合编号
            name:荷载组合名
            combine_type:荷载组合类型 1-叠加  2-判别  3-包络 4-SRss 5-AbsSum
            describe:描述
            combine_info:荷载组合信息 [(荷载工况类型,工况名,系数)...] 工况类型如下
                _"ST"-静力荷载工况  "CS"-施工阶段荷载工况  "CB"-荷载组合
                _"MV"-移动荷载工况  "SM"-沉降荷载工况_ "RS"-反应谱工况 "TH"-时程分析
        Example:
            mdb.add_load_combine(name="荷载组合1",combine_type=1,describe="无",combine_info=[("CS","合计值",1),("CS","恒载",1)])
        Returns: 无
        """
        try:
            # if combine_info is None:
            #     combine_info = []
            # s = "*LOADCOMB\r\n" + f"NAME={name},{combine_type},{describe}\r\n"
            # s += "\r\n".join(f'{','.join(f'{x:g}' if isinstance(x, float) else str(x) for x in row)}' for row in
            #                  combine_info) + "\r\n"
            # print(s)
            # QtServer.post_command(s, "QDAT")
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
                "index": index,
                "name": name,
                "combine_type": combine_type,
                "describe": describe,
                "combine_info": combine_info or [],
            }
            json_string = json.dumps(params, indent=2, ensure_ascii=False)
            QtServer.get_command(header="ADD-LOAD-COMBINE", command=json_string)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def update_weight_stage(name: str = "", structure_group_name: str = "", weight_stage_id: int = 1):
        """
        更新施工阶段自重
        Args:
           name:施工阶段信息
           structure_group_name:结构组名
           weight_stage_id: 计自重阶段号 (0-不计自重,1-本阶段 n-第n阶段)
        Example:
           mdb.update_weight_stage(name="施工阶段1",structure_group_name="默认结构组",weight_stage_id=1)
        Returns: 无
        """
        try:
            # 创建参数字典
            params = {
                "version":QtServer.QT_VERSION, # 版本控制
                "name": name,
                "structure_group_name": structure_group_name,
                "weight_stage_id": weight_stage_id,
            }
            json_string = json.dumps(params, indent=2)
            # 假设这里需要将命令发送到服务器或进行其他操作
            QtServer.get_command(header="UPDATE-WEIGHT-STAGE", command=json_string)
        except Exception as ex:
            raise Exception(ex)
    # endregion

    # region 荷载工况操作
    @staticmethod
    def add_sink_group(name: str = "", sink: float = 0.1, node_ids: (Union[int, List[int], str]) = None):
        """
        添加沉降组
        Args:
             name: 沉降组名
             sink: 沉降值
             node_ids: 节点编号，支持数或列表
        Example:
            mdb.add_sink_group(name="沉降1",sink=0.1,node_ids=[1,2,3])
        Returns: 无
        """
        try:
            if isinstance(node_ids, int):
                node_ids = [node_ids]
            if node_ids is None:
                id_str = ""
            elif isinstance(node_ids, list):
                id_str = MdbDataHelper.parse_int_list_to_str(node_ids)
            else:
                id_str = str(node_ids)
            s = "*SINK-GROUP\r\n" + f"{name},{sink:g},{id_str}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_sink_case(name: str, sink_groups: (Union[str, List[str]]) = None):
        """
        添加沉降工况
        Args:
            name:荷载工况名
            sink_groups:沉降组名，支持字符串或列表
        Example:
            mdb.add_sink_case(name="沉降工况1",sink_groups=["沉降1","沉降2"])
        Returns: 无
        """
        try:
            if isinstance(sink_groups, str):
                sink_groups = [sink_groups]
            s = "*SINK-CASE\r\n" + f"{name},{','.join(sink_groups)}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_concurrent_reaction(names: (Union[str, List[str]])):
        """
        添加并发反力组
        Args:
             names: 结构组名称集合
        Example:
            mdb.add_concurrent_reaction(names=["默认结构组"])
        Returns: 无
        """
        try:
            if names is None:
                raise Exception("操作错误，添加并发反力组时结构组名称不能为空")
            if isinstance(names, str):
                names = [names]
            s = "*CCT-REACT\r\n" + ",".join(names) + "\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_concurrent_force(names: (Union[str, List[str]])):
        """
        创建并发内力组
        Args:
            names: 结构组名称集合
        Example:
            mdb.add_concurrent_force(names=["默认结构组"])
        Returns: 无
        """
        try:
            if isinstance(names, str):
                names = [names]
            s = "*CCT-FORCE\r\n" + ",".join(names) + "\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_load_case(name: str = "", case_type: str = "施工阶段荷载"):
        """
        添加荷载工况
        Args:
            name:工况名
            case_type:荷载工况类型
            _"施工阶段荷载", "恒载", "活载", "制动力", "风荷载","体系温度荷载","梯度温度荷载",
            _"长轨伸缩挠曲力荷载", "脱轨荷载", "船舶撞击荷载","汽车撞击荷载","长轨断轨力荷载", "用户定义荷载"
        Example:
            mdb.add_load_case(name="工况1",case_type="施工阶段荷载")
        Returns: 无
        """
        try:
            s = "*LOADCASE\r\n" + f"{name},{case_type}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_load_group(name: str = ""):
        """
        根据荷载组名称添加荷载组
        Args:
             name: 荷载组名称
        Example:
            mdb.add_load_group(name="荷载组1")
        Returns: 无
        """
        try:
            if name != "":
                s = "*LOADGROUP\r\n" + f"{name}\r\n"
                print(s)
            else:
                s = ""
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    # endregion


