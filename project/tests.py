from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from project.models import Project, Type

User = get_user_model()


class TestList(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ozcan", password="helloWorld_")
        self.type = Type.objects.create(name="Type 1")

    def testDbWithData(self):
        Project.objects.create(
            user=self.user,
            type=self.type,
            name="Test 1"
        )
        projects = Project.objects.count()

        self.assertGreater(projects, 0)

    def testDbWithoutData(self):
        projects = Project.objects.count()

        self.assertEqual(projects, 0)

    def testGET(self):
        Project.objects.create(
            user=self.user,
            type=self.type,
            name="Test 1"
        )

        response = self.client.get(path="/project/",content_type="application/json")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], "Test 1")

    def testPOST(self):
        data = {
            "user": self.user.id,
            "type": self.type.id,
            "name": "Test Project"
        }
        response = self.client.post(path="/project/", data=data, content_type="application/json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], "Test Project")

    def testPOSTWithWrongData(self):
        data = {
            # "user": 1,
            "type": 1,
            "name": "Hello"
        }
        self.assertRaises(ValidationError,
                          lambda: self.client.post(path="/project/", data=data, content_type="application/json"))
