#!/usr/bin/python3
""" Console to manage hbnb data """

import cmd

class HBNBCommand(cmd.Cmd):
    """ Class HBNBCommand CLI, entry command interpreter """
    prompt = '(hbnb) '

    def quit(self, line):
        """Quit command to exit the program"""
        return True

    def EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Handle empty line when is passed as an argument"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
