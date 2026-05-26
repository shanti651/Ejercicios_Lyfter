class Head:
    def __init__(self):
        self.eyes = 2
        self.ears = 2
        self.mouth = 1

class Hand:
    def __init__(self):
        self.fingers = 5
        
class Arm:
    def __init__(self, hand):
        self.hand = hand

class Feet:
    def __init__(self):
        self.toes = 5

class Leg:
    def __init__(self, feet):
        self.feet = feet

class Torso:
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):

        self.head = head

        self.right_arm = right_arm
        self.left_arm = left_arm

        self.right_leg = right_leg
        self.left_leg = left_leg

class Human:
    def __init__(self):
        self.head = Head()
        self.right_arm = Arm(Hand())
        self.left_arm = Arm(Hand())
        self.right_leg = Leg(Feet())
        self.left_leg = Leg(Feet())
        self.torso = Torso(
            self.head,
            self.right_arm,
            self.left_arm,
            self.right_leg,
            self.left_leg
        )

person = Human()





