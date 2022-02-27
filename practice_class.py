class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flayable 생성자")        

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super로 하게된다면, 순차적으로 하나씩 밖에 상속을 받아오지 못해
        # super().__init__() 
        Unit.__init__(self)  # 따로 명시해서, 초기화하여 사용
        Flyable.__init__(self)


# 드롭쉽
dropship = FlyableUnit()