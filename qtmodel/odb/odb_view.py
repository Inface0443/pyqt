class OdbView:
    """
    用于调整模型视图获取模型视图信息
    """
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
        try:
            # qt_model.DisplayNodeId(showId=show_id)
            pass
        except Exception as ex:
            raise Exception(ex)