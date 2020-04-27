from django.test import TestCase
from courses import Course, Category, Branch, Contact

class CategoryModelTest(TestCase):
    @classmethod
    def setUp(cls):
        Category.objects.create(name="Culinary", imgpath="Some image")
    def test_category_name(self):
        category = Category.objects.get(id=1)
        field_label = category.name
        self.assertEquals(field_label, 'Culinary')
class CourseModelTest(TestCase):
    @classmethod
    def setUp(cls):
        contact = Contact.objects.create(choice="FACEBOOK")
        category = Category.objects.create(name="Language", imgpath="Some image")
        Course.objects.create(name="German Language courses", description="Really good course", logo="Some logo", contact=contact, category=category)

    def test_course_got_correct_category_name(self):
        course_category = Course.objects.get(id=1).category.name
        self.assertEquals(course_category, "Language")
    def test_course_got_correct_contact(self):
        course_contact = Course.objects.get(id=1).contact.choice
        self.assertEquals(course_contact, "FACEBOOK")
    def test_course_description_does_not_exceed_the_limit(self):
        max_length = Course.objects.get(id=1)._meta.get_field("description").max_length
        self.assertEquals(max_length, 500)

class BranchModelTest(TestCase):
    @classmethod
    def setUp(self) -> None:
        contact = Contact.objects.create(choice="FACEBOOK")
        category = Category.objects.create(name="Language", imgpath="Some image")
        course_to_test = Course.objects.create(name="German Language courses", description="Really good course", logo="Some logo", contact=contact, category=category)
        Branch.objects.create(latitude="13.4", longtitude="14.3", address="Manasa st.", course=course_to_test)

    def test_branch_is_attached_to_the_correct_course(self):
        branch = Branch.objects.get(id=1)
        course = Course.objects.get(id=1)
        self.assertEquals(branch.course, course)









        






#
##class BranchModelTest(TestCase):
##    def setUp(cls):
##        Branch.objects.create(latitude="13.4",longtitude="14.3", address="Chui St.")
# # def test_date_of_death_label(self):
# #     author=Author.objects.get(id=1)
# #     field_label = author._meta.get_field('date_of_death').verbose_name
# #     self.assertEquals(field_label,'died')
# #
# # def test_first_name_max_length(self):
# #     author=Author.objects.get(id=1)
# #     max_length = author._meta.get_field('first_name').max_length
# #     self.assertEquals(max_length,100)
# #
# # def test_object_name_is_last_name_comma_first_name(self):
# #     author=Author.objects.get(id=1)
# #     expected_object_name = '%s, %s' % (author.last_name, author.first_name)
# #     self.assertEquals(expected_object_name,str(author))
# #
# # def test_get_absolute_url(self):
# #     author=Author.objects.get(id=1)
# #     #This will also fail if the urlconf is not defined.
# #     self.assertEquals(author.get_absolute_url(),'/catalog/author/1')
# #