"""과제 2: 이동평균 필터 — 실차 시험 데이터 후처리의 기본기.

요구사항:
1. t = 0~10s (0.01s 간격), 신호 = sin(t) + 가우시안 노이즈(std=0.3)
2. 윈도우 크기 N의 이동평균 필터를 "직접" 구현 (np.convolve 금지, for문 허용)
3. N=5, 20, 50 세 경우를 원본과 함께 한 그래프에 플롯
4. N이 커질 때 지연(lag)이 생기는 이유를 주석으로 3줄 설명 <- 시험 데이터 분석 면접 단골
"""
import numpy as np
import matplotlib.pyplot as plt

def moving_average(x: np.ndarray, n: int) -> np.ndarray:
    # TODO: 직접 구현
    raise NotImplementedError

if __name__ == "__main__":
    pass  # TODO
