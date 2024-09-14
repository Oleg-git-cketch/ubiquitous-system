class Player:
    def __init__(self, sila, tochnost, speed, durablity):
        self.sila = sila
        self.tochnost = tochnost
        self.speed = speed
        self.durablity = durablity

class Nap(Player):
    def vozmoznost(self, run_vpered_polya):
        self.run_vpered_polya = run_vpered_polya

class Zash(Player):
    def vozmoznost(self, run_v_zonu_vratarya):
        self.run_v_zonu_vratarya = run_v_zonu_vratarya


class Pzash(Player):
    def vozmoznost(self, bit_v_seredine):
        self.bit_v_seredine = bit_v_seredine


class Goalkeeper(Player):
    def vozmoznost(self, brat_mach):
        self.brat_mach = brat_mach
