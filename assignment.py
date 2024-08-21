# Programmer: Grace-Ann Morris 
# Course: CS701/GB-731, Dr. Yalew
# Date: August 20, 2024 
# Programming Assignment: 5

# Advanced List Operations with 2D Lists 
# Function that creates a 2D list filled with integers starting from 1.
def create_2d_list(rows, cols): 
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append((i * cols) + j + 1)
        matrix.append(row)
    return matrix

# Function that returns the sum of the elements in a specified row of a 2D list.
def sum_of_row(matrix, row_index): 
    row_sum = 0
    for num in matrix[row_index]:
        row_sum += num
    return row_sum

# Function that returns the maximum value in a specified column of a 2D list.
def max_in_column(matrix, col_index):
    max_value = matrix[0][col_index]
    for row in matrix:
        if row[col_index] > max_value:
            max_value = row[col_index]
    return max_value

# Function that returns a 1D list containing all elements of the 2D list.
def flatten_matrix(matrix):
    flat_list = []
    for row in matrix:
        for num in row:
            flat_list.append(num)
    return flat_list

def main():
    # Task 1: Create a 2D list of 4x4 initialized with numbers from 1 to 16
    matrix = create_2d_list(4, 4)
    # Task 2: Calculate the sum of the third row
    sum_third_row = sum_of_row(matrix, 2)
    # Task 3: Find the maximum element in the last column
    max_last_column = max_in_column(matrix, 3)
    # Task 4: Flatten the matrix into a 1D list
    flat_list = flatten_matrix(matrix)
    # Task 5: Perform list modifications
    # Append an element to the list
    flat_list.append(99)
    # Insert an element at a specific position
    flat_list.insert(2, 42)
    # Sort the list
    flat_list.sort()
    # Reverse the list
    flat_list.reverse()
    # Find the minimum and maximum elements
    min_value = min(flat_list)
    max_value = max(flat_list)
    # Find the index of a specific element
    index_of_42 = flat_list.index(42)
    # Print all results: 
    print("Original 2D List:")
    for row in matrix:
        print(row)
    print("Sum of the third row:", sum_third_row)
    print("Max of the last column:", max_last_column)
    print("Flattened List:", flat_list)
    print("Modified List:", flat_list)
    print("Minimum Value:", min_value)
    print("Maximum Value:", max_value)
    print("Index of 42:", index_of_42)

    # Task 6: Decision making - Check if the minimum value in the modified list is greater than 0
    is_min_greater_than_zero = min_value > 0
    print("Is the minimum value greater than 0?:", is_min_greater_than_zero)

if __name__ == "__main__":
    main()