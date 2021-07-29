import numpy as np
import matplotlib.pyplot as plt

def show(data, epochs, wHistory, lossHistory, ylim=None):
    data = np.array(data)
    
    #loss evolution
    graph_x = np.arange(0, epochs)
    graph_y = lossHistory
    plt.plot(graph_x, graph_y)  
    plt.show()    
    
    #len(lossHistory)

    #data points
    X = data[:, [0,1]]
    Y = data[:, [2]]

    rows1 = data[data[:,2] == 1]
    rows0 = data[data[:,2] == 0]    
    
    plt.scatter(rows0[:,0],rows0[:,1])
    plt.scatter(rows1[:,0],rows1[:,1])        

    #solutions evolution
    #plt.xlim(minx-1,maxx+1)
    if(ylim != None):
        plt.ylim(ylim)
    n=0    
    for line in wHistory:
        n+=1
        if(n%10==0):
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
