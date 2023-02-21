#!/usr/bin/python3
""" Console to manage hbnb data """

import cmd


class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand CLI, entry command interpreter """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Handle empty line when is passed as an argument"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
