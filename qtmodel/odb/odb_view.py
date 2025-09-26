from qtmodel.core import QtServer


class OdbView:
    """
    用于调整模型视图获取模型视图信息
    """

    # region 视图控制

    @staticmethod
    def display_node_id(show_id: bool = True):
        """
        设置节点号显示
        Args:
            show_id:是否打开节点号显示
        Example:
            odb.display_node_id()
            odb.display_node_id(False)
        Returns: 无
        """
        payload = {
            "show_id": show_id,
        }
        return QtServer.send_post("DISPLAY-NODE-ID", payload)

    @staticmethod
    def display_element_id(show_id: bool = True):
        """
        设置单元号显示
        Args:
            show_id:是否打开单元号显示
        Example:
            odb.display_element_id()
            odb.display_element_id(False)
        Returns: 无
        """
        payload = {
            "show_id": show_id,
        }
        return QtServer.send_post("DISPLAY-ELEMENT-ID", payload)

    @staticmethod
    def set_view_camera(
            camera_point: tuple[float, float, float],
            focus_point: tuple[float, float, float],
            camera_rotate: tuple[float, float, float] = (45, 45, 0),
            scale: float = 0.5
    ):
        """
        更改三维显示相机设置
        Args:
            camera_point: 相机坐标点
            focus_point: 相机焦点
            camera_rotate:相机绕XYZ旋转角度
            scale: 缩放系数
        Example:
           odb.set_view_camera(camera_point=(-100,-100,100),focus_point=(0,0,0))
        Returns: 无
        """
        direction = [
            camera_point[0], camera_point[1], camera_point[2],
            focus_point[0], focus_point[1], focus_point[2],
            camera_rotate[0], camera_rotate[1], camera_rotate[2],
            scale
        ]
        payload = {
            "direction": direction
        }
        return QtServer.send_post("SET-VIEW-CAMERA", payload)

    @staticmethod
    def set_view_direction(
            direction: int = 1,
            horizontal_degree: float = 0,
            vertical_degree: float = 0,
            scale: float = 1
    ):
        """
        更改三维显示默认视图
        Args:
            direction: 1-空间视图1 2-前视图 3-三维视图2 4-左视图  5-顶视图 6-右视图 7-空间视图3 8-后视图 9-空间视图4 10-底视图
            horizontal_degree:水平向旋转角度
            vertical_degree:竖向旋转角度
            scale:缩放系数
        Example:
           odb.set_view_direction(direction=1,scale=1.2)
        Returns: 无
        """
        payload = {
            "direction": direction,
            "horizontal_degree": horizontal_degree,
            "vertical_degree": vertical_degree,
            "scale": scale
        }
        return QtServer.send_post("SET-VIEW-DIRECTION", payload)

    @staticmethod
    def activate_structure(node_ids=None, element_ids=None):
        """
        激活指定阶段和单元,默认激活所有
        Args:
            node_ids: 节点集合支持XtoYbyN形式字符串
            element_ids: 单元集合支持XtoYbyN形式字符串
        Example:
           odb.activate_structure(node_ids=[1,2,3],element_ids=[1,2,3])
        Returns: 无
        """
        payload = {}
        if node_ids is not None:
            payload["node_ids"] = node_ids
        if element_ids is not None:
            payload["element_ids"] = element_ids

        return QtServer.send_post(
            "ACTIVATE-STRUCTURE",
            payload if payload else None  # 两者都空则只发 Header
        )

    @staticmethod
    def set_unit(unit_force: str = "KN", unit_length: str = "MM"):
        """
        修改视图显示时单位制,不影响建模
        Args:
            unit_force: 支持 N KN TONF KIPS LBF
            unit_length: 支持 M MM CM IN FT
        Example:
           odb.set_unit(unit_force="N",unit_length="M")
        Returns: 无
        """
        payload = {
            "unit_force": unit_force,
            "unit_length": unit_length
        }
        return QtServer.send_post("SET-UNIT", payload)

    @staticmethod
    def remove_display():
        """
        删除当前所有显示,包括边界荷载钢束等全部显示
        Args: 无
        Example:
           odb.remove_display()
        Returns: 无
        """
        return QtServer.send_post("DISPLAY-RESET", None)

    @staticmethod
    def save_png(file_path: str):
        """
        保存当前模型窗口图形信息
        Args:
            file_path: 文件全路径
        Example:
           odb.save_png(file_path=r"D:\\QT\\aa.png")
        Returns: 无
        """
        payload = {
            "file_path": file_path
        }
        return QtServer.send_post("SAVE-PNG", payload)

    @staticmethod
    def set_render(flag: bool = True):
        """
        消隐设置开关
        Args:
            flag: 默认设置打开消隐
        Example:
           odb.set_render(flag=True)
        Returns: 无
        """
        payload = {
            "flag": flag
        }
        return QtServer.send_post("SET-RENDER", payload)

    @staticmethod
    def change_construct_stage(stage: int = 0):
        """
        消隐设置开关
        Args:
            stage: 施工阶段名称或施工阶段号  0-基本
        Example:
           odb.change_construct_stage(0)
           odb.change_construct_stage(stage=1)
        Returns: 无
        """
        payload = {
            "stage": stage
        }
        return QtServer.send_post("CHANGE-STAGE", payload)
    # endregion
