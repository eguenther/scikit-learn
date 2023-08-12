"""
================
The Iris Dataset
================
This data sets consists of 3 different types of irises'
(Setosa, Versicolour, and Virginica) petal and sepal
length, stored in a 150x4 numpy.ndarray

The rows being the samples and the columns being:
Sepal Length, Sepal Width, Petal Length and Petal Width.

The below plot uses the first two features.
See `here <https://en.wikipedia.org/wiki/Iris_flower_data_set>`_ for more
information on this dataset.

"""

# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

# %%
# Setup: Import the iris dataset
# ------------------------------
from sklearn import datasets

iris = datasets.load_iris()


# %%
# Scatter Plot of the Iris dataset
# --------------------------------
import matplotlib.pyplot as plt  # noqa: E402

# unused but required import for doing 3d projections with matplotlib < 3.2
import mpl_toolkits.mplot3d  # noqa: F401, E402

# Prepare the plot size
plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points across the 1st and 2nd feature
# (sepal length and sepal width)
plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.xticks(())
plt.yticks(())
# Each point in the scatter plot refers to one of the 150 iris flowers
# in the dataset, with the color indicating their respective type
# (Setosa, Versicolour, and Virginica).
# Just based on the the 2 dimensions used in this plot - sepal width
# and sepal length - you can already see a patttern, but there's still
# overlap. Let's apply a PCA analysis to bettter differentiatte between
# the three types!

# %%
# Plot a PCA representation
# -------------------------
# Let's apply a PCA to the iris dataset and then plot the irises
# across the first three PCA dimensions.
# This will give us a better understanding of our analysis results.
from sklearn.decomposition import PCA  # noqa: E402

fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=iris.target,
    s=40,
)

ax.set_title("First three PCA dimensions")
ax.set_xlabel("1st Eigenvector")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("2nd Eigenvector")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("3rd Eigenvector")
ax.zaxis.set_ticklabels([])

plt.show()

# We've now applied a PCA analysis and plotted the irises
# along the first three dimensions (= Eigenvectors).
# Looks like the first dimension already does a pretty good job
# in differentiating the types of irises!

# %%
