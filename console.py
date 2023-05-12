#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
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

    prompt = ' (hbnb) '

    def __init__(self, completekey='tab'):
        super().__init__(completekey=completekey)
        self.__models = {'BaseModel': BaseModel}
        self.__valid_methods = ['create', 'show', 'destroy', 'all', 'update']
        self.allowed_classes = list(self.__models.keys())
        self.__options = [
                '{}.{}'.format(k, v)
                for k, v in self.__models.items()
                for v in dir(v) if not v.startswith('_')
                ]

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def do_create(self, line):
        """Create command to create a new instance of a class"""
        args = line.split()
        if not args:
            print("** iclass name missing **")
            return

        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, line):
        """Show command to print the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return

        instance = all_instances[key]
        print(instance)

    def do_destroy(self, line):
        """Destroy command to delete an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = class_name + '.' + instance_id
        all_instances = storage.all()
        if key not in all_instances:
            print("** no instance found **")
            return

        del all_instances[key]
        storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or
        not on the class name.
        Usage:
            all             Prints all string representaion of all instances
                            from all classes.

            all <class name>Prints all sting representaion of all instances
                            from the given class name.
        """
        args = line.split()
        all_instances = storage.all()

        if len(args) == 0:
            print([str(all_instances[k]) for k in all_instances])
        else:
            class_name = args[0]
            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return

            instances = [str(all_instances[k]) for k in all_instances
                         if k.split('.')[0] == class_name]
            print(instances)

    def do_update(self, line):
        """Update command to update an instance"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.allowed_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = None
        value = None

        if len(args) < 3:
            print("** attribute name missing **")
            return

        key = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        value_str = args[3]
        try:
            value = int(value_str)
        except ValueError:
            if value_str.startswith('"') and value_str.endswith('"'):
                value = value_str[1:-1]
            else:
                print("** value missing **")
                return

        objs = storage.all()
        key_to_update = class_name + "." + obj_id
        if key_to_update not in objs:
            print("** no instance found **")
            return

        obj = objs[key_to_update]
        setattr(obj, key, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
