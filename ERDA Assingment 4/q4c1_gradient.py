import numpy as np

class NeuralNetwork:
    def __init__(self):
        self.wij = np.random.rand(10, 1) # random initial weights
        self.bj = np.random.rand(10, 1)

    def sigmoid(self,z):

        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def gradient_descent(self,x,y,iterations):
        etha = 0.1

        for i in range(iterations):
            Xi = x
            zj =  np.dot(Xi, self.wij)+self.bj
            yhat = self.sigmoid(zj)

            # gradients for hidden to output weights

            deltaj = np.dot((y - yhat),self.sigmoid_derivative(zj))
            g_wij = np.dot(Xi,deltaj)

            g_bj = deltaj


            # update weights
            self.wij -= etha*g_wij
            self.bj -= etha*g_bj




        print("The weights are:")
        print(self.wij)

        print("The biasis are:")
        print(self.bj)

        print("The prediction is")
        print(yhat)





if __name__ == '__main__':
    neural_network = NeuralNetwork()
    print('Random starting input to hidden weights: ')
    print(neural_network.wij)


    #matriz com as especficacoes das aeronaves
    Sn = np.array([[268., 60.30, 58.37, 17.40, 880., 8800., 233000., 180000., 168000., 7.],
                   [292., 60.3, 63.69, 16.8, 880., 8200., 233000., 182000., 173000., 8.],
                   [142., 35.8, 33.62, 12.6, 850., 3500., 65317., 58604., 37648., 3.],
                   [188., 35.8, 42.12, 12.6, 850., 4300., 76900., 66361., 42493., 3.],
                   [408., 64.44, 70.67, 19.4, 920., 11500., 390100., 295743., 184567., 9.],
                   [320., 60.9, 63.8, 18.5, 900., 11800., 297500., 201800., 134800., 5.],
                   [408., 64.8, 73.86, 18.5, 920., 12000., 351543., 237680., 159570., 7.],
                   [294., 60.1, 68.3, 17.02, 903., 12000., 254100., 202000., 118000., 8.],
                   [344., 60.1, 68.3, 17.02, 903., 12000., 254100., 202000., 118000., 8.],
                   [88., 26., 31.68, 9.86, 850., 3300., 36500., 34000., 21810., 2.]])


    #aqui eu tenti normalizar os vetores das especificacoes pra ver se concertava o erro q da com a funcao sigmoide
    X = np.zeros((10,10))
    i=0
    for line in Sn.T:
        X[i] = line/np.linalg.norm(line)
        i+=1


    y = np.array([0.,.1,.2,.3,.4,.5,.6,.7,.8,.9]).T #vetor q quer q chegue pro treinamento


    neural_network.gradient_descent(X.T, y, 10000)#ajustar os pesos usando a matriz X e tentando chegar em Y, repetir o gradiente 10000 vezes