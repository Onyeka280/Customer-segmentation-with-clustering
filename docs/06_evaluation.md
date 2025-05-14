
---

### 📄 `docs/06_evaluation.md`

```markdown
# Evaluation

Evaluate the performance of clustering using silhouette scores and cross-tabulations.

## Silhouette Score

```python
from sklearn.metrics import silhouette_score

sil_score_kmeans = silhouette_score(X_scaled, data['kmeans_cluster'])
print("KMeans Silhouette Score:", sil_score_kmeans)

## Comparing Clustering Results

import pandas as pd

# Crosstab between KMeans and Hierarchical Clustering
pd.crosstab(data['kmeans_cluster'], data['hier_cluster'])
