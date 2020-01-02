<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.strings.length" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.strings.length

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/ops/string_ops.py">View source</a>



<!-- Start diff -->
String lengths of `input`.

``` python
tf.compat.v1.strings.length(
    input,
    name=None,
    unit='BYTE'
)
```



<!-- Placeholder for "Used in" -->

Computes the length of each string given in the input tensor.

#### Args:


* <b>`input`</b>: A `Tensor` of type `string`.
  The string for which to compute the length.
* <b>`unit`</b>: An optional `string` from: `"BYTE", "UTF8_CHAR"`. Defaults to `"BYTE"`.
  The unit that is counted to compute string length.  One of: `"BYTE"` (for
  the number of bytes in each string) or `"UTF8_CHAR"` (for the number of UTF-8
  encoded Unicode code points in each string).  Results are undefined
  if `unit=UTF8_CHAR` and the `input` strings do not contain structurally
  valid UTF-8.
* <b>`name`</b>: A name for the operation (optional).


#### Returns:

A `Tensor` of type `int32`.
