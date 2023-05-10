#!/usr/bin/python3
import cmd

"""Defines a HBNBCommand class."""


class HBNBCommand(cmd.Cmd):
    """
    Command-line interpreter that implements commands using 'cmd.Cmd'
    module.
    It displays a custom prompt (hbnb) and handles the quit and EOF commands.

    Attributes:
        prompt: A string that defines the prompt to display befor the user
                input.Default value is (
                hbnb).
    Methods:
        do_quit(args): A method that handles the 'quit' command.It returns
                        'True' to signal the program to exit.
        do_EOF(args): A method that handles the 'EOF'(End Of File)command,
                        It prints a newline and returns 'True' to signal the
                        program to exit.
    """

    prompt = ' (hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
