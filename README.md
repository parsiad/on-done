# on-done

on-done is an IPython/Jupyter cell magic to execute code after a cell succeeds or fails.
It is especially useful if you need a way to alert yourself that your code has terminated.

It is inspired by [this Stack Overflow answer](https://stackoverflow.com/a/57365710) by [Colin Carroll](https://stackoverflow.com/a/57365710).

## Example Usage

Start by launching an IPython session:

```console
$ ipython
Python 3.10.5 (main, Jun  6 2022, 18:49:26) [GCC 12.1.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.4.0 -- An enhanced Interactive Python. Type '?' for help.
```

Then, load the extension:

```python
In [1]: %load_ext on_done
```

Next, define a function to alert you that your code has terminated.

```python
In [2]: from datetime import datetime
   ...: import sys
   ...:
   ...: def alert():
   ...:     sys.stderr.write(f'Cell terminated at {str(datetime.now())}\n')
```

Note that in the above, a message is written to stderr.
You may instead want to send yourself an email, text message, Slack alert, etc.

Let's test it:

```python
In [3]: %%on_done alert()
   ...: import numpy as np
   ...:
   ...: np.random.randn(10**8)
Cell terminated at 2022-07-20 13:31:45.690233
```
