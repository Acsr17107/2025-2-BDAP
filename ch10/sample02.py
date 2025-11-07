import pandas as pd
import os

def get_population(file_path):

    try:
        df = pd.read_csv(file_path)
        index_df = df.set_index('date')

        population = index_df['population'].iat[0]
        return population

    except FileNotFoundError:
        print(f" 파일을 찾을 수 없습니다: {file_path}")
        return None
    except KeyError:
        print(f"️ 파일에 'date' 또는 'population' 열이 없습니다: {file_path}")
        return None
    except Exception as e:
        print(f" 데이터 처리 중 문제가 발생했습니다: {e}")
        return None


# --- 1. 파일 경로 설정 ---

# sample02.py에서 사용된 대한민국 데이터 파일 경로
kor_file_path = '../ch05/data/covid_korea.csv'

# sample01 (1).py를 실행했을 때 생성되는 하와이 데이터 파일 경로
# 이 스크립트 실행 전 sample01.py가 먼저 실행되어
# 'hi_covid_data.csv' 파일이 생성되어 있어야 함.
hi_file_path = './hi_covid_data.csv'

# --- 2. 로직 실행 및 결과 출력
print("데이터 추출을 시작합니다...")

kor_population = get_population(kor_file_path)
hi_population = get_population(hi_file_path)

print('-' * 50)
if kor_population is not None:
    print(f'대한민국 인구수: {kor_population:,.0f} 명')

if hi_population is not None:
    print(f'하와이 인구수: {hi_population:,.0f} 명')
print('-' * 50)

# --- 3. 인구 비율 계산
if kor_population is not None and hi_population is not None:
    rate = kor_population / hi_population
    print(f' 대한민국/하와이 인구 비율: {rate:.2f} 배')
else:
    print("인구수 정보를 모두 가져오지 못해 비율 계산을 생략.")