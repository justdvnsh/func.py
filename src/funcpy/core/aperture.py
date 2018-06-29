# **
#  * Chunks the list into array of arrays , depending on the n .
#  *
#  * @private
#  * @param {n} val The number to divide the array to.
#  * @param {lis} the list to be divided
#  * @return { list } the returned list of lists.
#  * @example
#  *
#  * aperture(10, [1,2,3,4,5,6,7,8,9,10,11] 
#  * [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]]
#  */

def aperture(n ,lis):
    idx = 0
    limit = len(lis) - ( n - 1 )
    acc = [0]*( limit if limit > 0 else 0 )
    while( idx < limit ):
        acc[idx] = lis[idx : idx + n]
        idx += 1
    
    return acc;

# print(aperture(10, [1,2,3,4,5,6,7,8,9,10,11]))