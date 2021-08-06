Status: published
Author: Ben Chuanlong Du
Date: 2013-10-22 13:49:14
Slug: cpp-tips
Title: Tips on C++
Category: Computer Science
Tags: tips, programming, C++, cpp
Modified: 2020-05-22 13:49:14

**
Things on this page are fragmentary and immature notes/thoughts of the author. 
Please read with your own judgement!
**


## IDE

1. Eclispe CDT is a good IDE for C/C++ development in Unix/Linux sytem. 
    Configuration of Eclipse CDT in Windows system is not pleasant. 
    Netbeans and code::blocks are good alternatives in Windows system.

2. SpaceVim is good choice for small C++ project if you prefer Vim.


## Tips

1. For situations where `++i;` and `i++;` (similar for `--i` and `i--`) can both be used, 
    you'd better your use the first one. 
    This is becuase `++i;` is usually more efficient than `i++;`
    especially when `i` is not of primitive type but some complex object. 
    Modern compilers might optimize the latter one to be as efficient as the former one, 
    but it never hurt to use the former one.
    You should be very careful when you use either `++i` or `i++` in your code. 
    Both these two expressions change the value of i. 
    So if `++i` or `i++` is used and `i` appears more than once in an expression, 
    you'd better thining twice. 
    My suggestion is to simply avoid these situations. 
    Do not wirte code that is difficult to read and understand.

1. Prefer functions/methods with fewer arguments. 
    If a function/method has many arguments, 
    it is suggested that you group related arguments into a single argument.
    This make the function/method easier to understand. 
    For example, 
    if a function/method takes two double arguments which are 
    the x and y coordinate of a point, you can group them into a pair of doubles.
    This does not make the function/method more convenient to use 
    (in the sense of saveing typing), 
    but the code will usually be more readable. 
    Also, 
    when you write a class, 
    it is recommended that you group related member variables into a single struct. 
    For example, 
    you can group all temporary variables 
    (variables do not need constructors to offer initializing values) into a single struct.
    This not only makes the code more readable but also make it 
    easier to write copy and move constructors.

4. Instead of letting a method return `void`, 
    you can return a reference to current object.
    This make is possible to write "chained" code and thus more convenient. 

## Error and Exceptions

1. the error of no convertion from `T *` to `T`, 
    this is probably because of const modifier, 
    the const modifier make cause lots of hard to understanding errors ... 
    basically it say some method is not found ...

2. When error happens and you do not want to throw exceptions, 
    you can use `std::cerr` to print out error message and then use `exit`
    to stop the program.

2. C++ does not allow multiple types in one auto statement 
    similar to non-auto declarations.

## Design

1. If the definition of a class X does not explicitly declare a move constructor, 
    one will be implicitly declared as defaulted if and only if

        - X does not have a user-declared copy constructor, and

        - X does not have a user-declared copy assignment operator,

        - X does not have a user-declared move assignment operator,

        - X does not have a user-declared destructor, and

        - the move constructor would not be implicitly defined as deleted.

1. not a good idea to define function/methods with the same name as those in std

2. do not overload functions unless absolutely necessary especially 
    when you are wrint private methods ... 
    overload brings convenience for public interface 
    but can easily casues troubles ...

1. You cannot use `using namespace std;` inside a class definition. 
    A way to circumambulate this is to put the class definition in a namespace 
    and then declare "using namespace std;" in the namespace. 

2. A funny code of using auto together with uniform initialization list. 
    I thought it is ... but GCC does not. 
    I think GCC is right. 

3. passing a method to a thread is different from passing a function to a thread, 
    because you have to also pass this pointer as an argument ...

4. the standard library has many useful and powerful functions. 
    However, theses functions are designed for general purpose, e.g., the algorithms library.
    Many of these functions takes iterator as arguments. 
    This is not very convenient to use and make the code hard to understand. 
    A good practice is to define helper functions that take contains as arguments. 
    This makes your code shorter and thus eaiser to understand.

## Libraries

1. about libraries for math special functions and statistical distributions:
    I do not boost is very good at this part, especially for statistical distributions. 
    very often, we need log likelihood, so an option for log is important for statistical related functions.
    what is more requring object in order to calculate statistical quantities sounds like a bad idea.
    this can be inefficient, epecially when generating random numbers with varying parameters.

