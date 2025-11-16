languages_a = {'C', 'JavaScript', 'Python', 'R', 'Swift', 'Kotlin'}
languages_b = {'C++', 'Java', 'Python', 'C#', 'JavaScript', 'R'}

# Q1 두 학급에서 공통으로 다루는 프로그래밍 언어는?
ans1 = languages_a & languages_b
print(ans1)

# Q2 A 학급에서만 다루는 프로그래밍 언어 3개는?
ans2 = languages_a - languages_b
print(ans2)

# Q3 B 학급에서만 다루은 프로그래밍 언어 3개는?
ans3 = languages_b - languages_a
print(ans3)

# Q4 두 학급에서 다루는 프로그래밍 언어는 총 몇 개?
ans4 = languages_a | languages_b
print(ans4)
print(len(ans4))


