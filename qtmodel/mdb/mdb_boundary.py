import json
from ..core.qt_server import QtServer
from .data_helper import MdbDataHelper
from typing import Union


class MdbBoundary:
    """
    用于边界操作
    """

    # region 边界操作
    @staticmethod
    def add_effective_width(element_ids, factor_i: float, factor_j: float, dz_i: float, dz_j: float,
                            group_name: str = "默认边界组"):
        """
        添加有效宽度系数
        Args:
           element_ids:边界单元号支持整形和整形列表且支持XtoYbyN形式
           factor_i:I端截面Iy折减系数
           factor_j:J端截面Iy折减系数
           dz_i:I端截面形心变换量
           dz_j:J端截面形心变换量
           group_name:边界组名
        Example:
           mdb.add_effective_width(element_ids=[1,2,3,4],factor_i=0.1,factor_j=0.1,dz_i=0.1,dz_j=0.1)
           mdb.add_effective_width(element_ids="1to4",factor_i=0.1,factor_j=0.1,dz_i=0.1,dz_j=0.1)
        Returns: 无
        """
        try:
            if isinstance(element_ids, list):
                id_str = MdbDataHelper.parse_int_list_to_str(element_ids)
            else:
                id_str = str(element_ids)
            s = "*EFCFACTOR\r\n" + f"{id_str},{factor_i},{factor_j},{dz_i},{dz_j},{group_name}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

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
        try:
            s = "*BNDRGROUP\r\n" + f"{name}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_general_elastic_support_property(name: str = "", data_matrix: list[float] = None):
        """
        添加一般弹性支承特性
        Args:
            name:一般弹性支承特性名称
            data_matrix:一般弹性支承刚度矩阵(数据需按列输入至列表,共计21个参数)
        Example:
            mdb.add_general_elastic_support_property(name = "特性1", data_matrix=[i for i in range(1,22)])
        Returns: 无
        """
        if data_matrix is None or len(data_matrix) != 21:
            raise Exception("添加一般弹性支承失败,矩阵参数有误(数据需按列输入至列表)")
        try:
            s = "*GSPRTYPE\r\n" + f"{name}," + ",".join(f"{x:g}" for x in data_matrix) + "\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

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
        try:
            if isinstance(node_id, list):
                id_str = MdbDataHelper.parse_int_list_to_str(node_id)
            else:
                id_str = str(node_id)
            s = "*GSPRING\r\n" + f"{id_str},{property_name},{group_name}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_general_support(node_id: Union[int, str, list[int]] = 1, boundary_info: list[bool] = None,
                            group_name: str = "默认边界组"):
        """
        添加一般支承
        Args:
             node_id:节点编号,支持整数或整数型列表且支持XtoYbyN形式字符串
             boundary_info:边界信息  [X,Y,Z,Rx,Ry,Rz]  ture-固定 false-自由
             group_name:边界组名,默认为默认边界组
        Example:
            mdb.add_general_support(node_id=1, boundary_info=[True,True,True,False,False,False])
            mdb.add_general_support(node_id="1to100", boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        try:
            if boundary_info is None or len(boundary_info) != 6:
                raise Exception("操作错误，要求输入一般支承列表长度为6")
            if isinstance(node_id, list):
                id_str = MdbDataHelper.parse_int_list_to_str(node_id)
            else:
                id_str = str(node_id)
            s = "*GSUPPORT\r\n" + f"{id_str}," + "".join(str(int(x)) for x in boundary_info) + f",{group_name}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_elastic_support(node_id: Union[int, str, list[int]] = 1, support_type: int = 1,
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
        try:
            if isinstance(node_id, list):
                id_str = MdbDataHelper.parse_int_list_to_str(node_id)
            else:
                id_str = str(node_id)
            s = "*ESUPPORT\r\n" + f"{id_str},"
            if support_type == 1 and (boundary_info is None or len(boundary_info) != 6):
                raise Exception("操作错误，要求输入弹性支承边界信息长度为6")
            elif support_type in (2, 3) and (boundary_info is None or len(boundary_info) != 2):
                raise Exception("操作错误，要求输入弹性支承边界信息长度为2")
            else:
                s += f"{support_type},{group_name}," + ",".join(f"{x:g}" for x in boundary_info) + "\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

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
        try:
            # type_mapping = {
            #     1: "GEN",
            #     2: "RIGID",
            #     3: "TENS",
            #     4: "COMP"
            # }
            # s = "*ELINK\r\n" + f"{type_mapping.get(link_type, 'UNKNOWN')},{start_id},{end_id},{beta_angle:g},{group_name}"
            # if link_type==1:
            #     s += ","+",".join(f"{x:g}" for x in boundary_info) + f",{dis_ratio:g}" + "\r\n"
            # elif link_type==2:
            #     s += "\r\n"
            # elif link_type in (3,4):
            #     s += f",{kx:g}" + "\r\n"
            # print(s)
            # QtServer.post_command(s, "QDAT")
            params = {
                "version": QtServer.QT_VERSION,  # 版本控制
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
            json_string = json.dumps(params, indent=2)
            QtServer.get_command(header="ADD-ELASTIC-LINK", command=json_string)
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_master_slave_links(node_ids: list[tuple[int, int]] = None, boundary_info: list[bool] = None,
                               group_name: str = "默认边界组"):
        """
        批量添加主从约束，不指定编号默认为最大编号加1
        Args:
             node_ids:主节点号和从节点号，主节点号位于首位
             boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             group_name:边界组名
        Example:
            mdb.add_master_slave_links(node_ids=[(1,2),(1,3),(4,5),(4,6)],boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        try:
            s = "*MSLINK\r\n"
            # 按照主节点分组
            master_slave_dict = {}
            for master_id, slave_id in node_ids:
                if master_id not in master_slave_dict:
                    master_slave_dict[master_id] = []
                master_slave_dict[master_id].append(slave_id)
            for master_id, slave_ids in master_slave_dict.items():
                ids_str = MdbDataHelper.parse_int_list_to_str(slave_ids)
                s += f"{master_id},{ids_str}," + "".join(str(int(x)) for x in boundary_info) + f",{group_name}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_master_slave_link(master_id: int = 1, slave_id=None,
                              boundary_info: list[bool] = None, group_name: str = "默认边界组"):
        """
        添加主从约束
        Args:
             master_id:主节点号
             slave_id:从节点号，支持整数或整数型列表且支持XtoYbyN形式字符串
             boundary_info:边界信息 [X,Y,Z,Rx,Ry,Rz] ture-固定 false-自由
             group_name:边界组名
        Example:
            mdb.add_master_slave_link(master_id=1,slave_id=[2,3],boundary_info=[True,True,True,False,False,False])
            mdb.add_master_slave_link(master_id=1,slave_id="2to3",boundary_info=[True,True,True,False,False,False])
        Returns: 无
        """
        try:
            if isinstance(slave_id, list):
                id_str = MdbDataHelper.parse_int_list_to_str(slave_id)
            else:
                id_str = str(slave_id)
            s = "*MSLINK\r\n" + f"{master_id},{id_str}," + "".join(
                str(int(x)) for x in boundary_info) + f",{group_name}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_beam_constraint(beam_id: int = 2, info_i: list[bool] = None, info_j: list[bool] = None,
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
        try:
            if info_i is None or len(info_i) != 6:
                raise Exception("操作错误，要求输入I端约束列表长度为6")
            if info_j is None or len(info_j) != 6:
                raise Exception("操作错误，要求输入J端约束列表长度为6")
            s = "*RESTRAINTS\r\n" + f"{beam_id}," + "".join(str(int(x)) for x in info_i) + "," + "".join(
                str(int(y)) for y in info_j) + f",{group_name}\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

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
        try:
            s = "*EQUATION\r\n" + f"{name},{group_name},{sec_node},{sec_dof}," + ",".join(
                f"{tuples}" for tuples in master_info) + "\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_node_axis(node_id: int = 1, input_type: int = 1, coord_info: list = None):
        """
        添加节点坐标
        Args:
             node_id:节点号
             input_type:输入方式 1-角度 2-三点  3-向量
             coord_info:局部坐标信息 -List<float>(角)  -List<List<float>>(三点 or 向量)
        Example:
            mdb.add_node_axis(input_type=1,node_id=1,coord_info=[45,45,45])
            mdb.add_node_axis(input_type=2,node_id=1,coord_info=[[0,0,1],[0,1,0],[1,0,0]])
            mdb.add_node_axis(input_type=3,node_id=1,coord_info=[[0,0,1],[0,1,0]])
        Returns: 无
        """
        try:
            s = "*LOCALAXIS\r\n" + f"{node_id},"
            if coord_info is None:
                raise Exception("操作错误，输入坐标系信息不能为空")
            tran_info = coord_info
            if input_type == 1:
                tran_info = MdbDataHelper.convert_angle_to_vectors(coord_info)
            elif input_type == 2:
                tran_info = MdbDataHelper.convert_three_points_to_vectors(coord_info)
            s += f"V1({','.join(f'{axis:g}' for axis in tran_info[0])}),V2({','.join(f'{axis:g}' for axis in tran_info[1])})\r\n"
            print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            pass
            raise Exception(ex)

    @staticmethod
    def remove_elastic_link(index: int = 1):
        """
        根据弹性连接号删除弹性连接
        Args:
             index:弹性连接号
        Example:
            mdb.remove_elastic_link(index=1)
        Returns: 无
        """
        # todo
        pass

    @staticmethod
    def update_elastic_link(index: int = 1, link_type: int = 1, start_id: int = 1, end_id: int = 2,
                            beta_angle: float = 0,
                            boundary_info: list[float] = None,
                            group_name: str = "默认边界组", dis_ratio: float = 0.5, kx: float = 0):
        """
        更新弹性连接，根据指定的index
        Args:
            index:弹性连接号
            link_type:节点类型 1-一般弹性连接 2-刚性连接 3-受拉弹性连接 4-受压弹性连接
            start_id:起始节点号
            end_id:终节点号
            beta_angle:贝塔角
            boundary_info:边界信息
            group_name:边界组名
            dis_ratio:距i端距离比 (仅一般弹性连接需要)
            kx:受拉或受压刚度
        Example:
            mdb.update_elastic_link(index=1,link_type=1,start_id=1,end_id=2,boundary_info=[1e6,1e6,1e6,0,0,0])
            mdb.update_elastic_link(index=2,link_type=2,start_id=1,end_id=2)
            mdb.update_elastic_link(index=3,link_type=3,start_id=1,end_id=2,kx=1e6)
        Returns: 无
        """
        # todo
        pass
    # region
