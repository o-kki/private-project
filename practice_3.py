from cgi import print_directory, print_environ_usage


sentence = '나는 소년입니다.'
print(sentence)
sentence2 = "파이썬은 쉬워요."
print(sentence2)
sentence3 = """나는 소년이고, 
파이썬은 쉬워요"""
print(sentence3)
jumin = "901211-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 직전까지 0,1
print("월 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7가리 : " + jumin[7:])
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서부터 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print([python.replace("Python","Java")])


index = python.index("n")
print(index)    
index = python.index("n", index + 1) # 문자열이 없으면 에러 출력
print(index)
print(python.find('Java')) # 문자열이 없으면 -1 나온다.
print(python.count("n")) # n개의 문자가 몇번 들어갔는지 출력




