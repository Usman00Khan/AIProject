import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
def limit(x):
    x = round(x,1)
    if x>10:
        return 10
    elif x<1:
        return 1
    return x

def aptigen(nt,t):
    a = []
    for i in range(len(t)):
        a.append(round((t[i]+nt[i])/2,1))
    return a
eynt = np.random.normal(9, 1, 201)
eyt = np.random.normal(5, 1, 201)

eynt = list(map(limit,eynt))
eyt = list(map(limit,eyt))
eya = aptigen(eyt,eynt)
# count, bins, ignored = plt.hist(s, 30, normed=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
# np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
# linewidth=2, color='r')
# plt.show()
dnt = np.random.normal(6.5, 1, 201)
dt = np.random.normal(9, 1, 201)
dnt = list(map(limit,dnt))
dt = list(map(limit,dt))
da = aptigen(dt,dnt)

lnt = np.random.normal(5, 1, 201)
lt = np.random.normal(4, 1.5, 201)
lnt = list(map(limit,lnt))
lt = list(map(limit,lt))
la = aptigen(lt,lnt)
e = pd.read_csv("./LTI.csv")
e['Technical'] = lt
e['Verbal'] = lnt
e['Aptitude'] = la
e.to_csv("LTIN.csv",index = False)

f = pd.read_csv("./EY.csv")
f['Technical'] = eyt
f['Verbal'] = eynt
f['Aptitude'] = eya
f.to_csv("EYN.csv",index = False)

g = pd.read_csv("./DeutscheBank.csv")
g['Technical'] = dt
g['Verbal'] = dnt
g['Aptitude'] = da
g.to_csv("DeutscheN.csv",index = False)


# plt.scatter(eyt,eynt)
# plt.scatter(dt,dnt)
# plt.scatter(lt,lnt)

# t = eyt+lt+dt
# nt = eynt+lnt+dnt

# X =[]
# for i in range(600):
#     X.append([t[i],nt[i]])
# X = np.array(X)
# cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
# cluster.fit_predict(X)
# print(cluster.labels_)
# plt.scatter(X[:,0],X[:,1], c=cluster.labels_, cmap='rainbow')
# # plt.scatter(t,nt)
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.show()

# plt.scatter(eyt,eynt)
# plt.scatter(dt,dnt)
# plt.scatter(lt,lnt)
# plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
# plt.show()

