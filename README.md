lamderp
=======

Simple easy python lambda DSL

Usage
-----
Lambderp is very easy to use, and models small lambda functions easily.
```Python
from lamderp import _

identity = _
even = filter(_ % 2 == 0, range(50))
odd = filter(_ % 2 == 1, range(50))

square = _ ** 2
```

Install
-------
`pip install lamderp`

Why
---
Python lambda syntax is _ugly_ and makes functional programming painful.
