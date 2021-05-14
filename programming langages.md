
# Institut des Algorithmes du Sénégal



# Java

In this program, an object of Scanner class, reader  is created to take inputs from standard input, which is keyboard.

Then, Enter a number prompt is printed to give the user a visual cue as to what they should do next.

reader.nextInt()then reads all entered integers from the keyboard unless it encounters a new line character \n (Enter). The entered integers are then saved to the integer variable number.

If you enter any character which is not an integer, the compiler will throw an InputMismatchException.

Finally, number is printed onto the standard output (System.out) - computer screen using the function println().

```ruby
import java.util.Scanner;

public class HelloWorld {

    public static void main(String[] args) {

        // Creates a reader instance which takes
        // input from standard input - keyboard
        Scanner reader = new Scanner(System.in);
        System.out.print("Enter a number: ");

        // nextInt() reads the next integer from the keyboard
        int number = reader.nextInt();

        // println() prints the following line to the output screen
        System.out.println("You entered: " + number);
    }
}
```

# Python

```ruby
number = input ('Please enter a number ')
print("number is %s of type %s" % (number, type(number)))
print("number is {} of type {}".format(number, type(number)))

y = number ** 2
print("y is {} of type {}".format(y, type(y)))

z = number **5
print("z is {} of type {}".format(z, type(z)))

print (y+z)
```

AS you can see, number is a string because in python3, input returns the users input as a string

change it to int(input('Please enter a number')).

# C++

```ruby
#include <iostream>
using namespace std;

int main()
{    
    int number;

    cout << "Enter an integer: ";
    cin >> number;

    cout << "You entered " << number;    
    return 0;
}
```

This program asks user to enter a number.

When user enters an integer, it is stored in variable number using cin.

Then it is displayed in the screen using cout.


# Julia
In the below example, user input is obtained using the readline() method. We can prompt the user with the help of a print statement prior. It is to be noted that readline method reads the input into a string data type.

```ruby
# Julia program to take input from user
  
# prompt to input
print("What's your name ? \n\n") 
  
# Calling rdeadline() function
name = readline()
  
println("The name is ", name)
print("\n\n")
  
# typeof() determines the datatype.
println("Type of the input is: ", typeof(name)) 
```

# R

Here, we see that with the prompt argument we can choose to display an appropriate message for the user.

In the above example, we convert the input age, which is a character vector into integer using the function as.integer().

This is necessary for the purpose of doing further calculations.

```ruby
my.name <- readline(prompt="Enter name: ")
my.age <- readline(prompt="Enter age: ")
# convert character into integer
my.age <- as.integer(my.age)
print(paste("Hi,", my.name, "next year you will be", my.age+1, "years old."))
```
