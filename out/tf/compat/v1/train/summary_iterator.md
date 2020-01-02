<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.train.summary_iterator" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.train.summary_iterator

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/summary/summary_iterator.py">View source</a>



<!-- Start diff -->
An iterator for reading `Event` protocol buffers from an event file.

``` python
tf.compat.v1.train.summary_iterator(path)
```



<!-- Placeholder for "Used in" -->

You can use this function to read events written to an event file. It returns
a Python iterator that yields `Event` protocol buffers.

Example: Print the contents of an events file.

```python
for e in tf.compat.v1.train.summary_iterator(path to events file):
    print(e)
```

Example: Print selected summary values.

```python
# This example supposes that the events file contains summaries with a
# summary value tag 'loss'.  These could have been added by calling
# `add_summary()`, passing the output of a scalar summary op created with
# with: `tf.compat.v1.summary.scalar('loss', loss_tensor)`.
for e in tf.compat.v1.train.summary_iterator(path to events file):
    for v in e.summary.value:
        if v.tag == 'loss':
            print(v.simple_value)
```

See the protocol buffer definitions of
[Event](https://www.tensorflow.org/code/tensorflow/core/util/event.proto)
and
[Summary](https://www.tensorflow.org/code/tensorflow/core/framework/summary.proto)
for more information about their attributes.

#### Args:


* <b>`path`</b>: The path to an event file created by a `SummaryWriter`.


#### Yields:

`Event` protocol buffers.