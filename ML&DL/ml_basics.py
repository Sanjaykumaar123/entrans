import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification, load_iris, make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import tensorflow as tf

print("\n--- Linear Regression (Scikit-Learn) ---")
X = np.array([[1],[2],[3],[4],[5]])
y = np.array([3,5,7,9,11])
lr_model = LinearRegression()
lr_model.fit(X, y)
print("Coef:", lr_model.coef_)
print("Intercept:", lr_model.intercept_)
print("Prediction (x=6):", lr_model.predict([[6]]))


print("\n--- Linear Regression (Keras) ---")
Xk = np.array([1,2,3,4,5], dtype=float)
yk = np.array([3,5,7,9,11], dtype=float)

keras_model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=[1]),
    tf.keras.layers.Dense(1)
])

keras_model.compile(optimizer='adam', loss='mse')
keras_model.fit(Xk, yk, epochs=200, verbose=0)

print(keras_model.predict(np.array([[6.0]])))


print("\n--- Logistic Regression ---")
Xc, yc = make_classification(
    n_samples=300,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1
)
Xc_train, Xc_test, yc_train, yc_test = train_test_split(Xc, yc, test_size=0.2)

log_model = LogisticRegression()
log_model.fit(Xc_train, yc_train)

print("Accuracy:", log_model.score(Xc_test, yc_test))


print("\n--- Regularization (Ridge & Lasso) ---")
ridge = Ridge(alpha=1.0)
lasso = Lasso(alpha=0.1)

ridge.fit(Xc_train, yc_train)
lasso.fit(Xc_train, yc_train)

print("Ridge Score:", ridge.score(Xc_test, yc_test))
print("Lasso Score:", lasso.score(Xc_test, yc_test))


print("\n--- KNN (K-Nearest Neighbors) ---")
iris = load_iris()
X_knn, y_knn = iris.data, iris.target

knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_knn, y_knn)

print("Prediction:", knn_model.predict([X_knn[0]]))


print("\n--- K-Means Clustering ---")
Xkmeans, _ = make_blobs(n_samples=200, centers=3)

kmeans_model = KMeans(n_clusters=3)
labels = kmeans_model.fit_predict(Xkmeans)

print("Cluster labels (first 10):", labels[:10])


print("\n--- PCA (Dimensionality Reduction) ---")
iris = load_iris()
X_pca = iris.data

pca_model = PCA(n_components=2)
X2 = pca_model.fit_transform(X_pca)

print("PCA transformed (first 5 rows):")
print(X2[:5])
