#!/usr/bin/python3
""" Console to manage hbnb data """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json


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

    __classes = {'BaseModel', 'User', 'State', 'City',
                 'Amenity', 'Place', 'Review'}

    def do_create(self, args):
        """ceate an instance of Basemodel"""
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            cmd_dm = {'BaseModel': BaseModel,
                      'Place': Place,
                      'State': State,
                      'City': City,
                      'Amenity': Amenity,
                      'Review': Review,
                      'User': User}

            my_obj = cmd_dm[args]()
            my_obj.save()
            print("{}".format(my_obj.id))
            storage.save()

    def do_show(self, line):
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

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        arg = line.split()
        object_dict = storage.all()
        if len(arg) < 1:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            word = "{}.{}".format(arg[0], arg[1])
            if word in object_dict:
                del object_dict[word]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """prints all string representation of all instances"""
        begin = 0
        all_obj = [str(v) for v in storage.all().values()]
        if not args:
            begin = 1
            print('{}'.format(all_obj))
        elif args:
            arg_list = args.split()
        if args and arg_list[0] in HBNBCommand.__classes:
            begin = 1
            all_obj = storage.all()  # all() method from file_storage.py
            name = arg_list[0]
            all_obj = [str(v) for k, v in all_obj.items()
                       if name == v.__class__.__name__]
            print(all_obj)

        if begin == 0:
            print("** class doesn't exist **")

    def do_update(self, line):
        """update an instance based on the class name and id"""
        args = line.split()
        no_change = ["id", "created_at", "updated_at"]
        object_dict = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_id = "{}.{}".format(args[0], args[1])
            if class_id not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif args[2] not in no_change:
                new_obj = object_dict[class_id]
                new_obj.__dict__[args[2]] = args[3]
                new_obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
