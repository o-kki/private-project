from ast import expr_context


try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자 입력하세요 : ")))
    nums.append(int(input("두번째 숫자 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # 에러 명칭
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err: # 에러 명칭
    print(err)
except Exception as err: # 나머지 모든 에러는 여기서 처리
    print("알수없는 에러가 발생하였습니다. ")
    print(err) # 어떠한 에러를 내는지 알 수 있다.