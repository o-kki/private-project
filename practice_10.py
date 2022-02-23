gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

def std_weight(height, gender):
    if gender == '남자':
        # std_weght = height * height * 22
        return height * height * 22
    else :
        # std_weght = height * height * 21
        return height * height * 21

    #print("키 {0} {1}의 표준 몸무게는 {2} 입니다.".format(height, gender,round(std_weght*0.0001,2)))

std_weight(175,'남자')
height = 175
gender = "남자"
weight = round(std_weight(height / 100, gender),2)
print("키 {0} {1}의 표준 몸무게는 {2} 입니다.".format(height, gender,weight))
