# Programming Assignment: Advanced List Operations with 2D Lists

## Objective

This assignment is designed to test your understanding of list operations, including 2D lists, using functions, decisions, loops, and various list methods in Python. You will perform a series of tasks involving list creation, manipulation, and querying.

## Problem Statement

You will work with a 2D list (matrix) and perform several operations such as calculating row sums, finding column maximums, flattening the matrix, modifying the list using list methods, and making decisions based on conditions.

### Tasks

1. **Create a 2D List**:

   - Write a function `create_2d_list(rows, cols)` that creates and returns a 2D list `matrix` with dimensions 4x4, filled with numbers from 1 to 16.

2. **Sum of a Row**:

   - Write a function `sum_of_row(matrix, row_index)` to return the sum of the elements in a specified row of the 2D list.

3. **Max in a Column**:

   - Write a function `max_in_column(matrix, col_index)` to return the maximum value in a specified column of the 2D list.

4. **Flatten the Matrix**:

   - Write a function `flatten_matrix(matrix)` to return a 1D list containing all elements of the 2D list.

5. **Modify the List**:

   - In the `main()` function, perform the following operations on the flattened list:
     - Append the number 99 to the list.
     - Insert the number 42 at the third position.
     - Sort the list.
     - Reverse the list.
     - Find the minimum and maximum values in the list.
     - Find the index of the number 42 in the list.

6. **Print Results**:

   - Print the original 2D list, the sum of the third row, the maximum of the last column, the flattened list, the modified list, the minimum and maximum values, and the index of 42.

7. **Decision Making**:
   - Check if the minimum value in the modified list is greater than 0 and print the result.

## Submission

- Clone the project
- Follow the instructions on the README.md file and the comment on code
  - Complete the code
  - You can look into the `test_assignment.py` for inspiratin too
- **Test the program**: by running `pytest`
  - If the test passes
    - Push the project to the repository
      - If this is hard
      - Submit the assignment.py on moodle
