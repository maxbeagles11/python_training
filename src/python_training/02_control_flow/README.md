# 02 Control Flow
`Control flow` is essential to any programming/scripting language. It describes how your code will make decisions or perform certain actions.
Essentially allowing it to "think" before doing something.

Before we begin, I highly suggest you familiarize yourself with the concepts of logic (if you have no prior experience with it). You can check out the description of logic on [Wikipedia](https://en.wikipedia.org/wiki/Logic) as it does a good job of covering the basics.


This folder will cover the following basic concepts:
1. Logic and logical expressions.
> Making decisions using `if`, `elif`, and `else` conditional statements. Using operators like `or`, `and`, and `not`.
2. Loops.
> Repeating actions with `for` loops and `while` loops.
3. Exceptions.
> How to handle failures, known as `exceptions` within a script.

Additionally, there are some problems you can try in `try_these_problems.py` to practice what you've learned. The solutions will be found in `solutions.py`.

## Operator Reference
So far we've briefly touched on certain operators such as addition `+` and assignment `=`. This section will dive deeper into the `logical operators` mentioned above, however Python has **many more** operators to choose from.
Please use the table below as a reference for these operators.

## Python Operators Overview

<details>
<summary>🧮 1. Arithmetic Operators</summary>
Used for basic math operations.

| Operator | Name              | Example     | Result |
|----------|-------------------|-------------|--------|
| `+`      | Addition           | `2 + 3`     | `5`    |
| `-`      | Subtraction        | `5 - 2`     | `3`    |
| `*`      | Multiplication     | `3 * 4`     | `12`   |
| `/`      | Division           | `10 / 2`    | `5.0`  |
| `//`     | Floor Division     | `7 // 2`    | `3`    |
| `%`      | Modulus            | `7 % 2`     | `1`    |
| `**`     | Exponentiation     | `2 ** 3`    | `8`    |
</details>

---

<details>
<summary>🔍 2. Comparison (Relational) Operators</summary>
Used to compare values. Returns `True` or `False`.

| Operator | Meaning               | Example        |
|----------|------------------------|----------------|
| `==`     | Equal to               | `3 == 3` → `True` |
| `!=`     | Not equal to           | `4 != 5` → `True` |
| `>`      | Greater than           | `5 > 2` → `True`  |
| `<`      | Less than              | `2 < 5` → `True`  |
| `>=`     | Greater than or equal  | `5 >= 5` → `True` |
| `<=`     | Less than or equal     | `4 <= 5` → `True` |

</details>
---

<details>
<summary>🧠 3. Logical Operators</summary>
Used to combine conditional statements.

| Operator | Meaning     | Example             | Result     |
|----------|--------------|----------------------|------------|
| `and`    | Logical AND  | `True and False`     | `False`    |
| `or`     | Logical OR   | `True or False`      | `True`     |
| `not`    | Logical NOT  | `not True`           | `False`    |
</details>

---

<details>
<summary>🪄 4. Assignment Operators</summary>
Used to assign or update variables.

| Operator | Example     | Same as        |
|----------|--------------|----------------|
| `=`      | `x = 5`      |                |
| `+=`     | `x += 3`     | `x = x + 3`    |
| `-=`     | `x -= 2`     | `x = x - 2`    |
| `*=`     | `x *= 4`     | `x = x * 4`    |
| `/=`     | `x /= 2`     | `x = x / 2`    |
| `//=`    | `x //= 2`    | `x = x // 2`   |
| `%=`     | `x %= 3`     | `x = x % 3`    |
| `**=`    | `x **= 2`    | `x = x ** 2`   |
</details>

---

<details>
<summary>🧱 5. Bitwise Operators</summary>
Used for binary-level operations.

| Operator | Meaning      | Example        | Result  |
|----------|---------------|----------------|---------|
| `&`      | AND           | `5 & 3`        | `1`     |
| `|`      | OR            | `5 | 3`        | `7`     |
| `^`      | XOR           | `5 ^ 3`        | `6`     |
| `~`      | NOT           | `~5`           | `-6`    |
| `<<`     | Left shift    | `5 << 1`       | `10`    |
| `>>`     | Right shift   | `5 >> 1`       | `2`     |
</details>

---

<details>
<summary>🧪 6. Identity Operators</summary>
Used to check if two variables refer to the **same object**.

| Operator | Meaning               | Example      |
|----------|------------------------|--------------|
| `is`     | Same object?           | `x is y`     |
| `is not` | Not the same object?   | `x is not y` |
</details>

---

<details>
<summary>📦 7. Membership Operators</summary>
Used to check for **membership in a sequence** (like list, string, etc.).

| Operator | Meaning        | Example                 | Result |
|----------|----------------|--------------------------|--------|
| `in`     | Value in?      | `"a" in "cat"`           | `True` |
| `not in` | Value not in?  | `5 not in [1, 2, 3]`     | `True` |
</details>

---

## 📖 Further Reading

- 🧠 [Python Docs – Control Flow](https://docs.python.org/3/tutorial/controlflow.html)
- 🧮 [W3Schools – Python Conditions](https://www.w3schools.com/python/python_conditions.asp)
- 🔁 [W3Schools – Python Loops](https://www.w3schools.com/python/python_for_loops.asp)
- ⚠️ [Python Docs – Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
