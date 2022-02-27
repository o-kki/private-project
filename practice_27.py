from ast import expr_context
from logging import exception

class BigNumberError(Exception): # 에러메시지 남기기
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자 입력하세요 : "))
    num2 = int(input("두번째 숫자 입력하세요 : "))

    if num1 >= 10 or num2 >= 10: # 일부러 에러를 발생시켜서 해당 에러로 보낼 수 있다.
        # raise ValueError
        raise BigNumberError("입력값 : {0},{1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
    
except ValueError: 
    print("한 자리 숫자만 입력하세요.")
except BigNumberError as err: 
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
finally: # 무조건 마지막 표출
    print("계산기를 이용해 주셔서 감사합니다.")