class wheel(): ## ASSUME NO SLIP FOR THIS MODEL
    def __init__(self,moment_of_inertia,mass,wheel_motor, radius):
        self.I = moment_of_inertia
        self.m = mass
        self.motor = wheel_motor
        self.R = radius
    def getAppliedForce(self):
        return self.motor.getOutputs() / self.R
        