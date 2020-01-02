<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.constraints.MinMaxNorm" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.keras.constraints.MinMaxNorm

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/constraints.py">View source</a>



## Class `MinMaxNorm`

<!-- Start diff -->
MinMaxNorm weight constraint.

Inherits From: [`Constraint`](../../../tf/keras/constraints/Constraint.md)

### Aliases:

* Class `tf.compat.v1.keras.constraints.MinMaxNorm`
* Class `tf.compat.v1.keras.constraints.min_max_norm`
* Class `tf.compat.v2.keras.constraints.MinMaxNorm`
* Class `tf.compat.v2.keras.constraints.min_max_norm`
* Class `tf.keras.constraints.min_max_norm`


<!-- Placeholder for "Used in" -->

Constrains the weights incident to each hidden unit
to have the norm between a lower bound and an upper bound.

#### Arguments:


* <b>`min_value`</b>: the minimum norm for the incoming weights.
* <b>`max_value`</b>: the maximum norm for the incoming weights.
* <b>`rate`</b>: rate for enforcing the constraint: weights will be
    rescaled to yield
    `(1 - rate) * norm + rate * norm.clip(min_value, max_value)`.
    Effectively, this means that rate=1.0 stands for strict
    enforcement of the constraint, while rate<1.0 means that
    weights will be rescaled at each step to slowly move
    towards a value inside the desired interval.
* <b>`axis`</b>: integer, axis along which to calculate weight norms.
    For instance, in a `Dense` layer the weight matrix
    has shape `(input_dim, output_dim)`,
    set `axis` to `0` to constrain each weight vector
    of length `(input_dim,)`.
    In a `Conv2D` layer with `data_format="channels_last"`,
    the weight tensor has shape
    `(rows, cols, input_depth, output_depth)`,
    set `axis` to `[0, 1, 2]`
    to constrain the weights of each filter tensor of size
    `(rows, cols, input_depth)`.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="/code/stable/tensorflow/python/keras/constraints.py">View source</a>

``` python
__init__(
    min_value=0.0,
    max_value=1.0,
    rate=1.0,
    axis=0
)
```

Initialize self.  See help(type(self)) for accurate signature.




## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/keras/constraints.py">View source</a>

``` python
__call__(w)
```

Call self as a function.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/keras/constraints.py">View source</a>

``` python
get_config()
```





