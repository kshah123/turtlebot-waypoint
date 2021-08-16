class pid:
    def __init__(self, Kp, Ki, Kd):
        self.kp = Kp
        self.ki = Ki
        self.kd = Kd
        self.err_int = 0
        self.first = True
    def set_kp(self, Kp):
        self.kp = Kp
    def set_ki(self, Ki):
        self.ki = Ki
    def set_kd(self, Kd):
        self.kd = Kd
    def getOutput(self,err, err_prev, dt):
        if self.first:
            self.first = False
            return self.kp*err
        derr_dt = (err_prev - err)/dt
        self.err_int+=(dt/2*(err+err_prev))
        return self.kp*err + self.ki * self.err_int + self.kd * derr_dt
