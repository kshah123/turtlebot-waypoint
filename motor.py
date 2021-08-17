class motor:
    def __init__(self, Kt, Ke, Resistance, Inductance, Damping_coeff):
        self.kt = Kt
        self.ke = Ke
        self.R = Resistance
        self.L = Inductance
        self.b = Damping_coeff
        self.back_emf_prev = 0
        self.didt_prev = 0
        self.i_int = 0
        self.V = 0
    def getOutputs(self, dt, ang_vel):
        didt = (self.V - self.R * self.i_int - self.ke*self.back_emf_prev)/self.L
        self.i_int += dt/2*(didt+self.didt_prev)
        self.didt_prev = didt
        self.back_emf_prev = self.R * self.i_int
        T_net = self.kt*self.i_int-self.b*ang_vel
        return T_net
