<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.gradients" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.gradients

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Returns the gradients of `loss` w.r.t. `variables`.

### Aliases:

* `tf.compat.v1.keras.backend.gradients`
* `tf.compat.v2.keras.backend.gradients`


``` python
tf.keras.backend.gradients(
    loss,
    variables
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`loss`</b>: Scalar tensor to minimize.
* <b>`variables`</b>: List of variables.


#### Returns:

A gradients tensor.
