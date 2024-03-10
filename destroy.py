def do_destroy(self, arg):
        """Usage: destroy <class> <id>
        Delete a class instance of a given id."""
        args = split(arg)
        classes = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in classes.keys():
            print("** no instance found **")
        else:
            del classes["{}.{}".format(args[0], args[1])]
            storage.save()
            

def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        args = split(arg)
        classes = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in classes:
            print("** no instance found **")
        else:
            print(classes["{}.{}".format(args[0], args[1])])


def do_all(self, arg):
     """Usage: all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
     args = split(arg)
     if len(args) > 0 and args[0] not in HBNBCommand.__classes:
           print("** class doesn't exist **")
     else:
          alllist = []
          for val in storage.all().values():
               if len(args )> 0 and args[0] == val.__class__.__name__:
                    alllist.append(val.__str__())
               elif len(args) == 0:
                    alllist.append(val.__str__())
                    print(alllist)
                    
def do_count(self, arg):
     """Usage: count <class> or <class>.count()"""
     args = split(arg)
     count = 0
     for val in storage.all().values():
          if arg[0] == val.__class__.__name__:
               count+=1
     print(count)
     