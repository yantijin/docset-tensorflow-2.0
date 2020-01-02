<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.tf_decorator.tf_stack.extract_stack" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.tf_decorator.tf_stack.extract_stack

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/util/tf_stack.py">View source</a>



<!-- Start diff -->
A lightweight, extensible re-implementation of traceback.extract_stack.

### Aliases:

* `tf.compat.v1.app.flags.tf_decorator.tf_stack.extract_stack`


``` python
tf.compat.v1.flags.tf_decorator.tf_stack.extract_stack(limit=None)
```



<!-- Placeholder for "Used in" -->

NOTE(mrry): traceback.extract_stack eagerly retrieves the line of code for
    each stack frame using linecache, which results in an abundance of stat()
    calls. This implementation does not retrieve the code, and any consumer
    should apply _convert_stack to the result to obtain a traceback that can
    be formatted etc. using traceback methods.

#### Args:


* <b>`limit`</b>: A limit on the number of frames to return.


#### Returns:

A list of 5-tuples
    (filename, lineno, name, frame_globals, func_start_lineno)
corresponding to the call stack of the current thread.  The returned tuples
have the innermost stack frame at the end, unlike the Python inspect
module's stack() function.
