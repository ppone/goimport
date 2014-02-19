#!/usr/bin/env python3.3

#Author: Parag Patel

import os
import re
import subprocess

"""
        Prequisties need $GOPATH set and go binary in $PATH
"""

go_extension = ".go"
current_directory = os.getcwd()
package_to_install_dir = os.path.basename(current_directory)
package_to_install_re = r"package(\s)+" + package_to_install_dir
go_test = "go test oauth1"
go_dir = os.environ["GOPATH"] + "/src/"
go_dir_package = go_dir + package_to_install_dir + "/"
go_install = "go install"
make_dir_go_dir_package = "mkdir " + go_dir_package
copy_files_from_cwd_to_go_path_src = "cp " + "*" + go_extension + " " + go_dir_package


def run_command(command):
    run_c = subprocess.getstatusoutput(command)
    if run_c[0] != 0:
        err_msg = "Error running command: " + run_c[1]
        raise Exception(err_msg)
    return run_c[1]

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
    test_result = run_command(go_test)
    if 'ok' not in test_result:
        raise Exception("Please fix your Go Tests before you install package")

def check_else_make_directory():
    if not os.path.exists(go_dir_package):
        run_command(make_dir_go_dir_package)


check_package_files_using_same_package_name_as_directory()

check_go_test_is_ok()

check_else_make_directory()

run_command(copy_files_from_cwd_to_go_path_src)

os.chdir(go_dir_package)

run_command(go_install)

print("Package " + package_to_install_dir + " successfully installed")

