A = set(input().split())#first set of numbers
B = set(input().split())#second set of numbers
z = []#empty list that will be used for the answer
m = 0#this will help sort the variables while creating the new list


C1 = A.intersection(B)#creates a new set of numbers that are both in B and A
C = sorted(C1) #sorts them

c = list(C)#turns the set into a list
x = len(c)#finds the number of items in list


for i in range(x):#for i in range of the list numbers
  q = c[i]#q will equal the list item
  if int(q) > m:#turn the item into an intiger and compare it to the lowest value
    z.append(int(q))# if it's larger then add it  to the empty list
    
    
print(sorted(z))#print the list after it is made and sorted


  
  
