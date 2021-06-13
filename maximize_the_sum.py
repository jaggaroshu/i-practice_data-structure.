# Maximize the sum
# link https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/maximize-sum-0423b95e/

# approach first.
# storing the value into array and sorting them and taking the sum of first K elements. 
# 
# points:- 
#   case not handaled :- 
#               i) here acc. to question we don't want K elemnts but we want K distinct elements i.e we can have more than K elemnt but the distinct number should not exceed than K 
#               
#  approach 2nd. 
#  storing them into array.
#  as we know the size of array will not exceed than 10**5, so we can have another array with size 10**5 where we can store all the value. 
#  now as we have the other array with the maximum capactiy now instead of storing the input values in this array we can simply store how occurance of the input array in the new array.
#  i.e  lets say my input_array = [5,4,3,4,3,2] and my k = 2
#  my new_array = [0,0,0,0,..... size 10**5]
#  now as we can see we have 5 one time and 4 2 times and 3 2 times and 2 one time.
#  so in the array i can have 
#  index                                        =   0   1    2    3     4    5 .... 10**5
#  occurance                                    =   0   0    1    2     2    1
#  sum(of the same number) = occurance* number  =   0   1    2    6     8    5
#  now we can see we can only take k = 2 distince number and we can take 3 and 4 as they are top 2. having sum = 14.
# 
#  points : - 
#       case not handled :- 
#                       but but in our array we are having negative numbers also so how do we store there count ??
#  but again this is the question of maximum sum so do we really need to include sum of negative number ??
#  no right as the decrease our sum. so that is edge case here.

