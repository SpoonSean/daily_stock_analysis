import sys
import os

# 把当前目录加入Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 直接导入你原项目的 Web 启动
from main import app

# 给 uwsgi 使用
application = app