number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number -= 2
number /= 2
print(number)
print(abs(-5)) # 절대값 5 반환
print(pow(4, 2)) # 4^2 = 16
print(max(5, 20)) # 12
print(min(5, 20)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import *
print(floor(4.99)) # 내림. 4
print(ceil(3.14)) # 올림. 4
print(sqrt(16)) # 제곱근. 4

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(int(random()*10))

print(randrange(1,46)) # 1 ~ 46 미만의 임의의 값 생성
print(randint(1, 45))



study_day = randint(1,28)
if study_day >= 1 and study_day <=3 :
    print("스터디 준비날 입니다.")
else :
    print("오프라인 스터디 모임 날짜는 매월 " + str(study_day) + " 일로 선정되었습니다.")
