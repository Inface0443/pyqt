from qtmodel.core.qt_server import QtServer
from typing import Union, List
from qtmodel.core.data_helper import QtDataHelper


class MdbTemperatureLoad:
    """
    用于温度荷载和制作偏差模型操作
    """

    # region 温度与制造
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
        payload = {
            "element_id": QtDataHelper.parse_ids_to_array(element_id),
            "case_name": case_name,
            "group_name": group_name,
            "orientation": orientation,
            "temperature_data": temperature_data,
        }
        return QtServer.send_dict("ADD-CUSTOM-TEMPERATURE", payload)

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
        payload = {
            "element_id": QtDataHelper.parse_ids_to_array(element_id),
            "case_name": case_name,
            "temperature": temperature,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-ELEMENT-TEMPERATURE", payload)

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
        payload = {
            "case_name": case_name,
            "temperature": temperature,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-SYSTEM-TEMPERATURE", payload)

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
        payload = {
            "element_id": QtDataHelper.parse_ids_to_array(element_id),
            "case_name": case_name,
            "temperature": temperature,
            "section_oriental": section_oriental,
            "element_type": element_type,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-GRADIENT-TEMPERATURE", payload)

    @staticmethod
    def add_beam_section_temperature(element_id, case_name: str = "", code_index: int = 1,
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
        payload = {
            "element_id": QtDataHelper.parse_ids_to_array(element_id),
            "case_name": case_name,
            "code_index": code_index,
            "sec_type": sec_type,
            "t1": t1,
            "t2": t2,
            "t3": t3,
            "t4": t4,
            "thick": thick,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-BEAM-SECTION-TEMPERATURE", payload)

    @staticmethod
    def add_index_temperature(element_id, case_name: str = "", temperature: float = 0, index: float = 1,
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
        payload = {
            "element_id": QtDataHelper.parse_ids_to_array(element_id),
            "case_name": case_name,
            "temperature": temperature,
            "index": index,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-INDEX-TEMPERATURE", payload)

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
        payload = {
            "element_id": QtDataHelper.parse_ids_to_array(element_id),
            "case_name": case_name,
            "temperature": temperature,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-TOP-PLATE-TEMPERATURE", payload)

    @staticmethod
    def remove_element_temperature(element_id, case_name: str):
        """
        删除指定单元温度
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
        Example:
            mdb.remove_element_temperature(case_name="荷载工况1",element_id=1)
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "element_id": element_id,
        }
        return QtServer.send_dict("REMOVE-ELEMENT-TEMPERATURE", payload)

    @staticmethod
    def remove_top_plate_temperature(element_id, case_name: str):
        """
        删除梁单元顶板温度
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
        Example:
            mdb.remove_top_plate_temperature(case_name="荷载工况1",element_id=1)
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "element_id": element_id,
        }
        return QtServer.send_dict("REMOVE-TOP-PLATE-TEMPERATURE", payload)

    @staticmethod
    def remove_beam_section_temperature(element_id, case_name: str):
        """
        删除指定梁或板单元梁截面温度
        Args:
            case_name:荷载工况名
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
        Example:
            mdb.remove_beam_section_temperature(case_name="工况1",element_id=1)
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "element_id": element_id,
        }
        return QtServer.send_dict("REMOVE-BEAM-SECTION-TEMPERATURE", payload)

    @staticmethod
    def remove_gradient_temperature(element_id, case_name: str):
        """
        删除梁或板单元梯度温度
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
        Example:
            mdb.remove_gradient_temperature(case_name="工况1",element_id=1)
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "element_id": element_id,
        }
        return QtServer.send_dict("REMOVE-GRADIENT-TEMPERATURE", payload)

    @staticmethod
    def remove_custom_temperature(element_id, case_name: str):
        """
        删除梁单元自定义温度
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
        Example:
            mdb.remove_custom_temperature(case_name="工况1",element_id=1)
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "element_id": element_id,
        }
        return QtServer.send_dict("REMOVE-CUSTOM-TEMPERATURE", payload)

    @staticmethod
    def remove_index_temperature(element_id, case_name: str):
        """
        删除梁单元指数温度且支持XtoYbyN形式字符串
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
        Example:
            mdb.remove_index_temperature(case_name="工况1",element_id=1)
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "element_id": element_id,
        }
        return QtServer.send_dict("REMOVE-INDEX-TEMPERATURE", payload)

    # endregion

    # region 偏差荷载
    @staticmethod
    def add_deviation_parameter(name: str = "", parameters: list[float] = None):
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
        if parameters is None:
            raise ValueError("输入参数有误，请核查制造偏差参数")
        payload = {
            "name": name,
            "parameters": parameters,
        }
        return QtServer.send_dict("ADD-DEVIATION-PARAMETER", payload)

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
        if isinstance(parameters, str):
            param_list = [parameters] if parameters else []
        else:
            param_list = parameters

        payload = {
            "element_id": QtDataHelper.parse_ids_to_array(element_id),
            "case_name": case_name,
            "parameters": param_list,
            "group_name": group_name,
        }
        return QtServer.send_dict("ADD-DEVIATION-LOAD", payload)

    @staticmethod
    def update_deviation_parameter(name: str = "", new_name: str = "", element_type: int = 1, parameters: list[float] = None):
        """
        更新制造误差参数
        Args:
            name:名称
            new_name:新名称，默认不修改名称
            element_type:单元类型  1-梁单元  2-板单元
            parameters:参数列表
                 _梁杆单元为[轴向,I端X向转角,I端Y向转角,I端Z向转角,J端X向转角,J端Y向转角,J端Z向转角]
                _板单元为[X向位移,Y向位移,Z向位移,X向转角,Y向转角]
        Example:
            mdb.update_deviation_parameter(name="梁端制造误差",element_type=1,parameters=[1,0,0,0,0,0,0])
            mdb.update_deviation_parameter(name="板端制造误差",element_type=1,parameters=[1,0,0,0,0])
        Returns: 无
        """
        payload = {
            "name": name,
            "new_name": new_name,
            "element_type": element_type,
            "parameters": parameters,
        }
        return QtServer.send_dict("UPDATE-DEVIATION-PARAMETER", payload)

    @staticmethod
    def remove_deviation_parameter(name: str, para_type: int = 1):
        """
        删除指定制造偏差参数
        Args:
            name:制造偏差参数名
            para_type:制造偏差类型 1-梁单元  2-板单元
        Example:
            mdb.remove_deviation_parameter(name="参数1",para_type=1)
        Returns: 无
        """
        payload = {
            "name": name,
            "para_type": para_type,
        }
        return QtServer.send_dict("REMOVE-DEVIATION-PARAMETER", payload)

    @staticmethod
    def remove_deviation_load(element_id, case_name: str, group_name: str = "默认荷载组"):
        """
        删除指定制造偏差荷载
        Args:
            element_id:单元编号，支持数或列表且支持XtoYbyN形式字符串
            case_name:荷载工况名
            group_name: 荷载组
        Example:
            mdb.remove_deviation_load(case_name="工况1",element_id=1,group_name="荷载组1")
        Returns: 无
        """
        payload = {
            "case_name": case_name,
            "element_id": element_id,
            "group_name": group_name,
        }
        return QtServer.send_dict("REMOVE-DEVIATION-LOAD", payload)

    # endregion
