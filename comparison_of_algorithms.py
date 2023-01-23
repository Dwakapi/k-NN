import numpy as np
from sklearn.neighbors import KNeighborsClassifier
#from knn import KNN

# dane treningowe
X = [[-0.755361772373776, -0.110758570439906], [0.652678337192101, -0.0351242864470454], [-0.0220014124195332, -0.494010408199842], [-0.478607087365011, 0.586726870177197],[0.627484497857731, -0.482938788853083], [-0.0491722308941985, 0.521089586021265], [-0.0592987675192851, 0.242890283245286], [-0.332063573997143, 0.324661270569826], [0.787934740072651, 0.627094056773882], [-0.0865488968289083, 0.177448746648886], [-0.501029335965194, 0.322094965589177], [-0.911373814855242, 0.353514283057417], [-0.342747498243968, 0.531552713606467], [-0.0591377434972606, 0.191903449038155], [0.654634093345164, 0.0261765222792463], [0.455695502916498, -0.0125975055587794], [0.334697279083480, -0.307612112312620], [0.228610493066602, -0.821865064077959], [-0.236290024972645, 0.776697373869424], [0.244289492248572, -0.357308429681734]]
labels = [1, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2]

# dane testowe
Y = [[0,0], [-0.2, 0.2], [0.4,0], [2,1], [0,0.4], [-0.2, 1], [1.4,2],[-2.2, 1],[0.2, 1.2],[-0.2, 1.6],[-0.2, -0.3]]
n = len(Y)

#implementacja algorytmu K-NN z biblioteki sklearn
sklearn_knn = KNeighborsClassifier(n_neighbors=3)
sklearn_knn.fit(X, labels)
sklearn_labels = sklearn_knn.predict(Y)

#implementaja naszego algorytmu K-NN
our_knn = KNN(k=3)
our_knn.add_data(X, labels)
our_labels = our_knn.predict(Y)

#porównani tych dwóch algorytmów
good = 0

for i in range(0, n):
  if our_labels[i] == sklearn_labels[i]:
    good += 1

print("Wyniki naszego algorytmu pokrywają się z wynikami algorytmu z bibloteki sklearn w " + str(good/n*100) + "%")
print(good)

