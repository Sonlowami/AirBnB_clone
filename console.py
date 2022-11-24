#!/usr/bin/python3

"""

Command Enterpreter entry point
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """

    Main class of the console
    """
    
    prompt = "(hbnb) "

    def do_quit(self, line):
        """exit"""
        return True

    def do_EOF(self, line):
        """exit"""
        return True

    def emptyline(self):
        "Do nothing"
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
