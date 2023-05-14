#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
import json


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

    def __init__(self):
        super().__init__()
        self.instances = {}
        self.__models = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }
        self.__valid_methods = ['create', 'show', 'destroy', 'all', 'update']
        self.allowed_classes = list(self.__models.keys())
        self.__options = [
                '{}.{}'.format(k, v)
                for k, v in self.__models.items()
                for v in dir(v) if not v.startswith('_')
                ]

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
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

    def help_create(self):
        """Dislay information about the create command."""
        print("Usage: create <class>")
        print("Create a new class, print its id, and save it to file.json")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
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

    def help_show(self):
        """Displays help information for the show command"""
        print("Displays an object's string representation based\
                on the objects class and id")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
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

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()

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

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name.
        Usage:
            all             Prints all string representaion of all instances
                            from all classes.

            <class name>.all() Prints all string representaion of all instances
                                from the given class name.
        """
        if not arg:
            print("class name missing")
            return
        if arg not in self.__models:
            print("class doesn't exist")
            return
        result = []
        for instance in self.instances.values():
            if arg == "*" or instance["__class__"] == arg:
                result.append(json.dumps(instance, indent=4))
                print("\n".join(result))

    def default(self, line):
        """
        Called on an input line when the command prefix is not recognized.
        """
        parts = line.split(".")
        if len(parts) == 2 and parts[1] == "all()":
            # Retrieve all instances of the specified class
            class_name = parts[0]
            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return
            all_instances = storage.all()
            instances = [str(obj) for obj in all_instances.values()
                         if type(obj).__name__ == class_name]
            print(instances)
        elif len(parts) == 2 and parts[1] == "count()":
            # Retrieve the count of all instances of the specified class
            class_name = parts[0]
            if class_name not in self.allowed_classes:
                print("** class doesn't exist **")
                return
            all_instances = storage.all()
            count = sum(1 for obj in all_instances.values()
                        if type(obj).__name__ == class_name)
            print(count)
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
