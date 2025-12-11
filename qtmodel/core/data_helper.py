import math
import re
from typing import List, Optional, Union


class QtDataHelper:
    """
    用于内部数据处理，不暴露给用户接口
    """

    @staticmethod
    def str_concrete_box_beam(symmetry: bool = True, sec_info: list[float] = None, box_num: int = 3, box_height: float = 2,
                              charm_info: list[str] = None, sec_right: list[float] = None, charm_right: list[str] = None,
                              box_other_info: dict[str, list[float]] = None, box_other_right: dict[str, list[float]] = None):
        """混凝土箱梁信息编码
        """
        bridge_width = (2 * sec_info[10]) if symmetry else (sec_info[10] + sec_right[10])
        s = f"{bridge_width:g},{box_num},{box_height},{'YES' if symmetry else 'NO'}\r\n"

        s += ",".join(f"{x:g}" for x in sec_info) + "\r\n"
        s += ",".join("(" + ",".join(x for term in item.split(",") for x in term.split("*")) + ")" for item in
                      (charm_info[0], charm_info[2], charm_info[1], charm_info[3])) + "\r\n"

        if box_other_info and any(k in box_other_info for k in ("i1", "B0", "B4", "T4")):
            s += "\r\n".join(
                f"L{k}=" + ",".join(f"{v:g}" for v in box_other_info[k]) for k in ("i1", "B0", "B4", "T4") if k in box_other_info) + "\r\n"

        if not symmetry:
            s += ",".join(f"{x:g}" for x in sec_right) + "\r\n"
            s += ",".join("(" + ",".join(x for term in item.split(",") for x in term.split("*")) + ")" for item in
                          (charm_right[0], charm_right[2], charm_right[1], charm_right[3])) + "\r\n"

            if box_other_right and any(k in box_other_right for k in ("i1", "B0", "B4", "T4")):
                s += "\r\n".join(
                    f"R{k}=" + ",".join(f"{v:g}" for v in box_other_info[k]) for k in ("i1", "B0", "B4", "T4") if k in box_other_info) + "\r\n"
        return s

    @staticmethod
    def str_steel_beam(sec_info: list[float] = None, rib_info: dict[str, list[float]] = None,
                       rib_place: list[tuple[int, int, float, str, int, str]] = None):
        """钢梁信息编码
        """
        s = ",".join(f"{x:g}" for x in sec_info) + "\r\n"
        if rib_info is not None:
            s += "\r\n".join(f"RIB={name}," + ",".join(f"{x:g}" for x in params) for name, params in rib_info.items()) + "\r\n"
        if rib_place is not None:
            s += "\r\n".join(f"PLACE={','.join(f'{x:g}' if isinstance(x, float) else str(x) for x in row)}" for row in rib_place) + "\r\n"
        return s

    @staticmethod
    def str_custom_compound_beam(mat_combine: list[float] = None, loop_segments: list[dict] = None, secondary_loop_segments: list[dict] = None):
        """自定义组合梁信息编码
        """
        s = ",".join(f"{x:g}" for x in mat_combine) + "\r\n"
        s += "M=\r\n"
        if loop_segments:
            for seg in loop_segments:
                for key, pts in seg.items():
                    s += f'{"MAIN" if key.lower() == "main" else "SUB"}={",".join(f"({x:g},{y:g})" for x, y in pts)}\r\n'
        s += "S=\r\n"
        if secondary_loop_segments:
            for seg in secondary_loop_segments:
                for key, pts in seg.items():
                    s += f'{"MAIN" if key.lower() == "main" else "SUB"}={",".join(f"({x:g},{y:g})" for x, y in pts)}\r\n'
        return s

    @staticmethod
    def str_compound_section(sec_info: list[float] = None, mat_combine: list[float] = None):
        """组合截面信息编码
        """
        s = ",".join(f"{x:g}" for x in sec_info) + "\r\n"
        s += ",".join(f"{x:g}" for x in mat_combine) + "\r\n"
        return s

    @staticmethod
    def str_custom_section(loop_segments: list[dict] = None, sec_lines: list[tuple[float, float, float, float, float]] = None):
        """自定义截面信息编码
        """
        s = ""
        if loop_segments:
            for seg in loop_segments:
                for key, pts in seg.items():
                    s += f'{"MAIN" if key.lower() == "main" else "SUB"}={",".join(f"({x:g},{y:g})" for x, y in pts)}\r\n'
        if sec_lines:
            s += "\r\n".join(f"LINE={','.join(f'{x:g}' for x in row)}" for row in sec_lines) + "\r\n"
        return s

    @staticmethod
    def get_str_by_data(sec_type: str, sec_data: dict):
        s = QtDataHelper.str_section(
            sec_type=sec_type,
            sec_info=sec_data.get("sec_info", []),
            symmetry=sec_data.get("symmetry", True),
            chamfer_info=sec_data.get("charm_info", None),
            sec_right=sec_data.get("sec_right", None),
            chamfer_right=sec_data.get("charm_right", None),
            box_num=sec_data.get("box_num", 3),
            box_height=sec_data.get("box_height", 2),
            box_other_info=sec_data.get("box_other_info", None),
            box_other_right=sec_data.get("box_other_right", None),
            mat_combine=sec_data.get("mat_combine", None),
            rib_info=sec_data.get("rib_info", None),
            rib_place=sec_data.get("rib_place", None),
            loop_segments=sec_data.get("loop_segments", None),
            sec_lines=sec_data.get("sec_lines", None),
            secondary_loop_segments=sec_data.get("secondary_loop_segments", None)
        )
        return s

    @staticmethod
    def str_section(
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
            rib_place: list[tuple[int, int, float, str, int, str]] = None,
            loop_segments: list[dict] = None,
            sec_lines: list[tuple[float, float, float, float, float]] = None,
            secondary_loop_segments: list[dict] = None):
        """仅返回字符串片段,需要拼接"""
        if sec_type == "混凝土箱梁":
            s = QtDataHelper.str_concrete_box_beam(symmetry, sec_info, box_num, box_height, chamfer_info, sec_right, chamfer_right, box_other_info,
                                                   box_other_right)
        elif sec_type == "箱梁边腹板" or sec_type == "箱梁中腹板" :
            s =",".join(f"{x:g}" for x in sec_info) + "\r\n" + ",".join(f"({s})" for s in chamfer_info)
        elif sec_type == "工字钢梁" or sec_type == "箱型钢梁" or sec_type == "单箱多室钢梁":
            s = QtDataHelper.str_steel_beam(sec_info, rib_info, rib_place)
        elif sec_type == "特性截面":
            s = ",".join(f"{x:g}" for x in sec_info) + "\r\n"
        elif sec_type.startswith("自定义组合"):
            s = QtDataHelper.str_custom_compound_beam(mat_combine, loop_segments, secondary_loop_segments)
        elif sec_type.endswith("组合梁") or sec_type in ("钢管砼", "钢箱砼", "哑铃型钢管混凝土", "哑铃型钢管混凝土竖向"):
            s = QtDataHelper.str_compound_section(sec_info, mat_combine)
        elif sec_type.startswith("自定义"):
            s = QtDataHelper.str_custom_section(loop_segments, sec_lines)
        else:  # 一般参数截面
            s = ",".join(f"{x:g}" for x in sec_info) + "\r\n"
        return s

    @staticmethod
    def parse_int_list_to_str(ids: Union[int, List[int], str]) -> str:
        """将列表转XtoYbyZ字符串"""
        if ids is None or isinstance(ids, str):
            return "" if ids is None else str(ids)
        if isinstance(ids, int):
            return str(ids)
        sorted_ids = sorted(set(ids))  # 排序并去重
        if len(sorted_ids) == 1:
            return str(sorted_ids[0])
        if len(sorted_ids) == 2:
            return f"{sorted_ids[0]} {sorted_ids[1]}"

        def create_id_expression(id_from: int, id_to: int, increment: int) -> str:
            """生成等差数列表达式"""
            if increment == 1:
                return f"{id_from}to{id_to}"
            else:
                return f"{id_from}to{id_to}by{increment}"

        result = []
        id_count = len(sorted_ids)
        start_index = 0
        current_index = 2
        id_increment = sorted_ids[start_index + 1] - sorted_ids[start_index]

        while True:
            current_increment = sorted_ids[current_index] - sorted_ids[current_index - 1]
            if current_increment == id_increment:
                if current_index >= id_count - 1:
                    result.append(create_id_expression(sorted_ids[start_index], sorted_ids[current_index], id_increment))
                    break
                current_index += 1
                continue

            # 增量不一致
            prev_count = (sorted_ids[current_index - 1] - sorted_ids[start_index]) // id_increment + 1
            if prev_count <= 2:
                # 前面只有 2 个
                result.append(str(sorted_ids[start_index]))
                if current_index >= id_count - 1:
                    result.append(f"{sorted_ids[current_index - 1]} {sorted_ids[current_index]}")
                    break
                start_index = current_index - 1
                id_increment = sorted_ids[start_index + 1] - sorted_ids[start_index]
                current_index = start_index + 2
            else:
                # 前面有 3 个及以上
                result.append(create_id_expression(sorted_ids[start_index], sorted_ids[current_index - 1], id_increment))
                if current_index >= id_count - 1:
                    result.append(str(sorted_ids[current_index]))
                    break
                if current_index == id_count - 2:
                    result.append(f"{sorted_ids[current_index]} {sorted_ids[current_index + 1]}")
                    break
                start_index = current_index
                id_increment = sorted_ids[start_index + 1] - sorted_ids[start_index]
                current_index = start_index + 2

        return " ".join(result)

    @staticmethod
    def convert_three_points_to_vectors(points):
        """
        将三点转换为正交的向量格式
        P1, P2, P3 -> V1, V2
        """
        if (len(points) != 3) or (len(points[0]) != 3):
            raise ValueError("操作错误，需要三个三维坐标点")
        p1, p2, p3 = points
        # 计算向量 V1 = P2 - P1 (归一化)
        v1 = [p2[i] - p1[i] for i in range(3)]
        v1_length = math.sqrt(sum(x * x for x in v1))
        v1 = [x / v1_length for x in v1] if v1_length > 0 else v1
        # 计算向量 V2 = (P3 - P1) 在垂直于V1的平面上的投影 (归一化)
        v3 = [p3[i] - p1[i] for i in range(3)]
        dot_product = sum(v1[i] * v3[i] for i in range(3))
        projection = [v1[i] * dot_product for i in range(3)]
        v2 = [v3[i] - projection[i] for i in range(3)]
        v2_length = math.sqrt(sum(x * x for x in v2))
        v2 = [x / v2_length for x in v2] if v2_length > 0 else v2
        return [v1, v2]

    @staticmethod
    def convert_angle_to_vectors(angles):
        """
        将欧拉角转换为向量格式
        角度绕X,Y,Z旋转（弧度制）
        """
        if (len(angles) != 3) or (angles == [0, 0, 0]):
            raise ValueError("操作错误，数据无效")
        rx, ry, rz = map(math.radians, angles)
        ca, sa = math.cos(rx), math.sin(rx)
        cb, sb = math.cos(ry), math.sin(ry)
        cg, sg = math.cos(rz), math.sin(rz)
        # V1 = R @ [1,0,0] (局部X轴)
        v1x = cb * cg
        v1y = sa * sb * cg + ca * sg
        v1z = -ca * sb * cg + sa * sg
        # V2 = R @ [0,1,0] (局部Y轴)
        v2x = -cb * sg
        v2y = -sa * sb * sg + ca * cg
        v2z = ca * sb * sg + sa * cg
        # 四舍五入到6位小数
        v1 = [round(v1x, 6), round(v1y, 6), round(v1z, 6)]
        v2 = [round(v2x, 6), round(v2y, 6), round(v2z, 6)]
        return [v1, v2]

    @staticmethod
    def live_load_set_line(code: int, calc_type: int, groups: list[str]):
        """用于更新移动荷载分析设置"""
        if groups is None:
            return f"{code},{calc_type},\r\n"
        return f"{code},{calc_type}," + ",".join(groups) + "\r\n"

    @staticmethod
    def parse_ids_to_array(ids: Union[int, List[int], str, None],allow_empty = True) -> List[int]:
        """
        支持整形、列表、XtoYbyZ形式字符串 统一解析为 int 列表
        """
        def parse_number_string(input_str: str) -> Optional[List[int]]:
            """
            将带“to/by”的字符串解析为 int 列表。
            规则与给定 C# 版本一致：
              - 以空白分隔各段；段内若包含 'to' 则按 'start to end [by step]' 解析
              - 仅支持紧凑写法：例如 '3to10by2' 或 '3to10'（不支持 '3 to 10 by 2'）
              - step 缺省为 1；返回为包含端点的等差序列（若整除）
              - 对于无法解析的段、step<=0、end<start 的段会跳过
              - 空或全空白字符串返回 None
            """
            if input_str is None:
                return None
            s = input_str.strip()
            if s == "":
                return None

            results: List[int] = []
            tokens = s.split()
            for tok in tokens:
                if "to" in tok:
                    # 按 'to'/'by' 拆分；例如 '3to10by2' -> ['3','10','2']
                    parts = re.split(r'to|by', tok)
                    if len(parts) >= 2:
                        try:
                            start = int(parts[0])
                            end = int(parts[1])
                        except ValueError:
                            continue
                        step = 1
                        if len(parts) > 2:
                            try:
                                step = int(parts[2])
                            except ValueError:
                                step = 1
                        if step <= 0 or end < start:
                            continue
                        count = (end - start) // step + 1
                        results.extend(start + n * step for n in range(count))
                else:
                    try:
                        results.append(int(tok))
                    except ValueError:
                        continue

            return results

        result_ids = []
        if ids is None:
            return result_ids
        if isinstance(ids, int):
            result_ids.append(ids)
        elif isinstance(ids, str):
            result_ids.extend(parse_number_string(ids))
        else:
            result_ids.extend(ids)
        if len(result_ids) == 0 and allow_empty is False:
            raise Exception("集合不可为空，请核查数据")
        return result_ids
