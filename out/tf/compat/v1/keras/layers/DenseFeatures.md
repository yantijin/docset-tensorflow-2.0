<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.keras.layers.DenseFeatures" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
</div>

# tf.compat.v1.keras.layers.DenseFeatures

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/feature_column/dense_features.py">View source</a>



## Class `DenseFeatures`

<!-- Start diff -->
A layer that produces a dense `Tensor` based on given `feature_columns`.



<!-- Placeholder for "Used in" -->

Generally a single example in training data is described with FeatureColumns.
At the first layer of the model, this column oriented data should be converted
to a single `Tensor`.

This layer can be called multiple times with different features.

This is the V1 version of this layer that uses variable_scope's to create
variables which works well with PartitionedVariables. Variable scopes are
deprecated in V2, so the V2 version uses name_scopes instead. But currently
that lacks support for partitioned variables. Use this if you need
partitioned variables.

#### Example:



```python
price = numeric_column('price')
keywords_embedded = embedding_column(
    categorical_column_with_hash_bucket("keywords", 10K), dimensions=16)
columns = [price, keywords_embedded, ...]
feature_layer = DenseFeatures(columns)

features = tf.io.parse_example(..., features=make_parse_example_spec(columns))
dense_tensor = feature_layer(features)
for units in [128, 64, 32]:
  dense_tensor = tf.compat.v1.keras.layers.Dense(
                     units, activation='relu')(dense_tensor)
prediction = tf.compat.v1.keras.layers.Dense(1)(dense_tensor)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="/code/stable/tensorflow/python/feature_column/dense_features.py">View source</a>

``` python
__init__(
    feature_columns,
    trainable=True,
    name=None,
    **kwargs
)
```

Constructs a DenseFeatures layer.


#### Args:


* <b>`feature_columns`</b>: An iterable containing the FeatureColumns to use as
  inputs to your model. All items should be instances of classes derived
  from `DenseColumn` such as `numeric_column`, `embedding_column`,
  `bucketized_column`, `indicator_column`. If you have categorical
  features, you can wrap them with an `embedding_column` or
  `indicator_column`.
* <b>`trainable`</b>:  Boolean, whether the layer's variables will be updated via
  gradient descent during training.
* <b>`name`</b>: Name to give to the DenseFeatures.
* <b>`**kwargs`</b>: Keyword arguments to construct a layer.


#### Raises:


* <b>`ValueError`</b>: if an item in `feature_columns` is not a `DenseColumn`.



