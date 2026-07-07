"""캡스톤: AEB 종방향 시뮬레이터 스켈레톤.

구성 (전부 직접 구현):
- Vehicle: 위치 s, 속도 v, dt마다 갱신 (종방향만, Week3 모델 단순화)
- ttc(gap, rel_v): 상대속도가 접근 방향일 때만 유한값
- AEBController: ttc < threshold 이면 최대감속(-9.8*mu) 명령
- simulate(tc): 하나의 Test Case dict를 받아 시계열 dict 반환
- 충돌 판정: gap <= 0

검증 아이디어: 등속 접근 시 해석해(정지거리 v^2/2a)와 시뮬레이션 정지거리 비교.
"""
# TODO: Day 3~4에 구현
