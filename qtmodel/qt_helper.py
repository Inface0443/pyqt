# 第三方调用示例
# import requests
#
#
# class PostQt:
#     @staticmethod
#     def post_file(file_path: str, url: str = "http://localhost:55125/pythonForQt/"):
#         response = requests.post(url, headers={'Content-Type': 'PyFile'}, data=file_path.encode('utf-8'))
#         if response.status_code == 200:
#             print(response.text)
#         elif response.status_code == 400:
#             raise Exception(response.text)
#         else:
#             raise Exception("连接错误，请重新尝试")
#
#     @staticmethod
#     def post_command(command: str, url: str = "http://localhost:55125/pythonForQt/"):
#         response = requests.post(url, headers={'Content-Type': 'Python'}, data=command.encode('utf-8'))
#         if response.status_code == 200:
#             print(response.text)
#         elif response.status_code == 400:
#             raise Exception(response.text)
#         else:
#             raise Exception("连接错误，请重新尝试")
#
#
# PostQt.post_file(r"D:\FilePath.py")


class QtHelper:
    """
    用于辅助建模
    """

    @staticmethod
    def parse_number_string(input_string: str):
        """
        将类似”1to5by2 11 13to18“的字符串转为list<int>型变量
        Args:
            input_string:传入字符串，字符串各部分用空格分开
        Returns:
            list[int]
        """
        if not input_string.strip():
            return None

        if input_string == 'nan':
            return None

        string_list = input_string.split(" ")
        ids = []
        for str_ids in string_list:
            if "to" in str_ids:
                range_parts = str_ids.split("to")
                if "by" in range_parts[1]:
                    range_parts = range_parts[1].split("by")

                start = end = step = 0
                if range_parts[0].isdigit() and range_parts[1].isdigit():
                    start = int(range_parts[0])
                    end = int(range_parts[1])
                if len(range_parts) > 2 and range_parts[2].isdigit():
                    step = int(range_parts[2])
                else:
                    step = 1
                ids += [start + n * step for n in range((end - start) // step + 1)]
            else:
                ids.append(int(str_ids))
        return ids
