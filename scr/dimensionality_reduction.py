from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def apply_pca(X_scaled):
    pca = PCA(n_components=2)
    return pca.fit_transform(X_scaled)

def apply_tsne(X_scaled):
    tsne = TSNE(n_components=2, random_state=42)
    return tsne.fit_transform(X_scaled)
