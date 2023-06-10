from django.contrib.auth import get_user_model
from django.test import TestCase

class UserManagerTests(TestCase):
    """
    Test creating custom users using email and metadata
    """
    def test_create_user(self):
        User = get_user_model
        user = User.objects.create_user(email="admin@shine.com", password="shine123")
        self.assertEqual(user.email, "admin@shine.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertFalse(user.is_superuser)
        
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="shine123")
            
    
    def test_create_superuser(TestCase):
        """Test case to create super user """
        User = get_user_model()
        admin_user = User.objects.create_user(email="admin@shine.com", password="shine123")
        self.assertEqual(admin_user.email, "admin@shine.com")
        self.assertEqual(admin_user.password, "shine123")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
        try:
            self.assertIsNone(admin_user.username)        
        except AttributeError:
            pass
        
        with self.assertRaises(ValueError):
            User.objects.create_super_user(email="admin@shine.com", password="shine123")
                       
            