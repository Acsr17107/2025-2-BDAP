import pandas as pd
import matplotlib.pyplot as plt
import platform
from matplotlib import rc

# 1. 한글 폰트 설정 (시각화 시 글자 깨짐 방지)
system_name = platform.system()

if system_name == 'Windows':
    rc('font', family='Malgun Gothic')
else:
    print("Unknown System. 한글 폰트 설정이 필요.")

# 한글 폰트 설정
plt.rcParams['axes.unicode_minus'] = False


# 2. 데이터 로드 및 전처리
file_name = '../ch11/survey_raw.csv'

try:
    # CSV 파일을 DataFrame으로 읽음
    df_raw = pd.read_csv(file_name)
except FileNotFoundError:
    # 파일 경로가 틀렸을 경우 예외 처리
    print(f"오류: '{file_name}' 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
    exit()

# Age 컬럼이 35-44 years old인 행만 추출
df_target = df_raw[df_raw['Age'] == '35-44 years old'].copy()

# 분석할 타겟 설정
col_lang = 'LanguageHaveWorkedWith'

# 결측치 제거
data_lang = df_target[col_lang].dropna()

# 문자열 분리
data_lang_split = data_lang.str.split(';')

data_lang_exploded = data_lang_split.explode()


# 3. 데이터 집계 및 상위 항목 추출
# 빈도수 계산
lang_counts = data_lang_exploded.value_counts()

# Top 5 추출
top_5_languages = lang_counts.nlargest(5)

print('-'*50)
print(f"35-44세 개발자가 사용하는 언어 Top 5 (총 표본 수: {len(data_lang)}명)")
print(top_5_languages)
print('-'*50)


# 4. 시각화 (파이 차트)
plt.figure(figsize=(10, 10))  # 차트 크기 설정

# 파이 차트 그리기
top_5_languages.plot.pie(
    autopct='%1.2f%%',         # 비율 표시 포맷 (소수점 둘째 자리)
    startangle=90,             # 차트의 시작 각도를 90도로 설정
    counterclock=False,        # 시계 방향으로 데이터 배치
    textprops={'fontsize': 12} # 차트 내 글자 크기 설정
)

# 차트 제목
plt.title('35-44세 개발자가 가장 많이 사용하는 언어 Top 5', fontsize=15)

# y축 라벨 제거
plt.ylabel('')

# 요소들이 겹치지 않게 레이아웃 자동 조정
plt.tight_layout()

# 이미지 저장
save_path = './lang_data_35_44_korean.png'
plt.savefig(save_path)

print(f"차트가 '{save_path}' 경로에 저장되었습니다.")

# 차트 화면 출력
plt.show()