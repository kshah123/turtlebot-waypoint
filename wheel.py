class wheel(): ## ASSUME NO SLIP FOR THIS MODEL
    def __init__(self,T_motor,r_wheel):
        self.F_wheel = T_motor/r_wheel
    def getForce(self):
        return self.F_wheel
    def setForce(self,T_motor,r_wheel):
        self.F_wheel = T_motor/r_wheel