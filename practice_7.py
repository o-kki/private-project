from tracemalloc import start


for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토리", "아이엠 그루트"]
for customers in starbucks :
    print("{0}님, 커피가 준비되었습니다. ".format(customers))


# while
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피가 처분되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비되었습니다.호출 {1} 회".format(customer,index))
    index += 1
