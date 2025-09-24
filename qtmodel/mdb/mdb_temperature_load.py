from ..core.qt_server import QtServer
from typing import Union, List
from .data_helper import MdbDataHelper


class MdbTemperatureLoad:

    # region 温度与制造偏差荷载
    @staticmethod
    def add_deviation_parameter(name: str = "",  parameters: list[float] = None):
        """
        添加制造误差
        Args:
            name:名称
            parameters:参数列表
                _梁杆单元为[轴向,I端X向转角,I端Y向转角,I端Z向转角,J端X向转角,J端Y向转角,J端Z向转角]
                _板单元为[X向位移,Y向位移,Z向位移,X向转角,Y向转角]
        Example:
            mdb.add_deviation_parameter(name="梁端制造误差",parameters=[1,0,0,0,0,0,0])
            mdb.add_deviation_parameter(name="板端制造误差",parameters=[1,0,0,0,0])
        Returns: 无
        """
        try:
            if parameters is None:
                raise Exception("操作错误，制造误差信息不能为空")
            if len(parameters) != 7 and len(parameters) != 5 :
                raise Exception("操作错误，制造误差信息数量有误，请核查数据")
            s = "*DEVPARAM\r\n" + f"{name},{','.join(f'{x:g}' for x in parameters)}" + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_deviation_load(element_id, case_name: str = "",
                           parameters: (Union[str, List[str]]) = None, group_name: str = "默认荷载组"):
        """
        添加制造误差荷载
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            parameters:参数名列表
                _梁杆单元为制造误差参数名称
                _板单元为[I端误差名,J端误差名,K端误差名,L端误差名]
            group_name:荷载组名
        Example:
            mdb.add_deviation_load(element_id=1,case_name="工况1",parameters="梁端误差")
            mdb.add_deviation_load(element_id=2,case_name="工况1",parameters=["板端误差1","板端误差2","板端误差3","板端误差4"])
        Returns: 无
        """
        try:
            if parameters is None:
                raise Exception("操作错误，制造误差名称信息不能为空")
            if element_id is None:
                id_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                id_str = MdbDataHelper.parse_int_list_to_str(element_id)
            else:
                id_str = str(element_id)
            s = "*DEVLOAD\r\n" + f"{id_str},{case_name},{group_name},"
            if isinstance(parameters, str):
                s += f"{parameters}\r\n"
            elif isinstance(parameters, list):
                s += ",".join(f"{s}" for s in parameters) + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_custom_temperature(element_id, case_name: str = "", group_name: str = "默认荷载组",
                               orientation: int = 1, temperature_data: List[tuple[int, float, float]] = None):
        """
        添加梁自定义温度
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            group_name:指定荷载组,后续升级开放指定荷载组删除功能
            orientation: 1-局部坐标z 2-局部坐标y
            temperature_data:自定义数据[(参考位置1-顶 2-底,高度,温度)...]
        Example:
            mdb.add_custom_temperature(case_name="荷载工况1",element_id=1,orientation=1,temperature_data=[(1,1,20),(1,2,10)])
        Returns: 无
        """
        try:
            if element_id is None:
                id_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                id_str = MdbDataHelper.parse_int_list_to_str(element_id)
            else:
                id_str = str(element_id)
            s = "*USER-TEMP\r\n" + f"{id_str},{case_name},{group_name},{orientation},"
            s += ",".join(f"({','.join(f'{x:g}' for x in data)})" for data in temperature_data) + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_element_temperature(element_id, case_name: str = "", temperature: float = 1,
                                group_name: str = "默认荷载组"):
        """
        添加单元温度
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            temperature:最终温度
            group_name:荷载组名
        Example:
            mdb.add_element_temperature(element_id=1,case_name="自重",temperature=1,group_name="默认荷载组")
        Returns: 无
        """
        try:
            if element_id is None:
                id_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                id_str = MdbDataHelper.parse_int_list_to_str(element_id)
            else:
                id_str = str(element_id)
            s = "*ELE-TEMP\r\n" + f"{id_str},{case_name},{group_name},{temperature:g}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_system_temperature(case_name: str = "", temperature: float = 1, group_name: str = "默认荷载组"):
        """
        添加系统温度
        Args:
            case_name:荷载工况名
            temperature:最终温度
            group_name:荷载组名
        Example:
            mdb.add_system_temperature(case_name="荷载工况",temperature=20,group_name="默认荷载组")
        Returns: 无
        """
        try:
            s = "*SYSTEM-TEMP\r\n" + f"{case_name},{group_name},{temperature:g}\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_gradient_temperature(element_id, case_name: str = "",
                                 temperature: float = 1, section_oriental: int = 1,
                                 element_type: int = 1, group_name: str = "默认荷载组"):
        """
        添加梯度温度
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            temperature:温差
            section_oriental:截面方向,默认截面Y向 (仅梁单元需要, 0-截面Y向  1-截面Z向)
            element_type:单元类型,默认为梁单元 (1-梁单元  2-板单元)
            group_name:荷载组名
        Example:
            mdb.add_gradient_temperature(element_id=1,case_name="荷载工况1",group_name="荷载组名1",temperature=10)
            mdb.add_gradient_temperature(element_id=2,case_name="荷载工况2",group_name="荷载组名2",temperature=10,element_type=2)
        Returns: 无
        """
        try:
            s = ""
            if element_id is None:
                id_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                id_str = MdbDataHelper.parse_int_list_to_str(element_id)
            else:
                id_str = str(element_id)
            if element_type == 1:  # 1-梁单元
                s = "*BEAMGRD-TEMP\r\n" + f"{id_str},{case_name},{group_name},{section_oriental},{temperature:g}" + "\r\n"
            elif element_type == 2:  # 2-板单元
                s = "*PLATEGRD-TEMP\r\n" + f"{id_str},{case_name},{group_name},{temperature:g}" + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_beam_section_temperature(element_id=1, case_name: str = "", code_index: int = 1,
                                     sec_type: int = 1, t1: float = 0, t2: float = 0, t3: float = 0,
                                     t4: float = 0, thick: float = 0, group_name: str = "默认荷载组"):
        """
        添加梁截面温度
        Args:
            element_id:单元编号，支持整数或整数型列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            code_index:规范编号  (1-公路规范2015  2-美规2017)
            sec_type:截面类型(1-混凝土 2-组合梁)
            t1:温度1
            t2:温度2
            t3:温度3
            t4:温度4
            thick:厚度
            group_name:荷载组名
        Example:
            mdb.add_beam_section_temperature(element_id=1,case_name="工况1",code_index=1,sec_type=1,t1=-4.2,t2=-1)
        Returns: 无
        """
        try:
            if element_id is None:
                id_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                id_str = MdbDataHelper.parse_int_list_to_str(element_id)
            else:
                id_str = str(element_id)
            s = "*SEC-TEMP\r\n" + f"{id_str},{case_name},{group_name},{code_index},{sec_type},{t1:g},{t2:g},{t3:g},{t4:g},{thick:g}" + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_index_temperature(element_id=None, case_name: str = "", temperature: float = 0, index: float = 1,
                              group_name: str = "默认荷载组"):
        """
        添加指数温度
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            temperature:温差
            index:指数
            group_name:荷载组名
        Example:
            mdb.add_index_temperature(element_id=1,case_name="工况1",temperature=20,index=2)
        Returns: 无
        """
        try:
            if element_id is None:
                id_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                id_str = MdbDataHelper.parse_int_list_to_str(element_id)
            else:
                id_str = str(element_id)
            tem_dir = 1  # 目前仅支持截面高度方向温度加载
            s = "*INDEX-TEMP\r\n" + f"{id_str},{case_name},{group_name},{tem_dir},{temperature:g},{index:g}" + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    @staticmethod
    def add_top_plate_temperature(element_id, case_name: str = "", temperature: float = 0,
                                  group_name: str = "默认荷载组"):
        """
        添加顶板温度
        Args:
             element_id:单元编号
             case_name:荷载
             temperature:温差，最终温度于初始温度之差
             group_name:荷载组名
        Example:
            mdb.add_top_plate_temperature(element_id=1,case_name="工况1",temperature=40,group_name="默认荷载组")
        Returns: 无
        """
        try:
            if element_id is None:
                id_str = ""
            elif isinstance(element_id, list):  # 列表转化为XtoYbyN
                id_str = MdbDataHelper.parse_int_list_to_str(element_id)
            else:
                id_str = str(element_id)
            s = "*TOPPLATE-TEMP\r\n" + f"{id_str},{case_name},{group_name},{temperature:g}" + "\r\n"
            # print(s)
            QtServer.post_command(s, "QDAT")
        except Exception as ex:
            raise Exception(ex)

    # endregion
