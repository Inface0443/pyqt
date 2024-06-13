class Node:
    def __init__(self, node_id: int, x: float, y: float, z: float):
        """
        节点编号和位置信息
        Args:
            node_id: 单元类型 支持 BEAM PLATE
            x: 单元节点列表
            y: 单元截面id号或板厚id号
            z: 材料号
        """
        self.node_id = node_id
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class Element:
    def __init__(self, index: int, ele_type: str, node_list: list[int], mat_id: int, sec_id: int, beta: float = 0,
                 initial_type: int = 1, initial_value: float = 0):
        """
        单元详细信息
        Args:
            index: 单元截面id号或板厚id号
            ele_type: 单元类型 支持 BEAM PLATE CABLE LINK
            node_list: 单元节点列表
            mat_id: 材料号
            sec_id: 截面号或板厚号
            beta: 贝塔角
            initial_type: 张拉类型  (仅索单元需要)
            initial_value: 张拉值  (仅索单元需要)
        """
        self.ele_type = ele_type
        self.node_list = node_list
        self.index = index
        self.mat_id = mat_id
        self.sec_id = sec_id
        self.beta = beta
        self.initial_type = initial_type
        self.initial_value = initial_value

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class Material:
    def __init__(self, mat_id: int, name: str, mat_type: str, standard: str, database: str, data_info: list[float] = None,
                 modified: bool = False, construct_factor: float = 1.0, creep_id: int = -1, f_cuk: float = 0):
        """
        材料信息
        Args:
           mat_id: 材料号
           name: 材料名称
           mat_type: 材料类型
           standard: 规范名
           database: 数据库名称
           data_info: 材料参数列表[弹性模量,容重,泊松比,热膨胀系数] (修改和自定义需要)
           modified: 是否修改材料信息
           construct_factor: 构造系数
           creep_id: 收缩徐变号 默认-1表示不考虑收缩徐变
           f_cuk: 立方体抗压强度标准值 (自定义材料考虑收缩徐变)
        """
        self.mat_id = mat_id
        self.name = name
        self.mat_type = mat_type
        self.standard = standard
        self.database = database
        self.construct_factor = construct_factor
        self.modified = modified
        self.data_info = data_info
        self.is_creep = creep_id
        self.f_cuk = f_cuk

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class GeneralSupport:
    def __init__(self, support_id: int = 1, node_id: int = 1, boundary_info: tuple[bool, bool, bool, bool, bool, bool] = None,
                 group_name: str = "默认边界组", node_system: int = 1):
        """
        一般支承边界信息
        Args:
           support_id: 一般支撑编号
           node_id: 节点号
           boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]  ture-固定 false-自由
           group_name: 边界组名称
           node_system: 0-整体  1-局部 (若节点未定义局部坐标系 则按照整体坐标计算)
        """
        self.support_id = support_id
        self.node_id = node_id
        self.boundary_info = boundary_info
        self.group_name = group_name
        self.node_system = node_system

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class ElasticLink:
    def __init__(self, link_id: int, link_type: int, start_id: int, end_id: int, beta_angle: float = 0,
                 boundary_info: tuple[float, float, float, float, float, float] = None,
                 group_name: str = "默认边界组", dis_ratio: float = 0, kx: float = 0):
        """
        弹性连接信息
        Args:
            link_id: 弹性连接编号
            link_type: 弹性连接类型 1-一般弹性连接 2-刚性连接 3-受拉弹性连接 4-受压弹性连接
            start_id:起始节点号
            end_id:终节点号
            beta_angle:贝塔角
            boundary_info:边界信息
            group_name:边界组名
            dis_ratio:距i端距离比 (仅一般弹性连接需要)
            kx:受拉或受压刚度
        """
        self.link_id = link_id
        self.link_type = link_type
        self.start_id = start_id
        self.end_id = end_id
        self.beta_angle = beta_angle
        self.boundary_info = boundary_info
        self.group_name = group_name
        self.dis_ratio = dis_ratio
        self.kx = kx

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class ElasticSupport:
    def __init__(self, support_id: int, node_id: int, support_type: int, boundary_info: tuple[float, float, float, float, float, float] = None,
                 group_name: str = "默认边界组", node_system: int = 1):
        """
        Args:
            support_id:弹性支承编号
            node_id:节点编号
            support_type:支承类型 1-线性  2-受拉  3-受压
            boundary_info:边界信息 受拉和受压时列表长度为1  线性时列表长度为6
            group_name:边界组
        """
        self.support_id = support_id
        self.node_id = node_id
        self.support_type = support_type
        self.boundary_info = boundary_info
        self.group_name = group_name
        self.node_system = node_system

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class MasterSlaveLink:
    def __init__(self, link_id: int, master_id: int, slave_id: int,
                 boundary_info: tuple[bool, bool, bool, bool, bool, bool] = None, group_name: str = "默认边界组"):
        """
        Args:
            link_id:主从连接号
            master_id:主节点号
            slave_id:从节点号
            boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
            group_name:边界组
        """
        self.link_id = link_id
        self.master_id = master_id
        self.slave_id = slave_id
        self.boundary_info = boundary_info
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class ConstraintEquation:
    def __init__(self, constraint_id: int, name: str, sec_node: int, sec_dof: int = 1,
                 master_info: list[tuple[int, int, float]] = None, group_name: str = "默认边界组"):
        """
        Args:
            constraint_id: 约束方程编号
            name:约束方程名
            sec_node:从节点号
            sec_dof: 从节点自由度 1-x 2-y 3-z 4-rx 5-ry 6-rz
            master_info:主节点约束信息列表
            group_name:边界组名
        """
        self.constraint_id = constraint_id
        self.name = name
        self.sec_node = sec_node
        self.sec_dof = sec_dof
        self.master_info = master_info
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class BeamConstraint:
    def __init__(self, constraint_id: int, beam_id: int, info_i: tuple[bool, bool, bool, bool, bool, bool] = None,
                 info_j: tuple[bool, bool, bool, bool, bool, bool] = None, group_name: str = "默认边界组"):
        """
        梁端约束信息
        Args:
            constraint_id:梁端约束编号
            beam_id:梁单元号
            info_i:i端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
            info_j:j端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
            group_name:边界组名
        """
        self.constraint_id = constraint_id
        self.beam_id = beam_id
        self.info_i = info_i
        self.info_j = info_j
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class NodalLocalAxis:
    def __init__(self, node_id: int, vector_x: tuple[float, float, float] = None, vector_y: tuple[float, float, float] = None):
        """
        节点局部坐标系
        Args:
            node_id:节点编号
            vector_x:节点局部坐标X方向向量
            vector_y:节点局部坐标Y方向向量
        """
        self.node_id = node_id
        self.vector_x = vector_x
        self.vector_y = vector_y

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class PreStressLoad:
    def __init__(self, case_name: str, tendon_name: str, tension_type: int, force: float, group_name: str = "默认荷载组"):
        """
        预应力荷载
        Args:
            case_name: 荷载工况名
            tendon_name:钢束名称
            tension_type:0-始端 1-末端 2-两端
            force:节点局部坐标Y方向向量
            group_name: 荷载组名称
        """
        self.case_name = case_name
        self.tendon_name = tendon_name
        self.tension_type = tension_type
        self.force = force
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class NodalMass:
    def __init__(self, node_id: int, mass_info: tuple[float, float, float, float] = None):
        """
        节点质量
        Args:
            node_id:节点编号
            mass_info:[m,rmX,rmY,rmZ]
        """
        self.node_id = node_id
        self.mass_info = mass_info

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class NodalForce:
    def __init__(self, node_id: int, case_name: str, load_info: tuple[float, float, float, float, float, float] = None, group_name: str = "默认荷载组"):
        """
        节点质量
        Args:
            node_id:节点编号
            case_name:荷载工况名
            load_info:荷载信息列表 [Fx,Fy,Fz,Mx,My,Mz]
            group_name:荷载组名
        """
        self.node_id = node_id
        self.case_name = case_name
        self.load_info = load_info
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class NodalForceDisplacement:
    def __init__(self, node_id: int = 1, case_name: str = "", load_info: tuple[float, float, float, float, float, float] = None,
                 group_name: str = "默认荷载组"):
        """
        节点位移信息
        Args:
            node_id:节点编号
            case_name:荷载工况名
            load_info:节点位移列表 [Dx,Dy,Dz,Rx,Ry,Rz]
            group_name:荷载组名
        """
        self.node_id = node_id
        self.case_name = case_name
        self.load_info = load_info
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class BeamElementLoad:
    def __init__(self, beam_id: int, case_name: str, load_type: int, coord_system: int,
                 list_x: list[float, float] = None,
                 list_load: list[float, float] = None, group_name="默认荷载组",
                 load_bias: tuple[bool, int, int, float] = None, projected: bool = False):
        """
        节点位移信息
        Args:
            beam_id:梁单元号
            case_name:荷载工况名
            load_type:荷载类型  1-集中力 2-集中弯矩 3-分布弯矩 4-分布弯矩
            coord_system: 1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z
            list_x:位置信息列表
            list_load:荷载信息列表
            group_name:荷载组名
            load_bias:偏心荷载 (是否偏心,0-中心 1-偏心,偏心坐标系-int,偏心距离)
            projected:荷载是否投影
        """
        self.beam_id = beam_id
        self.case_name = case_name
        self.load_type = load_type
        self.coord_system = coord_system
        self.list_x = list_x
        self.list_load = list_load
        self.group_name = group_name
        self.load_bias = load_bias
        self.projected = projected

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class PlateElementLoad:
    def __init__(self, element_id: int, case_name: str, load_type: int, load_place: int, coord_system: int,
                 group_name: str = "默认荷载组", load_list: list[float] = None, xy_list: tuple[float, float] = None):
        """
        板单元荷载
        Args:
            element_id:单元id
            case_name:荷载工况名
            load_type:荷载类型
               _1-集中力  2-集中弯矩  3-分布力  4-分布弯矩_
            load_place:荷载位置
               _0-面IJKL 1-边IJ  2-边JK  3-边KL  4-边LI  (仅分布荷载需要)_
            coord_system:坐标系  (默认3)
               _1-整体坐标X  2-整体坐标Y 3-整体坐标Z  4-局部坐标X  5-局部坐标Y  6-局部坐标Z_
            group_name:荷载组名
            load_list:荷载列表
            xy_list:荷载位置信息 [IJ方向绝对距离x,IL方向绝对距离y]  (仅集中荷载需要)
        """
        self.element_id = element_id
        self.case_name = case_name
        self.load_type = load_type
        self.load_place = load_place
        self.coord_system = coord_system
        self.group_name = group_name
        self.load_list = load_list
        self.xy_list = xy_list

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class DeviationParameter:
    def __init__(self, name: str, element_type: int = 1, parameters: list[float] = None):
        """
        制造偏差参数
        Args:
            name:名称
            element_type:单元类型  1-梁单元  2-板单元
            parameters:参数列表
                    _梁杆单元:[轴向,I端X向转角,I端Y向转角,I端Z向转角,J端X向转角,J端Y向转角,J端Z向转角]_
                    _板单元:[X向位移,Y向位移,Z向位移,X向转角,Y向转角]_
        """
        self.name = name
        self.element_type = element_type
        self.parameters = parameters

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class DeviationLoad:
    def __init__(self, element_id: int = 1, case_name: str = "", parameters: list[str] = None, group_name: str = "默认荷载组"):
        """
        Args:
            element_id:单元编号
            case_name:荷载工况名
            parameters:参数名列表
                _梁杆单元时-[制造误差参数名称]_
                _板单元时-[I端误差名,J端误差名,K端误差名,L端误差名]_
            group_name:荷载组名
        """
        self.element_id = element_id
        self.case_name = case_name
        self.parameters = parameters
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class ElementTemperature:
    def __init__(self, element_id: int = 1, case_name: str = "", temperature: float = 1, group_name: str = "默认荷载组"):
        """
        单元温度
        Args:
            element_id:单元编号
            case_name:荷载工况名
            temperature:最终温度
            group_name:荷载组名
        """
        self.element_id = element_id
        self.case_name = case_name
        self.temperature = temperature
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class GradientTemperature:
    def __init__(self, element_id: int, case_name: str, temperature: float, section_oriental: int = 1,
                 element_type: int = 1, group_name: str = "默认荷载组"):
        """
        添加梯度温度
        Args:
             element_id:单元编号
             case_name:荷载工况名
             temperature:温差
             section_oriental:截面方向 (仅梁单元需要) 1-截面Y向(默认)  2-截面Z向
             element_type:单元类型 1-梁单元(默认)  2-板单元
             group_name:荷载组名
        """
        self.element_id = element_id
        self.case_name = case_name
        self.temperature = temperature
        self.section_oriental = section_oriental
        self.element_type = element_type
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class BeamSectionTemperature:
    def __init__(self, element_id: int, case_name: str, paving_thick: float, temperature_type: int = 1,
                 paving_type: int = 1, group_name: str = "默认荷载组", modify: bool = False, temp_list: tuple[float, float] = None):
        """
        梁截面温度
        Args:
            element_id:单元编号
            case_name:荷载工况名
            paving_thick:铺设厚度(m)
            temperature_type:温度类型  1-升温(默认) 2-降温
            paving_type:铺设类型 1-沥青混凝土(默认)  2-水泥混凝土
            group_name:荷载组名
            modify:是否修改规范温度
            temp_list:温度列表[T1,T2]  (仅修改时需要)
        """
        self.element_id = element_id
        self.case_name = case_name
        self.paving_thick = paving_thick
        self.temperature_type = temperature_type
        self.paving_type = paving_type
        self.modify = modify
        self.temp_list = temp_list
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class IndexTemperature:
    def __init__(self, element_id: int, case_name: str, temperature: float = 0, index: float = 1, group_name: str = "默认荷载组"):
        """
        指数温度
        Args:
            element_id:单元编号
            case_name:荷载工况名
            temperature:温差
            index:指数
            group_name:荷载组名
        """
        self.element_id = element_id
        self.case_name = case_name
        self.temperature = temperature
        self.index = index
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()


class TopPlateTemperature:
    def __init__(self, element_id: int, case_name: str, temperature: float = 0, group_name: str = "默认荷载组"):
        """
        顶板温度
        Args:
            element_id:单元编号
            case_name:荷载工况名
            temperature:温差
            group_name:荷载组名
        """
        self.element_id = element_id
        self.case_name = case_name
        self.temperature = temperature
        self.group_name = group_name

    def __str__(self):
        attrs = vars(self)
        dict_str = '{' + ', '.join(f"'{k}': {v}" for k, v in attrs.items()) + '}'
        return dict_str

    def __repr__(self):
        return self.__str__()

