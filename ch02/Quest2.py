import random
scores = dict()

for i in range(10, 50):
    scores['S' + str(i)] = random.randrange(50, 100)
print(scores)

# Q1 40명 학생의 평균 점수는?
avg = 0
for i in scores.values():
    avg += i
avg /= len(scores)
print(avg)

# Q2 40명 중 최고 득점을 한 학생과 점수 출력, 여러 명인 경우 학번이 빠른 한 명만 출력
max_s = ''
max = 0
for i in scores.keys():
    if scores[i] > max:
        max_s = i
        max = scores[i]
print(f'{max_s} : {max}')



