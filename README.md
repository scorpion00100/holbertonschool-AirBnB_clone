# AirBnB clone project

![enter image description here](https://i.imgur.com/44u0pXG.png)

The goal of the project was to deploy a recreation of the AirBnB website. 

The first step of this project is to write a command interpreter to manage our AirBnB objects. This first step is very important because we will use what we build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

In our case, we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object


## Learning Objectives

- Serialization / Deserialization flow (object <-> Dict <-> Json <-> file)
- Packages / Modules / Cyclical imports / How to import / Prevent execution /Etc.
- Layered architecture
- Interfaces (storage)
- Abstract Classes (BaseClass)

### General

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function


## Execution

Your shell should work like this in interactive mode:

```bash
  $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash
  $ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash


## Console commands

| Name | Description     |
| :-------- | :-------------- |
| `create`      | creates a new instance of the class passed by argument | 
| `show` | Prints the string representation of an instance |
| `destroy`| Deletes an instance that was already created |
| `all` | Prints string representation of all instances or of all instances of a specified class |
| `update` | Updates an instance attribute if exists otherwise create it. |
| `quit` | Exit the program. |
| `EOF` | Exit the program. |

## Supported classes :

- **BaseModel** : parent class
- **User** : inherits from BaseModel class
- **State** : inherits from BaseModel class
- **City** : inherits from BaseModel class
- **Amenity** : inherits from BaseModel class
- **Place** : inherits from BaseModel class
- **Review**: inherits from BaseModel class

## Authors

- Dan Bethel IRYIVUZE - 5625@holbertonschool.com
- Marlyne IHORIMBERE - 5635@holbertonschool.com
