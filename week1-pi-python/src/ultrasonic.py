"""과제 1: HC-SR04 초음파 거리 측정 (라즈베리파이).

배선 주의: Echo(5V)를 Pi GPIO(3.3V)에 바로 넣지 말 것 -> 분압저항 필요.
  Echo --[1kΩ]--+--[2kΩ]--GND
                |
             GPIO(Echo핀)

요구사항:
1. gpiozero.DistanceSensor 사용 (trigger, echo 핀 지정)
2. 0.1초마다 거리(cm) 출력
3. 값이 튀므로 최근 5개 이동평균을 함께 출력  <- 실차 센서 후처리의 기본
"""
# from gpiozero import DistanceSensor
# from time import sleep

# TODO: 직접 구현 (핀 번호는 본인 배선에 맞게)
