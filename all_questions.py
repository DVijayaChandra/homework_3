# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "hierarchical clustering focuses on merging groups that share similarities, offering a more gradual and robust approach, whereas K-means can be influenced by individual data points, especially outliers, due to its reliance on proximity to centroids"

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "As both approaches carry the possibility of yielding varied results in successive runs"

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = " the introduction of a new centroid can result in an expanded distance between the centroid and the data points,So  Sum of Squared Residuals (SSE) might experience an increase"

    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "This is because the split aims to create two sub-clusters that are potentially more homogeneous, bringing the data points closer to their respective centroids. As a result, the overall sum of squared distances within each sub-cluster (SSE) may reduce, leading to a lower SSE for the entire clustering solution"
    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In K-means clustering, the objective is to minimize the Sum of Squared Errors (SSE), which is a measure of the total distance between data points.As SSE decreases, it implies that the data points are getting closer to their respective cluster centroids"

    # type: bool (True/False)
    answers["(f)"] = False

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "When clustering a dataset using K-means, whenever SSB increases, separation increases."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Improving cohesion (reducing SSE) focuses on making data points within a cluster more similar to each other. However, reducing SSE does not necessarily imply an improvement in separation (larger SSB). It is possible to have tight clusters (low SSE) without having well-separated clusters (large SSB)."

    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "SSE + BSS is constant because it equals TSS, but SSE and BSS individually are not constant and can change based on how well the data is clustered."


    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Increasing cohesion (reducing SSE) focuses on making data points within a cluster more similar to each other, but it doesn't necessarily imply an improvement in separation (larger SSB). "

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = " After completion of the k-means algorithm, each shaded circle will be associated with a single cluster centroid positioned at its center."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Upon the conclusion of the k-means algorithm, certain clusters among the final two may encompass points from both shaded regions."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "When the k-means algorithm completes, the final clustering for k-means contains an empty cluster."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = '4*R^2'

    # type: a string that evaluates to a float
    answers["(b) SSE"] = '4*squart(a^2+b^2)'

    # type: a string that evaluates to a float
    answers["(c) SSE"] = '10*R^2'

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "optimal clusturing will happen"

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Due to the comparable distances between circles A and B, as well as between circles B and C, each centroid is expected to converge within its respective original circle."

    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "For achieving optimal clustering, this distribution ensures that each centroid is closest to the cluster it initially belonged to"

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A","Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The shortest path separating the top left point in Group A from the top right point in Group B is the distance between them."

    # type: set
    answers["(b)"] = {'Group A','Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The longest distance between the bottom left point in Group C and the bottom right point in Group A is the separation between them."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E','B','F','G','C','L','M','I'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','E','F','G','D'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','D','E','F','G','I','J','L','M'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 exhibits the highest entropy, suggesting a diverse composition of land cover types within it."

    # type: string
    answers["(b)"] = "cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 demonstrates the lowest entropy, indicating a more homogeneous collection of land cover categories within it."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset-z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Blue color signifies short distances, indicating distinct and well-separated clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Varied color patterns indicate a different arrangement of clusters."

    # type: string
    answers["(a) Matrix 2"] = "Dataset-x"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Blue color signifies short distances, indicating distinct and well-separated clusters"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "All other colors indicate long distances, suggesting distinct boundaries between clusters."

    # type: string
    answers["(a) Matrix 3"] = "Dataset-y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Diagonal entry corresponds to the distance of a point from itself"

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Certain areas in green and yellow suggest clusters that overlap or are less clearly defined."

    # type: string
    answers["(b) Row 1"] = "Cluster-a"

    # type: string
    answers["(b) Row 2"] = "Cluster-b"

    # type: string
    answers["(b) Row 3"] = "Cluster-c"

    # type: string
    answers["(b) Row 4"] = "Cluster-d"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The diagonal entry appears less distinct, suggesting a lower level of cohesion within the cluster. In contrast, all off-diagonal entries exhibit various colors, signifying different distances from it (closest to B, followed by C, and furthest from A)."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The diagonal entry appears sharper, indicating a cohesive cluster. Out of the three off-diagonal entries, two share the same color, suggesting that two other clusters (A and C) are closer to it. Despite the off-diagonal entries indicating distances with A being less distinct, it is evident that the cluster is furthest from one other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The diagonal entry appears sharper, indicating a cohesive cluster. Out of the three off-diagonal entries, two share the same color, suggesting that two other clusters (B and D) are closer to it. Despite the off-diagonal entries indicating distances with A being less distinct, it is evident that the cluster is furthest from one other cluster (D)."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The diagonal entry appears less distinct, suggesting a lower level of cohesion within the cluster. In contrast, all off-diagonal entries exhibit various colors, signifying different distances from it (closest to C, followed by B, and furthest from A)."

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(b)"] = ['partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping', 'partial']

    # type: list
    answers["(e)"] = ['partitional', 'exclusive', 'complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Partitioning clustering is applicable when assigning letter grades in a class, ensuring that each student is placed in precisely one grade category with no overlap between the categories."

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In FIG B, the effectiveness of DBSCAN in identifying facial representations lies in its ability to evaluate the spatial density of the data points."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "It is a method that clusters similar data points to recognize patterns in a dataset. Concerning facial characteristics, k-means can be employed to identify patterns based on dimensions, positions, and shapes."

    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
