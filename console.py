#!/usr/bin/python3
"""This module contains a command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        return

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program.\n"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
