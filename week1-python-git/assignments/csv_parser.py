"""과제 1: pandas 없이 CSV 파서 만들기.

요구사항:
1. sample.csv (직접 만들 것: time,speed,accel 3열 x 50행)를 open()으로 읽는다
2. 각 숫자 열의 최소/최대/평균을 계산해 출력한다
3. 잘못된 행(빈 줄, 숫자 아님)은 건너뛰고 몇 행을 건너뛰었는지 출력한다

금지: pandas, csv 모듈. 오직 open(), split(), float()만.
"""

def parse_csv(path: str) -> dict:
    # TODO: 여기를 직접 구현
    raise NotImplementedError

if __name__ == "__main__":
    stats = parse_csv("sample.csv")
    print(stats)
