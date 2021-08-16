class eom():
    def __init__(self,Fx,Fy,T,M,I):
        self.force_x = Fx
        self.force_y = Fy
        self.trq = T
        self.mass = M
        self.inertia = I
    def getForce(self):
        return self.force
    def getTorque(self):
        return self.trq
    def setForce(self,F):
        self.force = F
    def setTorque(self,T):
        self.trq = T
    def getAccelX(self):
        return self.force_x/self.mass
    def getAccelY(self):
        return self.force_y/self.mass
    def getAngAccel(self):
        return self.trq/self.inertia
    def getVelX(self,Vx,dt):
        return self.getAccelX()*dt + Vx
    def getVelY(self,Vy,dt):
        return self.getAccelY()*dt + Vy
    def getPosX(self,Px,dt):
        return self.getVelX()*dt + Px
    def getPosY(self,Py,dt):
        return self.getVelY()*dt + Py
    def getAngVel(self,w,dt):
        return self.getAngAccel()*dt + w
    def getAngle(self,angle,dt):
        return self.getAngVel()*dt + angle
