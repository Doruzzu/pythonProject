def eval_cat_err(y, yhat):
    """
    Calculate the categorization error
    Args:
      y    : (ndarray  Shape (m,) or (m,1))  target value of each example
      yhat : (ndarray  Shape (m,) or (m,1))  predicted value of each example
    Returns:|
      cerr: (scalar)
    """
    m = len(y)
    incorrect = 0
    for i in range(m):

        if y[i] != yhat[i]:
            incorrect += 1

    cerr = incorrect / m

    return (cerr)


model_r = Sequential(
    [
     Dense(120,activation='relu',kernel_regularizer=tf.keras.regularizers.l2(0.1)),
     Dense(40,activation='relu',kernel_regularizer=tf.keras.regularizers.l2(0.1)),
     Dense(6,activation='linear')
    ], name= None
)
model_r.compile(loss=SparseCategoricalCrossentropy(from_logits=True), optimizer=tf.keras.optimizers.Adam(learning_rate=0.01))
