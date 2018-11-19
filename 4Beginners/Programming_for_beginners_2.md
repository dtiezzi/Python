# Programming for beginners #2
### Daniel Tiezzi

## How to improve my calculator

Our first code runs a simple calculator. We want to make it better. How can we make improvements?

My first idea was to enable the user to do multiple calculations. So, how can we automatize our code to do this? The answer is to use **loops**. Loops are repetition structures we can use to do a task as many time as we want. In Python there are two types of loop: the `for` and `while` loops. What is the difference?

The `for` loop executes a code block for a pre-defined number of times. The `while` loop executes until a specific condition is not `True` anymore. Let's look an example. Imagine I want to sum all the integer numbers from 0 to 9. So, my calc wold be `result = 0 + 1 + 2 + ... + 9`. Instead type all this numbers and `+` sign, I can use a `for` so repeat the addition 10 times. In Python, the `for` syntax is like this:

```python {.line-numbers}
result = 0
for i in range(0, 10):
	result += i
print(result)
```

We create a variable `result` assigned a value of `0`. Then we have the `for` loop. This is the syntax meaning: for the value i in a range from 0 to 9 (in Python the `range()` function do not include the maximum value) do a sum of result plus i. So, the loop will run 10 times and, after this, we are printing the final result. To make it clear, open the editor and type the code bellow:

```python {.line-numbers}
result = 0
for i in range(0, 10):
	print(i)
	result += i
print(result)
```

Now save in your `Python` directory as forLoop.py and run in `Terminal` as `python ;`. This will be the output on your screen:

![fig1](/Users/dtiezzi/Python/4beginers/fig2_1.png)

Note we are printing the value of `i` for every loop iteration and, in the end, we print the final result. Try to change the `range(0, 10)` for `range(0, 100)`.

The `while` loop syntax is a bit different:

```python {.line-numbers}
result = 0
answer = "Y"
i = 0
while (answer == "Y"):
	print(i)
	result += i
	i += 1
	answer = input("Keep adding (Y/N)?").upper()
print(result)
```

Here we create a variable `result` assigning the value of `0`, a character variable `answer` assigned as `Y` and a variable `i`. The `while` loop will be repeating until the answer is equal to `Y`. The `while` syntax here means while answer is equal to `Y` do something. Note before we compare again, we ask the user if he wants to keep adding or not. If his answer is not `Y`, the `while` loop ends. So, save this as whileLoop.py and run. The output should be something like this:

![fig2](/Users/dtiezzi/Python/4beginers/fig2_2.png)

Note the loop repeats the addition only if the user answer `Y`. Note the `upper()` function at the end of out `input()` function. It capitalizes the character, thus if the user type `y` it converts to `Y`. **Python is case sensitive**. 

Now is easy to implement this loop in our calculator. We can use the same `while` loop asking the user if he wants to do another calc. **DONT FORGET THE INDENTATION**. The code block running into a loop has to be indented. Let's do it:

```python {.line-numbers}
ans = 'Y'
menu = '''
1 - Addition;
2 - Subtraction;
3 - Multiplication;
4 - Division; 
'''

while (ans == 'Y'):
    print(menu)
    op = input("Choose one of the options above: ")

    n1 = float(input("Type the first number: "))
    n2 = float(input("Type the second number: "))

    if (op == '1'):
        print(n1 + n2)
    elif (op == '2'):
        print(n1 - n2)
    elif (op == '3'):
        print(n1 * n2);
    elif (op == '4'):
        if (n2 == 0):
            print("Impossible to divide by 0.")
        else:
            print(n1 / n2)
    else:
        print("Wrong option!")
    ans = input("New calc (Y/N)?").upper()
```
What have I changed? The line `1` create the variable `ans = "Y"`. The `while` loop starts in the line `9` and will repeat if `ans == "Y"`. Before checking the `ans` value again, I ask to the user if he wants to do another calc. Easy, isn't it?

In the next section, we are implementing a new functionality to our calculator. Imagine if the user want to add multiple values, not only two. We will se we can create a structure to store all the values and the use a loop to sum them up. See you there!