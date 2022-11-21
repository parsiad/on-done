<p align="center">
  <img alt="on-done" src="https://raw.githubusercontent.com/parsiad/on-done/master/logo.png">
</p>

An IPython/Jupyter cell magic to execute code after a cell succeeds or fails so you can receive an alert when your code terminates.

![](https://github.com/parsiad/on-done/blob/main/tty.gif?raw=true)

## Installation

```console
$ pip install on-done
```

## Example

Start by launching an IPython session:

```console
$ ipython
```

Then, load the extension:

```python
In [1]: %load_ext on_done
```

Next, define a function to alert you that your code has terminated.

```python
In [2]: def alert():
   ...:     from datetime import datetime
   ...:     print(f"Cell terminated at {str(datetime.now())}\n")
```

**You can change this function to send yourself an email, Slack alert, etc.**

Putting `%%on_done alert()` at the top of a cell will cause it to alert:

```python
In [3]: %%on_done alert()
   ...: import numpy as np
   ...: x = np.random.randn(10**8)
   ...: print(f"mean={x.mean()}")
mean=0.00021783589122321365
Cell terminated at 2022-11-21 00:35:40.678180
```

In particular, the alert will also occur if the cell failed:

```python
In [4]: %%on_done alert()
   ...: import numpy as np
   ...: x = np.random.randn(10**8)
   ...: print(f"mean={x.mean(axis=1)}")
Cell terminated at 2022-11-21 00:35:50.654766

---------------------------------------------------------------------------
AxisError                                 Traceback (most recent call last)
...
```

## Credit

on-done is inspired by [this Stack Overflow answer](https://stackoverflow.com/a/57365710) by [Colin Carroll](https://colindcarroll.com)
