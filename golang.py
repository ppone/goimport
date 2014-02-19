#Author: Parag Patel

import os
import re
import subprocess

'''
        Prequisties need $GOPATH set and go binary in $PATH
'''

#TODO change to commandline argument
go_extension = ".go"
current_directory = os.getcwd()
package_to_install_dir = os.path.basename(current_directory)
package_to_install_re = r"package(\s)+" + package_to_install_dir
go_test = "go test"
go_dir = os.environ["GOPATH"] + "/src/" + package_to_install_dir
go_install = "go install"



def check_package_files_using_same_package_name_as_directory():
    """
        This code double checks that all of our package files have the same package.
        Raises a detailed exception message if at least one file does not have the same package.
        If all files have the same package, it does nothing
    """
    for file in os.listdir():
        if os.path.isfile(file) and go_extension in file:
            if re.match(package_to_install_re,open(file).read()):
                continue
            else:
                files_do_not_have_same_package_exception = "Make sure all " + go_extension + \
                    "files in this directory have the package " + package_to_install_dir
                raise Exception(files_do_not_have_same_package_exception)


def check_go_test_is_ok():
    """
        Make sure all go tests for the package run before we install the package
    """
    test_result = subprocess.getstatusoutput(go_test)[1]
    if 'ok' not in test_result:
        raise Exception("Please fix your Go Tests before you install package")

check_package_files_using_same_package_name_as_directory()

check_go_test_is_ok()

copy_files_from_cwd_to_go_path_src = "cp " + ""


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

