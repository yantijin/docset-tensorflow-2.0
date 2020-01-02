<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.losses.categorical_hinge" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.losses.categorical_hinge

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/losses.py">View source</a>



<!-- Start diff -->
Computes the categorical hinge loss between `y_true` and `y_pred`.

### Aliases:

* `tf.compat.v1.keras.losses.categorical_hinge`
* `tf.compat.v2.keras.losses.categorical_hinge`
* `tf.compat.v2.losses.categorical_hinge`
* `tf.losses.categorical_hinge`


``` python
tf.keras.losses.categorical_hinge(
    y_true,
    y_pred
)
```



<!-- Placeholder for "Used in" -->


#### Args:


* <b>`y_true`</b>: The ground truth values. `y_true` values are expected to be -1 or 1.
  If binary (0 or 1) labels are provided they will be converted to -1 or 1.
* <b>`y_pred`</b>: The predicted values.


#### Returns:

A tensor.
