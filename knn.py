import numpy as np
import collections

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
        distances_labels = self.distances(y)
        distances_labels = self.mergeSort(distances_labels)
        most_common_label = self.majority_vote(distances_labels, self.k)
        return most_common_label

    def distances(self, y):
        distances_labels = []
        for i, x in enumerate(self.m_X):
            distance_squared = 0
            for j in range(0, len(x)):
                distance_squared += (x[j] - y[j]) ** 2
            distance = np.sqrt(distance_squared)
            distances_labels.append((distance, self.m_labels[i]))
        return distances_labels

    def majority_vote(self, distances_labels, k):
        k_neighbors_labels = [label for distance, label in distances_labels[:k]]
        most_common_label, count = collections.Counter(k_neighbors_labels).most_common(1)[0]
        return most_common_label

    def mergeSort(self, distances_labels):
        if len(distances_labels) > 1:
            r = len(distances_labels) // 2
            L = distances_labels[:r]
            M = distances_labels[r:]

            L = self.mergeSort(L)
            M = self.mergeSort(M)

            i = j = 0
            sorted_distances_labels = []
            while i < len(L) and j < len(M):
                if L[i][0] < M[j][0]:
                    sorted_distances_labels.append(L[i])
                    i += 1
                else:
                    sorted_distances_labels.append(M[j])
                    j += 1
            while i < len(L):
                sorted_distances_labels.append(L[i])
                i += 1
            while j < len(M):
                sorted_distances_labels.append(M[j])
                j += 1
            return sorted_distances_labels
        else:
            return distances_labels
