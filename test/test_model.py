import sys
module_path = r'E:/pyqt'
sys.path.append(rf"{module_path}")
from qtmodel import *
mdb.set_url("http://10.33.176.44:61076/")
import json
ids = "484to503"
a = odb.get_reaction(ids=ids,stage_id=9,result_kind=1)
b= odb.get_reaction(ids=ids,stage_id=8,result_kind=1)
a_list = json.loads(a)
b_list = json.loads(b)
fz_list_a = [{'node_id': d['node_id'], 'fz': d['fz']/1000} for d in a_list]
fz_list_b = [{'node_id': d['node_id'], 'fz': d['fz']/1000} for d in b_list]
# 先把 b 的数据按 node_id 做成字典，方便查找
fz_b_dict = {item['node_id']: item['fz'] for item in fz_list_b}

# 1）如果你想要一个带 node_id 和差值的新列表
dead_load2 = [
    {
        'node_id': item_a['node_id'],
        'fz_diff': (item_a['fz'] - fz_b_dict[item_a['node_id']])
    }
    for item_a in fz_list_a
    if item_a['node_id'] in fz_b_dict
]