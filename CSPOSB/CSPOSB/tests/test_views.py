import unittest
from django.test import TestCase, Client
from CSB.views import TESTcheckRequirements
from django.urls import reverse


class TestRC(unittest.TestCase):
    def test_checkRequirements(self):
        classes = []
        valid = TESTcheckRequirements(classes, 1, "software engineering")[0]
        self.assertEqual(valid, True)
        #'Depth', 'Breadth', 'SAGES', 'TechnicalElectiveGroup1', 'TotalCS', 'TotalCredits', 'GeneralBreadth', 'Core', 'Engineering'))


class TestViews(TestCase):
    def test_index_GET(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_posb(self):
        client = Client()
        response = client.get(reverse('PoSB'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProgramBuilder.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_rChecker(self):
        client = Client()
        response = client.get(reverse('RChecker'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'RChecker.html')
        self.assertTemplateUsed(response, 'base.html')
