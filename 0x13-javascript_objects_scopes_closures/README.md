# JAVASCRIPT - Objects, Scopes and Closures.

## Introduction
An object is a collection of related data and/or functionality. These usually consist of several variables and functions
(which are called properties and methods when they are inside objects).

As with many things in JavaScript, creating an object often begins with defining and initializing a variable
	const person = {};

### Dot Notation
You access the object's properties and methods using dot notation. The object name (person) acts as the 
namespace — it must be entered first to access anything inside the object. 
Next you write a dot, then the item you want to access — this can be the name of a simple property, 
an item of an array property, or a call to one of the object's methods,
	person.age;

### Bracket notation
Bracket notation provides an alternative way to access object properties. Instead of using dot notation
	person["age"];

> [!TIP]
> Dot notation is generally preferred over bracket notation because it is more succinct and easier to read. 
> However there are some cases where you have to use square brackets. For example, if an object property 
> name is held in a variable, then you can't use dot notation to access the value, but you can access the value using bracket notation.

- [x] I love coding
- [x] I use Kali linux

:kenya:
