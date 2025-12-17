from qtmodel.core.qt_server import QtServer
from qtmodel.core.data_helper import QtDataHelper
from typing import Union, List, Tuple


class MdbBoundary:
    """
    用于边界操作
    """

    # region 边界操作
    @staticmethod
    def add_effective_width(element_ids, factor_i: float, factor_j: float, dz_i: float, dz_j: float,
                            group_name: str = "默认边界组",factor_i_z: float = 0,factor_j_z: float = 0,
                            dy_i: float = 0, dy_j: float = 0,factor_i_ax: float = 0,factor_j_ax: float = 0):
        """
        添加有效宽度系数
        Args:
           element_ids:边界单元号支持整形和整形列表且支持XtoYbyN形式
           factor_i:I端截面Iy折减系数
           factor_j:J端截面Iy折减系数
           dz_i:I端截面形心变换量
           dz_j:J端截面形心变换量
           factor_i_z:J端截面形心变换量
           factor_j_z:J端截面形心变换量
           dy_i:J端截面形心变换量
           dy_j:J端截面形心变换量
           factor_i_ax:J端截面形心变换量
           factor_j_ax:J端截面形心变换量
           group_name:边界组名
        Example:
           mdb.add_effective_width(element_ids=[1,2,3,4],factor_i=0.1,factor_j=0.1,dz_i=0.1,dz_j=0.1)
           mdb.add_effective_width(element_ids="1to4",factor_i=0.1,factor_j=0.1,dz_i=0.1,dz_j=0.1)
        Returns: 无
        """
        payload = {
            "element_ids": QtDataHelper.parse_ids_to_array(element_ids),
            "factor_i": float(factor_i),
            "factor_j": float(factor_j),
            "dz_i": float(dz_i),
            "dz_j": float(dz_j),
            "group_name": group_name,

            "factor_i_z": float(factor_i_z),
            "factor_j_z": float(factor_j_z),
            "dy_i": float(dy_i),
            "dy_j": float(dy_j),
            "factor_i_ax": float(factor_i_ax),
            "factor_j_ax": float(factor_j_ax),
        }
        return QtServer.send_dict("ADD-EFFECTIVE-WIDTH", payload)

    @staticmethod
    def add_boundary_group(name: str = ""):
        """
        新建边界组
        Args:
            name:边界组名
        Example:
            mdb.add_boundary_group(name="边界组1")
        Returns: 无
        """
        payload = {
            "name": name,
        }
        return QtServer.send_dict("ADD-BOUNDARY-GROUP", payload)

    @staticmethod
    def add_general_elastic_support_property(name: str = "", data_matrix: list[float] = None):
        """
        添加一般弹性支承特性，默认单位为N,m
        Args:
            name:一般弹性支承特性名称，支持覆盖添加
            data_matrix:一般弹性支承刚度矩阵(数据需按列输入至列表,共计21个参数)
        Example:
            mdb.add_general_elastic_support_property(name = "特性1", data_matrix=[i for i in range(1,22)])
        Returns: 无
        """
        payload = {
            "name": name,
            "data_matrix": data_matrix,
        }
        return QtServer.send_dict("ADD-GENERAL-ELASTIC-SUPPORT-PROPERTY", payload)

    @staticmethod
    def add_general_elastic_support(node_id=None, property_name: str = "", group_name: str = "默认边界组"):
        """
        添加一般弹性支承特性
        Args:
            node_id:节点号,支持整数或整数型列表且支持XtoYbyN形式字符串
            property_name:一般弹性支承特性名
            group_name:一般弹性支承边界组名
        Example:
            mdb.add_general_elastic_support(node_id=1, property_name = "特性1",group_name="边界组1")
        Returns: 无
        """
        payload = {
            "node_id": QtDataHelper.parse_ids_to_array(node_id),
            "property_name": property_name,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-GENERAL-ELASTIC-SUPPORT", payload)

    @staticmethod
    def add_general_support(node_id: Union[int, str, list[int]] = 1, boundary_info: Union[list[bool], list[int]] = None,
                            group_name: str = "默认边界组"):
        """
        添加一般支承
        Args:
             node_id:节点编号,支持整数或整数型列表且支持XtoYbyN形式字符串
             boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]  ture-固定 false-自由,也可传数值列表(0-自由 1-固定)
             group_name:边界组名,默认为默认边界组
        Example:
            mdb.add_general_support(node_id=1, boundary_info=[True,True,True,False,False,False])
            mdb.add_general_support(node_id="1to100", boundary_info=[True,True,True,False,False,False])
            mdb.add_general_support(node_id="1to100", boundary_info=[1,1,1,0,0,0])
        Returns: 无
        """
        if boundary_info is None:
            boundary_info = [1, 1, 1, 0, 0, 0]
        boundary_info_norm = [True if x>0.5 else False for x in boundary_info]
        payload = {
            "node_id": QtDataHelper.parse_ids_to_array(node_id),
            "boundary_info": boundary_info_norm,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-GENERAL-SUPPORT", payload)


    @staticmethod
    def add_elastic_support(node_id, support_type: int = 1,
                            boundary_info: list[float] = None, group_name: str = "默认边界组"):
        """
        添加弹性支承
        Args:
             node_id:节点编号,支持数或列表且支持XtoYbyN形式字符串
             support_type:支承类型 1-线性  2-受拉  3-受压
             boundary_info:边界信息 受拉和受压时列表长度为2-[direct(1-X 2-Y 3-Z),stiffness]  线性时列表长度为6-[kx,ky,kz,krx,kry,krz]
             group_name:边界组
        Example:
            mdb.add_elastic_support(node_id=1,support_type=1,boundary_info=[1e6,0,1e6,0,0,0])
            mdb.add_elastic_support(node_id=1,support_type=2,boundary_info=[1,1e6])
            mdb.add_elastic_support(node_id=1,support_type=3,boundary_info=[1,1e6])
        Returns: 无
        """
        if boundary_info is None:
            boundary_info = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        boundary_info = [float(x) for x in boundary_info]
        payload = {
            "node_id": QtDataHelper.parse_ids_to_array(node_id),
            "support_type": support_type,
            "boundary_info": boundary_info,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-ELASTIC-SUPPORT", payload)


    @staticmethod
    def add_elastic_link(index: int = -1, link_type: int = 1, start_id: int = 1, end_id: int = 2, beta_angle: float = 0,
                         boundary_info: list[float] = None,
                         group_name: str = "默认边界组", dis_ratio: float = 0.5, kx: float = 0):
        """
        添加弹性连接，建议指定index(弹性连接编号)
        Args:
            index:弹性连接编号,默认自动识别
            link_type:节点类型 1-一般弹性连接 2-刚性连接 3-受拉弹性连接 4-受压弹性连接
            start_id:起始节点号
            end_id:终节点号
            beta_angle:贝塔角
            boundary_info:边界信息
            group_name:边界组名
            dis_ratio:距i端距离比 (仅一般弹性连接需要)
            kx:受拉或受压刚度
        Example:
            mdb.add_elastic_link(link_type=1,start_id=1,end_id=2,boundary_info=[1e6,1e6,1e6,0,0,0])
            mdb.add_elastic_link(link_type=2,start_id=1,end_id=2)
            mdb.add_elastic_link(link_type=3,start_id=1,end_id=2,kx=1e6)
        Returns: 无
        """
        if boundary_info is None:
            boundary_info = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        boundary_info = [float(x) for x in boundary_info]

        payload = {
            "index": index,
            "link_type": link_type,
            "start_id": start_id,
            "end_id": end_id,
            "beta_angle": beta_angle,
            "boundary_info": boundary_info,
            "group_name": group_name,
            "dis_ratio": dis_ratio,
            "kx": kx,
        }
        return QtServer.send_dict("ADD-ELASTIC-LINK", payload)

    @staticmethod
    def add_master_slave_links(node_ids: List[Tuple[int, int]] = None,
                               boundary_info: List[bool] = None,
                               group_name: str = "默认边界组"):
        """
        添加多个主节点对应的主从约束
        Args:
            node_ids: [(masterNodeId, slaveNodeId), ...]
            boundary_info: 约束自由度列表 [Ux, Uy, Uz, Rx, Ry, Rz]，True=约束/耦合，False=不约束
            group_name: 边界组名
        Example:
            mdb.add_master_slave_links(node_ids=[(1,2),(3,4)], boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        if boundary_info is None:
            boundary_info = [True, True, True, True, True, True]
        if len(boundary_info) != 6:
            raise ValueError("主从约束边界信息有误，请核查边界数据")
        if node_ids is None:
            raise ValueError("主从约束节点有误，请核查主从节点数据列表")
        payload = {
            "node_ids": node_ids,
            "boundary_info": boundary_info,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-MASTER-SLAVE-LINKS", payload)

    @staticmethod
    def add_master_slave_link(master_id: int, slave_id: Union[int, str, List[int]] = None,
                              boundary_info: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加单个主节点对应的主从约束
        Args:
             master_id:主节点号
             slave_id:从节点号，支持整数或整数型列表且支持XtoYbyN形式字符串
             boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由 默认全部固定
             group_name:边界组名
        Example:
            mdb.add_master_slave_link(master_id=1,slave_id=[2,3],boundary_info=[True,True,True,False,False,False])
            mdb.add_master_slave_link(master_id=1,slave_id="2to3",boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        if boundary_info is None:
            boundary_info = [True,True,True,True,True,True]
        if len(boundary_info) != 6:
            raise ValueError("主从约束边界信息有误，请核查边界数据")
        payload = {
            "master_id": int(master_id),
            "slave_id": QtDataHelper.parse_ids_to_array(slave_id),
            "boundary_info": boundary_info,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-MASTER-SLAVE-LINK", payload)

    @staticmethod
    def add_beam_constraint(beam_id: int, info_i: list[bool] = None, info_j: list[bool] = None,
                            group_name: str = "默认边界组"):
        """
        添加梁端约束
        Args:
             beam_id:梁号
             info_i:i端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             info_j:j端约束信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             group_name:边界组名
        Example:
            mdb.add_beam_constraint(beam_id=2,info_i=[True,True,True,False,False,False],info_j=[True,True,True,False,False,False])
        Returns: 无
        """
        if info_i is None:
            info_i = [False, False, False, False, False, False]
        if info_j is None:
            info_j = [False, False, False, False, False, False]
        payload = {
            "beam_id": int(beam_id),
            "info_i": list(info_i),
            "info_j": list(info_j),
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-BEAM-CONSTRAINT", payload)

    @staticmethod
    def add_constraint_equation(name: str, sec_node: int, sec_dof: int = 1,
                                master_info: list[tuple[int, int, float]] = None, group_name: str = "默认边界组"):
        """
        添加约束方程
        Args:
             name:约束方程名
             sec_node:从节点号
             sec_dof: 从节点自由度 1-x 2-y 3-z 4-rx 5-ry 6-rz
             master_info:主节点约束信息列表
             group_name:边界组名
        Example:
            mdb.add_beam_constraint(beam_id=2,info_i=[True,True,True,False,False,False],info_j=[True,True,True,False,False,False])
        Returns: 无
        """
        if master_info is None:
            master_info = []
        master_list = [[int(n), int(d), float(k)] for (n, d, k) in master_info]
        payload = {
            "name": name,
            "sec_node": int(sec_node),
            "sec_dof": int(sec_dof),
            "master_info": master_list,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-CONSTRAINT-EQUATION", payload)

    @staticmethod
    def add_node_axis(node_id: int, input_type: int = 1, coord_info: list[list[float]] = None,angle_info:tuple[float,float,float]=None):
        """
        添加节点坐标
        Args:
             node_id:节点号
             input_type:输入方式 1-角度 2-三点  3-向量
             coord_info:局部坐标信息  -List<List<float>>(三点 or 向量)
             angle_info:角度信息
        Example:
            mdb.add_node_axis(input_type=1,node_id=1,angle_info=(45,45,45))
            mdb.add_node_axis(input_type=2,node_id=1,coord_info=[[0,0,1],[0,1,0],[1,0,0]])
            mdb.add_node_axis(input_type=3,node_id=1,coord_info=[[0,0,1],[0,1,0]])
        Returns: 无
        """
        if coord_info is None:
            coord_info = []

        payload = {
            "node_id": int(node_id),
            "input_type": int(input_type),
            "coord_info": coord_info,
            "angle_info": angle_info,
        }
        return QtServer.send_dict("ADD-NODE-AXIS", payload)

    @staticmethod
    def update_boundary_group(name: str, new_name: str):
        """
        更改边界组名
        Args:
            name:边界组名
            new_name:新边界组名
        Example:
            mdb.update_boundary_group("旧边界组","新边界组")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-BOUNDARY-GROUP", payload)

    @staticmethod
    def update_node_axis_id(node_id: int, new_id: int):
        """
        更新节点局部坐标系编号（仅改编号，不改坐标系内容）
        Args:
            node_id: 原节点号（被更新的节点）
            new_id:  新节点号（更新后的节点号）
        Example:
            mdb.update_node_axis_id(node_id=10, new_id=20)
        Returns: 无
        """
        payload = {
            "node_id": int(node_id),
            "new_id": int(new_id),
        }
        return QtServer.send_dict("UPDATE-NODE-AXIS-ID", payload)

    @staticmethod
    def update_general_elastic_support_property_name(name: str, new_name: str):
        """
        更新一般弹性支承特性名称（仅改名）
        Args:
            name: 原特性名
            new_name: 新特性名
        Example:
            mdb.update_general_elastic_support_property_name(name="特性1", new_name="特性2")
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
        }
        return QtServer.send_dict("UPDATE-GENERAL-ELASTIC-SUPPORT-PROPERTY-NAME", payload)

    @staticmethod
    def remove_effective_width(element_ids, group_name: str = "默认边界组"):
        """
        删除有效宽度系数
        Args:
           element_ids:边界单元号支持整形和整形列表且支持XtoYbyN形式
           group_name:边界组名
        Example:
           mdb.remove_effective_width(element_ids=[1,2,3,4],group_name="边界组1")
           mdb.remove_effective_width(element_ids="1to4",group_name="边界组1")
        Returns: 无
        """
        payload = {
            "element_ids": element_ids,
            "group_name": group_name,
        }
        return QtServer.send_dict("REMOVE-EFFECTIVE-WIDTH", payload)



    @staticmethod
    def remove_boundary_group(name: str = ""):
        """
        按照名称删除边界组
        Args:
            name: 边界组名称，默认删除所有边界组 (非必须参数)
        Example:
            mdb.remove_boundary_group()
            mdb.remove_boundary_group(name="边界组1")
        Returns: 无
        """
        # 为空表示删除所有
        payload = {"name": name} if name else None
        return QtServer.send_dict("REMOVE-BOUNDARY-GROUP", payload)

    @staticmethod
    def remove_all_boundary():
        """
        根据边界组名称、边界的类型和编号删除边界信息,默认时删除所有边界信息
        Args:无
        Example:
            mdb.remove_all_boundary()
        Returns: 无
        """
        return QtServer.send_dict("REMOVE-ALL-BOUNDARY", None)

    @staticmethod
    def remove_boundary(remove_id: int, kind: str, group_name: str = "默认边界组", extra_name="I"):
        """
        根据节点号删除一般支撑、弹性支承/根据弹性连接I或J端(需指定)节点号删除弹性连接/根据单元号删除梁端约束/根据从节点号和约束方程名删除约束方程/根据从节点号删除主从约束
        Args:
            remove_id:节点号 or 单元号  or 从节点号
            kind:边界类型  ["一般支承", "弹性支承","一般弹性支承", "主从约束", "一般/受拉/受压/刚性弹性连接", "约束方程", "梁端约束"]
            group_name:边界所处边界组名
            extra_name:删除弹性连接或约束方程时额外标识,约束方程名或指定删除弹性连接节点类型 I/J
        Example:
            mdb.remove_boundary(remove_id=11, kind="一般弹性连接",group_name="边界组1", extra_name="J")
            mdb.remove_boundary(remove_id=12, kind="约束方程",group_name="边界组1", extra_name="约束方程名")
        Returns: 无
        """
        payload = {
            "remove_id": remove_id,
            "kind": kind,
            "group_name": group_name,
            "extra_name": extra_name,
        }
        return QtServer.send_dict("REMOVE-BOUNDARY", payload)

    @staticmethod
    def remove_general_elastic_support_property(name: str = ""):
        """
        添加一般弹性支承特性
        Args:
            name:一般弹性支承特性名称
        Example:
            mdb.remove_general_elastic_support_property(name = "特性1")
        Returns: 无
        """
        payload = {"name": name}
        return QtServer.send_dict("REMOVE-GENERAL-ELASTIC-SUPPORT-PROPERTY", payload)

    @staticmethod
    def remove_node_axis(node_id: int=-1):
        """
        删除节点局部坐标
        Args:
             node_id:节点号，不为正数时则删除所有节点局部坐标
        Example:
            mdb.remove_node_axis(node_id=1)
        Returns: 无
        """
        payload = {"node_id": node_id}
        return QtServer.send_dict("REMOVE-NODE-AXIS", payload)
    # region
