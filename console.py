#!/usr/bin/python3

"""

Command Enterpreter entry point
"""

import cmd
import models

class HBNBCommand(cmd.Cmd):
    """

    Main class of the console
    """
    
    prompt = "(hbnb) "
    classes = {"BaseModel" : models.base_model.BaseModel}

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
            models.storage.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
