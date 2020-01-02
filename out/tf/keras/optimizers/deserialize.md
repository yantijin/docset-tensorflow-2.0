<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.optimizers.deserialize" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.optimizers.deserialize

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/optimizers.py">View source</a>



<!-- Start diff -->
Inverse of the `serialize` function.

### Aliases:

* `tf.compat.v1.keras.optimizers.deserialize`
* `tf.compat.v2.keras.optimizers.deserialize`
* `tf.compat.v2.optimizers.deserialize`
* `tf.optimizers.deserialize`


``` python
tf.keras.optimizers.deserialize(
    config,
    custom_objects=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`config`</b>: Optimizer configuration dictionary.
* <b>`custom_objects`</b>: Optional dictionary mapping names (strings) to custom
  objects (classes and functions) to be considered during deserialization.


#### Returns:

A Keras Optimizer instance.
