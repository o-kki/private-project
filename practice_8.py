absent = [2,5]
no_book = [7]
for student in range(1, 11):
    if student in absent :
        continue
    elif student in no_book:
        print("오늘 수업 여기까지!, {0}는 교무실 따라와".format(student))
        break 
    print("{0}, 책을 읽어봐".format(student))


# 한줄 for 문
students = ["김김김","남남남남남","씨씨"]
students = [len(i) for i in students]
print(students)

students = ['llll','kkkkk','qqqqq']
students = [i.upper() for i in students]
print(students)



from random import *
# passenger = []
cnt = 0
for i in range(1,51):
    time = randint(5,51)    
    if time <= 5 or time >= 15 :
        # passenger.append("{0}".format(i))
        print("[0] {0}번쨰 손님 (소요시간 :{1}분)".format(i,time))
        cnt += 1
    else:
        print("[] {0}번쨰 손님 (소요시간 :{1}분)".format(i,time))
        
print("총 탑승 승객 : {0}".format(cnt))  
    