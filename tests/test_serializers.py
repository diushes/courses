from django.test import TestCase
from courses import Course, Category, Contact
from courses import CourseSerializer


class Test_CourseSerializer(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.contact = Contact.objects.create(choice="FACEBOOK")
        self.category = Category.objects.create(name="Language", imgpath="Some image")
    def test_serializer_create_method_works(self):
        data = {
        "name": "Chinese language school",
        "description": "Learn how to speak chinese in a month or less",
        "logo": "Some logo",
        "contact": "FACEBOOK",
        "category": "Language",
        "branches": [
            {
                "latitude": "103.5",
                "longtitude": "158.6",
                "address": "Bakery street 27"
            }
        ]
                }
        serializer = CourseSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        serializer.save()

        exists = Course.objects.get(id=1)
        self.assertIsNotNone(exists)