5. when compiling armadillo, you must link it using -larmadillo 

8. C++ is hard is partly become you try to write the smartest code when you coding in C++.
    You focus on write good code, not accomplish your task. 
    You should learn to develop fast, first do not care too much about performance, but keep structure clean.
    if the code does not run as fast as required, then come back to optimize it ...

## Algorithms

1. when writing c++ code, 
    it is nature to write loops, 
    but you should always thinking about whether there are non-loop version, this might you develop faster ...

1. Functions in `<algorithm>` are very useful 
    and they make it easier and more conveneint to write code. 
    However, 
    sometimes it can be more convenient, 
    concise and efficient (both time and memory) 
    to write code by yourself rather than using functions in `<algorithm>`. 

12. the implementation of std::includes is not good, 
    it does not use size to decide ... 
    note that duplicated elements are allowed ....

## IO

1. The `operator<<` method of `stream` is for writing formated text 
    while the 'write' method of `stream` is for writing binary data.

14. Do not use the `eof` method of ifstream, instead, use the `fail` method.

15. `sizeof` works for both type and variable, 
    variable is recommended as a rule of thumb because you migth changed the type of the variable 

16. `istream_iterator` and istringstream only take white space (or just space?) as delimiter

17. `static_assert` compile time check

18. though it is considered C style to pass a ouput variable to function 
    and it is recommended to take advantage of the move functionality in C++, 
    it is sometimes make things more convenient to pass output variable (e.g., contains) to a function, 
    also this is alwasy efficient
    This technic is really helpful if you want to share an object among multiple calls.

20. std::distance distance between iterators, pointers and so on

## Coding Style

1. Use headers of the style `<header>` instead of `<header.h>`.

2. Avoid using `using namespace std`, etc., in your code.
    It is suggested that you always write the namespaces.
    However, it is OK to use `using std::cout;`, etc., in a function scope
    if you found writing the namespace prefix to be verbosal.

3. Many C++ programmer likes to use short variable/function/member names 
    to make their code more concise. 
    However, I think readability and rigorous is more important than conciseness. 
    It is suggested that you use (long) meaning names for variables/functions/members.

23. Generally speaking, it is a bad practice to always use `i`, `j`, etc., as loop variable. 
    It increases the chance of overwriting outer loop variables. 
    It is suggested that you use more meaningful loop variables.

24. It suggested that you keep each function/method as small as possible. 
    This has tremendous advantages.
    First, 
    it makes your tasks small and clear and thus easy to implement. 
    Second, 
    it makes variable naming easier as naming confliction is less likely to happen.
    Last but not least,
    it reduces the chances of bugs.

25. when you use nested loop, be careful about loop varialbes, 
    do not use conflict varables ...
    it suggested that you not to use nested loops, 
    but instead to use functions to replace inner loops ...

26. cannot shift equal or more than the width of type, 
    a way to overcome this problem is to shift twice

29. do not do premature optimization!!!

31. do not try to be too smart, 
    letting users to supply parameters that are legal can make your program simpler and faster. 
    this is generally speaking how STL is implemented.

32. when you want to fork/modify original code, 
    do not do too much at once.
    do it little by little, commit often and debug often 

35. computation error does not come from calculating but from storing numbers. 

36. NRVO: return type is the same as declared type, no need to use move manually

## Random Number Generator

1. You'd better use only one global base random number generator (e.g., Mersenne Twister)
    unless you have good reasons not to do this.

## Some Concepts

1. Argument Dependent Looup (ADL)/Koenig Lookup

2. Template Argument Deduction

## Debug
3. mostly non-logical (i.e., not algorithm related) bugs are due to container operations, 
    be careful!!!  

## Lambda Functions

1. you can save the definition of a lambda function for use later auto f = [](){} ...

## Containers/Collections

1. at vs [] const ...
    Use `at` instead of `operator[]` if you want a const reference.

27. it sounds like that working on list: do not use const iterator, ....

1. Avoid using `arrays` in C++. 
    Use `vectors` instead. 

