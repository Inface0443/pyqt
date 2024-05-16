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
