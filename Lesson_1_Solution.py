
list_int = [5.5,10.0,11.5,12.5,13.5,14,15.5,17.0]


#Code to count the number of even numbers in list_int
print (len((list(filter(lambda x: x % 2 == 0,list_int)))))


#Code to count the number of odd numbers in list_int
print (len((list(filter(lambda x: x % 2 != 0,list_int)))))

#Code to square the values in list_int
Square_of_list =list(map(lambda x:x**2, list_int))
print(Square_of_list)


#Code to cube the values in list_int
Cube_of_list =list(map(lambda x:x**3, list_int))
print(Cube_of_list)