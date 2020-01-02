<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.maximum" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.layers.maximum

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/layers/merge.py">View source</a>



<!-- Start diff -->
Functional interface to the `Maximum` layer that computes

### Aliases:

* `tf.compat.v1.keras.layers.maximum`
* `tf.compat.v2.keras.layers.maximum`


``` python
tf.keras.layers.maximum(
    inputs,
    **kwargs
)
```



<!-- Placeholder for "Used in" -->

   the maximum (element-wise) list of `inputs`.

#### For example:



```python
input1 = tf.keras.layers.Input(shape=(16,))
x1 = tf.keras.layers.Dense(8, activation='relu')(input1) #shape=(None, 8)
input2 = tf.keras.layers.Input(shape=(32,))
x2 = tf.keras.layers.Dense(8, activation='relu')(input2) #shape=(None, 8)
max_inp=tf.keras.layers.maximum([x1,x2]) #shape=(None, 8)
out = tf.keras.layers.Dense(4)(max_inp)
model = tf.keras.models.Model(inputs=[input1, input2], outputs=out)
```

#### Arguments:


* <b>`inputs`</b>: A list of input tensors (at least 2) of same shape.
* <b>`**kwargs`</b>: Standard layer keyword arguments.


#### Returns:

A tensor (of same shape as input tensor) with the element-wise
maximum of the inputs.



#### Raises:


* <b>`ValueError`</b>: If input tensors are of different shape.