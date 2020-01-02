<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.backend.print_tensor" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.backend.print_tensor

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/backend.py">View source</a>



<!-- Start diff -->
Prints `message` and the tensor value when evaluated.

### Aliases:

* `tf.compat.v1.keras.backend.print_tensor`
* `tf.compat.v2.keras.backend.print_tensor`


``` python
tf.keras.backend.print_tensor(
    x,
    message=''
)
```



<!-- Placeholder for "Used in" -->

Note that `print_tensor` returns a new tensor identical to `x`
which should be used in the following code. Otherwise the
print operation is not taken into account during evaluation.

#### Example:



```python
   >>> x = K.print_tensor(x, message="x is: ")
```

#### Arguments:


* <b>`x`</b>: Tensor to print.
* <b>`message`</b>: Message to print jointly with the tensor.


#### Returns:

The same tensor `x`, unchanged.
