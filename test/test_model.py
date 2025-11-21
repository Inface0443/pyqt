import json
import time
from collections import defaultdict
from qtmodel import odb, mdb
import pandas as pd


class Force:
    """
    力类 - 表示三维空间中的力和力矩

    属性:
        fx, fy, fz: 力在x, y, z方向的分量
        mx, my, mz: 力矩在x, y, z方向的分量
    """

    def __init__(self, fx: float = 0.0, fy: float = 0.0, fz: float = 0.0,
                 mx: float = 0.0, my: float = 0.0, mz: float = 0.0):
        """
        初始化力对象

        Args:
            fx: x方向力分量 (默认: 0.0)
            fy: y方向力分量 (默认: 0.0)
            fz: z方向力分量 (默认: 0.0)
            mx: x方向力矩分量 (默认: 0.0)
            my: y方向力矩分量 (默认: 0.0)
            mz: z方向力矩分量 (默认: 0.0)
        """
        self.fx = float(fx)
        self.fy = float(fy)
        self.fz = float(fz)
        self.mx = float(mx)
        self.my = float(my)
        self.mz = float(mz)

    def get_components(self):
        """返回力分量的字典"""
        return {
            'fx': self.fx/1000,
            'fy': self.fy/1000,
            'fz': self.fz/1000,
            'mx': self.mx/1000,
            'my': self.my/1000,
            'mz': self.mz/1000
        }

def get_force_dic(force_json: object) -> object:
    temp_dic = {}
    for force in force_json:
        elementId = int(force['element_id'])
        forceI = Force(force['force_i']['Fx'], force['force_i']['Fy'], force['force_i']['Fz'], force['force_i']['Mx'],
                       force['force_i']['My'], force['force_i']['Mz'])
        forceJ = Force(force['force_j']['Fx'], force['force_j']['Fy'], force['force_j']['Fz'], force['force_j']['Mx'],
                       force['force_j']['My'], force['force_j']['Mz'])
        if elementId not in temp_dic:
            temp_dic[elementId] = []
        temp_dic[elementId].append(forceI)
        temp_dic[elementId].append(forceJ)

    return temp_dic

def export_forces_to_excel(element_self_concurrent_force_result, filename="force_analysis.xlsx"):
    """
    将 element_self_concurrent_force_result 数据导出到 Excel

    Args:
        element_self_concurrent_force_result: 包含力数据的嵌套字典
        filename: 输出的Excel文件名
    """

    # 准备数据列表
    data_rows = []

    # 遍历所有元素
    for element_id, element_data in element_self_concurrent_force_result.items():
        # 处理 I 节点
        if "I" in element_data:

            # 获取 I 节点的力分量
            i_force_data = element_data["I"]
            for component in ['fx', 'fy', 'fz', 'mx', 'my', 'mz']:
                i_data = {
                    'element_id': element_id,
                    'I/J': 'I'
                }
                i_data['分量'] = component
                if component in i_force_data:
                    force_obj = i_force_data[component]
                    # 假设 Force 对象有获取值的方法或属性
                    if hasattr(force_obj, 'get_components'):
                        # 如果 Force 类有 get_components 方法
                        components = force_obj.get_components()
                        for component in ['fx', 'fy', 'fz', 'mx', 'my', 'mz']:
                            i_data[component] = components.get(component, 0)
                    elif hasattr(force_obj, 'value'):
                        # 如果 Force 类有 value 属性
                        i_data[component] = force_obj.value
                    else:
                        # 默认处理
                        i_data[component] = float(force_obj) if hasattr(force_obj, '__float__') else 0
                data_rows.append(i_data)

        # 处理 J 节点
        if "J" in element_data:

            # 获取 J 节点的力分量
            j_force_data = element_data["J"]
            for component in ['fx', 'fy', 'fz', 'mx', 'my', 'mz']:
                j_data = {
                    'element_id': element_id,
                    'I/J': 'J'
                }
                j_data['分量'] = component
                if component in j_force_data:
                    force_obj = j_force_data[component]
                    # 假设 Force 对象有获取值的方法或属性
                    if hasattr(force_obj, 'get_components'):
                        components = force_obj.get_components()
                        for component in ['fx', 'fy', 'fz', 'mx', 'my', 'mz']:
                            j_data[component] = components.get(component, 0)
                    elif hasattr(force_obj, 'value'):
                        j_data[component] = force_obj.value
                    else:
                        j_data[component] = float(force_obj) if hasattr(force_obj, '__float__') else 0

                data_rows.append(j_data)

    # 创建 DataFrame
    df = pd.DataFrame(data_rows)

    # 设置列顺序
    column_order = ['element_id', 'I/J', '分量', 'fx', 'fy', 'fz', 'mx', 'my', 'mz']
    df = df.reindex(columns=column_order)

    # 导出到 Excel
    df.to_excel(filename, index=False, sheet_name='力分析结果')
    print(f"数据已导出到 {filename}")
    print(f"共导出 {len(data_rows)} 行数据")

    return df

