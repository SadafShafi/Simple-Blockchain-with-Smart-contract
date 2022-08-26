import pickle

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
        print(f'Added to token1: {self.data.token1}')
    
    def subToken1(self):
        if self.data.token1>0:
            self.data.token1-=1
            print(f'Subtracted from token1: {self.data.token1}')
            
    def addToken2(self):
        self.data.token2+=18
        print(f'Added to token2: {self.data.token2}')
        
    def subToken2(self):
        if self.data.token2>0:
            self.data.token2-=2
            print(f'Subtracted from token2: {self.data.token2}')
    
    def run(self):
        anomaly_detector = pickle.load(open('anomaly_detector.sav', 'rb'))
        with open('oracle.txt', 'r') as oracle:
            for l in oracle:
                new_temp = int(l)
                if anomaly_detector.predict([[new_temp]]) == 1:
                    self.addToken1()
                    self.subToken1()
                    self.addToken2()
                    self.subToken2()
                else:
                    print('Possible Anomaly Detected!')
                    print('Halting...')
                    exit()
                    
        return self.data
     

