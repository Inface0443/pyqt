class OdbModel:
    """
    用于获取模型信息
    """
    @staticmethod
    def get_deviation_load(case_name: str):
        """
        获取指定荷载工况的制造偏差荷载
        Args:
            case_name:荷载工况名
        Example:
            odb.get_deviation_load(case_name="荷载工况1")
        Returns: 包含信息为list[dict]
        """
        try:
            res_list = []
            # beam_list_load = qt_model.GetBeamDeviationLoadData(case_name)
            # for item in beam_list_load:
            #     res_list.append(DeviationLoad(item.Element.Id, case_name=case_name,
            #                                   parameters=[item.BeamDeviationParameter.Name],
            #                                   group_name=item.LoadGroup.Name).__str__())
            # plate_list_load = qt_model.GetPlateDeviationLoadData(case_name)
            # for item in plate_list_load:
            #     res_list.append(DeviationLoad(item.Element.Id, case_name=case_name,
            #                                   parameters=[item.PlateDeviation[0].Name, item.PlateDeviation[0].Name,
            #                                               item.PlateDeviation[2].Name,
            #                                               item.PlateDeviation[3].Name]).__str__())
            return res_list
        except Exception as ex:
            raise Exception(ex)