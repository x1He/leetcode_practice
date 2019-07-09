import numpy as np


def kmeans(data, k=2):
    def _distance(p1, p2):
        """
        Return Eclud distance between two points.
        p1 = np.array([0,0]), p2 = np.array([1,1]) => 1.414
        """
        tmp = np.sum((p1 - p2) ** 2)
        return np.sqrt(tmp)

    def _rand_center(data, k):
        """Generate k center within the range of data set."""
        n = data.shape[1]  # features
        centroids = np.zeros((k, n))  # init with (0,0)....
        for i in range(n):
            dmin, dmax = np.min(data[:, i]), np.max(data[:, i])
            centroids[:, i] = dmin + (dmax - dmin) * np.random.rand(k)
        return centroids

    def _converged(centroids1, centroids2):

        # if centroids not changed, we say 'converged'
        set1 = set([tuple(c) for c in centroids1])
        set2 = set([tuple(c) for c in centroids2])
        return (set1 == set2)

    n = data.shape[0]  # number of entries
    centroids = _rand_center(data, k)
    label = np.zeros(n, dtype=np.int)  # track the nearest centroid
    assement = np.zeros(n)  # for the assement of our model
    converged = False

    while not converged:
        old_centroids = np.copy(centroids)
        for i in range(n):
            # determine the nearest centroid and track it with label
            min_dist, min_index = np.inf, -1
            for j in range(k):
                dist = _distance(data[i], centroids[j])
                if dist < min_dist:
                    min_dist, min_index = dist, j
                    label[i] = j
            assement[i] = _distance(data[i], centroids[label[i]]) ** 2

        # update centroid
        for m in range(k):
            centroids[m] = np.mean(data[label == m], axis=0)
        converged = _converged(old_centroids, centroids)
    return centroids, label, np.sum(assement)