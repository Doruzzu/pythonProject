def compute_entropy(y):
    """
    Computes the entropy for

    Args:
       y (ndarray): Numpy array indicating whether each example at a node is
           edible (`1`) or poisonous (`0`)

    Returns:
        entropy (float): Entropy at that node

    """
    # You need to return the following variables correctly
    entropy = 0.
    if len(y) == 0:
        return 0
    else:
        p_1 = len(y[y == 1]) / len(y)
        if p_1 == 0 or p_1 == 1:
            return entropy
        else:
            entropy += -p_1 * np.log2(p_1) - (1 - p_1) * np.log2(1 - p_1)

    return entropy


def split_dataset(X, node_indices, feature):
    """
    Splits the data at the given node into
    left and right branches

    Args:
        X (ndarray):             Data matrix of shape(n_samples, n_features)
        node_indices (list):     List containing the active indices. I.e, the samples being considered at this step.
        feature (int):           Index of feature to split on

    Returns:
        left_indices (list):     Indices with feature value == 1
        right_indices (list):    Indices with feature value == 0
    """

    left_indices = []
    right_indices = []

    for i in node_indices:
        if X[i, feature] == 1:
            left_indices.append(i)
        else:
            right_indices.append(i)
    return left_indices, right_indices


def compute_information_gain(X, y, node_indices, feature):
    """
    Compute the information of splitting the node on a given feature

    Args:
        X (ndarray):            Data matrix of shape(n_samples, n_features)
        y (array like):         list or ndarray with n_samples containing the target variable
        node_indices (ndarray): List containing the active indices. I.e, the samples being considered in this step.

    Returns:
        cost (float):        Cost computed

    """
    # Split dataset
    left_indices, right_indices = split_dataset(X, node_indices, feature)

    # Some useful variables
    X_node, y_node = X[node_indices], y[node_indices]
    X_left, y_left = X[left_indices], y[left_indices]
    X_right, y_right = X[right_indices], y[right_indices]

    information_gain = 0

    w_left = len(X_left) / (len(X_left) + len(X_right))
    w_right = len(X_right) / (len(X_left) + len(X_right))

    entropy_node = compute_entropy(y_node)
    entropy_left = compute_entropy(y_left)
    entropy_right = compute_entropy(y_right)
    information_gain += entropy_node - (w_left * entropy_left + w_right * entropy_right)

    return information_gain


def get_best_split(X, y, node_indices):
    """
    Returns the optimal feature and threshold value
    to split the node data

    Args:
        X (ndarray):            Data matrix of shape(n_samples, n_features)
        y (array like):         list or ndarray with n_samples containing the target variable
        node_indices (ndarray): List containing the active indices. I.e, the samples being considered in this step.

    Returns:
        best_feature (int):     The index of the best feature to split
    """
    best_feature = -1

    info_gains = np.zeros(num_features)

    for feature in range(num_features):
        info_gains[feature] = compute_information_gain(X, y, node_indices, feature)

    if np.max(info_gains) == 0:
        return best_feature
    else:
        best_feature = np.argmax(info_gains)

    return best_feature