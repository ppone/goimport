#Author: Parag Patel

import os
import re


#TODO change to commandline argument
go_extension = ".go"
current_directory = os.getcwd()
packagetoinstalldir = os.path.basename(current_directory)
packagetoinstallre = r"package(\s)+" + packagetoinstalldir


def check_package_files_using_same_package():
    """
        This code double checks that all of our package files have the same package.  Raises a detailed exception message if at least one file does not have the same package.
        If all files have the same package, it does nothing
    """
    for file in os.listdir():
        if os.path.isfile(file) and go_extension in file:
            if re.match(packagetoinstallre,open(file).read()):
            #print("package is in file ", file)
                continue
            else:
                files_do_not_have_same_package_exception =  "Make sure all " + go_extension + " files in this directory have the package " + packagetoinstalldir
                raise Exception(files_do_not_have_same_package_exception)



check_package_files_using_same_package()

packageinstalled = False

#
# print(current_directory)
# print("hello")
# os.chdir("/")
# print(os.getcwd)
# godir = os.environ["GOPATH"] + "/src"
# os.chdir(godir)
# print("Current directory is ", os.getcwd())
# for i in os.listdir():
#         if i == packagetoinstall:
#             packageinstalled = True
#             break

#if packageinstalled:

