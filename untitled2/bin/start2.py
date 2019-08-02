'''
2019/06/18
'''
import os, sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)
from lib.interface import server_sign
from conf.setting import SERVER_PORT

server_sign.run(host='0.0.0.0', port=SERVER_PORT, debug=True)
