# 튜플 

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add('생선까스')

# name = "김종국"
# age= "20"
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


# 세트(set ) : 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석","김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합칩합 (java와 python 모두 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹어서 김태호 빠져
java.remove("김태호")
print(java)


# 자료구조 변경
meun = {"커피", "우유", "주스"}

menu = list(menu)
menu = tuple(menu)
menu = set(menu)

print(menu, type(menu))


from random import *
users = range(1,21) # 1부터 21까지 숫자를 생성
# print(type(users))
users = list(users)
shuffle(users)
winners = sample(users,4)
print("----담청자 발표---")
print("치킨 담청자 : {0}".format(winners[0]))
print("커피 담청자 : {0}".format(winners[1:]))
print("----축하합니다---")
