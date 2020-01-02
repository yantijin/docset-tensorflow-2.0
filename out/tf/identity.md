<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.identity" />
<meta itemprop="path" content="Stable" />
</div>

# tf.identity

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/array_ops.py">View source</a>



<!-- Start diff -->
Return a tensor with the same shape and contents as input.

### Aliases:

* `tf.compat.v1.identity`
* `tf.compat.v2.identity`


``` python
tf.identity(
    input,
    name=None
)
```



<!-- Placeholder for "Used in" -->


#### For example:



```python
import tensorflow as tf
val0 = tf.ones((1,), dtype=tf.float32)
a = tf.atan2(val0, val0)
a_identity = tf.identity(a)
print(a.numpy())          #[0.7853982]
print(a_identity.numpy()) #[0.7853982]
```

#### Args:


* <b>`input`</b>: A `Tensor`.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor`. Has the same type as `input`.
