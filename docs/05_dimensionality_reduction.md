
---

### 📄 `docs/05_dimensionality_reduction.md`

```markdown
# Dimensionality Reduction

Dimensionality reduction helps visualize high-dimensional data in 2D or 3D space.

## PCA (Principal Component Analysis)

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

data['pca1'] = X_pca[:, 0]
data['pca2'] = X_pca[:, 1]

## t-SNE (t-distributed Stochastic Neighbor Embedding)

from sklearn.manifold import TSNE

tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

data['tsne1'] = X_tsne[:, 0]
data['tsne2'] = X_tsne[:, 1]
