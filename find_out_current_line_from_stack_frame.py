import unittest
from inspect import currentframe, getframeinfo
from os import path

def print_loc():
    fi = getframeinfo(currentframe().f_back)
    print("at line ",fi.lineno, " in ", path.basename(fi.filename))

# print_loc()

def get_loc():
    fi = getframeinfo(currentframe().f_back)
    return fi.lineno

def get_filename():
    fi = getframeinfo(currentframe().f_back)
    return path.basename(fi.filename)

class TestStackFrame(unittest.TestCase):

    def test_line_no(self):
        self.assertEqual(22,get_loc())

    def test_file_name(self):
        self.assertEqual("find_out_current_line_from_stack_frame.py",get_filename())

if __name__ == '__main__':
    unittest.main()
