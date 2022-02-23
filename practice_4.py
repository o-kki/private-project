print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

print("나는 %s 살입니다. " )
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))


print("나는 {}살입니다." . format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란","빨간"))
print("나는 {0}색과 {1}색을 좋아해요." .format("파란","빨간"))  #순번에 맞춰서 출력
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간")) #순번에 맞춰서 출력

print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

## v3.6이상
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# \n : 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")
print('저는 "나노코딩" 입니다. ')
print("저는 \'나노코딩\' 입니다. ")

# \\ : 문장 내에서 \
print("C:\\Users\\young\\OneDrive\\바탕 화면\\python code>")

# \r : 커서를 맨앞으로
print("Red Apple\rPine")
# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")
# \t : 탭
print("Red\tApple")


data = "http://naver.com"
data_mod = data[7:-4] # 규칙 1 
print("생성된 비밀번호 : ", data_mod[:3]+str(len(data_mod))+str(data_mod.count('e'))+"!")

my_str = data.replace("http://","") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!" # 규칙 3
print("{0}의 비밀번호는 {1} 입니다. " .format(data,password))


