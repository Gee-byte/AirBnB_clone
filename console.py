#!/usr/bin/python3
import cmd

"""
This module defines the HBNBCommand class, a command interpreter that
implements commands for creating, showing, destroying, updating and listing
instances of classes that inherit from BaseModel.

Usage:
    $./console.py
Inside the console, the user can enter commands in the following format:

(hbnb) command class_name class_id [attribute_name] [attribute_value]

Examples:
(hbnb) create BaseModel
(hbnb) show BaseModel 1234-1234-1234
(hbnb) destroy BaseModel 1234-1234-1234
(hbnb) all BaseModel
(hbnb) update BaseModel 1234-1234-1234 email "sara@mail.com"

"""


class HBNBCommand(cmd.Cmd):
    """
    This class defines a command-line interpreter for managing instances of
    classes that inherit form 'BaseModel'.It allows the user to create,
    show, destroy, update and list instances of classes,
    and saves all changes to a JSON file.

    Attributes:
        prompt (str): The prompt displayed befor the user input.
                        Default value is "(hbnb)".

    Methods:
        do_quit(args) -> bool:
            Exit the command-line interpreter.

        do_EOF(args) -> bool:
            Exit the command-line interpreter when the end-of-file
            character is received.

        do_create(line):
            Create a new instance of a class that inherits from `BaseModel`.

        do_show(line):
            Display the string representation of an instance of a class
            that inherits from `BaseModel`.

        do_all(line):
            Display the string representations of all instances of a
            class that inherits from `BaseModel`.

        do_destroy(line):
            Delete an instance of a class that inherits from `BaseModel`.

        do_update(line):
            Update an instance of a class that inherits from `BaseModel`.

    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Return True upon receiving quit command"""
        return True

    def help_quit(self):
        """Dispaly information about the quit command."""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Retrun upon receiving an EOF signal"""
        print("")
        return True

    def help_EOF(self):
        """Display information about EOF signal handling."""
        print("EOF signal to exit the program")

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
