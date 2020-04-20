import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork:
    def __init__(self):
        self.wij = 2*np.random.rand(10, 10)-np.ones((10,10)) # random initial weights
        #self.bj = np.random.rand(10, 1)

    def use_weights(self,X):
        zj_out = np.dot(X, self.wij)#+self.bj
        guess = self.sigmoid(zj_out)

        return guess

    def sigmoid(self,z):

        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    def gradient_descent(self,x,y,iterations):
        etha = 1
        error = []
        index = []
        for i in range(iterations):
            Xi = x
            zj =  np.dot(Xi, self.wij)#+self.bj
            yhat = self.sigmoid(zj)

            # gradients for hidden to output weights
            yyhat = (y - yhat)
            sigmoidd = self.sigmoid_derivative(zj)
            deltaj = np.dot(yyhat,sigmoidd)
            g_wij = np.dot(Xi,deltaj)

            #g_bj = deltaj


            # update weights
            if np.linalg.det(g_wij) !=0:
                self.wij += etha*np.linalg.inv(g_wij)
            #self.bj += etha*g_bj

            error.append(np.linalg.norm(y-yhat))
            index.append(i)


        print("The weights are:")
        print(self.wij)

        #print("The biasis are:")
        #print(self.bj)

        print("The prediction is")
        print(yhat)
        plt.plot(index,error)
        plt.show()





if __name__ == '__main__':
    neural_network = NeuralNetwork()
    print('Random starting input to hidden weights: ')
    print(neural_network.wij)


    #matriz com as especficacoes das aeronaves
    Sn = np.array([[320, 60.9, 63.8, 18.5, 900, 11800, 297500, 201800, 134800, 5],
                                [294, 60.1, 62.8, 16.3, 920, 11500, 252650, 192776, 110677, 6],
                                [344, 60.1, 68.3, 17.02, 903, 12000, 254100, 202000, 118000, 8],
                                [268, 60.30, 58.37, 17.40, 880, 8800, 233000, 180000, 168000, 7],
                                [292, 60.3, 63.69, 16.8, 880, 8200, 233000, 182000, 173000, 8],
                                [408, 64.8, 73.86, 18.5, 920, 12000, 351543, 237680, 159570, 7],
                                [408, 64.44, 70.67, 19.4, 920, 11500, 390100, 295743, 184567, 9],
                                [142, 35.8, 33.62, 12.6, 850, 3500, 65317, 58604, 37648, 3],
                                [188, 35.8, 42.12, 12.6, 850, 4300, 76900, 66361, 42493, 3],
                                [88, 26, 31.68, 9.86, 850, 3300, 36500, 34000, 21810, 2]])


    #aqui eu tenti normalizar os vetores das especificacoes pra ver se concertava o erro q da com a funcao sigmoide
    X = np.zeros((10,10))
    i=0
    for line in Sn.T:
        X[i] = line/np.linalg.norm(line)
        i+=1

    X = X.T
    #y = np.array([0.,.1,.2,.3,.4,.5,.6,.7,.8,.9]).T #vetor q quer q chegue pro treinamento

    y = np.array([[1., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                  [0., 1., 0., 0., 0., 0., 0., 0., 0., 0.],
                  [0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
                  [0., 0., 0., 1., 0., 0., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 1., 0., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
                  [0., 0., 0., 0., 0., 0., 0., 0., 1., 0.],
                  [0., 0., 0., 0., 0., 0., 0., 0., 0., 1.]])


    neural_network.gradient_descent(X, y, 100)#ajustar os pesos usando a matriz X e tentando chegar em Y, repetir o gradiente 10000 vezes
    print("the guess is")
    print(neural_network.use_weights(X[0]))