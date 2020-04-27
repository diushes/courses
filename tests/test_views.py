from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from courses import CourseSerializer
from courses import Course, Category, Contact, Branch
class Test_CourseListView(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.client = APIClient()
        self.contact = Contact.objects.create(choice="FACEBOOK")
        self.category = Category.objects.create(name="Language", imgpath="Some image")

    def test_get_all_courses(self):
        for i in range(5):
            course = Course.objects.create(name="Some test course", description="Really good test course", logo="Some test logo",
                              contact=self.contact, category=self.category)
            Branch.objects.create(latitude=str(i), longtitude=str(i), address="Some test address", course=course)
        response = self.client.get(reverse('courses:courses'))
        courselist = Course.objects.all()
        serializer = CourseSerializer(courselist, many=True)
        self.assertEquals(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_post_course(self):
        payload = {
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
        resp = self.client.post(reverse("courses:courses"), payload, content_type="application/json")
        self.assertEquals(resp.status_code, 201)
        exists = Course.objects.filter(name=resp.data["name"]).exists()
        self.assertTrue(exists)


class Test_SingleCourseView(TestCase):
    @classmethod
    def setUp(self) -> None:
        self.client = APIClient()
        self.contact = Contact.objects.create(choice="FACEBOOK")
        self.category = Category.objects.create(name="Language", imgpath="Some image")
        self.course = Course.objects.create(name="Some test course", description="Really good test course", logo="Some test logo",
                              contact=self.contact, category=self.category)
        Branch.objects.create(latitude="14.3", longtitude="13.4", address="Manas street 56", course=self.course)

    def test_get_single_course(self):
        response = self.client.get(
            reverse('courses:retrieve', kwargs={'pk': self.course.pk}))
        one_course = Course.objects.get(pk=self.course.pk)
        serializer = CourseSerializer(one_course)
        self.assertEquals(response.data, serializer.data)

    def test_delete_course(self):
        response = self.client.delete(
            reverse('courses:retrieve', kwargs={'pk': self.course.pk}))
        self.assertEquals(response.status_code, 204)









