import numpy as np


class KNN:
    def __init__(self, k):
        self.k = k

    def add_data(self, X, labels):
        self.m_X = X
        self.m_labels = labels

    def predict(self, Y):
        predicted_labels = [self._predict(y) for y in Y]
        return predicted_labels

    def _predict(self, y):
        distances = self.distances(y)
        labels = self.mergeSort(distances, self.m_labels)
        return self.majority_vote(labels, self.k)

    def distances(self, y):
        distances = []
        for x in self.m_X:
            distance_squared = 0
            for i in range(0, len(x)):
                distance_squared += (x[i] - y[i]) ** 2
            distances.append(np.sqrt(distance_squared))
        return distances

    def majority_vote(self, labels, k):
        k_labels = labels[:k]
        labels_amount = dict()
        for label in k_labels:
            x = labels_amount.setdefault(label, 0)
            if x == 0:
                labels_amount.update({label: 1})
            else:
                labels_amount.update({label: x + 1})
        return max(labels_amount, key=lambda k: labels_amount[k])

    def mergeSort(self, values, labels):
        if len(values) > 1:
            r = len(values) // 2
            L = values[:r]
            M = values[r:]
            r2 = len(labels) // 2
            L2 = labels[:r2]
            M2 = labels[r2:]
            self.mergeSort(L, L2)
            self.mergeSort(M, M2)
            i = j = k = 0
            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    values[k] = L[i]
                    labels[k] = L2[i]
                    i += 1
                else:
                    values[k] = M[j]
                    labels[k] = M2[j]
                    j += 1
                k += 1
            while i < len(L) and i < len(L2):
                values[k] = L[i]
                labels[k] = L2[i]
                i += 1
                k += 1
            while j < len(M) and j < len(M2):
                values[k] = M[j]
                labels[k] = M2[j]
                j += 1
                k += 1
        return labels
