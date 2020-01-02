<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.flags.tf_decorator.tf_stack.extract_stack_file_and_line" />
<meta itemprop="path" content="Stable" />
</div>

# tf.compat.v1.flags.tf_decorator.tf_stack.extract_stack_file_and_line

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">
</table>

<a target="_blank" href="/code/stable/tensorflow/python/util/tf_stack.py">View source</a>



<!-- Start diff -->
A version of extract_stack that only returns filenames and line numbers.

### Aliases:

* `tf.compat.v1.app.flags.tf_decorator.tf_stack.extract_stack_file_and_line`


``` python
tf.compat.v1.flags.tf_decorator.tf_stack.extract_stack_file_and_line(max_length=1000)
```



<!-- Placeholder for "Used in" -->

Callers often only require filenames and line numbers, and do not need the
additional information gathered by extract_stack, as they never call
convert_stack.

As a further optimisation, we allow users to specify a limit on the number of
frames examined.

#### Args:


* <b>`max_length`</b>: The maximum length of stack to extract.


#### Returns:

A list of FileAndLine objects corresponding to the call stack of the current
thread.
