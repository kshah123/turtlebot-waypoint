from motor import motor


class vehicle():
    def __init__(self,wheels,motors,mass,inertia):
        if len(wheels) != len(motors):
            return "Error: number of wheels does not match number of motors"
        self.wheels = wheels
        self.motors = motors
        self.mass = mass
        self.inertia = inertia
    def getWheels(self):
        return self.wheels
    def getMotors(self):
        return self.motors
    def getMass(self):
        return self.mass
    def getInertia(self):
        return self.inertia
    def getWheelTorques(self,voltages,dt,angVels):
        if len(voltages) != len(angVels):
            return "Error: length of voltages does not match angVels"
        trq = [0] * len(voltages)
        for i in self.motors:
            trq(i) = self.motors(i).getOutputs(voltages(i),dt,angVels(i))
        return trq
    def getForces(self,voltages,dt,angVels,radii):
        if len(voltages) != len(angVels) or len(voltages) != len(radii):
            return "Error: length of voltages does not match angVels"
        forces = [0] * len(voltages)
        torques = self.getWheelTorques(voltages,dt,angVels)
        for i in forces:
            forces(i) = torques(i) / radii(i)
            ## NEXT: Get net Fx, net Fy, and net Torque


        