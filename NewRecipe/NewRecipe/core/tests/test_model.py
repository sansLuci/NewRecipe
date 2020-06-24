from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

	def test_create_user_with_email_successful(self):
		email = 'sanskar@jain.com'
		password = 'sanskar123'
		user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.password, password)

	def test_new_user_email_normalized(self):
		"""Normalized means '@ABC.COM' should be in lowercase(not case sensitive) => '@abc.com'"""
		email = 'sanskarj@JAIN.COM'
		user = get_user_model().objects.create_user(email, 'hello123')

		self.assertEqual(user.email, email.lower())

	def test_new_user_invalid_email(self):
		"""Validate email to raise a ValueError"""
		with self.assertRaises(ValueError):
			get_user_model().objects.create_user(None, 'abcd')

	def test_create_new_superuser(self):
		'''Test for creating superuser'''
		user = get_user_model().objects.create_superuser(
				'sankar@abc.com',
				'admin'
			)

		self.assertTrue(user.is_superuser)
		self.assertTrue(user.is_staff)
