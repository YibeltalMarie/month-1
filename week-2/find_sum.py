
#function to find the sum of the given list of numbers
def find_sum(list):
    sum_of_elements = 0
    for each_element in list:
        sum_of_elements += each_element
    return sum_of_elements

list1 = [1,2,3,4,5,6]
print(find_sum(list1))

# to find the first even numbers between 1 to 20
def print_even():
    for i in range(1,21):
        if i%2 == 0:
            print(i)
print_even()

# to find the maximum number in the given list
def find_maximum(list):
    max = 0
    for each_element in list:
        if each_element > max:
            max = each_element
    return max
    # or another method
    # return max(list)
print(find_maximum(list1))
