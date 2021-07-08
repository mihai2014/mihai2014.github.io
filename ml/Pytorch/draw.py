import numpy as np
import matplotlib.pyplot as plt

def display_solution(data,finalPrediction,predictionHistory,lossHistory,epochs,ylim=None):
    
    #loss evolution
    graph_x = np.arange(0, epochs)
    graph_y = lossHistory
    plt.plot(graph_x, graph_y)  
    plt.show()

    #data points and final line boundary
    X = data[:, [0,1]]
    Y = data[:, [2]]

    rows1 = data[data[:,2] == 1]
    rows0 = data[data[:,2] == 0]

    #w1 x1 + w2 x2 + b = 0
    #w1 x + w2 y + b = 0
    #y = (1/w2) * (-w1 x - b)
    w1 = finalPrediction[0]
    w2 = finalPrediction[1]
    b = finalPrediction[2]

    minx = np.min(X[:,0])
    maxx = np.max(X[:,0])

    xx_line = np.linspace(minx,maxx,100)
    #or
    #xx.line =np.range(minx, maxx, 0.1)
    yy_line = (1/w2) * (-w1 * xx_line - b)
    print(xx_line.shape)
    print(yy_line.shape)

    plt.scatter(rows0[:,0],rows0[:,1])
    plt.scatter(rows1[:,0],rows1[:,1])

    #solutions evolution
    #plt.xlim(minx-1,maxx+1)
    if(ylim != None):
        plt.ylim(ylim)
    for line in predictionHistory:
        w1 = line[0]
        w2 = line[1]
        b = line[2]
        minx = np.min(X[:,0])
        maxx = np.max(X[:,0])
        xx_line = np.linspace(minx,maxx,100)
        #xx.line =np.range(minx, maxx, 0.1)
        yy_line = (1/w2) * (-w1 * xx_line - b)

        plt.plot(xx_line, yy_line,'g:')
    
    #final solution line    
    plt.plot(xx_line, yy_line, 'r'); 
