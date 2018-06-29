import functools
import fastnumbers

_is_Number = functools.partial(fastnumbers.isint, num_only=True)