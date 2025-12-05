from qtmodel import *
import pandas as pd
import json
case_names = ["ST:整体升温","ST:整体降温","ST:梯度升温","ST:梯度降温","SM:支点沉降_最大","SM:支点沉降_最小",
              "MV:移动分析工况1_合计_最大","MV:移动分析工况1_合计_最小","CB:标准组合_最大","CB:标准组合_最小"]
cq_name = "CQ:成桥(合计)"
ids = [502, 500, 488, 486, 484]
a = odb.get_reaction(ids=ids, stage_id=9, result_kind=1)
b = odb.get_reaction(ids=ids, stage_id=8, result_kind=1)
operation_result = json.loads(odb.get_reaction(ids=ids,stage_id=-1,case_name=cq_name))

a_list = json.loads(a)
b_list = json.loads(b)

fz_list_a = [{'node_id': d['node_id'], 'fz': d['fz'] / 1000} for d in a_list]
fz_list_b = [{'node_id': d['node_id'], 'fz': d['fz'] / 1000} for d in b_list]
fz_list_operation= [{'node_id': d['node_id'], 'fz': d['fz'] / 1000} for d in operation_result]
# 先变成 dict，方便按 node_id 查
fz_a_dict = {item['node_id']: item['fz'] for item in fz_list_a}
fz_b_dict = {item['node_id']: item['fz'] for item in fz_list_b}
fz_operation_dict = {item['node_id']: item['fz'] for item in fz_list_operation}

# 获取二恒
dead_load2 = [
    {
        'node_id': nid,
        'fz_diff': fz_a_dict[nid] - fz_b_dict[nid]
    }
    for nid in ids
    if nid in fz_a_dict and nid in fz_b_dict
]
dead_load2_dict = {item['node_id']: item['fz_diff'] for item in dead_load2}
# 获取一恒，为运营阶段减去二恒
dead_load1 = [
    {
        'node_id': nid,
        'fz': fz_operation_dict[nid] - dead_load2_dict.get(nid, 0.0)
    }
    for nid in ids
    if nid in fz_operation_dict
]
dead_load1_dict = {item['node_id']: item['fz'] for item in dead_load1}
# ========= 其他工况列（跟 CQ:成桥(合计) 一样的调用方式） =========
case_fz_dicts = {}   # {case_name: {node_id: fz}}

for cname in case_names:
    result = json.loads(
        odb.get_reaction(ids=ids, stage_id=-1, case_name=cname)
    )
    case_fz_dicts[cname] = {
        d['node_id']: d['fz'] / 1000 for d in result
    }

# ========= 组装 DataFrame，按 ids 顺序 =========
rows = []
for nid in ids:
    row = {
        '节点号': nid,
        cq_name:      fz_operation_dict.get(nid, None),   # CQ:成桥(合计)
        '一期恒载':   dead_load1_dict.get(nid, None),
        '二期恒载':   dead_load2_dict.get(nid, None),
    }
    # 动态加上 case_names 对应的列
    for cname in case_names:
        row[cname] = case_fz_dicts.get(cname, {}).get(nid, None)
    rows.append(row)

df = pd.DataFrame(rows).round(1)  # 保留 1 位小数，可按需调整

# 输出 Excel
df.to_excel(r'支座反力分解_含其他工况.xlsx', index=False)
print("已导出：支座反力分解_含其他工况.xlsx")

