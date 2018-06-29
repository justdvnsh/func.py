# **
#  * Tests whether or not an object is an array.
#  *
#  * @private
#  * @param {*} val The object to test.
#  * @return {Boolean} `true` if `val` is a list, `false` otherwise.
#  * @example
#  *
#  *      _isList([]); //=> true
#  *      _isList(None); //=> false
#  *      _isList({}); //=> false
#  */

def isList(val):
    return ( val != None and len(val) >= 0 and isinstance(val, list))

# print(isList([]))
# print(len([]))
# print(isinstance([], list))