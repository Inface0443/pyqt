from typing import Union
from qtmodel.core.qt_server import QtServer


class CdbConcreteCheck:
    """
    用于混凝土结构验算
    """
    @staticmethod
    def add_check_load_combine(index: int = -1, name: str = "", combine_type: int = 1,standard:int=1,
                       kind:int=1,  combine_info: list[tuple[str, float, float]] = None):
        """
        添加混凝土检算荷载组合
        Args:
            index: 荷载组合索引，-1表示在最后添加
            name: 荷载组合名称
            combine_type: 0-相加并判别，1-包络
            standard: 1-公规2015 2-铁规2017 3-铁路极限状态 4-英规BS5400 5-美规
            kind: 类型参考界面
                公规2015|1-基本 2-偶然 3-标准 4-频遇 5-准永久 6-疲劳组合
                铁路TB1002| 1-主力组合 2-主加附组合 3-主加特殊组合
                铁路极限状态法| 1~11-组合I~XI 12-标准值组合 13-主力组合 14-主加附组合
                英规| 1-承载能力极限状态 2-正常使用极限状态
                美规| 1-强度组合 2-极端事件 3-使用组合I 4-使用组合II 5-使用组合III 6-使用组合IV 7-疲劳组合 8-永久作用组合
            combine_info: 荷载组合信息，格式为[(荷载工况,不利系数,有利系数)]
        Example:
            cdb.add_check_load_combine(name="P1+P2",standard=1,kind=1,combine_info=[("P1 (ST)",1,1),("P2 (ST)",1,1)])
        Returns: 无
        """
        QtServer.send_dict(header="ADD-CHECK-LOAD-COMBINE",payload={
            "index": index,
            "name": name,
            "combine_type": combine_type,
            "standard": standard,
            "kind": kind,
            "combine_info": combine_info
        })

    @staticmethod
    def remove_check_load_combine(index: int = -1, name: str = ""):
        """
        删除混凝土检算荷载组合
        Args:
            index: 荷载组合索引，-1表示删除所有
            name: 荷载组合名称
        Example:
            cdb.remove_check_load_combine(index=1)
            cdb.remove_check_load_combine(name="P1+P2")
        Returns: 无
        """
        QtServer.send_dict(header="REMOVE-CHECK-LOAD-COMBINE",payload={
            "index": index,
            "name": name,
        })

    @staticmethod
    def add_concrete_check_case(name:str="",standard:int=1,structure_type:int=1,group_name="默认结构组"):
        """
        添加混凝土检算工况
        Args:
            name: 检算名称
            standard: 混凝土标准，1为JTG3362-2018，2为TB10092-2017
            structure_type: 结构类型，1为钢筋混凝土，2为B构件，3为A类构件，4为全预应力构件
            group_name: 结构组名称
        Example:
            cdb.add_concrete_check_case(name="混凝土检算",standard=1,structure_type=1,group_name="默认结构组")
        Returns: 无
        """
        QtServer.send_dict(header="ADD-CONCRETE-CHECK-CASE",payload={
            "name": name,
            "standard": standard,
            "structure_type": structure_type,
            "group_name": group_name
        })

    @staticmethod
    def remove_concrete_check_case(name:str=""):
        """
        删除混凝土检算工况
        Args:
            name: 检算名称
        Example:
            cdb.remove_concrete_check_case(name="混凝土检算")
        Returns: 无
        """
        QtServer.send_dict(header="REMOVE-CONCRETE-CHECK-CASE",payload={
            "name": name,
        })

    @staticmethod
    def solve_concrete_check(name:str=""):
        """
        混凝土检算分析
        Args:
            name: 检算名称
        Example:
            cdb.solve_concrete_check(name="混凝土检算")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        QtServer.send_dict(header="SOLVE-CONCRETE-CHECK",payload=payload)

    @staticmethod
    def add_check_material(name:str="",properties:list[float]=None,model:int=1,
                           parameter_data:list[float]=None,
                           curve_data:list[tuple[float,float]]=None,
                           user_material:int =1,user_standard:int =1):
        """
        添加混凝土检算材料,需要修改检算材料信息才添加检算材料
        Args:
            name: 材料名称
            properties: 属性值列表,依据材料规范填写
                JTG 3362-2018 公路规范-[弹性模量,fcuk,fck,ftk,ftd]
                JTG D62-2004 公路规范-[弹性模量,fcuk,fck,ftk,ftd]
                JTJ 024-1985 公路规范-[弹性模量,fcuk,fck,ftk,ftd]
                TB 1002-2017 铁路规范-[弹性模量,fcuk,fc,ftc]
                ASTM 美国材料试验协会-[弹性模量,fc',fr]
                AASHTO-[弹性模量,fc',fr]
                BS 5400-1990-[弹性模量,fcu]
                铁路极限状态法-[弹性模量,fcuk,fck,fctk]
            model: 应力应变曲线类型，1-损伤演化模型 2-修正Kent-Park模型 3-约束混凝土 4-无约束混凝土 5-钢管混凝土
            parameter_data: 检算材料应力应变特性参数
            curve_data: 用户自定义模型数据，格式为[(应变,应力)]
            user_material: 用户自定义材料类型 1-混凝土 2-钢材 3-预应力 4-钢筋
            user_standard: 参考Ui对应规范
        Example:
            cdb.add_check_material(name="混凝土",properties=[3.45e10,5e7,3.24e7,2.65e6,1.83e6],model=1)
        Returns: 无
        """
        QtServer.send_dict(header="ADD-CONCRETE-CHECK-MATERIAL",payload={
            "name": name,
            "properties": properties,
            "model": model,
            "parameter_data": parameter_data,
            "curve_data": curve_data,
            "user_material": user_material,
            "user_standard": user_standard
        })

    @staticmethod
    def add_parameter_reinforcement(sec_id:int,position:int=0,has_outer:bool=True,has_inner:bool=True,outer_type:int=0,inner_type:int=0,
                                    outer_info:list[list[float]]=None,inner_info:list[list[float]]=None):
        """
        添加参数化配筋
        Args:
            sec_id: 截面ID
            position: 变截面位置，0为截面I端，1为截面J端
            has_outer: 是否有外部钢筋
            has_inner: 是否有内部钢筋
            outer_type: 0-按间距分布 1-按数量分布
            inner_type: 0-按间距分布 1-按数量分布
            outer_info: 外部钢筋信息，格式为[[直径,材料号,层边距,钢筋间距/数量,每束根数],...]
            inner_info: 内部钢筋信息，格式为[[直径,材料号,层边距,钢筋间距/数量,每束根数],...]
        Example:
            cdb.add_parameter_reinforcement(sec_id=1,has_outer=True,has_inner=True,outer_type=0,inner_type=0,
                                            outer_info=[[20,1,50,150,1]],inner_info=[[20,1,50,150,1]])
        Returns: 无
        """
        QtServer.send_dict(header="ADD-PARAMETER-REINFORCEMENT",payload={
            "sec_id": sec_id,
            "position": position,
            "has_outer": has_outer,
            "has_inner": has_inner, 
            "outer_type": outer_type,
            "inner_type": inner_type,
            "outer_info": outer_info,
            "inner_info": inner_info,
        })

    @staticmethod
    def add_part_parameter_reinforcement(sec_id:int,position:int=0,data_info:list[list[float]]=None):
        """
        添加局部参数化配筋
        Args:
            sec_id: 截面ID
            position: 截面位置，0为截面I端，1为截面J端
            data_info: 钢筋数据，列表中每项参数为10个，格式为[[基准线号,分布方式,布置方向,直径,钢筋材料号,层边距,间距/数量,每束根数,首点偏移,尾点偏移],...]
                分布方式| 0-按间距分布 1-按数量分布
                布置方向| 0-向内布置 1-向外布置
        Example:
            cdb.add_part_parameter_reinforcement(sec_id=1,position=0,data_info=[[11,0,0,20,4,50,150,1,0,0]])
        Returns: 无
        """
        QtServer.send_dict(header="ADD-PART-PARAMETER-REINFORCEMENT",payload={
            "sec_id": sec_id,
            "position": position,
            "data_info": data_info,
        })

    @staticmethod
    def add_reinforcement_by_point(sec_id:int,position:int=0,bar_data:Union[list[tuple[float,float,float,int]],list[list[float]]] =None):
        """
        添加自定义截面纵向钢筋数据
        Args:
            sec_id: 截面ID
            position: 变截面位置，0为截面I端，1为截面J端
            bar_data: 钢筋数据列表，格式为[(x,y,直径,钢筋材料号)]
        Example:
            cdb.add_reinforcement_by_point(sec_id=1,position=0,bar_data=[(0.1,0.5,20,1),(0.3,0.6,22,1)])
        Returns: 无
        """
        QtServer.send_dict(header="ADD-REINFORCEMENT-BY-POINT",payload={
            "sec_id": sec_id,
            "sec_name": sec_id,
            "position": position,
            "bar_data": bar_data
        })

    @staticmethod
    def get_reinforcement_data():
        """
        获取全部纵向钢筋坐标信息
        Args: 无
        Example:
            cdb.get_reinforcement_data()
        Returns: list[dict]类型字符串
        """
        QtServer.send_dict(header="GET-REINFORCEMENT-DATA")

    @staticmethod
    def get_stirrup_data():
        """
        获取全部箍筋信息
        Args: 无
        Example:
            cdb.get_stirrup_data()
        Returns: list[dict]类型字符串
        """
        QtServer.send_dict(header="GET-STIRRUP-DATA")

    @staticmethod
    def get_check_material_data():
        """
        获取全部检算材料信息
        Args: 无
        Example:
            cdb.get_check_material_data()
        Returns: list[dict]类型字符串
        """
        QtServer.send_dict(header="GET-CHECK-MATERIAL-DATA")


    @staticmethod
    def add_steel_hoop(index:int,name:str,hoop_type:int=1,material_id:int=1,nums:int=1,
                        diameter:float=0,gap:float=0,core_diameter:float=0):
        """
        添加箍筋数据
        Args:
            index: 箍筋编号
            name: 箍筋名称
            hoop_type: 箍筋类型 0-普通箍筋 1-螺旋箍筋
            material_id: 箍筋材料号
            nums: 箍筋肢数或环数
            diameter: 箍筋直径
            gap: 箍筋间距
            core_diameter: 箍筋核心直径
        Example:
            cdb.add_steel_hoop(index=1,name="箍筋1",hoop_type=1,material_id=10,nums=2,diameter=20,gap=0.5,core_diameter=15)
        Returns: 无
        """
        QtServer.send_dict(header="ADD-STEEL-HOOP",payload={
            "index": index,
            "name": name,
            "hoop_type": hoop_type,
            "material_id": material_id,
            "nums": nums,
            "diameter": diameter,
            "gap": gap,
            "core_diameter": core_diameter
        })

    @staticmethod
    def update_element_steel_hoop(sec_id:int,bar_data:list[tuple[float,float,float,int]]):
        """
        更新单元箍筋数据
        Args:
            sec_id: 单元ID
            bar_data: 箍筋数据列表，格式为[(x,y,直径,箍筋材料号)]
        Example:
            cdb.update_element_steel_hoop(sec_id=1,bar_data=[(0.1,0.5,20,10),(0.3,0.6,22,10)])
        Returns: 无
        """
        QtServer.send_dict(header="UPDATE-ELEMENT-STEEL-HOOP",payload={
            "sec_id": sec_id,
            "bar_data": bar_data
        })

    @staticmethod
    def update_vertical_steel_hoop(nums:int=0,area:float=0.001,gap:float=0.2,effective_prestress:float=8e8,fpd:float=9e8):
        """
        更新竖向箍筋数据
        Args:
            nums: 箍筋肢数或环数
            area: 箍筋面积，单位：m²
            gap: 箍筋间距，单位：m
            effective_prestress: 有效预应力，单位：Pa (8e8 Pa = 800 MPa)
            fpd: 强度设计值，单位：Pa (9e8 Pa = 900 MPa)
        Example:
            cdb.update_vertical_steel_hoop(nums=4,area=0.000314,gap=0.15)
        Returns: 无
        """
        QtServer.send_dict(header="UPDATE-VERTICAL-STEEL-HOOP",payload={
            "nums": nums,
            "area": area,
            "gap": gap,
            "effective_prestress": effective_prestress,
            "fpd": fpd
        })


    @staticmethod
    def add_concrete_load_combination(name:str,standard:int=1,kind:int=1,combine_type:int=1,
                                      load_case_factors:list[tuple[str,float,float]]=None):
        """
        添加混凝土构件荷载组合
        Args:
            name: 荷载组合名称
            standard: 荷载组合标准 1-公路规范JTG D60-2015 2-铁路规范TB 10002-2017 
            kind:荷载组合类型，根据规范不同类型不同
                公路规范JTG D60-2015|1-基本组合 2-偶然组合 3-标准值组合 4-频遇组合 5-准永久组合
                铁路规范TB 10002-2017|1-主力组合 2-主加附组合 3-主加特殊组合
            combine_type: 组合方式 1-相加并判别 2-包络
            load_case_factors: 荷载工况列表，格式为[(荷载工况名称,不利系数,有利系数)]
        Example:
            cdb.add_concrete_load_combination(name="LC1",standard=1,kind=1,combine_type=1,load_case_factors=[("LC1-1",1.0,1.2)])
        Returns: 无
        """
        QtServer.send_dict(header="ADD-CONCRETE-LOAD-COMBINATION",payload={
            "name": name,
            "standard": standard,
            "kind": kind,
            "combine_type": combine_type,
            "load_case_factors": load_case_factors
        })

