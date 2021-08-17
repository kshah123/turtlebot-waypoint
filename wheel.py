class wheel(): ## ASSUME NO SLIP FOR THIS MODEL
    def __init__(self,wheel_motor, radius, relative_position, inertia):
        self.motor = wheel_motor
        self.R = radius
        self.relPos = relative_position #position offset from vehicle CG - should be a tuple of length 2
        self.I = inertia
        self.angVel = 0
        self.angAccel = 0
    def updateState(self, dt):
        wheel_torque = self.motor.getOutputs(dt,self.angVel)
        current_angAccel = wheel_torque/self.I
        current_angVel = self.angVel + dt/2*(current_angAccel + self.angAccel)
        self.angAccel = current_angAccel
        self.angVel = current_angVel
        return wheel_torque / self.R
    def getPos(self):
        return self.relPos
    def setVoltage(self, V):
        self.motor.V = V