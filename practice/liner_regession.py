import numpy as np

class SingleNeuronTwoInput:
    def __init__(self,w1_init,w2_init,b_init=0.0):
        self.w1 = w1_init
        self.w2 = w2_init
        self.b = b_init


    def z_cal(self,x1,x2):  #z = y^ calculating
        return self.w1*x1 + self.w2*x2 +self.b


    def train(self,x_train,y_train,learning_rate=0.01,epochs=90):
        for epoch in range(epochs):
            total_error=0
            for x1,x2,y in zip(x_train[:,0],x_train[:,1],y_train):
                z=self.z_cal(x1,x2) #z = y^
                error = z - y   #e


                dw1 = error*x1  
                dw2 = error*x2
                db = error

                self.w1 -= learning_rate*dw1
                self.w2 -=learning_rate*dw2
                self.b -= learning_rate*db

                total_error += (error)**2 #MSE

            loss = total_error / len(y_train)

            print(f"{epoch+1}/{epochs}, loss {loss:.4f}")



# y = 3*x1+2*x2+1

x_train = np.array([
    [1,4],
    [2,6],
    [3,2]
])

y_train = np.array([12,19,14])

neuron = SingleNeuronTwoInput(3,2,1.0)
neuron.train(x_train,y_train,0.01,100)

print(f"Last w1 = {neuron.w1:.4f}, w2 = {neuron.w2:.4f}\n last b = {neuron.b:.4f}")
