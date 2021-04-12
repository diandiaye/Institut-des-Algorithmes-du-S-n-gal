
# Institut des Algorithmes du Sénégal
## _C programming Langage_

# Getting set up - finding a C compiler

The very first thing you need to do, before starting out in C, is to make sure that you have a compiler. The question that can be asked is what is a compiler ?
A compiler turns the program that you write into an executable that your computer can actually understand and run. If you're taking a course, you probably have one provided through your school.

The first choss you will need to program in C is a compiler. A compiler translates your code into a lower level language that the computer can understand and run. 

Different types of C compilers:

-Xcode

-gcc

Code Block : https://www.cprogramming.com/code_blocks/
 

# Introduction to C programming Langage

Every correct C program must include a function main in it's beginig. A function is a combination of different commands that do something.
To access the standard functions of C, you need to include a header with the #include directive. 

#include permet d'accéder aux différentes fonctions de base, comme la fonction printf, qui est fondamentale

# 1. Affichage
```ruby
#include <stdio.h>
#include <stdlib.h>
int main() //Cette ligne dit au compilateur qu'il y a une fonction appelée main() et que cette fonction doit retourner un integer
{
    printf("bienvenue dans le cours d'introduction à la programmation avec c\n");
    return 0;
}
```


# 2. Using variables in C

Our programs, as you will see, are full of variables.

In C language, a variable is made of two things:


- a value: this is the number it stores, for example 5 ;

- a name : this is what allows to recognize it. When programming in C, you don't have to remember the memory address (phew!): instead, you just indicate variable names. The compiler will do the conversion between the name and the address. This is already one less problem.


Every programmer has his own way of naming variables. During this course I will show you my way of doing things:

- I start all my variable names with a lower case letter ;

- if there are several words in my variable name, I put a capital letter at the beginning of each new word.

The bottom line is that whatever you do, make sure you give your variables clear names.

# declaration of a variable

Variable declarations can be found :

- outside any function, they are global variables;
- inside a block, they are local variables;
- in the header of a function, they are then formal arguments, placed
- either in the parentheses of the header (function defined in ANSI syntax with a prototype),
- or between the function name and the initial f (function defined in original syntax or without prototype).

```ruby
#include <stdio.h>
#include <stdlib.h>
int main(){
int x;
int a, b, c, d;
char letter;
float the_float;

}
```

# Reading input
```ruby
int main()
{
    int this_is_a_number;
 
    printf( "Please enter a number: " );
    scanf( "%d", &this_is_a_number );
    printf( "You entered %d", this_is_a_number );
    getchar();
    return 0;
}
```









```ruby
#include <stdio.h>
#include <stdlib.h>

int main()
{
  printf("Bonjour"); // Cette instruction affiche Bonjour à l'écran
  return 0;          // Le programme renvoie le nombre 0 puis s'arrête
}
```
The #include allow you to add libraries to your program. Libraries are actually files with lots of ready-made functions inside. For example the printf() function, the getchar() function...

An other important function in this code is the main() function; this function tells to your compiler, that there is a funtion named main and it returns an integer(tha's why we made int before main()).

Finally, at the end of the program, we return a value from main to the operating system by using the return statement. This return value is important as it can be used to tell the operating system whether our program succeeded or not. It means that, the program returns 0 and stop.

## Arithmetic operations

So far you should be able to write a simple program to display information typed in by you, the programmer and to describe your program with comments. That's great, but what about interacting with your user? Fortunately, it is also possible for your program to accept input.

But first, before you try to receive input, you must have a place to store that input. In programming, input and data are stored in variables. There are several different types of variables; when you tell the compiler you are declaring a variable, you must include the data type along with the name of the variable. Several basic types include char, int, and float. Each type can store different types of data.


```ruby
int x;
int a, b, c, d;
char letter;
float the_float;
```

# Reading input

#include <stdio.h>
 
```ruby
int main(){
int a = 5;
int b = 6;
int add;
int sous;
int div;
int mult;
int inc;
// Addition
  add = a+b;
  printf("La somme entre a et b est %d\n",add);

// soustraction
sous = a-b;
printf("La différence entre a et b est %d\n",sous);

// multiplication
mult = a*b;
printf("La valeur du produit entre a et b est %d\n",mult);

// incrémenter un entier

inc = a++;
printf("La valeur de lopperation est %d\n",inc);

}
```

