<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.layers.StackedRNNCells" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="output_size"/>
<meta itemprop="property" content="state_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="get_initial_state"/>
</div>

# tf.keras.layers.StackedRNNCells

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/layers/recurrent.py">View source</a>



## Class `StackedRNNCells`

<!-- Start diff -->
Wrapper allowing a stack of RNN cells to behave as a single cell.

Inherits From: [`Layer`](../../../tf/keras/layers/Layer.md)

### Aliases:

* Class `tf.compat.v1.keras.layers.StackedRNNCells`
* Class `tf.compat.v2.keras.layers.StackedRNNCells`


<!-- Placeholder for "Used in" -->

Used to implement efficient stacked RNNs.

#### Arguments:


* <b>`cells`</b>: List of RNN cell instances.


#### Examples:



```python
cells = [
    keras.layers.LSTMCell(output_dim),
    keras.layers.LSTMCell(output_dim),
    keras.layers.LSTMCell(output_dim),
]

inputs = keras.Input((timesteps, input_dim))
x = keras.layers.RNN(cells)(inputs)
```

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="/code/stable/tensorflow/python/keras/layers/recurrent.py">View source</a>

``` python
__init__(
    cells,
    **kwargs
)
```






## Properties

<h3 id="output_size"><code>output_size</code></h3>




<h3 id="state_size"><code>state_size</code></h3>






## Methods

<h3 id="get_initial_state"><code>get_initial_state</code></h3>

<a target="_blank" href="/code/stable/tensorflow/python/keras/layers/recurrent.py">View source</a>

``` python
get_initial_state(
    inputs=None,
    batch_size=None,
    dtype=None
)
```






