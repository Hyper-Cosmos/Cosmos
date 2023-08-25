import numpy as np
import random
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfTransformer

class GreyWolfOptimize:
    def __init__(self, varRangesC,varRangesG):
        self.lowerBoundC = varRangesC[0]
        self.upperBoundC = varRangesC[1]
        self.lowerBoundG = varRangesG[0]
        self.upperBoundG = varRangesG[1]
        
    def read_dataset(filename):
        with open(filename, "r") as f:
            data = f.readlines()
        dataset = [line.strip().split(";") for line in data]
        for row in dataset:
            if len(row) != len(dataset[0]):
                raise ValueError("All rows in the dataset must have the same number of columns.")
        dataset = np.array(dataset)

        return dataset
    
    def initializingPop(self):
        tabulist = []
        for _ in range (5):
            randomVariableDesignC = float(random.uniform(self.lowerBoundC, self.upperBoundC))
            randomVariableDesignG = float(random.uniform(self.lowerBoundG, self.upperBoundG))
            roundedRandomVariableDesignC = round(randomVariableDesignC, 2)
            roundedRandomVariableDesignG = round(randomVariableDesignG, 2)
            # print("Output C: ",roundedRandomVariableDesignC, "Output G:",roundedRandomVariableDesignG)
            tabulist.append([roundedRandomVariableDesignC, roundedRandomVariableDesignG])

        return tabulist

    def mainGWO(self):
        if __name__ == "__main__":  
            filename = "UCP_Dataset.csv"
            dataset = read_dataset(filename)
            vectorizer = TfidfTransformer()
            x = vectorizer.fit_transform(dataset['content_normal'])
            y = dataset['label']
            
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0)
            clf = svm.SVC(kernel='linear')
            clf.fit(x_train, y_train)
            y_pred = clf.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
             
            print(accuracy)
        
            
        # populasi_awal = run.initializingPop()
        # print(populasi_awal)
        
varRangesC = [0.01,100]
varRangesG = [0.01,50]

run = GreyWolfOptimize(varRangesC,varRangesG)

run.mainGWO()