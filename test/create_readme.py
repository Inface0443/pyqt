from datetime import datetime


class Readme:
    """用于生成帮助文档"""
    version = "V2.1.1"
    version_qdat = "V1.2.4"
    _data_str = []

    @staticmethod
    def get_def_and_helper(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取文件的所有行
            lines = file.readlines()
        for i in range(len(lines) - 1):
            if lines[i].startswith("    @staticmethod"):
                i = i + 1
                while not lines[i].startswith("        try:"):
                    Readme.print_str(lines[i])
                    i = i + 1
            continue

    @staticmethod
    def get_note(file_path):
        # 使用with语句打开文件，这样可以保证文件在操作完成后被正确关闭
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取文件的所有行
            lines = file.readlines()

        list_def = []
        for i in range(len(lines) - 1):
            if lines[i].strip().startswith("# region"):
                list_def.append(lines[i].strip().split("region")[1])
            if lines[i].strip().startswith("@staticmethod"):
                def_info = []
                while not lines[i + 1].strip().startswith("@staticmethod"):
                    if lines[i].strip().startswith("# region"):
                        list_def.append(lines[i].strip().split("region")[1])
                    if i > len(lines) - 3:
                        break
                    i = i + 1
                    if lines[i].strip() != "":
                        def_info.append(lines[i].strip())
                list_def.append(def_info)

        note_list = []
        for item in list_def:
            if type(item) == str:
                note_list.append("## " + item)
                continue
            def_note = [item[0].replace("def ", "### ").split("(")[0]]
            start_position = item.index("\"\"\"") if "\"\"\"" in item else None
            last_position = len(item) - item[::-1].index("\"\"\"") - 1 if "\"\"\"" in item else None
            if start_position is not None and last_position is not None:
                def_note.extend(item[start_position + 1:last_position])
                note_list.append(def_note)

        return note_list

    @staticmethod
    def print_md_file(db):
        for item in db:
            if type(item) == str:
                Readme.print_str(item)
            else:
                for k in range(len(item)):
                    if item[k].startswith("#"):
                        Readme.print_str(item[k])
                        k = k + 1
                        Readme.print_str(item[k])
                    elif item[k].startswith("Args:"):
                        Readme.print_str("> 参数:  ")
                        k = k + 1
                        while not item[k].startswith("Example:"):
                            Readme.print_str("> " + item[k] + "  ")
                            k = k + 1
                    elif item[k].startswith("Example"):
                        Readme.print_str("```Python")
                        Readme.print_str("# 示例代码")
                        Readme.print_str("from qtmodel import *")
                        k = k + 1
                        while not item[k].startswith("Returns"):
                            Readme.print_str(item[k])
                            k = k + 1
                    elif item[k].startswith("Returns"):
                        Readme.print_str("#"+item[k])
                        Readme.print_str("```  ")


    @staticmethod
    def print_md_file_context():
        # 获取当前日期和时间
        Readme.print_str(f"> 最新qtmodel版本 {Readme.version} - {datetime.now().date()} ")
        Readme.print_str(f"> 最新qdat数据版本 {Readme.version_qdat} ")
        Readme.print_str("> pip install --upgrade qtmodel -i https://pypi.org/simple")
        Readme.print_str("- 新增更新结构组接口 ")
        Readme.print_str("# 建模操作 ")
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_structure.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_property.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_section.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_boundary.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_tendon.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_static_load.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_live_load.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_dynamic_load.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_temperature_load.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_construction_stage.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/mdb/mdb_analysis_setting.py'))
        Readme.print_str("# 视图与结果提取 ")
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_model_material.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_model_structure.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_model_section.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_model_boundary.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_model_load.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_model_stage.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_result_data.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_result_plot.py'))
        Readme.print_md_file(Readme.get_note(r'../qtmodel/odb/odb_view.py'))
        try:
            with open(r"../README.md", 'w', encoding='utf-8') as file:
                for item in Readme._data_str:
                    file.write(item + '\n')
            print(f"列表已成功写入文件")
        except Exception as e:
            print(f"写入文件时出错: {e}")

    @staticmethod
    def print_str(data):
        Readme._data_str.append(data)


Readme.print_md_file_context()
