![alt text](assets/hbnb.png)

# AirBnB clone

# Description
AirBnB clone is a web application that is still under development. It is a clone of AirBnB, and it integrates database storage, a back-end APIs, and front-end interfacing. Currently, only the back-end console has been implemented.

# Console
The console is an interactive command-line interpreter designed to manage the backend of an AirBnB clone application. It provides a user-friendly interface for handling and manipulating all classes utilized by the application and It implements commands for creating, showing, destroying, updating, and listing instances of these classes. All changes made to the instances are saved to a JSON file.

# Getting Started
To start using Console, clone the repository from GitHub:
```
$ git clone https://github.com/username/AirBnB_clone.git
```
# Usage

The AirBnB console can be run both interactively and non-interactively. To run the console in interactive mode you need to execute the command ./console.py in your terminal. This will start the console and you will see a prompt (hbnb) indicating that the console is ready to receive commands. You can then enter a command and press enter to execute it.
```$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
To run the console non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.
```$ echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
$
```
Once the interpreter has started, you can enter commands in the following format:
```
(hbnb) command class_name class_id [attribute_name] [attribute_value]
```
Where ```command``` can be one of the following:
- ```create```:create a new instance of a class that inherits from BaseModel.
- ```show```: display the string representation of an instance of a class.
- ```all```: display the string representations of all instances of a class.
- ```destroy```: delete an instance of a class.
-  ```update```: update an instance of a class.
```class_name``` is the name of the class you want to create an instance of, and
class_id is the ID of the instance you want to create, show, destroy, or update.
```attribute_name``` and ```attribute_value``` are optional arguments that allow you to update the attributes of an 
instance.
For example, to create a new instance of the BaseModel class:
```(hbnb) create BaseModel```
This will create a new instance of the class and return its ID.

To show the string representation of an instance of the BaseModel class:
```
(hbnb) show BaseModel 1234-1234-1234
```
This will display the string representation of the instance with the ID ```1234-1234-1234```.

To display the string representations of all instances:
```
(hbnb) all BaseModel
```
This will display the string representations of all instances.

To delete an instance of the BaseModel class:
```
(hbnb) destroy BaseModel 1234-1234-1234
```
This will delete the instance with the ID ```1234-1234-1234```.

To update an instance of the BaseModel class:
```
(hbnb) update BaseModel 1234-1234-1234 email "sara@mail.com"
```
This will update the email attribute of the instance with the ID ```1234-1234-1234``` to 
**sara@mail.com**.














