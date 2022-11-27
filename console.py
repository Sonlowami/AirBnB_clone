#!/usr/bin/python3

"""

Command Enterpreter entry point
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """

    Main class of the console
    """
    prompt = "(hbnb) "
    
    classes = {"BaseModel" : BaseModel, "User" : User, "State" : State, "City" : City, "Amenity" : Amenity, "Place" : Place, "Review" : Review}

    def do_quit(self, line):
        """exit"""
        return True

    def do_EOF(self, line):
        """exit"""
        return True

    def emptyline(self):
        "Do nothing"
        pass

    def do_create(self, line):
        """Create a BaseModel object"""
        if not line:
            print("** class name missing **")
        elif line in self.classes.keys():
            obj = self.classes[line]()
            print(obj.id)
            obj.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Print a string representation of an object"""
        if line:
            args = line.split(" ")
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                dic = storage.all()
                obj = dic[args[0] + "." +args[1]]
                print(obj)
            except KeyError:
                """if args[1] os not found"""
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        else:
                print("** class name missing **")

    def do_destroy(self, line):
        """Destroy one object"""
        if line:
            args = line.split(" ")
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                dic = storage.all()
                del dic[args[0] + "." +args[1]]
                storage.save()
            except KeyError:
                """if args[1] os not found"""
                print("** no instance found **")
            except IndexError:
                print("** instance id missing **")
        else:
                print("** class name missing **")

    def do_all(self, line):
        """Print all objects of the same class. Prints all
        objects if no class specified"""
        args = line.split(" ")
        dic = storage.all()
        if line and args[0] not in self.classes.keys():
            print("** class doesn't exist **")
            return
        try:
            res = []
            for val in dic.values():
                if type(val) == self.classes[args[0]]:
                    res.append(str(val))
            print(res)
        except IndexError:
            print(dic.values())
        except KeyError:
            for val in dic.values():
                res.append(str(val))
                print(res)
    
    def change_value(self, obj, args):
        """change values of attributes of an object"""
        print(len(args))
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return
        try:
            if hasattr(obj, args[2]):
                value = type(getattr(obj, args[2]))(args[3])
                setattr(obj, args[2], value)

        except (TypeError):
            print("** value missing **")

    def do_update(self, line):
        """Update an attribute in an object"""
        if line:
            args = line.split(" ")
            if args[0] not in self.classes.keys():
                print("** class doesn't exist **")
                return
            try:
                dic = storage.all()
                obj = dic[args[0] + "." +args[1]]
                self.change_value(obj, args)
                storage.save()
            except KeyError:
                print("** no instance found **")
        else:
                print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
