# 참고 자료

## 하드웨어 실습
- 라즈베리파이 gpiozero 공식 문서 — GPIO/센서 제어
- HC-SR04 데이터시트, 아두이노 `pulseIn` / `NewPing` 라이브러리
- MCP2515 라이브러리: coryjfowler/MCP_CAN_lib (GitHub) — 아두이노 CAN
- 라즈베리파이 MCP2515 설정: `dtoverlay=mcp2515-can0` (config.txt), 크리스털 주파수 확인 필수
- can-utils: candump, cansend, cangen, canplayer — 리눅스 CAN 표준 도구(실무 그대로)
- python-can / cantools 공식 문서

## 차량보안 + 임베디드 (동아리 핵심)
- The Car Hacker's Handbook (무료 공개, opengarages.org) — CAN/UDS/보안 표준 입문서
- ICSim (GitHub: zombieCraig/ICSim) — 실물 없이도 vcan으로 스니핑/인젝션 연습(WSL2/리눅스)
- ISO/SAE 21434 개요 — TARA 개념 (원문 유료, 개요 강의/블로그로)
- UDS(ISO 14229) 진단 프로토콜 개요 — 제어기 검증 실무 필수
- SecOC(보안 온보드 통신) 개념 — 메시지 인증으로 스푸핑 방어

## 코딩
- 점프 투 파이썬(위키독스, 무료), 모두의 코드 "씹어먹는 C"
- 코드업(codeup.kr) 기초 100제, 프로그래머스 코딩테스트 연습
- 백준(acmicpc.net) — 2026.4 종료 후 데이원컴퍼니 인수로 부활 예정, 정상화 시 최우선

## 차량/ADAS 도메인
- SAE J3016 자율주행 레벨 정의
- Euro NCAP AEB Car-to-Car 시험 프로토콜(무료 PDF) — 실제 시험이 어떻게 생겼나
- ISO 26262 / ISO 21448(SOTIF) 개요 강의

## 다음 단계
- STM32 Nucleo + HAL bxCAN — 양산 ECU에 더 가까운 임베디드
- MATLAB/Simulink Onramp(학생 무료) — 공고 dSPACE/Simulink 대응
- 자율주행/임베디드/보안 경진대회
