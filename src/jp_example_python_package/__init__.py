from __future__ import absolute_import, print_function
import io
import os
from .native import add


def message_cheeky():
    # The "wrong" way (but no external dependencies)
    with io.open(os.path.join(os.path.dirname(__file__), 'hello_world.txt')) as f:
        return f.read()


def message_correct():
    import pkg_resources
    # The "right" way (but makes package depend on setuptools)
    return pkg_resources.resource_string(__name__, 'hello_world.txt').decode('utf-8')


def hello(cheeky=True):
    if cheeky:
        print(message_cheeky())
    else:
        print(message_correct())


if __name__ == '__main__':
    hello()
