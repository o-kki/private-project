# sol 1 
for seat in range(21):
    if seat % 2 == 1:
        print('A'+str(seat), end=" ")


# sol 2
for seat in range(1, 21)[::2]: # 2 건너 뛰어서
    print(seat, end=" ")