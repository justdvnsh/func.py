Func.py
=============

A practical functional library for Python lovers.

Why Func.py?
----------

<img src="https://ramdajs.com/ramdaFilled_200x235.png" 
     width="170" height="190" align="right" hspace="12" />

There are already several excellent libraries with a functional flavor. Typically, they are meant to be general-purpose toolkits, suitable for working in multiple paradigms. Func.py has a more focused goal. We wanted a library designed specifically for a functional programming style, one that makes it easy to create functional pipelines, one that never mutates user data. 



What's Different?
-----------------

The primary distinguishing features of Func.py are:

* Func.py emphasizes a purer functional style. Immutability and side-effect free functions 
  are at the heart of its design philosophy. This can help you get the job done with simple, 
  elegant code.

* Func.py functions are automatically curried. This allows you to easily build up new functions 
  from old ones simply by not supplying the final parameters.

* The parameters to Func.py functions are arranged to make it convenient for currying. The data 
  to be operated on is generally supplied last.

The last two points together make it very easy to build functions as sequences of simpler functions, each of which transforms the data and passes it along to the next. Func.py is designed to support this style of coding.

Philosophy
----------
Using Func.py should feel much like just using Python.
It is practical, functional python. We're not introducing
lambda expressions in strings, we're not borrowing consed 
lists, we're not porting over all of the Clojure functions.

Our basic data structures are plain python objects, and our
usual collections are python arrays. We also keep other
native features of python, such as functions as objects
with properties.

Functional programming is in good part about immutable objects and 
side-effect free functions. While Func.py does not *enforce* this, it
enables such style to be as frictionless as possible.

We aim for an implementation both clean and elegant, but the API is king.
We sacrifice a great deal of implementation elegance for even a slightly
cleaner API.

Last but not least, Func.py strives for performance. A reliable and quick
implementation wins over any notions of functional purity.



Installation
------------

To use with pip:

```bash
pip install Func.py
```

Then in the console:

```python
import Func.py as fn
```

Or you can inject Func.py into virtually any unsuspecting website using [the bookmarklet](https://github.com/Func.py/Func.py/blob/master/BOOKMARKLET.md).

Documentation
-------------

Please review the [API documentation](https://justdvnsh.github.io/func.py).

Also available is our [Cookbook](https://github.com/Func.py/Func.py/wiki/Cookbook) of functions built from Func.py that you may find useful.

Running The Test Suite
----------------------

**Console:**

Tests are yet to be written


Usage
-----------------

```python
from func.py import * as fn 

identity = fn.identity
fn.map(identity, [1, 2, 3])
```

Destructuring imports from Func.py *does not necessarily prevent importing the entire library*. You can manually cherry-pick methods like the following, which would only grab the parts necessary for `identity` to work:

```py
from Func.py.src.identity import identity 

identity()
```

Manually cherry picking methods is cumbersome, however. Most bundlers like Webpack and Rollup offer tree-shaking as a way to drop unused Func.py code and reduce bundle size, but their performance varies, discussed [here](https://github.com/scabbiaza/Func.py-webpack-tree-shaking-examples). Here is a summary of the optimal setup based on what technology you are using:

1. Webpack + Babel - use [`babel-plugin-Func.py`](https://github.com/megawac/babel-plugin-Func.py) to automatically cherry pick methods. Discussion [here](http://www.andrewsouthpaw.com/2018/01/19/Func.py-tree-shaking-not-supported-out-of-the-box/), example [here](https://github.com/AndrewSouthpaw/Func.py-webpack-tree-shaking-examples/blob/master/07-webpack-babel-plugin-Func.py/package.json)
1. Webpack only - use `UglifyJS` plugin for treeshaking along with the `ModuleConcatenationPlugin`. Discussion [here](https://github.com/Func.py/Func.py/issues/2355), with an example setup [here](https://github.com/scabbiaza/Func.py-webpack-tree-shaking-examples/blob/master/06-webpack-scope-hoisted/webpack.config.js)
1. Rollup - does a fine job properly treeshaking, no special work needed; example [here](https://github.com/scabbiaza/Func.py-webpack-tree-shaking-examples/blob/master/07-rollup-Func.py-tree-shaking/rollup.config.js)

Translations
-----------------

Currently this library is only available in english. Please contribute to the library if you can translate into another language.