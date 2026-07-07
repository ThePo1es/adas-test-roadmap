"""과제: Kinematic Bicycle Model 구현.

상태: x, y, yaw(heading), v
입력: 가속도 a, 조향각 delta
갱신식 (dt마다):
    x += v * cos(yaw) * dt
    y += v * sin(yaw) * dt
    yaw += (v / L) * tan(delta) * dt
    v += a * dt

할 일:
1. 위 모델을 클래스로 구현 (L=2.7m, dt=0.01s)
2. v=10 m/s 유지, delta=5deg 고정 → 10초 궤적 플롯 (원이 나와야 정상)
3. 원의 반지름을 이론값 R = L/tan(delta) 와 비교해 검증  <- "시뮬레이션은 반드시 검증한다" 습관
"""
import numpy as np
import matplotlib.pyplot as plt

class BicycleModel:
    def __init__(self, wheelbase: float = 2.7, dt: float = 0.01):
        # TODO
        raise NotImplementedError

    def step(self, accel: float, steer: float):
        # TODO
        raise NotImplementedError

if __name__ == "__main__":
    pass  # TODO
