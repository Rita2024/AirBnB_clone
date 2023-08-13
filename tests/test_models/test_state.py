#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Tests instances and methods from State class """

    st = State()

    def test_class_exists(self):
        """tests if class exists"""
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.st)), res)

    def test_user_inheritance(self):
        """test if State is a subclass of BaseModel"""
        self.assertIsInstance(self.st, State)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.st, 'name'))
        self.assertTrue(hasattr(self.st, 'id'))
        self.assertTrue(hasattr(self.st, 'created_at'))
        self.assertTrue(hasattr(self.st, 'updated_at'))

    def test_types(self):
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.st.name, str)
        self.assertIsInstance(self.st.id, str)
        self.assertIsInstance(self.st.created_at, datetime.datetime)
        self.assertIsInstance(self.st.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
