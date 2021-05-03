from django.test import TestCase
from CSB.models import Course, Degree, Requirement, Requires, Fulfills


class PostTest(TestCase):
    def test_course(self):
        test_class = Course.objects.create(cid=11234532, number=299, department="CSDS", semester="Spring", credits=3,
                                           name="Test Class")
        self.assertEqual(test_class.cid, 11234532)

    def test_degree(self):
        test_degree = Degree.objects.create(did=21343542, name="Test Degree", total_credits=28)
        self.assertEqual(test_degree.total_credits, 28)

    def test_requirement(self):
        test_requirement = Requirement.objects.create(rid=32987235, name="Test Requirement")
        self.assertEqual(test_requirement.rid, 32987235)

    def test_fulfills(self):
        test_fulfills = Fulfills.objects.create(
            cid=Course.objects.create(cid=11234532, number=299, department="CSDS", semester="Spring", credits=3,
                                      name="Test Class"),
            rid=Requirement.objects.create(rid=32987235, name="Test Requirement"), concentration="none")
        self.assertEqual(test_fulfills.concentration, "none")

    def test_require(self):
        test_requires = Requires.objects.create(
            did=Degree.objects.create(did=21343542, name="Test Degree", total_credits=28),
            rid=Requirement.objects.create(rid=32987235, name="Test Requirement"), quantity=5, credits=15)
        self.assertEqual(test_requires.quantity, 5)
