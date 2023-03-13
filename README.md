# mana
Mana is a simple programming language.

# Getting Started
1. Create a .mana file with your Mana code.
2. Run main.py
3. Write your .mana file name

# Syntax
Mana has a simple and easy-to-read syntax. Here are some key features:

#Comments
Comments start with // and can be used to add notes to your code:
// This is a comment

#Variables
To create a variable in Mana, simply assign a value to a name:
x = 5
Mana is dynamically typed, so you can assign any value to any variable.
In mana to use Variables after you created it you need to add {val_name}

#Output
To output text or a variable's value, use the write function:
write Hello, world!
x = Hi
write {x}

#Math
Mana supports all basic math functions and operations. To perform math operations, use the num syntax:
num[2 + 3 * 4 / 2]
remmember that if you want to make a math in side a math use only one time num[]:
a = 12
b = {a} + {a}
c = num[{b} * {a}]
write {c}

#Input
To prompt the user for input, use the input function:
input name, Enter your name:
The user's input will be assigned to the variable name.

#Contributing
Contributions to Mana are welcome! If you find a bug or have an idea for a new feature, feel free to open an issue or submit a pull request on GitHub.

#License
Mana is licensed under the MIT License.
