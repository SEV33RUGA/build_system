import unittest
import os
from build_system import get_yaml, show_names, show_name_details


class TestGetYaml(unittest.TestCase):

    def test_get_yaml(self):
        self.assertEqual(*get_yaml('builds.yaml'), 'builds')
        self.assertEqual(*get_yaml('tasks.yaml'), 'tasks')

    def test_files(self):
        self.assertRaises(FileNotFoundError, get_yaml, 'anyfile')
        self.assertRaises(NotADirectoryError, get_yaml, os.getcwd())
        self.assertRaises(FileNotFoundError, get_yaml, '\\builds.yaml')
        self.assertRaises(FileNotFoundError, get_yaml, '\builds.yaml')

        with open("wrong.yaml", "wb") as f:
            f.write(bytes(0xFFFF))
            self.assertRaises(TypeError, get_yaml, "wrong.yaml")
        os.remove("wrong.yaml")

    def test_types(self):
        self.assertRaises(TypeError, get_yaml, True)
        self.assertRaises(TypeError, get_yaml, -12)
        self.assertRaises(TypeError, get_yaml, [1, 2, 3])
        self.assertRaises(TypeError, get_yaml, {"asd": 12})


class TestShowFuncs:
    builds = get_yaml("builds.yaml")
    tasks = get_yaml("tasks.yaml")


class TestShowNames(unittest.TestCase, TestShowFuncs):

    def test_show_names(self):
        self.assertEqual(isinstance(show_names(self.builds), list), True)
        self.assertEqual(isinstance(show_names(self.tasks), list), True)

    def test_types(self):
        self.assertRaises(TypeError, show_names, 32)
        self.assertRaises(TypeError, show_names, "string")
        self.assertRaises(TypeError, show_names, (1, 2, 3))
        self.assertRaises(TypeError, show_names, [1, 2])

    def test_dict(self):
        self.assertRaises(KeyError, show_names, {})
        self.assertRaises(KeyError, show_names, {"key": 123})


class TestShowNameDetails(unittest.TestCase, TestShowFuncs):

    def test_show_name_details(self):
        for d in [self.builds, self.tasks]:
            for name in show_names(d):
                self.assertEqual(show_name_details(d, name), True)
        self.assertEqual(show_name_details(self.tasks, "asd"), False)

    def test_types(self):
        self.assertRaises(TypeError, show_name_details, self.builds, 32)
        self.assertRaises(TypeError, show_name_details, 23.43, "approach_important")
        self.assertRaises(KeyError, show_name_details, {}, "approach_important")
        self.assertRaises((KeyError, TypeError), show_name_details, {}, ["any"])
        self.assertRaises(TypeError, show_name_details, "hello", {})
        self.assertRaises((KeyError, TypeError), show_name_details, {"key"}, "approach_important")
