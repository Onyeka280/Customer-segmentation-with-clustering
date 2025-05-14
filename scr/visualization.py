import matplotlib.pyplot as plt
import seaborn as sns

def plot_clusters(X, labels, method="PCA"):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=X[:,0], y=X[:,1], hue=labels, palette='viridis')
    plt.title(f"{method} Clustering Plot")
    plt.show()
