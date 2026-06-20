# Python Code Review

Notes, checklists, examples, and references for reviewing Python code. Useful for interview preparation, code review tasks, AI code evaluation, and general software engineering practice.

---

## Review Mindset

When reviewing code, focus on:

1. Correctness
2. Readability
3. Maintainability
4. Performance
5. Security
6. Pythonic Style

Ask:

- Does it work correctly?
- Is it easy to understand?
- Are there edge cases?
- Is there unnecessary complexity?
- Does it follow Python conventions?

---

## Quick Review Checklist

### Correctness

- Logic produces expected results.
- Handles edge cases.
- Avoids off-by-one errors.
- Handles empty inputs.
- Handles invalid inputs when necessary.

### Readability

- Clear variable names.
- Descriptive function names.
- Consistent formatting.
- Avoids deeply nested code.
- Uses comments only when needed.

### Maintainability

- Functions have a single responsibility.
- Repeated code is extracted.
- Magic numbers are avoided.
- Complex logic is broken into smaller functions.

### Performance

- Avoids unnecessary loops.
- Uses appropriate data structures.
- Avoids repeated expensive computations.
- Considers algorithm complexity.

### Security

- Avoids eval().
- Validates user input.
- Uses parameterized SQL queries.
- Does not expose secrets.

---

## Common Python Code Smells

### Mutable Default Arguments

Bad:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Good:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

### Broad Exception Handling

Bad:

```python
try:
    process_data()
except:
    pass
```

Good:

```python
try:
    process_data()
except ValueError as e:
    logger.error(e)
```

---

### Unnecessary List Creation

Bad:

```python
total = sum([x * 2 for x in numbers])
```

Better:

```python
total = sum(x * 2 for x in numbers)
```

---

### Long Functions

Bad signs:

- More than one responsibility.
- Multiple nested loops.
- Difficult to explain.

Refactor into smaller functions.

---

## Edge Cases to Check

### Strings

- Empty string
- Whitespace only
- Unicode characters
- Very long strings

### Lists

- Empty list
- Single item
- Duplicate values
- Large datasets

### Numbers

- Zero
- Negative values
- Large values
- Floating-point precision

### Dictionaries

- Missing keys
- Empty dictionaries
- Nested structures

---

## Algorithm Review Questions

### Time Complexity

Ask:

- Is there a nested loop?
- Can a lookup table be used?
- Can a set replace a list lookup?

Example:

Bad:

```python
for item in items:
    if item in large_list:
        ...
```

Better:

```python
lookup = set(large_list)

for item in items:
    if item in lookup:
        ...
```

---

## Readability Improvements

### Prefer Meaningful Names

Bad:

```python
def calc(x, y):
    return x * y
```

Better:

```python
def calculate_area(width, height):
    return width * height
```

---

### Early Returns

Instead of:

```python
if user:
    if user.is_active:
        return user.email
return None
```

Use:

```python
if not user:
    return None

if not user.is_active:
    return None

return user.email
```

---

## DataAnnotation Review Workflow

When reviewing AI-generated Python code:

### Step 1

Verify correctness.

- Does it solve the task?
- Does it match requirements?

### Step 2

Look for bugs.

- Missing edge cases
- Incorrect assumptions
- Runtime errors

### Step 3

Review code quality.

- Naming
- Structure
- Duplication

### Step 4

Review efficiency.

- Complexity
- Data structures
- Unnecessary work

### Step 5

Review Python style.

- PEP 8
- Idiomatic Python
- Standard library usage

---

## Useful Tools

### Formatting

- Black
- Ruff

### Type Checking

- mypy

### Testing

- pytest

### Security

- bandit

---

## References

### Style Guide

- https://peps.python.org/pep-0008/

### Python Documentation

- https://docs.python.org/3/

### Real Python

- https://realpython.com/

### Refactoring

- https://refactoring.guru/

---

## Personal Notes

Add examples of:

- Bugs found during reviews
- Good refactoring examples
- DataAnnotation evaluation patterns
- Common AI-generated mistakes
