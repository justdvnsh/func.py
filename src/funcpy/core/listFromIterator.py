# **
#  * makes a list to the given iterator.
#  *
#  * @private
#  * @param {iter} the iterator , list is to made upon.
#  * @return { list } the iterated list.
#  * @example
#  *
#  * listFromIterator(10) 
#  * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  */

def listFromIterator(iter):
    lis = []
    for i in range(iter + 1):
        lis.append(i)
    return lis[1:]

# print(listFromIterator(10))