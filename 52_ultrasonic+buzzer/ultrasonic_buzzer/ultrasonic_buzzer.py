# ******************************************************************************************
# * FileName     : ultrasonic_buzzer
# * Description  : 초음파센서와 부저를 사용하여 초음파센서로 물체의 거리를 측정하고
# *                물체와 거리가 가까워지면 부저를 이용하여 소리로 알림
# * Author       : 이승찬
# * Created Date : 2021.08.18
# * Reference    :
# * Modified     :
# ******************************************************************************************


# import
import time
from machine import Pin, time_pulse_us
from ETboard.lib.pin_define import *


# global variable
trigPin = Pin(D9)                                   # 초음파 송신부
echoPin = Pin(D8)                                   # 초음파 수신 부

PinD2 = Pin(D2)


# setup
def setup():
    # LED 출력모드 설정
    trigPin.init(Pin.OUT)
    echoPin.init(Pin.IN)
    PinD2.init(Pin.OUT)                             # 부저를 출력모드로 설정


# main loop
def loop():
    # 초음파 송신 후 수신부는 HIGH 상태로 대기
    trigPin.value(LOW)
    echoPin.value(LOW)
    time.sleep_ms(2)
    trigPin.value(HIGH)
    time.sleep_ms(10)
    trigPin.value(LOW)
    
    # echoPin 이 HIGH 를 유지한 시간 저장
    duration = time_pulse_us(echoPin, HIGH)
    # HIGH 였을 때 시간(초음파 송수신 시간)을 기준으로 거리를 계산
    distance = ((17 * duration) / 1000)
    
    # 초음파센서 값을 출력
    print(distance, " cm ")                        # 거리를 화면에 출력해줌
    time.sleep_ms(100)                             # 0.1초 대기
    
    # 초음파센서 값에 따라 부저 제어
    if distance < 15:                              # 거리가 10cm 미만이면
        for i in range(80):
            PinD2.value(HIGH)     
            time.sleep(0.001)        
            PinD2.value(LOW)      
            time.sleep(0.001)


if __name__ == "__main__":
    setup()
    while True:
        loop()

# ==========================================================================================
#
#  (주)한국공학기술연구원 http://et.ketri.re.kr
#
# ==========================================================================================
