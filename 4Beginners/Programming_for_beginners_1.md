# Programming for beginners #1
### Daniel Tiezzi

## My first program


There are lots of programming languages nowadays. You can choose anyone to start learning how to make computer programs. Here, we will be using Python, a general purpose language. I chose it because it is a high-level, interpreted (not compiled) dynamic programming language that focuses on code readability. Additionally, the Python syntax helps us to code using fewer steps as compared to other high-level languages.

In order to run Python programs in your computer you have to have its interpreter install in your machine. In Mac and Linux, the interpreter is native. However, if you are using Windows, you have to install it. [Install Python for Windows.](https://www.python.org/downloads/)

First of all, we need to use a text editor to write our scripts. There are plenty of. You can use anyone. Some of them can help you with your code. I recommend to use the [Visual Studio Code.](https://code.visualstudio.com/download) It's multi-platform and you can install useful plugins.

I'd like to explain something, before we start coding. I'm planning to create a simple calculator to help us on school. So, we will be working with numbers. In computer languages, there are primitive variable types we have to learn. In Python, numbers can be an integer `int` or a real (floating) number `float`. We do not have to declare variables in Python. However, it's important to know we have those two types because you can get a wrong result dividing integers. **Remember to work with `float` numbers to do math!**

Now, all you have to do is opening your text editor and let's start coding! I recommend you to type the code. **DO NOT PASTE AND COPY!** 

All you have to do is to write the code bellow in the text editor:

```python {.line-numbers}
menu = '''
1 - Addition;
2 - Subtraction;
3 - Multiplication;
4 - Division; 
'''
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
```

Now, let's understand the code. 

The first piece is:
`menu = '''
1 - Addition;
2 - Subtraction;
3 - Multiplication;
4 - Division; 
'''
`
Here we create a variable we called `menu` and assigned a string to it. String is another primitive variable type in Python. I used the triple single quote before and after the string just to format it, so we can print it nicely on the screen. For this, we are using the built-in function `print()` to display the menu. 

Them we have: 
`op = input("Choose one of the options above: ")`

Here we are using another built-in function `input`. This function gets an input from the keyboard. So, if the user type something and hit enter, this function gets the input and assign to a variable we called `op`. We are doing the same here:
`n1 = float(input("Type the first number: "))`
`n2 = float(input("Type the second number: "))`

Note I used the `float` before the `input`. This is to convert the input value to a float number. In Python, the `input` function always gets the value as a character, not a number. Thus, we have to convert them.

So, we have now three variables: `op` is a character, `n1` and `n2` are float numbers. The `op` is the type of math the user wants to do, and `n1` and `n2` are the values to be calculated.

Now we have a conditional structure to make decisions based on the user option.
In Python we can use this `if/else` structure to make decisions. Note we are deciding with operation will be performed. So, if the op variable is equal to 1 `if (op == '1'):` (I used quotes because the number 1 is stored as a character, not a number), the program does an addition and prints the result on the screen `print(n1 + n2)`. Note the `op == "1"` expression. Here the `==` is not an assignment code as `n1 =`. It's a code for comparison. The result of this is a boolean expression `True/False`. Boolean is another primitive variable in Python. 

Then I used `elif`. It means **else if** and in the end I used the last `else` statement. I used another `if/else` inside the option for division `elif (op == '4'):` because it's not possible to divide a number by `0`.

**THIS IS IMPORTANT**
In Python, some structures, as the conditionals, have to have indentation. So, after `if (something):` or `elif (something):` or `else:` statements, the code to be executed if the condition is `True` has to be indented, and the indentation has to be the same in all your code. Here I use a `tab`. You can use a `space`,  double `space` or whatever. But, it has to follow the pattern throughout your code.

Now, what we have to do is to save our code as a Python code. All you have to do is to save it as `calculator.py`. The name `calculator` may be anyone. You can choose other name, but I recommend you to save it as a `.py`. Here  is a trick. Is better to save your code as soon as you start coding then the editor knows you are writing a Python code and help you with the syntax.

Save the code in a specific file. Create a new file named `Python` for example and save in there.

**TIME TO RUN YOUR FIRST PROGRAM!**

In Linux or Mac open the `Terminal`. In Windows, open the `Cmd`. Both `Terminal` and `Cmd` are softwares that create an interface where the user is able to communicate with the computer via command line. So, you can write commands to be executed by the computer. However, it's not a graphical interface. It's a written interface. You have to change the directory you are working in the `Terminal` or `Cmd` to the `Python` directory you have just created. If you are not used with this, [please take a look at here!](https://github.com/dtiezzi/rgo5852/blob/master/linuxBasic.md)

Once you are in the `Python` repository, you can access your `calculator.py` file. All you have to do is to type `python calculator.py` and your program will be executed. This is snapshot from my `Terminal`:

![fig1](/Users/dtiezzi/Python/4beginers/fig1_1.png)

Are we done? Not yet. We are going to learn how we can modify this code to create a more functional calculator.