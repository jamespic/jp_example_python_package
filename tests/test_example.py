from jp_example_python_package import *


def test_adder():
    assert add(1, 2) == 3


def test_message_cheeky():
    assert message_cheeky() == 'Hello World!\n'


def test_message_correct():
    assert message_correct() == u'Hello World!\n'
