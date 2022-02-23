# 리스트 []

# 지하철 칸별로 10명 ,20명, 30명

subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)
print(subway.index("조세호")) # 조세호가 몇번째 칸에 있는지

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄

print(subway.pop()) # 하하 빠짐
print(subway)
print(subway.pop()) # 박명수 빠짐
print(subway)
print(subway.pop()) # 조세호 빠짐
print(subway)

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 리스트 정렬
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)
num_list.reverse()
print(num_list)
num_list.clear() # 제거
print(num_list)

num_list = [5, 2, 4, 3, 1]
mix_list = ['조세호', 20, True]
num_list.extend(mix_list)
print(num_list)


# 사전 dic
cabinet = {3:"유재석" , 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False

# 새 손님
cabinet = {"A-3":"유재석", "B-100":"김태호"}
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key, values 각각 호춣
print(cabinet.keys())
print(cabinet.values())

# key, values 쌍쌍 호춣
print(cabinet.items())
cabinet.clear()