2. In C++, a 1-dimensional array is equivalent to a pointer. 
    For example,
    if we have definition 
    ```c++
    int a[10]; 
    ```
    then `a` can be treated as a pointer to integers. 
    However, a 2-dimensional array in C/C++ is not the same as a pointer to pointers. 
    For example, if we have definition 
    ```c++
    int a[2][3];
    ```
    then `a` is not of the same type as `int **`. 
    As a matter of fact, `int **` is an array of pointers to integers. 
    If you pass you a 2-dimensional integer array to a function which requires an
    `int **` parameter, 
    the compiler will complain.

3. It is suggested that 
    you always traverse a container using an interator instead of an (integer) index
    unless (integer) index is absolutely necessary. 
    Traverse a container with (integer) index is error-prone.

2. Prefer iterating containings using iterators. 
    Iterating containings using an integer index variable can possible cause several problems. 
    First, integer index based iterating makes the code less portable. 
    Second, integer index based iterating might cause overflow problems.
    Due to the second reason, 
    if you do want to use an integer index variable (e.g., i) to iterate a container (e.g., c), 
    you'd better check boundry conditions by `if(i<0 || i>=c.size()) ...`.

19. The default capacity of a std::vector is 0. 
    You can initialize a vector with a given capacity and you can resize a vector.
    The default number of bucket for a hash table in the standard library 
    (e.g., `unordered_map` and `unordered_set`) is 23.

21. a big trap in C++ is invalidation of iterators, 
    you should be very careful about this
    in STL, 
    you use take advantage of the returned iterator of the method erase, 
    (list, e.g. `import`, for `set`, `vector` thought there are better ways, 
    list must use return result of erase ...), 
    boost::graph, 
    it seems that removing edges invadate parent iterators ... not sure, 
    the documentation is not clear. 
    A way to overcome this problem is to first save the parent vertices in a container. 

3. The `set` container returns only `constant_iterator` (even if it has both begin/end and cbegin/cend).  
    This means that you cannot change the value of elements of a set via iterator.
    However, you can add/remove elements to/from a set.

### erase-remove idiom

