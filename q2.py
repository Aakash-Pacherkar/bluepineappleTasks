#finding total occurences of each digit 0-9 using function

#function to count the occ of a digit in n
def mycounter(n, d):
    count = 0 
    while n>0:
        #check if the digit is d
        if n%10 == d: #last digit of n
            count += 1;

        n = n//10 #remove the last digit of n now .......coz we r done checking it (floor div) 

    #return the occurences of d in n
    return count


#get n from user 
n = int(input("Enter n :"))

# lets loop from 0 to 9 
for x in range(10):
    #call a function which takes the input number and the digit to count in it
    #here our x is our digit whose occurances our func will count
    res = mycounter(n,x)
    
    #to avoid printing msg for numbers which have occured zero times apply a condition
    if res > 0:
        print(x," occured ",res,"times in ",n)
