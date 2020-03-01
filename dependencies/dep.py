import subprocess
from pathlib import Path

common_install = {}
package_tree = {}


class package:
    def __init__(self, name, install_type=None, install_function=None):
        self.is_installed = False
        self.name = name
        self.install_type = install_type
        if install_function:
            self.install_function = install_function

    def install(self):
        if self.install_function:
            self.install_function()
        else:
            common_install[self.install_type]()
        # should check return on functions
        self.is_installed = True


def common_install_type(name):
    def wrap(f):
        common_install[name] = f
        return f
    return wrap


def requires(package_name, install_method=None, install_function=None, install_location=None):
    # register package
    if not package_name in package_tree:
        package_tree[package_name] = package(
            package_name, install_method, install_function)

    def wrap(f):
        return f
    return wrap


@requires("make", install_method="package-manager")
def hello():
    print("hello")


# allows types which require packages
@common_install_type("make")
@requires("build-essentials", "package-manager")
def mk(directory):
    subprocess.Popen("make")
    subprocess.Popen("sudo make install", stdin=subprocess.STDIN)


@requires("pynvim", None, lambda: subprocess.Popen("pip3 install --user pynvim"))
def custom_package():
    pass

@common_install_type("package-manager")
def package_manager(name)
    subprocess.Popen(f"sudo apt install {name}", stdin=subprocess.STDIN))
