# ******************************************************************************************
# * FileName     : 01._touch_sensor
# * Description  : 터치센서의 상태를 쉘에 출력
# * Author       : 이승찬
# * Created Date : 2021.08.18
# * Reference    :
# * Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin
from ETboard.lib.pin_define import *


# global variable
pt = Pin(D2)               # 터치센서 핀 지정


# setup
def setup():
    pt.init(Pin.IN)        # 터치센서 입력값 설정


# main loop
def loop():
    print(pt.value())      # 터치센서 값 출력
    time.sleep(0.1)        # 0.1초 대기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
