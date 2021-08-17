from vector import Vector2D
from motor import motor

class vehicle():
    def __init__(self,wheels:dict,mass,inertia, initial_pos:Vector2D, initial_heading):
        self.wheels = wheels # wheels = {"L":left_wheel, "R": right_wheel}
        self.mass = mass
        self.inertia = inertia
        self.pos = initial_pos #should be a Vector2D class
        self.vel = Vector2D(0,0)
        self.accel = Vector2D(0,0)
        self.heading = initial_heading
    def getWheels(self):
        return self.wheels
    def updateState(self, vehicle_accel:Vector2D, dt):
        current_vel = self.vel + dt/2*(vehicle_accel+self.accel)
        self.accel = vehicle_accel
        current_pos = self.pos + dt/2(current_vel + self.vel)
        self.vel = current_vel
        self.pos = current_pos
        return current_vel
    def setVoltages(self, wheel_voltages:dict):
        #wheel_voltages = {"L": voltage_for_left_wheel, "R": voltage_for_right_wheel}
        for key in wheel_voltages.keys():
            self.wheels[key].setVoltage(wheel_voltages[key])
   
    # def getWheelTorques(self,voltages,dt,angVels):
    #     if len(voltages) != len(angVels):
    #         return "Error: length of voltages does not match angVels"
    #     trq = [0] * len(voltages)
    #     for i in self.motors:
    #         trq(i) = self.motors(i).getOutputs(voltages(i),dt,angVels(i))
    #     return trq
    # def getForces(self,voltages,dt,angVels,radii):
    #     if len(voltages) != len(angVels) or len(voltages) != len(radii):
    #         return "Error: length of voltages does not match angVels"
    #     forces = [0] * len(voltages)
    #     torques = self.getWheelTorques(voltages,dt,angVels)
    #     for i in forces:
    #         forces(i) = torques(i) / radii(i)
    #         ## NEXT: Get net Fx, net Fy, and net Torque


        