import pandas as pd
import matplotlib.pyplot as plt
import platform

# 한글 폰트 설정

try:
    if platform.system() == 'Windows':
        font_name = 'Malgun Gothic'
    elif platform.system() == 'Darwin':
        font_name = 'AppleGothic'
    else:
        font_name = 'NanumGothic'

    plt.rcParams['font.family'] = font_name
    plt.rcParams['axes.unicode_minus'] = False

except Exception as e:
    print(f"한글 폰트 설정 중 오류 발생: {e}")
    print("차트의 한글이 깨질 수 있음. 폰트 설정을 확인.")
    pass

# 영문 국가명 -> 한글 국가명

country_translation_map = {
    'United States of America': '미국',
    'India': '인도',
    'Germany': '독일',
    'United Kingdom of Great Britain and Northern Ireland': '영국',
    'Canada': '캐나다',
    'France': '프랑스',
    'Brazil': '브라질',
    'Poland': '폴란드',
    'Netherlands': '네덜란드',
    'Australia': '호주',
    'Spain': '스페인',
    'Italy': '이탈리아',
    'Russian Federation': '러시아',
    'Ukraine': '우크라이나',
    'Sweden': '스웨덴',
    'Switzerland': '스위스',
    'Israel': '이스라엘',
    'Pakistan': '파키스탄',
    'China': '중국',
    'Japan': '일본',
    'South Korea': '대한민국',
    'Turkey': '터키 (튀르키예)',
    'Czech Republic': '체코',
    'Austria': '오스트리아',
    'Mexico': '멕시코',
    'Belgium': '벨기에',
    'Norway': '노르웨이',
    'Denmark': '덴마크',
    'Portugal': '포르투갈',
    'Romania': '루마니아',
    'Iran, Islamic Republic of...': '이란',
    'Other': '기타'
}

# 데이터 로드 및 처리

try:
    file_name = './survey_raw.csv'
    df_raw = pd.read_csv(file_name)

    COLUMN_COUNTRY = 'Country'

    # 국가별 응답자 수 집계
    size_by_country = df_raw[COLUMN_COUNTRY].value_counts()

    # 한글 라벨 적용

    size_by_country_korean = size_by_country.rename(index=country_translation_map)

    # 파이 차트 시각화

    plt.figure(figsize=(12, 12))

    size_by_country_korean.nlargest(20).plot.pie(
        figsize=(10, 10),
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.85,
        textprops={'rotation': 10}
    )

    plt.title('개발자 국가 분포 Top 20', fontsize=16)
    plt.ylabel('')
    plt.axis('equal')

    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print(f"오류: '{file_name}'을 찾을 수 없음.")
    print(" 'survey_raw.csv' 파일을 생성")
except Exception as e:
    print(f"코드 실행 중 예외 발생: {e}")