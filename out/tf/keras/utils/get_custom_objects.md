<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.utils.get_custom_objects" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.utils.get_custom_objects

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/utils/generic_utils.py">View source</a>



<!-- Start diff -->
Retrieves a live reference to the global dictionary of custom objects.

### Aliases:

* `tf.compat.v1.keras.utils.get_custom_objects`
* `tf.compat.v2.keras.utils.get_custom_objects`


``` python
tf.keras.utils.get_custom_objects()
```



<!-- Placeholder for "Used in" -->

Updating and clearing custom objects using `custom_object_scope`
is preferred, but `get_custom_objects` can
be used to directly access `_GLOBAL_CUSTOM_OBJECTS`.

#### Example:



```python
    get_custom_objects().clear()
    get_custom_objects()['MyObject'] = MyObject
```

#### Returns:

Global dictionary of names to classes (`_GLOBAL_CUSTOM_OBJECTS`).