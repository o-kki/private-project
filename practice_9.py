from pkg_resources import compatible_platforms


def open_accoutn():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    print("입금이 완료 되었습니다. 잔액은 {0} 원입니다. ".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money : # 잔액이 출금보다 많으면
        print("출금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else :
        print("출금이 완료 되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, money, balance - money - commission # return 값을 튜플 형식으로 보내주는것

balance = 0 # 잔액
balance = deposit(balance, 10000)
balance = withdraw(balance, 500)
print(balance)    
commission, money, balance = withdraw_night(balance, 400)
print("출금은 {1}, 수수료 {0} 원이며, 잔액은 {2} 원 입니다.".format(commission, money, balance))


def profile(name, age, main_lang):
    print("이름 {0}\t나이 :{1}\t주 사용 언어 :{2}" \
        .format(name, age, main_lang)) ## \ 사용하면 문장을 나눠어도 한줄로 의미된다.

profile("정영기", 20, '파이썬')
profile(name="김태호", main_lang="java", age="16") # 키워드 호출

def profile_2(name, age=17, main_lang="자바"):
    print("이름 {0}\t나이 :{1}\t주 사용 언어 :{2}" \
        .format(name, age, main_lang)) ## \ 사용하면 문장을 나눠어도 한줄로 의미된다.

profile_2("유재석")

def profile_3(name, age, *language): # 가변인자일때 * 사용
    print("이름 {0}\t나이 :{1}\t".format(name, age), end=" ")
    for lang in language :
        print(lang, end=" ")
    print()

profile_3("정영기" ,20 , "파이썬","자바","C언어")



