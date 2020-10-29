# All Occurrences of an Element in a List
# Create a function that returns the indices of all occurrences of an item in the list.

# Examples
# get_indices(["a", "a", "b", "a", "b", "a"], "a") ➞ [0, 1, 3, 5]

# get_indices([1, 5, 5, 2, 7], 7) ➞ [4]

# get_indices([1, 5, 5, 2, 7], 5) ➞ [1, 2]

# get_indices([1, 5, 5, 2, 7], 8) ➞ []

# Notes
# If an element does not exist in a list, return [].
# Lists are zero-indexed.
# Values in the list will be value-types (don't need to worry about nested lists).

def get_indices(arr, target):
  # create an empty list  
  occurrences_list = []
  for i in range(0,len(arr)):  
    # compare every item in the list with the target
    if arr[i] == target:
      # if they are equal then push it the empty list
      occurrences_list.append(i)
      
  print(occurrences_list)


get_indices(["a", "a", "b", "a", "b", "a"], "a") 
get_indices([1, 5, 5, 2, 7], 7)

get_indices([1, 5, 5, 2, 7], 5)

get_indices([1, 5, 5, 2, 7], 8)