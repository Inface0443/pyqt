# -*- coding: utf-8 -*-
from datetime import datetime
from setuptools import setup, find_packages

# 读取文件内容
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
"""
git config --global --get http.proxy
set http_proxy=
set https_proxy=
python setup.py sdist
twine upload dist/*
"""


setup(
    name="qtmodel",
    version=f"V2.2.1",
    author="dqy-zhj",
    author_email="1105417715@qq.com",
    description=f"python modeling for qt {datetime.now().date()} ",
    long_description=long_description,  # 使用读取的 README.md 文件内容
    long_description_content_type="text/markdown",  # 指明内容格式为markdown
    url="https://github.com/Inface0443/pyqt",
    packages=find_packages(include=['qtmodel', 'qtmodel.*']),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
)
