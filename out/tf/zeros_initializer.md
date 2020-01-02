<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.zeros_initializer" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__call__"/>
<meta itemprop="property" content="from_config"/>
<meta itemprop="property" content="get_config"/>
</div>

# tf.zeros_initializer

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/init_ops_v2.py">View source</a>



## Class `zeros_initializer`

<!-- Start diff -->
Initializer that generates tensors initialized to 0.

Inherits From: [`Initializer`](../tf/keras/initializers/Initializer.md)

### Aliases:

* Class `tf.compat.v2.initializers.Zeros`
* Class `tf.compat.v2.initializers.zeros`
* Class `tf.compat.v2.keras.initializers.Zeros`
* Class `tf.compat.v2.keras.initializers.zeros`
* Class `tf.compat.v2.zeros_initializer`
* Class `tf.initializers.Zeros`
* Class `tf.initializers.zeros`
* Class `tf.keras.initializers.Zeros`
* Class `tf.keras.initializers.zeros`


<!-- Placeholder for "Used in" -->


## Methods

<h3 id="__call__"><code>__call__</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/ops/init_ops_v2.py">View source</a>

``` python
__call__(
    shape,
    dtype=tf.dtypes.float32
)
```

Returns a tensor object initialized as specified by the initializer.


#### Args:


* <b>`shape`</b>: Shape of the tensor.
* <b>`dtype`</b>: Optional dtype of the tensor. If not provided will return tensor
 of <a href="../tf.md#float32"><code>tf.float32</code></a>.

<h3 id="from_config"><code>from_config</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/ops/init_ops_v2.py">View source</a>

``` python
from_config(
    cls,
    config
)
```

Instantiates an initializer from a configuration dictionary.


#### Example:



```python
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

#### Args:


* <b>`config`</b>: A Python dictionary.
  It will typically be the output of `get_config`.


#### Returns:

An Initializer instance.


<h3 id="get_config"><code>get_config</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/ops/init_ops_v2.py">View source</a>

``` python
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.


#### Returns:

A JSON-serializable Python dict.



