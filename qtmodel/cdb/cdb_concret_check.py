from qtmodel.core.qt_server import QtServer


class CdbConcretCheck:
    """
    用于混凝土结构验算
    """
    @staticmethod
    def add_concrete_load_combine(index: int = -1, name: str = "", combine_type: int = 1,standard:int=1,
                         combine_info: list[tuple[str, str, float]] = None):
        """
        添加混凝土检算荷载组合
        Args:
            index: 荷载组合索引，-1表示在最后添加
            name: 荷载组合名称
            standard: 1-公规2015 2-铁规2017 3-铁路极限状态 4-英规BS5400 5-美规
            kind: 类型参考界面
                公规2015|1-基本 2-偶然 3-标准 4-频遇 5-准永久...
            combine_type: 荷载组合类型，1-相加并判别，2-包络
            combine_info: 荷载组合信息，格式为[(荷载工况,不利系数,有利系数)]
        Example:
            cdb.add_check_load_combination(name="P1+P2",load_combinations=["P1","P2"])
        Returns: 无
        """
        QtServer.send_dict(header="ADD-CONCRET-LOAD-COMBINE",payload={
            "index": index,
            "name": name,
            "standard": standard,
            "combine_type": combine_type,
            "combine_info": combine_info
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
        QtServer.send_dict(header="ADD-CONCRET-CHECK-CASE",payload={
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
        QtServer.send_dict(header="REMOVE-CONCRET-CHECK-CASE",payload={
            "name": name,
        })

    @staticmethod
    def solve_concret_check(name:str=""):
        """
        混凝土检算分析
        Args:
            name: 检算名称
        Example:
            cdb.solve_concret_check(name="混凝土检算")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        QtServer.send_dict(header="SOLVE-CONCRET-CHECK",payload=payload)

    @staticmethod
    def add_check_material(name:str="",properties:list[float]=None,model:int=1,
                           user_model:bool=False,user_data:list[tuple[float,float]]=None):
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
            model: 模型类型，1-损伤演化模型 2-修正Kent-Park模型 3-约束混凝土 4-无约束混凝土 5-钢管混凝土 
            parameters: 自定义模式参数
            user_data: 用户自定义模型数据，格式为[(应变,应力)]
        Example:
            cdb.add_check_material(name="混凝土",properties=[3.45e10,5e7,3.24e7,2.65e6,1.83e6],model=1)
        Returns: 无
        """
        QtServer.send_dict(header="ADD-CONCRET-CHECK-MATERIAL",payload={
            "name": name,
            "properties": properties,
            "model": model,
            "user_model": user_model,
            "user_data": user_data
        })


    @staticmethod
    def update_section_steel_bar(sec_id:int,bar_data:list[tuple[float,float,float,int]]):
        """
        更新截面钢筋数据
        Args:
            sec_id: 截面ID
            bar_data: 钢筋数据列表，格式为[(x,y,直径,钢筋材料号)]
        Example:
            cdb.update_section_steel_bar(sec_id=1,bar_data=[(0.1,0.5,20,10),(0.3,0.6,22,10)])
        Returns: 无
        """
        QtServer.send_dict(header="UPDATE-SECTION-STEEL-BAR",payload={
            "sec_id": sec_id,
            "bar_data": bar_data
        })

    #添加箍筋信息
    @staticmethod
    def add_steel_hoop(index:int,name:str,hoop_type:int=1,material_id:int=1,nums:int=1,
                        diameter:float=0,gap:float=0,core_diameter:float=0):
        """
        添加箍筋数据
        Args:
            index: 箍筋编号
            name: 箍筋名称
            hoop_type: 箍筋类型 1-普通箍筋 2-螺旋箍筋
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

    # 添加混凝土构件荷载组合
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

