class Data:
    def __init__(self):
        self.token1 = 10
        self.token2 = 12

class SmartContract:
    def __init__(self):
        print("Smart contract initiated")
        self.data = Data()
        

    def addToken1(self):
        self.data.token1+=4
    
    def subToken1(self):
        if self.data.token1>0:
            self.data.token1-=1
    
    def addToken2(self):
        self.data.token2+=18
    
    def subToken2(self):
        if self.data.token2>0:
            self.data.token2-=2

    
    def run(self):
        self.addToken1()
        self.subToken1()
        self.addToken2()
        self.subToken2()
        return self.data 