1. Among all STL containers, only `list` and `forward_list` has methods `remove`/`remove_if`.
    Other contains have to use the function `std::remove`/`std::remove_if` to remove elements.
    You probably wonder that why the list and forward_list containers have the method `remove`/`remove_if`
    since they already have the `erase` method. 
    It turns out to be that `remove` and `remove_if` doesn't remove anything from a container. 
    They just move elements to remove to the end of the container. 
    You need to use `erase` to erase these elements to be removed (at the end of the container).
    This is called the erase-remove idiom 
    and is well explained on [Wiki](http://en.wikipedia.org/wiki/Erase%E2%80%93remove_idiom).

2. The erase-remove idiom cannot be used for containers that return `const_iterator` (e.g., set).

## Data Types

1. subtraction between unsigned integers are well defined, 
    however, you should be very careful about this!!!
    by default, the returned type is still unsigned int!!!
    It is suggested that you avoid using unsigned integers.

10. you should avoid subtraction between unsigned integers, 
    though the result is well defined, 
    the behavor depends on type casting and so on and can make your code break
    so `0U - 1U` is still an unsigned integer which is maximum value of unsigned integer.
    you have cast the results explicitly/implicityly, if you want an integer instead
    avoid arithmetic operations on `size_t` variables ...

22. it is generally speaking not a good idea to shift signed integers 

33. Do not mixing unsigned integers and signed integers in your code
    as it is a very bad practice.

7. C++11 supports specail values such as `nan` and `inf`, etc. 
    be careful with you do numerical computing with them ... 
    epscially when you use logical comparison envolve `nan` ...

## Move and Forward

1. Do not declare objects const if want to move from them.
    Applying `std::move` on a const object copies the object.
    `std::move` is essentially cast and `std::forward` is essentially conditional cast.

4. Using `std::move` does not guarantee anything will be moved.

30. `T&&` in template means universal reference or perfect forwarding, it binds everything
    but how about `T&&` where `T` is not a template parameter? 
    My question is that is it necessary to overload `const T &`?
 
## Questions

1. in C++, vector is the fastest, is the same for Java and other programming languages, 
    I think the concept of cache applies, but what about deep copy, etc.?

2. what's the difference between a vector of pointers and a vector of objects?
    if class object, how does it store them in memory ...? 
    does it save address or reference? and all objects (all contents) continus? 

1. when does one have to provide copy/move constructors and operator=?

3. different ways to pass a function/functor as argument? 
    It seems that to me that there are many diffrent ways. 
    For example, one can use function pointers,
    functional argument, or use template ...

    in the standard library, the template way is used a lot.
    which of them is recommended? 

    My opinion:
    function pointer is more C style,
    functon object is C++ style and cleaner. 
    Both of them requires you to specify the signature of the function.
    However, template is more flexible which doesn't require you to specify the signature. 

5. about "{}" initializing list? what's wrong? Do I misunderstand it?
    Just avoid using "auto" together with "{}".

6. multiple std::tolower function, how to resolve overload problem when using it as a function in algorithm functions?

7. what's the difference between std::min and std::fmin? 
    std::min is more general
    std::fmin is specifically for floating point numbers

8. the static_cast from integer/double to unsigned integer is very tricky. 
    be sure you understand how it works. -2 will be casted to a large number. 
    I think some bits are discarded ...

9. it seems to me that when using integers, 
    it's easy to get an overflow bug, especially when you use unsigned integers ...
    see whether there's a good practice to avoid this.

10. what happens if you use a reference to a reference? do we get a rvalue reference or what?

11. a question about boost::graph, vertex iterator and other iterator, sorted or not?

12. what happens if the arguments of make_pair is rvalues and a value 
    also does it get ...

13. when is recursive definition possible? in your HMM case, it seems that the components must be separated ...
    because it relies on defintion of ... and thus cannot be put into the definition ...

14. can we use g++ with libc++?
    g++ -nostdlib -lc++ -lc++abi -std=c++11 -o plop /usr/lib/x86_64-linux-gnu/crt1.o /usr/lib/x86_64-linux-gnu/crti.o foo.cpp /usr/lib/x86_64-linux-gnu/crtn.o -isystem/usr/include/c++/v1 -lc -lgcc_s

15. why C/C++ library offeres only shared memory model?

## Template Meta Programming

16. can a template class be defined in a non-template class?

1. how to define a hash function for a user defined class?

## File System

1. how to get the current working directory?


## References

- [Google C++ Style Guide](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Header_Files)  
- [C++ Reference](http://en.cppreference.com/w/)  
- [C++11 Concurrency](http://www.justsoftwaresolutions.co.uk/threading/multithreading-in-c++0x-part-1-starting-threads.html)
- [Bjarne Stroustrup](http://www.stroustrup.com/)
- [ISO C++](http://isocpp.org/)
- [Meeting C++](http://www.meetingcpp.com/index.php/start.html)
- [Herb Sutter](http://herbsutter.com/)
- [Regular Expression](http://cpprocks.com/regex-cheatsheet/)
- [GCC Status](http://gcc.gnu.org/onlinedocs/libstdc++/manual/status.html#status.iso.tr1)
- [GNC C++ Library Manual](http://gcc.gnu.org/onlinedocs/libstdc++/manual/index.html)



- [Day 1 Keynote - Bjarne Stroustrup: C++11 Style](http://channel9.msdn.com/Events/GoingNative/GoingNative-2012/Keynote-Bjarne-Stroustrup-Cpp11-Style)
- [C++ and Beyond 2012: Andrei Alexandrescu - Systematic Error Handling in C++](http://channel9.msdn.com/Shows/Going+Deep/C-and-Beyond-2012-Andrei-Alexandrescu-Systematic-Error-Handling-in-C)
- [C++ and Beyond 2012: Herb Sutter - You don't know [blank] and [blank]](C++ and Beyond 2012: Herb Sutter - You don't know [blank] and [blank])
- [C++ and Beyond 2012: Herb Sutter - C++ Concurrency](http://channel9.msdn.com/Shows/Going+Deep/C-and-Beyond-2012-Herb-Sutter-Concurrency-and-Parallelism)



- [Learn STL: Vector vs. Deque - part I](http://www.youtube.com/watch?v=Ct8ykaKrKOA)
- [Learn STL: Vector vs. Deque - part II](http://www.youtube.com/watch?v=pW2jDTf82IM)


- [Writing a Daemon in C](http://www.danielhall.me/2010/01/writing-a-daemon-in-c/)



http://blogs.msdn.com/b/vcblog/archive/2015/02/13/find-your-favorite-library-for-c-in-nuget.aspx

http://tgockel.github.io/json-voorhees/index.html

https://en.wikibooks.org/wiki/More_C%2B%2B_Idioms