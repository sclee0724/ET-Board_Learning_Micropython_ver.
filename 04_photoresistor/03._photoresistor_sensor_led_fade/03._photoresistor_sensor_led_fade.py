# ******************************************************************************************
# FileName     : 03._photoresistor_sensor_led_fade
# Description  : 조도센서 값에 따라 빨강 LED의 밝기가 달라짐
#                조도센서 값 쉘에 출력
# Author       : 이승찬
# Created Date : 2021.08.13
# Reference    :
# Modified     :
# ******************************************************************************************


# import
import time
from machine import ADC, Pin, PWM
from ETboard.lib.pin_define import *


# global variable
sensor = ADC(Pin(A1))                             # 조도센서 핀 지정
PinD2 = Pin(D2)                                   # 빨강 LED 핀 지정

# setup
def setup():
    sensor.atten(ADC.ATTN_11DB)                   # 조도 센서 입력모드 설정
    PinD2.init(Pin.OUT)                           # 빨강 LED 출력모드 설정


# main loop
def loop():
    sensor_result = 1023 - sensor.read() / 3      # 조도 센서 값 저장
    print(sensor_result)                          # 조도센서 값 출력
    
    pwm2 = PWM(Pin(D2), 500, int(sensor_result))

    time.sleep(0.1)                               # 0.1초 기다리기


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
