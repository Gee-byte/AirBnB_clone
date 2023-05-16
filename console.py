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
import shlex


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

    __classes = [
            "BaseModel",
            "User",
            "State",
            "Place",
            "City",
            "Amenity",
            "Review"
            ]

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        model_class = globals()[arg]
        if model_class is not None:
            obj = model_class()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """Dislay information about the create command."""
        print("Usage: create <class>")
        print("Create a new class, print its id, and save it to file.json")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objects = storage.all()
        key = args[0] + '.' + args[1]
        if key not in objects:
            print("** no instance found **")
            return
        obj = objects[key]
        print(obj.__str__())

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

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + '.' + args[1]
        all_instances = storage.all()
        if key not in all_instances.keys():
            print("** no instance found **")
            return

        del all_instances[key]
        storage.save()

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        try:
            args[1]
        except Exception:
            print("** instance id missing **")
            return
        objects_dict = storage.all()
        my_key = args[0] + "." + args[1]
        if my_key not in objects_dict:
            print("** no instance found **")
            return
        try:
            args[2]
        except Exception:
            print("** attribute name missing **")
            return
        try:
            args[3]
        except Exception:
            print("** value missing **")
            return
        if args[3]:
            setattr(objects_dict[my_key], args[2], args[3])
            storage.save()
        else:
            print("** attribute doesn't exist **")

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

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or
        not on the class name.
        Usage:
            all             Prints all string representaion of all instances
                            from all classes.

            all() <class name) Prints all string representaion of all instances
                                from the given class name.
        """
        tokens = arg.split()
        objects_dict = storage.all()
        if not tokens:
            str_repr_list = [str(obj) for obj in objects_dict.values()]
        else:
            class_name = tokens[0]
            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            str_repr_list = [str(obj) for obj in objects_dict.values()
                             if type(obj).__name__ == class_name]
        print(str_repr_list)

    def do_count(self, class_name):
        """
        Retrieves the number of instances of a given class.

        """
        count = 0
        for obj_id, obj in storage.all().items():
            if type(obj).__name__ == class_name:
                count += 1
        return count

    def do_update_dict(self, arg):
        """
        Updates an instance based on its ID with
        a dictionary representation.
        Usage: <class name>.update(<id>, <dictionary representation>)
        """
        args = shlex.split(arg)
        if len(args) < 3:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = class_name + '.' + obj_id
        objs = storage.all()
        if key not in objs:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return
        try:
            # Convert the dictionary string to a dictionary object
            update_dict = json.loads(args[2])
        except ValueError:
            print("** invalid JSON **")
            return
        obj = objs[key]
        for attr, value in update_dict.items():
            setattr(obj, attr, value)
            storage.save()

    def default(self, arg):
        """
        Parses input for the format <class name>.<method>() and calls the
        corresponding method.
        """
        # Define regex patterns for valid commands
        all_pattern = re.compile(r'^(\w+)\.all\(\)$')
        count_pattern = re.compile(r'^(\w+)\.count\(\)$')
        show_pattern = re.compile(r'^(\w+)\.show\(\"([\w-]+)\"\)$')
        destroy_pattern = re.compile(r'^(\w+)\.destroy\(\"([\w-]+)\"\)$')
        update_pattern = re.compile(r'^(\w+)\.update\(\"([\w-]+)\", '
                                    r'\"([\w\s_]+)\", \"([\w\s_]+)\"\)$')

        # Match input against regex patterns
        match = all_pattern.match(arg)
        if match:
            class_name = match.group(1)
            self.do_all(class_name)
            return

        match = count_pattern.match(arg)
        if match:
            class_name = match.group(1)
            count = self.do_count(class_name)
            print(count)
            return

        match = show_pattern.match(arg)
        if match:
            class_name = match.group(1)
            obj_id = match.group(2)
            self.do_show(f"{class_name} {obj_id}")
            return
        match = destroy_pattern.match(arg)
        if match:
            class_name = match.group(1)
            obj_id = match.group(2)
            key = class_name + '.' + obj_id
            objs = storage.all()
            if key in objs:
                objs.pop(key)
                storage.save()
                return
            else:
                print(f"** no instance found **")
                return
        match = update_pattern.match(arg)
        if match:
            class_name = match.group(1)
            obj_id = match.group(2)
            attr_name = match.group(3)
            attr_value = match.group(4)
            self.do_update(f"{class_name} {obj_id} {attr_name} {attr_value}")
            return

        # If input doesn't match any pattern, print an error message
        print(f"*** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
