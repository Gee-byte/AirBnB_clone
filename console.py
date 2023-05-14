#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd


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

            <class name>.all() Prints all string representaion of all instances
                                from the given class name.
        """
        args = line.split()
        all_instances = storage.all()

        if not args:
            print([str(key) for key in all_instances.values()])
            return
        else:
            try:
                class_name, method_name = line.split('.')
                if method_name != 'all()':
                    raise ValueError
                cls = models.classes[class_name]

                if args[0] not in self.allowed_classes:
                    print("** class doesn't exist **")
                return
            except (ValueError, KeyError):
                print("** Unknown syntax:", line)
                return

            print([str(obj) for obj in all_instances.all(cls).values()])

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
<<<<<<< HEAD
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
=======
>>>>>>> parent of 2560089... added a feature to retrieve the number of instances of a class
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
