<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.image.image_gradients" />
<meta itemprop="path" content="Stable" />
</div>

# tf.image.image_gradients

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/image_ops_impl.py">View source</a>



<!-- Start diff -->
Returns image gradients (dy, dx) for each color channel.

### Aliases:

* `tf.compat.v1.image.image_gradients`
* `tf.compat.v2.image.image_gradients`


``` python
tf.image.image_gradients(image)
```



<!-- Placeholder for "Used in" -->

Both output tensors have the same shape as the input: [batch_size, h, w,
d]. The gradient values are organized so that [I(x+1, y) - I(x, y)] is in
location (x, y). That means that dy will always have zeros in the last row,
and dx will always have zeros in the last column.

#### Arguments:


* <b>`image`</b>: Tensor with shape [batch_size, h, w, d].


#### Returns:

Pair of tensors (dy, dx) holding the vertical and horizontal image
gradients (1-step finite difference).



#### Raises:


* <b>`ValueError`</b>: If `image` is not a 4D tensor.