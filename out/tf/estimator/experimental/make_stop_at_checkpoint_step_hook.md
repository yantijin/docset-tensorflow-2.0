<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.estimator.experimental.make_stop_at_checkpoint_step_hook" />
<meta itemprop="path" content="Stable" />
</div>

# tf.estimator.experimental.make_stop_at_checkpoint_step_hook

<!-- Insert buttons -->

<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/hooks/hooks.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



<!-- Start diff -->
Creates a proper StopAtCheckpointStepHook based on chief status.

### Aliases:

* `tf.compat.v1.estimator.experimental.make_stop_at_checkpoint_step_hook`
* `tf.compat.v2.estimator.experimental.make_stop_at_checkpoint_step_hook`


``` python
tf.estimator.experimental.make_stop_at_checkpoint_step_hook(
    estimator,
    last_step,
    wait_after_file_check_secs=30
)
```



<!-- Placeholder for "Used in" -->
