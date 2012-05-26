#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 8
# found online at projecteuler.net/problem=8
# Solution by Timothy Reasa
#
###############################################################################


description = \
'Find the greatest product of five consecutive digits in the 1000-digit\n' + \
'number.\n\n' + \
'\t73167176531330624919225119674426574742355349194934\n' + \
'\t96983520312774506326239578318016984801869478851843\n' + \
'\t85861560789112949495459501737958331952853208805511\n' + \
'\t12540698747158523863050715693290963295227443043557\n' + \
'\t66896648950445244523161731856403098711121722383113\n' + \
'\t62229893423380308135336276614282806444486645238749\n' + \
'\t30358907296290491560440772390713810515859307960866\n' + \
'\t70172427121883998797908792274921901699720888093776\n' + \
'\t65727333001053367881220235421809751254540594752243\n' + \
'\t52584907711670556013604839586446706324415722155397\n' + \
'\t53697817977846174064955149290862569321978468622482\n' + \
'\t83972241375657056057490261407972968652414535100474\n' + \
'\t82166370484403199890008895243450658541227588666881\n' + \
'\t16427171479924442928230863465674813919123162824586\n' + \
'\t17866458359124566529476545682848912883142607690042\n' + \
'\t24219022671055626321111109370544217506941658960408\n' + \
'\t07198403850962455444362981230987879927244284909188\n' + \
'\t84580156166097919133875499200524063689912560717606\n' + \
'\t05886116467109405077541002256983155200055935729725\n' + \
'\t71636269561882670428252483600823257530420752963450\n'

def display(self):
    return description

magic = '7316717653133062491922511967442657474235534919493496983520312774' + \
'506326239578318016984801869478851843858615607891129494954595017379583319' + \
'528532088055111254069874715852386305071569329096329522744304355766896648' + \
'950445244523161731856403098711121722383113622298934233803081353362766142' + \
'828064444866452387493035890729629049156044077239071381051585930796086670' + \
'172427121883998797908792274921901699720888093776657273330010533678812202' + \
'354218097512545405947522435258490771167055601360483958644670632441572215' + \
'539753697817977846174064955149290862569321978468622482839722413756570560' + \
'574902614079729686524145351004748216637048440319989000889524345065854122' + \
'758866688116427171479924442928230863465674813919123162824586178664583591' + \
'245665294765456828489128831426076900422421902267105562632111110937054421' + \
'7506941658960408'

def solve(self):
    maxProduct = 0

    for index in range(5, len(magic)):
        product = int(magic[index-5]) * int(magic[index-4]) * \
		int(magic[index-3]) * int(magic[index-2]) * \
		int(magic[index-1])
        if product > maxProduct:
	    maxProduct = product

    return maxProduct


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
