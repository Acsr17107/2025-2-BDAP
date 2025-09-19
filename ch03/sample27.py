import random
import numpy as np

# 40명의 학생에게 50~100점 사이의 점수를 무작위로 할당
# Key: S11 ~ S50
scores = dict()
for i in range(11, 50 + 1):
    scores['S' + str(i)] = random.randrange(50, 100 + 1)
print("전체 학생 점수:", scores)
print('-' * 30)

# 문제 1: 40명 학생의 평균 점수를 구하시오
avg = sum(scores.values()) / len(scores)
print(f"학생들의 평균 점수: {avg:.2f}")

# (numpy를 사용한 평균 계산)
# score_value = np.array(list(scores.values()))
# avg_np = np.mean(score_value)
# print(f"numpy를 이용한 평균 점수: {avg_np:.2f}")

print('-' * 30)

# 문제 2: 40명 중 최고 득점을 한 학생과 점수를 출력하시오.
# 여러 명인 경우, 학번이 가장 빠른 한 명만 출력되도록 하시오.

# 1. 최고 점수 찾기
max_score = 0
for score in scores.values():
    if score > max_score:
        max_score = score

# 2. 최고 점수를 받은 학생 찾기
# 딕셔너리는 'S11'부터 순서대로 생성되었으므로,
# 처음 발견되는 학생이 학번이 가장 빠른 학생입니다.
top_student = ''
for student_id, score in scores.items():
    if score == max_score:
        top_student = student_id
        break  # 가장 빠른 학번의 학생을 찾았으므로 반복을 중단합니다.

print(f"최고 득점 학생: {top_student}")
print(f"최고 점수: {max_score}")

# [더 간결한 방법]
# max() 함수의 key 인자를 활용하여 한 줄로 해결할 수도 있습니다.
# 람다(lambda) 함수는 점수(item[1])를 기준으로 최댓값을 찾도록 지정합니다.
# top_student_id, max_val = max(scores.items(), key=lambda item: item[1])
# print(f"\n[간결한 방법]\n최고 득점 학생: {top_student_id}, 점수: {max_val}")