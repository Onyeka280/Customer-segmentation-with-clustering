# Clustering Methods

## KMeans Clustering

We use the KMeans algorithm to partition the data into a fixed number of clusters.

```python
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4, random_state=42)
kmeans_labels = kmeans.fit_predict(X_scaled)
data['kmeans_cluster'] = kmeans_labels

# Hierarchical Clustering
## We use agglomerative hierarchical clustering to group similar data points using a bottom-up approach.

from scipy.cluster.hierarchy import linkage, dendrogram, fcluster

linked = linkage(X_scaled, method='ward')

# Optional: Visualize the dendrogram
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.show()

## Extract clusters from the dendrogram:

data['hier_cluster'] = fcluster(linked, t=4, criterion='maxclust')


