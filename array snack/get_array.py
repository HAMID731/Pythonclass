def largest_element(lst):
    return max(lst)

def reverse_list(lst):
    return lst[::-1]

def element_occurs(lst, element):
    return element in lst

def odd_positions(lst):
    return lst[::2]

def even_positions(lst):
    return lst[1::2]

def running_total(lst):
    total = 0
    running_totals = []
    for num in lst:
        total += num
        running_totals.append(total)
    return running_totals

def is_palindrome(s):
    return s == s[::-1]

def sum_for_loop(lst):
    total = 0
    for num in lst:
        total += num
    return total

def sum_while_loop(lst):
    total = 0
    i = 0
    while i < len(lst):
        total += lst[i]
        i += 1
    return total

def concatenate_lists(lst1, lst2):
    return lst1 + lst2


lst = [1, 2, 3, 4, 5]
print(largest_element(lst)) 
print(reverse_list(lst))    
print(element_occurs(lst, 3))
print(odd_positions(lst))    
print(even_positions(lst))   
print(running_total(lst))    
print(is_palindrome("radar"))
print(sum_for_loop(lst))     
print(sum_while_loop(lst))   
print(concatenate_lists([1, 2], [3, 4]))    
 
