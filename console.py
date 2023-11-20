#!/usr/bin/python3
"""This module contains a command interpreter."""
import cmd
import models
import re


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to storage.

        Usage: create <class name>
        """
        line = line.strip()
        if line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval('models.' + line + '()')
            models.storage.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on
           the class name and id.

        Usage: show <class name> <id>
        """
        line = line.strip()
        if line == "":
            print("** class name missing **")
            return

        line_arr = line.split()
        if (line_arr[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")
            return

        if (len(line_arr) == 1):
            print("** instance id missing **")
            return

        object_store = models.storage.all()

        for key, val in object_store.items():
            if (key.find(line_arr[0]) != -1 and val.id == line_arr[1]):
                print(val)
                break
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.

        Usage: destroy <class name> <id>
        """
        line = line.strip()
        if line == "":
            print("** class name missing **")
            return

        line_arr = line.split()
        if (line_arr[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")
            return

        if (len(line_arr) == 1):
            print("** instance id missing **")
            return

        object_store = models.storage.all()

        for key, val in object_store.items():
            if (key.find(line_arr[0]) != -1 and val.id == line_arr[1]):
                object_store.pop(key)
                models.storage.save()
                return

        print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based
            or not on the class name.

        Usage: all <class name>
        """
        line = line.strip()

        if (line in HBNBCommand.__classes):
            object_store = models.storage.all()
            for key, val in object_store.items():
                if (key.find(line) != -1):
                    print(val)
            return

        if (line == ""):
            object_store = models.storage.all()
            for key, val in object_store.items():
                print(val)
            return

        print("** class doesn't exist **")

    def conv(self, val):
        if re.match(r'^[+-]?\d+$', val):
            return int(val)
        elif re.match(r'^[+-]?\d*\.\d+$', val):
            return float(val)
        else:
            return val

    def do_update(self, line):
        """Updates an instance based on the class name and id.

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        line = line.strip()
        if line == "":
            print("** class name missing **")
            return

        line_arr = line.split()
        if (line_arr[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")
            return

        if (len(line_arr) == 1):
            print("** instance id missing **")
            return

        object_store = models.storage.all()

        for key, val in object_store.items():
            if (key.find(line_arr[0]) != -1 and val.id == line_arr[1]):
                break
        else:
            print("** no instance found **")
            return

        if (len(line_arr) < 3):
            print("** attribute name missing **")
            return

        if (len(line_arr) < 4):
            print("** value missing **")
            return

        if (line_arr[2] in ['id', 'created_at', 'updated_at']):
            return

        attr_val = line_arr[3].lstrip('"').rstrip('"')
        conv_attr = self.conv(attr_val)

        for key, val in object_store.items():
            if (key.find(line_arr[0]) != -1 and val.id == line_arr[1]):
                setattr(val, line_arr[2], conv_attr)
                models.storage.save()
                break

    def emptyline(self):
        return

    def do_EOF(self, line):
        """EOF command to exit the program."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program.\n"""
        return True
    
    #************ new code
        
    def parseline(self, line):
        # print(f'parseline {line}')

        ret = cmd.Cmd.parseline(self, line)
        return ret
    
    #************ new code


if __name__ == "__main__":
    HBNBCommand().cmdloop()
