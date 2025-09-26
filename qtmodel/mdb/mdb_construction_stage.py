import json
from typing import Optional

from ..core.qt_server import QtServer


class MdbConstructionStage:
    """
    用于施工阶段操作
    """

    # region 施工阶段操作
    @staticmethod
    def add_construction_stage(name: str = "", duration: int = 0,
                               active_structures: Optional[list[tuple[str, float, int, int]]] = None,
                               delete_structures: Optional[list[str]] = None,
                               active_boundaries: Optional[list[tuple[str, int]]] = None,
                               delete_boundaries: Optional[list[str]] = None,
                               active_loads: Optional[list[tuple[str, int]]] = None,
                               delete_loads: Optional[list[tuple[str, int]]] = None,
                               temp_loads: Optional[list[str]] = None, index=-1,
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
                s += f"AELEM={','.join(','.join(str(x) if not isinstance(x, (int, float)) else f'{x:g}' for x in row) for row in active_structures)}\r\n"
            if delete_structures is not None:
                s += f"DELEM={','.join(map(str, delete_structures))}\r\n"
            if active_boundaries is not None:
                s += f"ABNDR={','.join(','.join(map(str, row)) for row in active_boundaries)}\r\n"
            if delete_boundaries is not None:
                s += f"DBNDR={','.join(map(str, delete_boundaries))}\r\n"
            if active_loads is not None:
                s += f"ALOAD={','.join(','.join(map(str, row)) for row in active_loads)}\r\n"
            if delete_loads is not None:
                s += f"DLOAD={','.join(','.join(map(str, row)) for row in delete_loads)}\r\n"
            if temp_loads is not None:
                s += f"TEPLOAD={','.join(map(str, temp_loads))}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(f"添加施工阶段:{name}错误,{ex}")

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
                "version": QtServer.QT_VERSION,  # 版本控制
                "name": name,
                "structure_group_name": structure_group_name,
                "weight_stage_id": weight_stage_id,
            }
            json_string = json.dumps(params, indent=2)
            # 假设这里需要将命令发送到服务器或进行其他操作
            QtServer.get_command(header="UPDATE-WEIGHT-STAGE", command=json_string)
        except Exception as ex:
            raise Exception(f"更新施工阶段自重:{name}错误,{ex}")

    @staticmethod
    def update_construction_stage(name: str = "", new_name="", duration: int = 0,
                                  active_structures: Optional[list[tuple[str, float, int, int]]] = None,
                                  delete_structures: Optional[list[str]] = None,
                                  active_boundaries: Optional[list[tuple[str, int]]] = None,
                                  delete_boundaries: Optional[list[str]] = None,
                                  active_loads: Optional[list[tuple[str, int]]] = None,
                                  delete_loads: Optional[list[tuple[str, int]]] = None,
                                  temp_loads: Optional[list[str]] = None,
                                  tendon_cancel_loss: float = 0,
                                  constraint_cancel_type: int = 2):
        """
        添加施工阶段信息
        Args:
           name:施工阶段信息
           new_name:新施工阶段名
           duration:时长
           active_structures:激活结构组信息 [(结构组名,龄期,安装方法,计自重施工阶段id),...]
                               _计自重施工阶段id 0-不计自重,1-本阶段 n-第n阶段
                               _安装方法1-变形法 2-接线法 3-无应力法
           delete_structures:钝化结构组信息 [结构组1，结构组2,...]
           active_boundaries:激活边界组信息 [(边界组1，位置),...]
                               _位置 0-变形前 1-变形后
           delete_boundaries:钝化边界组信息 [边界组1，结构组2,...]
           active_loads:激活荷载组信息 [(荷载组1,时间),...]
                               _时间 0-开始 1-结束
           delete_loads:钝化荷载组信息 [(荷载组1,时间),...]
                               _时间 0-开始 1-结束
           temp_loads:临时荷载信息 [荷载组1，荷载组2,..]
           tendon_cancel_loss:钝化预应力单元后预应力损失
           constraint_cancel_type:钝化梁端约束释放计算方法1-变形法 2-无应力法
        Example:
           mdb.update_construction_stage(name="施工阶段1",duration=5,active_structures=[("结构组1",5,1,1),("结构组2",5,1,1)],
               active_boundaries=[("默认边界组",1)],active_loads=[("默认荷载组1",0)])
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "duration": duration,
            "active_structures": active_structures,
            "delete_structures": delete_structures,
            "active_boundaries": active_boundaries,
            "delete_boundaries": delete_boundaries,
            "active_loads": active_loads,
            "delete_loads": delete_loads,
            "temp_loads": temp_loads,
            "tendon_cancel_loss": tendon_cancel_loss,
            "constraint_cancel_type": constraint_cancel_type,
        }
        return QtServer.send_post("UPDATE-CONSTRUCTION-STAGE", payload)

    @staticmethod
    def update_construction_stage_id(stage_id, target_id: int = 3):
        """
        更新部分施工阶段到指定编号位置之前，例如将1号施工阶段插入到3号之前即为1号与2号施工阶段互换
        Args:
            stage_id:修改施工阶段编号且支持XtoYbyN形式字符串
            target_id:目标施工阶段编号
        Example:
            mdb.update_construction_stage_id(1,3)
            mdb.update_construction_stage_id([1,2,3],9)
        Returns:无
        """
        payload = {
            "stage_id": stage_id,
            "target_id": target_id,
        }
        return QtServer.send_post("UPDATE-CONSTRUCTION-STAGE-ID", payload)

    @staticmethod
    def update_all_stage_setting_type(setting_type: int = 1):
        """
        更新施工阶段安装方式
        Args:
            setting_type:安装方式 (1-接线法 2-无应力法 3-变形法 4-切线法)
        Example:
           mdb.update_all_stage_setting_type(setting_type=1)
        Returns: 无
        """
        payload = {
            "setting_type": setting_type,
        }
        return QtServer.send_post("UPDATE-ALL-STAGE-SETTING-TYPE", payload)

    @staticmethod
    def update_section_connection_stage(name: str, new_name="", sec_id: int = 1, element_id=None,
                                        stage_name="", age: float = 0, weight_type: int = 0):
        """
        更新施工阶段联合截面
        Args:
            name:名称
            new_name:新名称
            sec_id:截面号
            element_id:单元号，支持整型和整型列表且支持XtoYbyN形式字符串
            stage_name:结合阶段名
            age:材龄
            weight_type:辅材计自重方式 0-由主材承担  1-由整体承担 2-不计辅材自重
        Example:
            mdb.update_section_connection_stage(name="联合阶段",sec_id=1,element_id=[2,3,4,5],stage_name="施工阶段1")
            mdb.update_section_connection_stage(name="联合阶段",sec_id=1,element_id="2to5",stage_name="施工阶段1")
        Returns:无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "sec_id": sec_id,
            "element_id": element_id,
            "stage_name": stage_name,
            "age": age,
            "weight_type": weight_type,
        }
        return QtServer.send_post("UPDATE-SECTION-CONNECTION-STAGE", payload)

    @staticmethod
    def remove_construction_stage(name: str = ""):
        """
        按照施工阶段名删除施工阶段,默认删除所有施工阶段
        Args:
            name:所删除施工阶段名称
        Example:
            mdb.remove_construction_stage(name="施工阶段1")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        return QtServer.send_post("REMOVE-CONSTRUCTION-STAGE", payload)

    @staticmethod
    def merge_all_stages(name: str = "一次成桥", setting_type: int = 1, weight_type: int = 1, age: float = 5,
                         boundary_type: int = 0, load_type: int = 0, tendon_cancel_loss: float = 0,
                         constraint_cancel_type: int = 1) -> None:
        """
        合并当前所有施工阶段
        Args:
            name: 阶段名称
            setting_type: 安装方式 1-变形法安装 2-无应力安装，默认为1
            weight_type: 自重类型 -1-其他结构考虑 0-不计自重 1-本阶段，默认为1
            age: 加载龄期，默认为5
            boundary_type: 边界类型 0-变形前 1-变形后，默认为0
            load_type: 荷载类型 0-开始 1-结束，默认为0
            tendon_cancel_loss: 钝化预应力单元后预应力损失率，默认为0
            constraint_cancel_type: 钝化梁端约束释放计算方法 1-变形法 2-无应力法，默认为1
        Example:
            mdb.merge_all_stages(name="合并阶段", setting_type=1, weight_type=1, age=5)
        Returns: 无
        """
        payload = {
            "name": name,
            "setting_type": setting_type,
            "weight_type": weight_type,
            "age": age,
            "boundary_type": boundary_type,
            "load_type": load_type,
            "tendon_cancel_loss": tendon_cancel_loss,
            "constraint_cancel_type": constraint_cancel_type,
        }
        return QtServer.send_post("MERGE-ALL-STAGES", payload)

    # endregion

    # region
    @staticmethod
    def add_section_connection_stage(name: str, sec_id: int, element_id=None, stage_name="", age: float = 0,
                                     weight_type: int = 0):
        """
        添加施工阶段联合截面
        Args:
            name:名称
            sec_id:截面号
            element_id:单元号，支持整型和整型列表,支持XtoYbyN形式字符串
            stage_name:结合阶段名
            age:材龄
            weight_type:辅材计自重方式 0-由主材承担  1-由整体承担 2-不计辅材自重
        Example:
            mdb.add_section_connection_stage(name="联合阶段",sec_id=1,element_id=[2,3,4,5],stage_name="施工阶段1")
        Returns:无
        """
        payload = {
            "name": name,
            "sec_id": sec_id,
            "element_id": element_id,
            "stage_name": stage_name,
            "age": age,
            "weight_type": weight_type,
        }
        return QtServer.send_post("ADD-SECTION-CONNECTION-STAGE", payload)

    @staticmethod
    def add_element_to_connection_stage(element_id, name: str):
        """
        添加单元到施工阶段联合截面
        Args:
            element_id:单元号，支持整型和整型列表且支持XtoYbyN形式字符串
            name:联合阶段名
        Example:
            mdb.add_element_to_connection_stage([1,2,3,4],"联合阶段")
        Returns:无
        """
        payload = {
            "element_id": element_id,
            "name": name,
        }
        return QtServer.send_post("ADD-ELEMENT-TO-CONNECTION-STAGE", payload)

    @staticmethod
    def remove_section_connection_stage(name: str):
        """
        删除施工阶段联合截面
        Args:
            name:名称
        Example:
            mdb.remove_section_connection_stage(name="联合阶段")
        Returns:无
        """
        payload = {
            "name": name,
        }
        return QtServer.send_post("REMOVE-SECTION-CONNECTION-STAGE", payload)
    # endregion
