"""
9-5 상속
https://youtu.be/kWiCuklohdY?t=14368
"""
# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name    
        self.hp = hp
        
# 공격 유닛
class AtttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name,location,self.damage))
    
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입렀습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))
# 메딕 : 의무병

# 파이어뱃 : 공격 유닛, 화염방사기.
firebat1 = AtttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)