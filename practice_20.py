from time import sleep


class Unit:
    # init은 생성자, self를 제외한 나머지 만큼을 호출(name, hp, damage) -->객체 형성 가능
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중유닛, 비행기, 클로킹
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 가정해
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
