
# Institut des Algorithmes du Sénégal
## _C programming Langage_

# Getting set up - finding a C compiler

The very first thing you need to do, before starting out in C, is to make sure that you have a compiler. The question that can be asked is what is a compiler ?
A compiler turns the program that you write into an executable that your computer can actually understand and run. If you're taking a course, you probably have one provided through your school.

If you haven't yet done so, go ahead and get a compiler set up--you'll need it for the rest of the tutorial. If you're on Windows, your best bet is to use Code::Blocks with MinGW. If you're on Linux, you can use gcc, and if you're on Mac OS X, you can use XCode.

# Introduction to C programming Langage

Every correct C program must include a function main in it's beginig. A function is a combination of different commands that do something.
To access the standard functions of C, you need to include a header with the #include directive. 

# 1. Affichage
```ruby
#include <stdio.h>
#include <stdlib.h>
int main()
{
    printf("bienvenue dans le cours d'introduction à la programmation avec c\n");
    return 0;
}
```


# 2. Using variables in C

Nos programmes, vous allez le voir, sont remplis de variables.

En langage C, une variable est constituée de deux choses : 

- une valeur : c'est le nombre qu'elle stocke, par exemple 5 ;

- un nom : c'est ce qui permet de la reconnaître. En programmant en C, on n'aura pas à retenir l'adresse mémoire (ouf !) : à la place, on va juste indiquer des noms de variables. C'est le compilateur qui fera la conversion entre le nom et l'adresse. Voilà déjà un souci de moins.
- 
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












```ruby
/*
Ci-dessous, ce sont des directives de préprocesseur.
Ces lignes permettent d'ajouter des fichiers au projet, 
fichiers que l'on appelle bibliothèques.
Grâce à ces bibliothèques, on disposera de fonctions toutes prêtes pour afficher
par exemple un message à l'écran.
*/

#include <stdio.h>
#include <stdlib.h>


/*
Ci-dessous, vous avez la fonction principale du programme, appelée main.
C'est par cette fonction que tous les programmes commencent.
Ici, ma fonction se contente d'afficher Bonjour à l'écran.
*/

int main()
{
  printf("Bonjour"); // Cette instruction affiche Bonjour à l'écran
  return 0;          // Le programme renvoie le nombre 0 puis s'arrête
}
```
The #include allow you to add libraries to your program. Libraries are actually files with lots of ready-made functions inside. For example the printf() function, the getchar() function...

An other important function in this code is the main() function; this function tells to your compiler, that there is a funtion named main and it returns an integer(tha's why we made int before main()).

Finally, at the end of the program, we return a value from main to the operating system by using the return statement. This return value is important as it can be used to tell the operating system whether our program succeeded or not. It means that, the program returns 0 and stop.

## Declaring and using variables 

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

