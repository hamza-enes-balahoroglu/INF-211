class Player():
    nickname = ""
    level = 1
    experience = 0
    kill_rate = 0
    HP = 0
    STR = 0
    DEX = 0
    INT = 0
    CHA = 0
    
    def __init__(self, name, level, experience, kill_rate, HP, STR, DEX, INT, CHA):
        self.set_nickname(name)
        self.set_level(level)
        self.set_experience(experience)
        self.set_kill_rate(kill_rate)
        self.set_HP(HP)
        self.set_STR(STR)
        self.set_DEX(DEX)
        self.set_INT(INT)
        self.set_CHA(CHA)
        pass
    
    def get_nickname(self):
        return self.nickname
    
    def get_level(self):
        return self.level
    def get_experience(self):
        return self.experience
    
    def get_kill_rate(self):
        return self.kill_rate
    
    def get_HP(self):
        return self.nickname
    
    def get_STR(self):
        return self.STR
    
    def get_DEX(self):
        return self.DEX
    
    def get_INT(self):
        return self.INT
    
    def get_CHA(self):
        return self.CHA
    
    def set_nickname(self, name):
        if isinstance(name, str):
            self.nickname = name
        else:
            print("Nick string olmak zorunda.")
    
    def set_level(self, level):
        if level>=1 and level<=99:
            self.level = level
            
    def set_experience(self, experience):
        if experience>=0 and experience<=10000:
            self.experience = experience
    
    def set_kill_rate(self, kill_rate):
        if kill_rate>=0 and kill_rate<=100:
            self.kill_rate = kill_rate
    
    def set_HP(self, HP):
        if HP>=0 and HP<=99:
            self.HP = HP
    
    def set_STR(self, STR):
        if STR>=0 and STR<=99:
            self.STR = STR
    
    def set_DEX(self, DEX):
        if DEX>=0 and DEX<=99:
            self.DEX = DEX
    
    def set_INT(self, INT):
        if INT>=0 and INT<=99:
            self.INT = INT
    
    def set_CHA(self,CHA):
        if CHA>=0 and CHA<=99:
            self.CHA = CHA

         
# return Player(name, level, experience, kill_rate, HP, STR, DEX, INT, CHA)

def quiz2():
    class Mega(Player):
        long_range_hit_bonus = 0
        def __init__(self, name, level, experience, kill_rate, HP, STR, DEX, INT, CHA, hit_bonus):
            super().__init__(name, level, experience, kill_rate, HP, STR, DEX, INT, CHA)
            self.set_long_range_hit_bonus(hit_bonus)
            
        def get_long_range_hit_bonus(self):
            return self.long_range_hit_bonus
        
        def set_long_range_hit_bonus(self, bonus):
            if bonus >=0 and bonus <= 10:
                self.long_range_hit_bonus = bonus
        pass
    class Warrior(Player):
        sword_critical_hit_bonus = 0
        def __init__(self, name, level, experience, kill_rate, HP, STR, DEX, INT, CHA, sword_critical_hit_bonus):
            super().__init__(name, level, experience, kill_rate, HP, STR, DEX, INT, CHA)
            self.set_sword_critical_hit_bonus(sword_critical_hit_bonus)
            
        def get_sword_critical_hit_bonus(self):
            return self.sword_critical_hit_bonus()
        
        def set_sword_critical_hit_bonus(self, bonus):
            if bonus >=0 and bonus <= 10:
                self.sword_critical_hit_bonus = bonus
        pass
    class Priest(Player):
        healing_buff = 0
        def __init__(self, name, level, experience, kill_rate, HP, STR, DEX, INT, CHA, healing_buff):
            super().__init__(name, level, experience, kill_rate, HP, STR, DEX, INT, CHA)
            self.set_healing_buff(healing_buff)
            
        def get_healing_buff(self):
            return self.healing_buff
        def set_healing_buff(self, bonus):
            if bonus >=0 and bonus <= 10:
                self.healing_buff = bonus
        pass
    class Priest(Player):
        close = 0
        def __init__(self, name, level, experience, kill_rate, HP, STR, DEX, INT, CHA, close):
            super().__init__(name, level, experience, kill_rate, HP, STR, DEX, INT, CHA)
            self.set_close(close)
            
        def get_close(self):
            return self.close
        def set_healing_buff(self, bonus):
            if bonus >=0 and bonus <= 10:
                self.close = bonus


    m = Mega("HAmza", 99, 10, 10, 10, 20, 30, 40, 14, 3)
    
    


# a = quiz1("HAmza", 99, 10, 10, 10, 20, 30, 40, 14)

b = quiz2()