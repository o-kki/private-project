from math import fabs
from random import randint
from re import A, I
# 일반 유닛
class Unit:
    # init은 생성자, self를 제외한 나머지 만큼을 호출(name, hp, damage) -->객체 형성 가능
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print('[지상 유닛 이동]')
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
            .format(self.name, location, self.speed)) 

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

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

class Marin(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 현재 시즈모드 아닐때 -> 시즈모드 
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드로 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False

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

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.cloecked = False

    def clocking(self):
        if self.cloecked == True:
            print("{0} : 클로킹 모드 해제 합니다.".format(self.name))
            self.cloecked = False
        else:
            print("{0} : 클로킹 모드 설정 합니다.".format(self.name))
            self.cloecked = True

def game_start():
    print("게임을 시작합니다.")

def game_over():
    print("player gg")
    print("player님이 게임을 나가셨습니다.")



# 실제 게임 진행
game_start()   

m1 = Marin()
m2 = Marin()
m3 = Marin()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")
    
# 탱크 시즈모드 개발
Tank.seize_developed = True
print("시즈 모드 개발 완료")

# 공격 모드 준비
for unit in attack_units:
    if isinstance(unit, Marin):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 폐쇄
for unit in attack_units:
     unit.damaged(randint(5, 21))

# 게임 종료
game_over()

