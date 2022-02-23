print(5)
print(-10)
print(2*8)
print(3*(3+1))

print('나비')
print("풍선")

print(not True)
print(not False)

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3
 
print("우리집 " + animal +"의 이름은 " + name + "예요")
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.") # 정수형은 + 를 포함한 프린트에서 사용하려면 str 을 사용해야함
print(name, "는 ", age, "살이며, ", hobby, '을 아주 좋아해요"')
print(name + "는 어른일까요? " + str(is_adult)) # bool형도 str 감싸야함

'''이렇게 하면 주석이 됩니다.'''


station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")