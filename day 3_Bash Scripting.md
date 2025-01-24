# Bash Scripting Guide for Beginners

Welcome to this comprehensive guide for Bash scripting. Whether you're a beginner or a DevOps enthusiast, this guide covers the essentials to get you started.

---

## 1. Basics of Bash

### `echo` - Printing Messages
**Usage:** `echo "message"`  
**Example:**
```bash
echo "Hello, World!"
echo "Welcome to Bash Scripting Guide!"
```

### Variables
**Definition:** Variables are used to store data.  
**Usage:** `VARIABLE_NAME="value"`  
**Example:**
```bash
NAME="Bash Scripting"
echo "This is a guide for $NAME."
```

### Constants
**Definition:** Use `readonly` to make variables immutable.  
**Example:**
```bash
readonly PI=3.14
echo "Value of PI: $PI"
```

---

## 2. Strings and Arrays

### String Operations
**Concatenation:**
```bash
FIRST="Hello"
SECOND="World"
FULL="$FIRST, $SECOND!"
echo $FULL
```

**Length of a String:**
```bash
STRING="BashScripting"
echo "Length: ${#STRING}"
```

### Arrays
**Definition:** Arrays store multiple values in one variable.  
**Usage:**
```bash
NAMES=("Alice" "Bob" "Charlie")
echo "First Name: ${NAMES[0]}"
echo "All Names: ${NAMES[@]}"
```

---

## 3. User Interaction

### Read Input
**Example:**
```bash
read -p "Enter your name: " NAME
echo "Hello, $NAME!"
```

---

## 4. Arithmetic Operations

### Basic Arithmetic
**Example:**
```bash
NUM1=10
NUM2=5
SUM=$((NUM1 + NUM2))
DIFF=$((NUM1 - NUM2))
MULT=$((NUM1 * NUM2))
DIV=$((NUM1 / NUM2))
echo "Sum: $SUM, Difference: $DIFF, Product: $MULT, Quotient: $DIV"
```

---

## 5. Conditional Statements

### If-Else Statements
**Definition:** Conditional statements execute code blocks based on conditions.  
**Usage:**
```bash
if [ condition ]; then
    # code if condition is true
else
    # code if condition is false
fi
```
**Example:**
```bash
NUMBER=10
if [ $NUMBER -gt 5 ]; then
    echo "The number $NUMBER is greater than 5."
else
    echo "The number $NUMBER is not greater than 5."
fi
```

### Elif Statements
**Definition:** For multiple conditions.  
**Example:**
```bash
read -p "Enter your score: " SCORE
if [ $SCORE -ge 90 ]; then
    echo "Grade: A"
elif [ $SCORE -ge 75 ]; then
    echo "Grade: B"
else
    echo "Grade: C"
fi
```

### Logical Operators
**Examples:**
```bash
if [ $AGE -ge 18 ] && [ $AGE -le 30 ]; then
    echo "Eligible for the program."
fi

if [ $NUM -eq 0 ] || [ $NUM -eq 1 ]; then
    echo "Binary number."
fi
```

---

## 6. Loops

### For Loop
**Definition:** Used to repeat a block of code for a set of values.  
**Usage:**
```bash
for VARIABLE in list; do
    # code block
done
```
**Example:**
```bash
for i in 1 2 3 4 5; do
    echo "Number: $i"
done
```

### While Loop
**Definition:** Repeats a block of code while a condition is true.  
**Usage:**
```bash
while [ condition ]; do
    # code block
done
```
**Example:**
```bash
COUNT=1
while [ $COUNT -le 3 ]; do
    echo "Count: $COUNT"
    ((COUNT++))
done
```

### Until Loop
**Definition:** Repeats a block of code until a condition becomes true.  
**Usage:**
```bash
until [ condition ]; do
    # code block
done
```
**Example:**
```bash
COUNT=1
until [ $COUNT -gt 3 ]; do
    echo "Count: $COUNT"
    ((COUNT++))
done
```

---

## 7. Functions and Arguments

### Functions
**Definition:** Functions are reusable blocks of code.  
**Usage:**
```bash
function_name() {
    # code block
}
```
**Example:**
```bash
greet() {
    echo "Hello, $1!"
}
greet "DevOps Engineer"
```

---

## 8. Operators

### Comparison Operators
- `-eq`: Equal to
- `-ne`: Not equal to
- `-gt`: Greater than
- `-lt`: Less than
- `-ge`: Greater than or equal to
- `-le`: Less than or equal to

**Example:**
```bash
if [ $1 -eq $2 ]; then
    echo "Numbers are equal."
else
    echo "Numbers are not equal."
fi
```

### Arithmetic Operators
- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Modulus

---

## 9. Redirection and Logging

### Redirection
**Definition:** Redirect output and errors.  
**Examples:**
```bash
echo "This is standard output." > output.log
ls nonexistent_file 2> error.log
echo "Both output and error." &> combined.log
```

### Logging Messages
**Example:**
```bash
LOGFILE="script.log"
echo "Script started at $(date)" >> $LOGFILE
```

---

## End of Guide

Congratulations! You've completed the **Bash Scripting Guide for Beginners**, now with additional advanced topics like string operations, arrays, user interaction, arithmetic operations, logical operators, and more!
