X = [[1,2],[3,2],[4,3],[7,2],[4,4],[8,1],[2,5],[8,2]]
labels = [1,1,3,2,3,1,0,1]
y = [[2,3],[2,3]]

neigh = KNN(k=3)
neigh.add_data(X, labels)
print(neigh.predict(y))