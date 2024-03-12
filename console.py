#!/usr/bin/python3
"""Defines the HBnB console."""
import difflib
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def tokenize(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            arg_split = split(arg[:brackets.span()[0]])
            stripped_arg = [i.strip(",") for i in arg_split]
            stripped_arg.append(brackets.group())
            return stripped_arg
    else:
        arg_split = split(arg[:braces.span()[0]])
        stripped_arg = [i.strip(",") for i in arg_split]
        stripped_arg.append(braces.group())
        return stripped_arg


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command line interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    new_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, arg):
        """Default behavior for cmdwhen input is invalid"""
        arg_dicts = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dicts.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    chars_remove = '":{}'
                    new_call = ''.join(
                            char for char in call if char not in chars_remove)
                    """clean_call = call.replace('"', '').replace("'", '')"""
                    return arg_dicts[command[0]](new_call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print()
        return True

    def emptyline(self):
        """Does nothing when receives an empty line."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id."""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an
            instance based on the class name and id"""
        classes = storage.all()
        args = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ".".join(args) not in classes:
            print("** no instance found **")
        else:
            print(classes["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        args = arg.split(" ")
        classes = storage.all()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in classes.keys():
            print("** no instance found **")
        else:
            del classes["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        args = tokenize(arg)
        if len(args) and args[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        else:
            alllist = []
            for val in storage.all().values():
                if len(args) > 0 and args[0] == val.__class__.__name__:
                    alllist.append(val.__str__())
                elif not arg:
                    alllist.append(val.__str__())
            print(alllist)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()"""
        count = 0
        for val in storage.all().values():
            argument = "".join(arg.split())
            val_class = val.__class__.__name__

            if argument == val_class:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class name> <id> <attribute name>
        '<attribute value>'
        """
        args = tokenize(arg)
        """print("args: '{}'\n".format(args))"""
        classes = storage.all()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.new_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in classes:
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        elif len(args) == 5:
            print("** value missing **")
        else:
            for val in storage.all().values():
                if args[0] == val.__class__.__name__:
                    class_instance = val
                    instance_attr = vars(class_instance)
                    for key, value in instance_attr.items():
                        if key == "id" and value == args[1]:
                            attr_name = args[2]
                            attr_value = args[3].strip('"')
                            instance_attr[attr_name] = attr_value
                            if len(args) == 6:
                                attr_name = args[4]
                                attr_value = args[5]
                                instance_attr[attr_name] = attr_value
                            break
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
