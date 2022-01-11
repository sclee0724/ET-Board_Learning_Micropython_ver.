# ******************************************************************************************
# FileName     : 01._temperature_sensor
# Description  : 온도 센서 값 쉘에 출력
# Author       : 이승찬
# Created Date : 2021.08.17
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import ADC, Pin
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A2))                  # 온도센서 핀 지정


# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)        # 온도센서 입력모드 설정


# main loop
def loop():
    sensor_result = sensor.read()      # 온도 센서 값 저장
    print(sensor_result)               # 온도 센서 값 출력
    
    time.sleep(0.1)                    # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
