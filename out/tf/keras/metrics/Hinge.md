<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.metrics.Hinge" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="reset_states"/>
<meta itemprop="property" content="result"/>
<meta itemprop="property" content="update_state"/>
</div>

# tf.keras.metrics.Hinge

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/metrics.py">View source</a>



## Class `Hinge`

<!-- Start diff -->
Computes the hinge metric between `y_true` and `y_pred`.



### Aliases:

* Class `tf.compat.v1.keras.metrics.Hinge`
* Class `tf.compat.v2.keras.metrics.Hinge`
* Class `tf.compat.v2.metrics.Hinge`
* Class `tf.metrics.Hinge`


<!-- Placeholder for "Used in" -->

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are
provided we will convert them to -1 or 1.

For example, if `y_true` is [-1., 1., 1.], and `y_pred` is [0.6, -0.7, -0.5]
the hinge metric value is 1.6.

#### Usage:



```python
m = tf.keras.metrics.Hinge()
m.update_state([-1., 1., 1.], [0.6, -0.7, -0.5])

# result = max(0, 1-y_true * y_pred) = [1.6 + 1.7 + 1.5] / 3

print('Final result: ', m.result().numpy())  # Final result: 1.6
```

Usage with tf.keras API:

```python
model = tf.keras.Model(inputs, outputs)
model.compile('sgd', metrics=[tf.keras.metrics.Hinge()])
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="/code/stable/tensorflow/python/keras/metrics.py">View source</a>

``` python
__init__(
    name='hinge',
    dtype=None
)
```

Creates a `MeanMetricWrapper` instance.


#### Args:


* <b>`fn`</b>: The metric function to wrap, with signature
  `fn(y_true, y_pred, **kwargs)`.
* <b>`name`</b>: (Optional) string name of the metric instance.
* <b>`dtype`</b>: (Optional) data type of the metric result.
* <b>`**kwargs`</b>: The keyword arguments that are passed on to `fn`.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="/code/stable/tensorflow/python/keras/metrics.py">View source</a>

``` python
__new__(
    cls,
    *args,
    **kwargs
)
```

Create and return a new object.  See help(type) for accurate signature.




## Methods

<h3 id="reset_states"><code>reset_states</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/keras/metrics.py">View source</a>

``` python
reset_states()
```

Resets all of the metric state variables.

This function is called between epochs/steps,
when a metric is evaluated during training.

<h3 id="result"><code>result</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/keras/metrics.py">View source</a>

``` python
result()
```

Computes and returns the metric value tensor.

Result computation is an idempotent operation that simply calculates the
metric value using the state variables.

<h3 id="update_state"><code>update_state</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/keras/metrics.py">View source</a>

``` python
update_state(
    y_true,
    y_pred,
    sample_weight=None
)
```

Accumulates metric statistics.

`y_true` and `y_pred` should have the same shape.

#### Args:


* <b>`y_true`</b>: The ground truth values.
* <b>`y_pred`</b>: The predicted values.
* <b>`sample_weight`</b>: Optional weighting of each example. Defaults to 1. Can be
  a `Tensor` whose rank is either 0, or the same rank as `y_true`,
  and must be broadcastable to `y_true`.


#### Returns:

Update op.




