lamderp
=======

Simple easy python lambda DSL

Usage
-----
Lambderp is very easy to use, and models small lambda functions easily.
```Python
from lambderp import _

even = filter(_ % 2 == 0, range(50))
odd = filter(_ % 2 == 1, range(50))
```