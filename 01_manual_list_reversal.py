number = [ 10 , 20 , 30 , 40 , 50 ]
start_index = 0 # sets index 
end_index = 4
temp = [] # Empty list

while start_index < end_index:
    # Logic for swaping 
    temp = number[ start_index] 
    number[start_index] = number[end_index]
    number[end_index] = temp

    start_index = start_index +1
    end_index = end_index - 1

print(number)
