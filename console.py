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

    def create(self, args):
        """ceate an instance of Basemodel"""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            cmd_dm = {'BaseModel': BaseModel}
            my_obj = cmd_dm[agrs]()
            my_obj.save()
            print("{}".format(my_obj.id))
            storage.save()

    def show(self, line):
        """printstring representation"""
        arg = line.split()
        object_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in object_dict:
            print("** no instance found **")
        else:
            print(object_dict["{}.{}".format(arg[0], arg[1])])

    def destroy(self, line):
        """Deletes an instance based on the class name and id"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
