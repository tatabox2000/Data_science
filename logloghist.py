import numpy as np
import pylab as plt
import pandas as pd
 
def histgram2(name):
    data = pd.read_csv(name)
    a = data['A']
    b = data['B']
    c = data['C']
    d = data['D']
    e = data['E']
    f = data['F']
    g = data['G']
    h = data['H']
    i = data['I']
    datalist = [a,b,c,d,e,f,g,h,i]
    print "median,mean,max,min"
    for col in datalist:
        
        print round(np.median(col.dropna()),2),',',round(np.mean(col.dropna()),2),',',round(np.max(col.dropna()),0),',',round(np.min(col.dropna()),2)

    """
    plt.subplot(3,3,1),plt.hist(a.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='r'),plt.gca().set_xscale("log")
    plt.subplot(3,3,2),plt.hist(b.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='g'),plt.gca().set_xscale("log")
    plt.subplot(3,3,3),plt.hist(c.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='r'),plt.gca().set_xscale("log")
    plt.subplot(3,3,4),plt.hist(d.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='g'),plt.gca().set_xscale("log")
    plt.subplot(3,3,5),plt.hist(e.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='r'),plt.gca().set_xscale("log")
    plt.subplot(3,3,6),plt.hist(f.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='g'),plt.gca().set_xscale("log")
    plt.subplot(3,3,7),plt.hist(g.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='r'),plt.gca().set_xscale("log")
    plt.subplot(3,3,8),plt.hist(h.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='g'),plt.gca().set_xscale("log")
    plt.subplot(3,3,9),plt.hist(i.dropna(),bins=np.logspace(-1, 4, 50),normed=True,log=True,color='r'),plt.gca().set_xscale("log")   
    """
    #plt.subplot(3,3,3),plt.hist(a.dropna(),bins=np.logspace(-1, 4, 50),alpha=0.2,normed=True,log=True,color='r'),plt.gca().set_xscale("log")
    #plt.subplot(3,3,3),plt.hist(b.dropna(),bins=np.logspace(-1, 4, 50),alpha=0.7,normed=True,log=True,color='g'),plt.gca().set_xscale("log")
    #plt.subplot(3,3,4),plt.hist(a.dropna(),bins=np.logspace(-1, 4, 50),alpha=0.7,normed=True,log=True,color='r'),plt.gca().set_xscale("log")
    #plt.subplot(4,1,4),plt.hist(b.dropna(),bins=np.logspace(-1, 4, 50),alpha=0.2,normed=True,log=True,color='g'),plt.gca().set_xscale("log")
    plt.show()
 
 
if __name__ == '__main__':
    import os
    os.chdir(u"F:\A_time")
    name = u"all.csv"
    histgram2(name)
