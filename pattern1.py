# Pattern 1
'''
########*########
#######***#######
######*****######
#####*******#####
####*********####
###***********###
##*************##
#***************#
*****************
#***************#
##*************##
###***********###
####*********####
#####*******#####
######*****######
#######***#######
########*########
'''
str1 = '#'
str2 = '*'
display_str = ' '
# num2 = input("Enter number of line:")
# print(type(num2))
# num1 = int(num2)
num1 = int (input("Enter number of line:"))
# num1 = 9
 
j=0
while j < num1 :
    display_str = str1 * (num1 - j) + str2 * (j*2 + 1) + str1 * (num1 - j)
    print(display_str)
    j= j + 1

display_str = str2 * (j *2 + 1)
print(display_str)

i = num1 
while i > 0 :
    display_str = str1 * (num1 - i + 1) + str2 * (i * 2 -1) + str1 * (num1 - i + 1)
    print(display_str)
    i = i - 1
# display_str = str1 * 2 (i*2+1)
# print(display_str)
