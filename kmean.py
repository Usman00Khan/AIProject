import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans as AgglomerativeClustering
class Cluster:
    def __init__(self):
        d = pd.read_csv("./fakedata/DeutscheN.csv")
        X = self.retxyDF(d)
        e = pd.read_csv("./fakedata/LTIN.csv")
        Y = self.retxyDF(e)
        e = pd.read_csv("./fakedata/EYN.csv")
        Z = self.retxyDF(e)
        FinalDataset = np.concatenate((X,Y,Z), axis=0, out=None)
        print(FinalDataset)
        self.cluster = AgglomerativeClustering(n_clusters=3)
        self.cluster.fit_predict(FinalDataset)
        outputc = list(self.cluster.labels_)
        acc, self.labels = self.accuracy(outputc)
        print("self.accuracy :", acc)
        print(self.cluster.cluster_centers_)
        plt.scatter(FinalDataset[:,0],FinalDataset[:,1], c=self.cluster.labels_, cmap='rainbow')

        plt.yticks([0,1,2,3,4,5,6,7,8,9,10])
        plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
        plt.xlabel("Technical skills")
        plt.ylabel("Verbal skills")
        plt.show()

    def retxyDF(self,d):
        df = pd.DataFrame(d)
        X =[]
        for i in range(df.shape[0]):
            X.append([df['Technical'][i],df['Verbal'][i]])
        X = np.array(X)
        return X

    def accuracy(self, output):
        r = 0
        import statistics as s
        d ={}
        d['tech'] = s.mode(output[:201])
        d['mass'] = s.mode(output[201:402])
        d['nontech'] = s.mode(output[402:])
        input = [d['tech']]*201 +[d['mass']]*201+[d['nontech']]*201
        print(input)
        for i in range(len(input)):
            if input[i] == output[i]:
                r += 1
        return r/len(input),d

    def predict(self, newpoint):
        newpoint = np.array(newpoint)
        i = 0
        if np.linalg.norm(self.cluster.cluster_centers_[i]-newpoint) > np.linalg.norm(self.cluster.cluster_centers_[1]-newpoint):
            i = 1
        if np.linalg.norm(self.cluster.cluster_centers_[i]-newpoint) > np.linalg.norm(self.cluster.cluster_centers_[2]-newpoint):
            i = 2
        
        if self.labels['tech'] ==  i:
            return 'tech'
        if self.labels['mass'] ==  i:
            return 'mass'
        if self.labels['nontech'] ==  i:
            return 'nontech'


if __name__ == "__main__":
    c = Cluster()
    print(c.predict([5,5]))

