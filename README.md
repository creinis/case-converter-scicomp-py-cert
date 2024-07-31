## Convert to Snake Case

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Convert to Snake Case applications, follow the instructions in the Setup section below.

## Project Structure

- `convert_to_snake_case_iteration.py`: Contains the iteration approach to convert a PascalCase or camelCase string to snake_case.
- `convert_to_snake_case_list.py`: Contains the list comprehension approach to convert a PascalCase or camelCase string to snake_case.
- `compare_approaches.py`: Compares the execution time of both approaches and displays the results.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/case-converter-scicomp-py-cert.git
   cd expense-tracker-fcc-scicomp-py-cert
   ```

2. Run the comparison script to compare both approaches:
   ```bash
   python3 compare_approaches.py
   ```

## Functionality

This project showcases two different approaches to converting a PascalCase or camelCase string to snake_case. Consistent and clear naming conventions are crucial in programming as they improve code readability and maintainability. This project emphasizes the importance of such practices by providing a tool to transform strings into a standardized format.

### Iteration Approach

The iteration approach uses a loop to process each character in the string individually. If a character is uppercase, it is converted to lowercase and prefixed with an underscore. This method is straightforward and easy to understand, making it suitable for beginners.

#### Benefits

- **Clarity:** Each step is explicitly defined, making the code easy to follow.
- **Educational Value:** Helps beginners understand the process of string manipulation.

### List Approach

The list comprehension approach achieves the same result more concisely by using a single line of code to build the list of characters. This method is typically more efficient and utilizes Python's capabilities to produce more compact and potentially faster code.

#### Benefits

- **Conciseness:** Reduces the amount of code needed, making it more readable for those familiar with list comprehensions.
- **Efficiency:** Can be faster due to Python's optimization of list comprehensions.
- **Pythonic:** Follows the Python philosophy of writing clear and expressive code.

## Practical Use Case

These functions can be used in projects where consistent string formats are required, such as converting variable names to adhere to specific coding standards or ensuring compatibility with certain APIs that expect snake_case inputs.

## Comparison

Running `compare_approaches.py` will display the execution times of both approaches and indicate which one is faster and by how many times. This comparison provides valuable insights into the performance trade-offs between clarity and conciseness.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>