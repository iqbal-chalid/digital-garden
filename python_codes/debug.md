# Debug Utility

A lightweight debugging helper for Python that focuses on **visual tracing** rather than full-featured logging.

The goal is to make it easy to understand recursive algorithms, sorting algorithms, tree traversals, graph searches, or any complex execution flow by producing readable, indented output.

---

# Philosophy

Instead of writing many `print()` statements such as

```python
print("Enter function")
print(i)
print(arr)
print(result)
```

this helper provides a consistent interface that automatically handles

- indentation
- function hierarchy
- colored output
- variable formatting
- execution counter
- list comparison

It is designed for developers who want to debug algorithms quickly without setting up a debugger.

---

# Features

- Automatic indentation
- Function call tracing
- Colored messages
- Variable printing
- List difference visualization
- Enable/disable debugging
- Print counter

---

# Creating the debugger

```python
from utils.debug import Debug

DX = Debug()
```

---

# Function Reference

## fx(message)

Marks the beginning of a function.

- Prints the function name in cyan.
- Automatically increases indentation.

```python
DX.fx("partition")
```

Output

```
Fx: partition
```

Nested calls become

```
Fx: quick_sort
  Fx: partition
    Fx: quick_sort
```

---

## print(message)

Prints a message using the current indentation.

```python
DX.print("Processing...")
```

Output

```
  Processing...
```

---

## print_val(variable, value)

Prints a variable name and value.

```python
DX.print_val("i", i)
```

Output

```
i : 3
```

Example

```python
DX.print_val("pivot", pivot)
DX.print_val("array", arr)
```

Output

```
pivot : 10
array : [8, 3, 5]
```

---

## print_cyan(message)

Prints text in cyan.

```python
DX.print_cyan("Start")
```

Useful for

- headers
- entering functions
- important milestones

---

## print_green(message)

Prints text in green.

```python
DX.print_green("Condition satisfied")
```

Useful for

- successful conditions
- positive paths

---

## print_red(message)

Prints text in red.

```python
DX.print_red("Condition failed")
```

Useful for

- failed conditions
- unexpected branches
- error diagnostics

---

## inc()

Manually increases indentation.

```python
DX.inc()
```

Usually you don't need to call this because `fx()` already does it.

---

## dec()

Removes one indentation level.

```python
DX.dec()
```

Useful when manually managing nested blocks.

---

## ON()

Enables all debug output.

```python
DX.ON()
```

---

## OFF()

Disables all debug output.

```python
DX.OFF()
```

Example

```python
DX.fx("quick_sort")
DX.OFF()

...
```

Nothing is printed after `OFF()` until `ON()` is called.

---

## get_counter()

Returns the number of printed debug messages.

```python
count = DX.get_counter()
```

---

## print_list_diff()

Compares two lists and highlights changed elements.

```python
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

Output

```
array : [3, 8, 1, 7]
```

where only modified elements are printed in green.

This is especially useful when debugging

- sorting algorithms
- dynamic programming tables
- graph updates
- state transitions

---

# Example

Quick Sort

```python
def partition(arr, low, high):
    DX.fx("partition")

    pivot = arr[high]

    DX.print(f"{low = }")
    DX.print(f"{high = }")
    DX.print(f"{pivot = }")

    DX.print_val("array", arr)

    ...
```

Output

```
Fx: partition
  low = 0
  high = 6
  pivot = 2
  array : [8, 3, 1, 7, 0, 10, 2]
```

---

# Typical Usage

```python
def dfs(node):
    DX.fx("dfs")

    DX.print_val("node", node)

    for child in node.children:
        dfs(child)

    DX.dec()
```

Output

```
Fx: dfs
  node : A
  Fx: dfs
    node : B
    Fx: dfs
      node : D
```

The indentation immediately reveals the recursive call hierarchy.

---

# Recommended Workflow

1. Create a single global debugger.

```python
DX = Debug()
```

2. Add `DX.fx()` at the beginning of important functions.

3. Print important variables using

```python
DX.print_val(...)
```

instead of raw `print()`.

4. Use colored output to distinguish

- successful conditions
- failures
- milestones

5. Disable debugging by calling

```python
DX.OFF()
```

instead of removing print statements.

---

# Best Use Cases

This utility is particularly useful for learning and debugging algorithms such as

- Quick Sort
- Merge Sort
- Heap Sort
- Binary Search
- DFS
- BFS
- Dijkstra
- Dynamic Programming
- Tree Traversal
- Backtracking
- Recursion
- Parsing algorithms

---

# Design Goals

This utility intentionally does **not** try to replace Python's `logging` module.

Instead, it aims to provide:

- very small API
- almost zero setup
- visually clear output
- recursion-friendly traces
- algorithm-oriented debugging

It is intended as a developer productivity tool for understanding code execution rather than for production logging.
