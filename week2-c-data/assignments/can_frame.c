/* 과제: CAN 프레임 신호 추출 — 실차 시험에서 매일 하는 일의 축소판.
 *
 * CAN 메시지는 8바이트(64비트) 데이터에 여러 신호가 비트 단위로 packed 되어 있다.
 * 아래 가상의 프레임에서:
 *   - 차속: byte0~1 (16bit, little-endian), scale 0.01 km/h
 *   - RPM : byte2~3 (16bit, little-endian), scale 0.25
 *   - 기어: byte4의 하위 4bit (0=P,1=R,2=N,3=D)
 * 를 추출해 물리값으로 출력하라. 비트연산(<<, |, &)만 사용.
 */
#include <stdio.h>
#include <stdint.h>

int main(void) {
    uint8_t frame[8] = {0x10, 0x27, 0xA0, 0x0F, 0x03, 0x00, 0x00, 0x00};
    /* 기대 출력: speed = 100.00 km/h, rpm = 1000.0, gear = D */

    // TODO: 여기를 직접 구현
    return 0;
}
