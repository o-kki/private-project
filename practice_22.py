from re import A
# 일반 유닛
class Unit:
    # init은 생성자, self를 제외한 나머지 만큼을 호출(name, hp, damage) -->객체 형성 가능
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed)) 

# 공격 유닛
class AttackUnit(Unit):  # 공격유닛은 일반유닛을 상속받아서 사용하는것! 공통적인 부분만, Unit이 부모,  AttackUnit이 자식
    # init은 생성자, self를 제외한 나머지 만큼을 호출(name, hp, damage) -->객체 형성 가능
    def __init__(self, name, hp, speed, damage):
        # self.name = name
        # self.hp =  dhp
        Unit.__init__(self, name, hp, speed)  # 이렇게 상속받은걸 사용 할 수 있다.
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("서플라이 디폿", 500, '7시')

def game_start():
    print("새로운 게임 시작합니다.")

def game_over():
    pass

game_start()
game_over()