# 模型路径
mdb.set_url("http://10.33.176.44:61076/")
model_file_path = "D:\白沙洲公铁桥-密横梁体系（不开裂）-2025.11.11.bfmd"
# 结果excel路径
result_excel_path="D:\力分析结果.xlsx"
# 施工阶段开始阶段
stage_start_id = 1
# 施工阶段结束阶段
stage_end_id = 84
# 施工阶段包络类型 envelop_type=1 最大；envelop_type=2 最大；envelop_type=3 包络
envelop_type=1

# 单元号
elementIds = []
# elementIds.extend([i for i in range(10001, 10211 + 1)])  #############改
elementIds.extend([i for i in range(11001, 11412 + 1)])  #############改
# elementIds.extend([i for i in range(12005, 12828 + 1)])  #############改
# elementIds.extend([i for i in range(70001, 70024 + 1)])  #############改
# elementIds.extend([i for i in range(71001, 71024 + 1)])  #############改
# elementIds.extend([i for i in range(72001, 72056 + 1)])  #############改

# mdb.open_file(model_file_path)

# 施工阶段包络结果  #############改
start = time.time()
element_forces_envelope = odb.get_element_force(ids=elementIds, stage_id=0,
                                                envelop_type=envelop_type)
element_forces_envelope = json.loads(element_forces_envelope)
element_force_envelope_dict = get_force_dic(element_forces_envelope)  # 施工阶段包络字典，key=单元号 value=I端内力，J端内力

end = time.time()
elapsed = end - start
print(f"获取施工阶段包络结果时间: {elapsed:.2f} 秒")
start = time.time()

# 获取所有施工阶段结果
element_forces_stage_dic = {}
for i in range(stage_start_id - 1, stage_end_id):
    temp_dic = {}
    if i + 1 not in element_forces_stage_dic:
        element_forces_stage_dic[i + 1] = []

    elements_stage = odb.get_elements_of_stage(i + 1)
    elements_stage = json.loads(elements_stage)
    elements_intersection = list(set(elementIds).intersection(elements_stage))

    if len(elements_intersection) == 0: continue

    element_forces = odb.get_element_force(ids=elements_intersection, stage_id=i + 1)
    element_forces = json.loads(element_forces)
    temp = get_force_dic(element_forces)

    for element_id in elements_intersection:
        temp_dic[element_id] = temp[element_id]

    element_forces_stage_dic[i + 1] = temp_dic

tolerance = 1e-20

end = time.time()
elapsed = end - start
print(f"获取施工阶段所有结果结果时间: {elapsed:.2f} 秒")
start = time.time()

element_self_concurrent_force_result = defaultdict(lambda: defaultdict(dict))
nodes = ["I", "J"]
components = ['fx', 'fy', 'fz', 'mx', 'my', 'mz']
edges = [("I", 0), ("J", 1)]

for element_id in elementIds:
    for node in nodes:
        for component in components:
            element_self_concurrent_force_result[element_id][node][component] = Force()

    if element_id in element_force_envelope_dict:
        for stageId in range(stage_start_id, stage_end_id):
            if element_id in element_forces_stage_dic[stageId]:

                for edge_name, temp_index in edges:
                    # 获取参考值和当前值
                    envelope_val = element_force_envelope_dict[element_id][temp_index]
                    stage_val = element_forces_stage_dic[stageId][element_id][temp_index]

                    # 对于每个分量进行比较和赋值
                    for comp in components:
                        # 获取分量的值，例如envelope_val.fx
                        env_comp_val = getattr(envelope_val, comp)
                        stage_comp_val = getattr(stage_val, comp)
                        if abs(env_comp_val - stage_comp_val) < tolerance:
                            # 赋值，注意分量名称是大写，如"Fx"
                            element_self_concurrent_force_result[element_id][edge_name][comp] = stage_val

end = time.time()
elapsed = end - start
print(f"获并发结果结果时间: {elapsed:.2f} 秒")
start = time.time()

result_df = export_forces_to_excel(element_self_concurrent_force_result, result_excel_path)



