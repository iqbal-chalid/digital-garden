# Debug Utility

A lightweight debugging helper for Python that focuses on **understanding code execution**, especially algorithms and recursive functions.

Unlike Python's `logging` module, this utility is designed to be **temporary**. It helps visualize execution flow while developing or debugging and is intended to be removed once the problem is solved.

> Think of it as a **debugging scalpel**, not a logging framework.

---

# Philosophy

This utility was created to answer questions like:

- Which function is currently executing?
- How deep is the recursion?
- Which values changed?
- Which branch was taken?
- What does the algorithm look like while running?

Instead of stepping through a debugger repeatedly, the execution becomes a readable trace.

---

# Features

- Function call tracing
- Automatic indentation
- Recursion level display
- Function call counter
- Global call counter
- Colored output
- Variable printing
- Condition highlighting
- List difference visualization
- List element highlighting
- Execution time measurement
- Function decorator
- Debug summary
- Enable / disable debugging

---

# Creating the debugger

```python
from utils.debug import Debug

DX = Debug()
```

---

# Function Tracing

## fx()

Marks the beginning of a function.

```python
DX.fx("partition")
```

Example output

```
0|Fx: quick_sort -> F1 : G1
  1|Fx: partition -> F1 : G2
    2|Fx: quick_sort -> F2 : G3
```

Where

- **Level** = recursion depth
- **F** = number of calls for that function
- **G** = global function call number

---

# Printing

## print()

```python
DX.print("Hello")
```

---

## print_val()

```python
DX.print_val("pivot", pivot)
```

Output

```
pivot : 8
```

---

## print_condition()

Useful for visualizing conditions.

```python
DX.print_condition("low < high", low < high)
```

Output

```
low < high
```

The text is printed

- green when True
- red when False

---

# Colored Messages

## print_cyan()

```python
DX.print_cyan("Partition")
```

Useful for

- titles
- function entries
- milestones

---

## print_green()

```python
DX.print_green("Success")
```

---

## print_red()

```python
DX.print_red("Failed")
```

---

# Lists

## print_list()

Highlights one element or a range of elements.

Highlight a single element

```python
DX.print_list("array", arr, 3)
```

Highlight a range

```python
DX.print_list("array", arr, [2, 5])
```

Example

```
array : [8, 3, 1, 7, 0, 10, 2]
```

where the selected elements are displayed in green.

---

## print_list_diff()

Displays two versions of a list while highlighting changed values.

```python
before = arr.copy()

...

after = arr.copy()

DX.print_list_diff(
    "array",
    after,
    before
)
```

Example

Before

```
[8, 3, 1, 7]
```

After

```
[3, 8, 1, 7]
```

Only the modified values are highlighted.

This is especially useful for

- Quick Sort
- Merge Sort
- Heap Sort
- Dynamic Programming
- State transitions

---

# Summary

## print_summary()

Prints a dictionary as a formatted summary.

```python
params = {
    "arr": arr,
    "len(arr)": len(arr),
}

DX.print_summary("INPUT", params)
```

Output

```
INPUT
arr : [8, 3, 1, 7]
len(arr) : 4
----------------------------------------
```

Useful for displaying

- function inputs
- configuration
- important state

---

# Enable / Disable

## ON()

Enable debugging.

```python
DX.ON()
```

---

## OFF()

Disable debugging.

```python
DX.OFF()
```

This allows temporary debugging without deleting the statements.

---

# Decorator

The utility also provides a decorator for tracing functions automatically.

Example

```python
@DX.debug(
    show_elapsed=True,
    show_args=True,
    show_return=True,
)
def partition(arr, low, high):
    ...
```

Available options

| Option       | Description                      |
| ------------ | -------------------------------- |
| show_elapsed | Display execution time           |
| show_args    | Display function arguments       |
| show_return  | Display returned value           |
| name         | Override displayed function name |

Example output

```
0|Fx: partition -> F1 : G1

args : ([8,3,1], 0, 2)

...

⏱️ partition -- elapsed : 0.000013 sec (G1)

return : 2
```

---

# Utility Functions

## line()

Prints a separator.

```python
DX.line()
```

Output

```
--------------------------------------------------------------------------------
```

Custom length

```python
DX.line(40)
```

---

## space()

Prints a blank line.

```python
DX.space()
```

---

## reset()

Resets all internal counters and state.

```python
DX.reset()
```

Resets

- indentation
- recursion level
- print counter
- function counters
- global counters

---

# Example

```python
def partition(arr, low, high):

    DX.fx("partition")

    pivot = arr[high]

    DX.print(f"{low=} {high=} {pivot=}")

    DX.print_val("i", i)

    before = arr.copy()

    ...

    after = arr.copy()

    DX.print_list_diff(
        "arr",
        after,
        before
    )
```

Produces output similar to

```
Fx: partition

low=0 high=6 pivot=2

i : -1

arr :
[1, 0, 8, 7, 3, 10, 2]

arr :
[1, 0, 2, 7, 3, 10, 8]
```

---

# Typical Usage

This utility works particularly well for

- Quick Sort
- Merge Sort
- Binary Search
- DFS
- BFS
- Dijkstra
- A\*
- Tree Traversal
- Backtracking
- Dynamic Programming
- Graph Algorithms
- General recursion

---

# Design Goals

This utility intentionally does **not** try to replace the standard `logging` module.

Instead, it focuses on:

- minimal API
- quick instrumentation
- easy removal
- readable execution traces
- recursive algorithm visualization
- developer productivity

It is designed for the period **between writing the code and deleting the debug statements**.
