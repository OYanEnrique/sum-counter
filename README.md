# sum-counter
A simple Python script demonstrating a sentinel-controlled loop. It sums and counts numbers provided by the user until the flag value 999 is entered.

# Sum and Count - Sentinel Loop Example

The program continuously prompts the user to enter numbers, adding them to a running total and counting each entry. The loop terminates when the user enters the special "sentinel" or "flag" value of `999`, at which point the final sum and count are displayed. It's a fundamental pattern for handling an unknown number of inputs.

## Features

-   Reads a stream of integer inputs from the user.
-   Calculates the cumulative sum of the numbers.
-   Counts how many numbers were entered.
-   Uses a sentinel value (`999`) to gracefully exit the input loop.
-   Outputs a final summary of the count and sum.

## How to Run

1.  Make sure you have [Python 3](https://www.python.org/downloads/) installed.
2.  Save the code as a Python file (e.g., `sum_counter.py`).
3.  Open your terminal or command prompt.
4.  Navigate to the directory containing the file.
5.  Execute the script with the command:
    ```bash
    python sum_counter.py
    ```

## Usage Example

You can enter as many numbers as you like. When you are finished, enter `999` to see the results.

```
Enter a number: [999 to stop]:
5
Enter a number: [999 to stop]
10
Enter a number: [999 to stop]
3
Enter a number: [999 to stop]
999
You entered 3 numbers and the sum of them was 18!
```
