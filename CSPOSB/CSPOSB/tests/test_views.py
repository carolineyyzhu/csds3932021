import unittest
from CSB.views import checkRequirements

class TestRC(unittest.TestCase):
    def test_checkRequirements(self):
        classes = []
        self.assertEqual(checkRequirements(classes),
                         (False, ["Total CS Credits", "Total CS Courses", "Core Courses", "Breadth Courses", "Depth Courses"]))
