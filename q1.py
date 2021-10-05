# perfect numbers between 1 to n
# a perfect number is a number which is the sum of all its factors eg: 6

#delcared vars
perfectNums = []

#get n
n = int(input("Enter n :"))

#since 1 is a perfect num we add it to the list beforehand  
perfectNums.append(1)

#lets iterate all numbers from 1 to n
for x in range(2, n+1):
    facSum = 0 # declaring it here so that for every new number in 1 to n the sum of factors for that number is reset

    #for every iteration we are dealing with 1 number from 1 to n so lets get its factors now by using another loop 
    for y in range(1,x): #get factors 
        if x % y == 0:
            #print("factor of ", x ,"is: ", y)
            #we are getting the factors in variable y ONE AT A TIME .....so gotta store it somewhere else to add them up... lets say we have facSum
            facSum = facSum + y 
    #print("addition of factors of ", x ,"is: ", facSum)
    
    #check if the sum of factors of number x is equal to the number itself i.e x 
    #if yes simply add it to the list of perfect numbers 
    if facSum == x:
        perfectNums.append(x)

    
#finally display the list containing all perfect numbers 
print("Perfect numbers between 1 and ", n , "are :", perfectNums)

# Regards - Aakash Pacherkar :)