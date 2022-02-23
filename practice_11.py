print("자바", "파이썬", "자바스크립트", sep=" vs ", end ="?") # end 는 연달아서 출력
print("무엇이 재미있을까요?")

import sys
print("Python","Java", file=sys.stdout) # 표준출력, 정상일경우 출력
print("Python","Java", file=sys.stderr) # 표준에러, 에러날경우 출력

scores = {"수학":0,"영어":100,"코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8),str(score).rjust(4), sep=":")

for num in range (0,100):
    print("대기번호 : " +str(num).zfill(3))

answer = input("아무 값이나 입력해주세요 : ")  # input으로 넣으면 무조건 str로 받는다.
print(type(answer))  



