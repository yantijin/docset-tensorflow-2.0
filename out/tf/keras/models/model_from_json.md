<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.keras.models.model_from_json" />
<meta itemprop="path" content="Stable" />
</div>

# tf.keras.models.model_from_json

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/keras/saving/model_config.py">View source</a>



<!-- Start diff -->
Parses a JSON model configuration file and returns a model instance.

### Aliases:

* `tf.compat.v1.keras.models.model_from_json`
* `tf.compat.v2.keras.models.model_from_json`


``` python
tf.keras.models.model_from_json(
    json_string,
    custom_objects=None
)
```



<!-- Placeholder for "Used in" -->


#### Arguments:


* <b>`json_string`</b>: JSON string encoding a model configuration.
* <b>`custom_objects`</b>: Optional dictionary mapping names
    (strings) to custom classes or functions to be
    considered during deserialization.


#### Returns:

A Keras model instance (uncompiled).
