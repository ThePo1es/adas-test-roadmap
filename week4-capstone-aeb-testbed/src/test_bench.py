"""캡스톤 시험 벤치 (라즈베리파이, python-can).

역할:
- can0에서 전 프레임 수신·타임스탬프 로깅
- 거리 프레임(ID 0x100) 디코딩, AEB 제동 프레임(ID 0x200 가정) 관측
- 반응시간 = (거리 임계 최초 통과 시각) ~ (제동 프레임 최초 관측 시각)
- 로그를 CSV로 저장

준비: sudo ip link set can0 up type can bitrate 500000
      pip install python-can cantools
실패 주의: 비트레이트/크리스털 불일치 시 수신 0. can0 down 상태면 예외.
"""
# import can
# TODO: 직접 구현
