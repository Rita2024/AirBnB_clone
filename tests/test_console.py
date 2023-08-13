#!/usr/bin/python3
"""console test"""

import unittest
import console
from console import HBNBCommand


class test_console(unittest.TestCase):
    """class test the console"""

    def create(self):
        """instance creation"""
        return HBNBBCommand()

    def test_quit(self):
        """quit method test
        """

        con = self.create()
        self.assertTrue(con.onecmd("quit"))

        def test_EOF(self):
            """EOF method test
            """

            con = self.create()
            self.assertTrue(con.onecmd("EOF"))
