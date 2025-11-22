import pandas as pd
import matplotlib.pyplot as plt
import platform  # 운영체제(OS) 확인을 위한 모듈
from matplotlib import rc  # 폰트 설정을 위한 모듈

# ========================================================
# 1. 한글 폰트 설정 (시각화 시 글자 깨짐 방지)
# ========================================================
# 현재 실행 중인 운영체제 이름을 가져옵니다. (Windows, Darwin(Mac), Linux 등)
system_name = platform.system()

if system_name == 'Windows':
    # 윈도우의 경우 기본 한글 폰트인 '맑은 고딕' 설정
    rc('font', family='Malgun Gothic')
elif system_name == 'Darwin':
    # 맥(Mac)의 경우 '애플고딕' 설정
    rc('font', family='AppleGothic')
else:
    # 리눅스 등 그 외 OS일 경우 경고 메시지 출력 (나눔고딕 등 별도 설정 필요)
    print("Unknown System. 한글 폰트 설정이 필요합니다.")

# 마이너스 기호(-)가 깨지는 현상을 방지하기 위한 설정
# (한글 폰트 설정 시 마이너스가 네모로 나오는 경우가 많음)
plt.rcParams['axes.unicode_minus'] = False


# ========================================================
# 2. 데이터 로드 및 전처리
# ========================================================
file_name = '../ch11/survey_raw.csv'

try:
    # CSV 파일을 DataFrame으로 읽어옵니다.
    df_raw = pd.read_csv(file_name)
except FileNotFoundError:
    # 파일 경로가 틀렸을 경우 프로그램이 비정상 종료되지 않도록 예외 처리
    print(f"오류: '{file_name}' 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
    exit()

# [필터링] 'Age' 컬럼이 '35-44 years old'인 행만 추출
# .copy()를 사용하는 이유:
# Pandas에서 원본 데이터의 일부를 자를 때(Slicing), 이것이 원본의 '뷰(View)'인지 '복사본(Copy)'인지 모호할 때가 있습니다.
# 추후 데이터 가공 시 'SettingWithCopyWarning' 경고를 방지하기 위해 명시적으로 깊은 복사(Deep Copy)를 수행합니다.
df_target = df_raw[df_raw['Age'] == '35-44 years old'].copy()

# 분석할 타겟 컬럼 설정 (사용해본 프로그래밍 언어)
col_lang = 'LanguageHaveWorkedWith'

# [결측치 제거] 언어 데이터가 비어있는(NaN) 행은 분석에서 제외합니다.
data_lang = df_target[col_lang].dropna()

# [문자열 분리] 'Python;Java;C++' 형태의 문자열을 세미콜론(;) 기준으로 잘라 리스트로 변환합니다.
# 예: "Python;Java" -> ["Python", "Java"]
data_lang_split = data_lang.str.split(';')

# [데이터 펼치기 - 중요] 리스트에 담긴 요소를 각각의 행(Row)으로 분리합니다.
# 하나의 응답자가 여러 언어를 쓴 경우, 이를 개별 언어 카운트로 산정하기 위함입니다.
# 예: [1번 사람: ["Python", "Java"]] -> [1번 사람: "Python"], [1번 사람: "Java"] 로 2행이 됨
data_lang_exploded = data_lang_split.explode()


# ========================================================
# 3. 데이터 집계 및 상위 항목 추출
# ========================================================
# [빈도수 계산] 각 언어가 몇 번 등장했는지 셉니다. (내림차순 정렬되어 반환됨)
lang_counts = data_lang_exploded.value_counts()

# [Top 5 추출] 가장 빈도수가 높은 상위 5개 언어만 남깁니다.
top_5_languages = lang_counts.nlargest(5)

print('-'*50)
print(f"35-44세 개발자가 사용하는 언어 Top 5 (총 표본 수: {len(data_lang)}명)")
print(top_5_languages)
print('-'*50)


# ========================================================
# 4. 시각화 (파이 차트)
# ========================================================
plt.figure(figsize=(10, 10))  # 차트 크기 설정 (가로, 세로 인치 단위)

# 파이 차트 그리기
top_5_languages.plot.pie(
    autopct='%1.2f%%',       # 비율 표시 포맷 (소수점 둘째 자리까지 표시)
    startangle=90,           # 차트의 시작 각도를 90도(12시 방향)로 설정 (보기 좋게)
    counterclock=False,      # 시계 방향으로 데이터 배치 (기본값은 반시계 방향)
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