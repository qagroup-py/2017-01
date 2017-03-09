class Chair:
    legs = 4
    material = 'metal'
    cover_material = 'textile'
    warranty = 3
    back_support = True
    height_adjustment = False
    rollers = False
    arm_rest = False

    def __init__(self, color):
        if type(color) is not str:
            raise Exception('Chair color must be string')
        else:
            self.color = color


class SimpleChair(Chair):
    pass


class SuperChair(Chair):
    arm_rest = True


class RollerChair(Chair):
    rollers = True
    arm_rest = True
