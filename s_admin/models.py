import random

from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from s_admin.managers import CustomUserManager


ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"
PENDING = "PENDING"
DELETED = "DELETED"
STATUS = ((ACTIVE, "ACTIVE"), (INACTIVE, "INACTIVE"), (PENDING, "PENDING"), (DELETED, "DELETED"))



# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Create custom user fields with this class """
    email = models.EmailField(_("email address"), unique=True, max_length=150)
    is_staff = models.BooleanField(_("is staff"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return self.email


class UserProfile(models.Model):
    """One-to-One mapping with Custom User model """
    # Gender Choices for Gender Field
    MALE = "M"
    FEMALE = "F"
    OTHERS = "O"
    GENDER_CHOICES = ((MALE, "MALE"), (FEMALE, "FEMALE"), (OTHERS, "OTHERS"))
        
    # Initial choices for Initials field
    MR = "MR"
    MRS = "MRS"
    MISS = "MISS"
    INITIAL_CHOICES = ((MR, "MR"), (MRS, "MRS"), (MISS, "MISS"), )
    
    user = models.OneToOneField("CustomUser", related_name='user_profile', verbose_name=_("user"), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    intials = models.CharField(_("initials"), choices=INITIAL_CHOICES, default=MRS, null=True)
    gender = models.CharField(_("gender"), choices=GENDER_CHOICES, default=FEMALE, null=True)
    dob = models.DateField(_("date of birth"), max_length=8, blank=True, null=True)
    profile_pic = models.ImageField(_("Profile picture"), upload_to="media/user_files/", null=True)
    employee_id = models.CharField(_("employee id"), max_length=10, editable=False, unique=True)
    created_at = models.DateTimeField(_("created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated"), auto_now=True)
    # created_by = models.ForeignKey('self', on_delete=models.CASCADE)
    status = models.CharField(_("status"), choices=STATUS, default=ACTIVE)
    
    REQUIRED_FIELDS = ["employee_id", "first_name"]
    
    class Meta:
        verbose_name = _("UserProfile")
        verbose_name_plural = _("UserProfiles")

    def __str__(self):
        return f"{self.intials}. {self.first_name} {self.last_name} (Emp ID: {self.employee_id})"

    def get_absolute_url(self):
        return reverse("user_profile", kwargs={"pk": self.pk})
    
    def generate_employee_id():
        """Generates unique 8 digit employee id """
        while True:
            employee_id = 'SH'.join(random.choices('0123456789', k=8))
            if not UserProfile.objects.filter(employee_id=employee_id).exists():
                return employee_id
            
    def save(self, *args, **kwargs):
        if not self.id:
            self.employee_id = 'SHU' + ''.join(random.choices('0123456789', k=7))
        super().save(*args, **kwargs)
         
    @receiver(post_save, sender=CustomUser)
    def create_and_update_profile(sender, instance, created, **kwargs):
        if created:
            
            UserProfile.objects.create(user=instance)
            # instance.user_profile.employee_id = generate_employee_id()
        
        instance.user_profile.save()
            
    
# Organization model 
class OrganizationSetting(models.Model):
    """Organization details"""
    organization_name  = models.CharField(_("organization_name"), max_length=50)
    org_code = models.CharField(_("org_code"), max_length=10)
    created_on = models.DateTimeField(_("created_on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(_("updated_on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(_("status"), choices=STATUS, default=ACTIVE)
    
    class Meta:
        verbose_name = _("OrganizationSetting")
        verbose_name_plural = _("OrganizationSettings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("OrganizationSetting_detail", kwargs={"pk": self.pk})
    

# Zone model
class Zone(models.Model):
    """Zonal areas"""
    zone_name = models.CharField(("zone name"), max_length=50)
    zone_code = models.CharField(("zone code"), max_length=6)
    zone_description = models.TextField(("zone description"), max_length=80)
    created_on = models.DateTimeField(("created on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)
    

    class Meta:
        verbose_name = ("Zone")
        verbose_name_plural = ("Zones")

    def __str__(self):
        return self.zone_name

    def get_absolute_url(self):
        return reverse("Zone_detail", kwargs={"pk": self.pk})
    

# Area model
class Area(models.Model):
    """List of areas in Zone"""
    area_name = models.CharField(("area name"), max_length=50)
    area_code = models.CharField(("area code"), max_length=50)
    pincode = models.IntegerField(("pincode"), max_length=6)
    area_description = models.TextField(("area description"))
    created_on = models.DateTimeField(("created on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)
    

    class Meta:
        verbose_name = ("Area")
        verbose_name_plural = ("Areas")

    def __str__(self):
        return self.area_name

    def get_absolute_url(self):
        return reverse("Area_detail", kwargs={"pk": self.pk})


# Street Model
class Streets(models.Model):
    """Street details"""
    street_name = models.CharField(("stree name"), max_length=50)
    street_description = models.CharField( ("street description"), max_length=100)
    created_on = models.DateTimeField( ("created_on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)
    
    class Meta:
        verbose_name = ("Streets")
        verbose_name_plural = ("Streets")

    def __str__(self):
        return self.street_name

    def get_absolute_url(self):
        return reverse("Streets_detail", kwargs={"pk": self.pk})

        
#Zone and areas group
class ZoneGroup(models.Model):
    """Grouping areas into zones"""
    zone_id = models.ForeignKey(Zone, verbose_name=("zone"), on_delete=models.CASCADE)
    area_id = models.ForeignKey(Area, verbose_name=("area"), on_delete=models.CASCADE)
    group_description = models.TextField(("zone group description"))
    created_on = models.DateTimeField(("created on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)
    
    class Meta:
        verbose_name = ("ZoneGroup")
        verbose_name_plural = ("ZoneGroups")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ZoneGroup_detail", kwargs={"pk": self.pk})


    
# Fee / Charges Model
class FeeSettings(models.Model):
    """Fee settings model"""
    
    
    
    ONE_TIME = "ONETIME"
    DAY = "DAYS"
    WEEK = "WEEKS"
    MONTH = "MONTHS"
    YEAR = "YEARS"
    
    FREQUENCY_CHOICE = ((ONE_TIME, "ONETIME"), (DAY, "DAYS"), (MONTH, "MONTHS"), (YEAR, "YEARS"))
    
    FLAT = "FLAT"
    PERCENTAGE = "PERCENTAGE"
    
    FEE_CHOICE = ((FLAT, "FLAT"), (PERCENTAGE, "PERCENTAGE"))
    
    fee_name = models.CharField(("fee name"), max_length=50)
    fee_description = models.TextField(("fee description"))
    fee_type = models.CharField(("Fee Mode"))
    fee_value = models.IntegerField(("fee value"), max_length=5)
    fee_unit = models.CharField(("fee unit"), choices=FEE_CHOICE)
    fee_frequency_value = models.IntegerField(("fee frequency value"), max_length=3)
    fee_frequency_unit = models.CharField(("fee frequency unit"), choices=FREQUENCY_CHOICE)
    created_on = models.DateTimeField(("created on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)

    
    class Meta:
        verbose_name = ("FeeSettings")
        verbose_name_plural = ("FeeSettingss")

    def __str__(self):
        return str(self.fee_value)

    def get_absolute_url(self):
        return reverse("FeeSettings_detail", kwargs={"pk": self.pk})

    
class RoleSettings(models.Model):
    role_name = models.CharField("role name", max_length=50)
    role_description = models.TextField("role description", max_length=150)
    created_on = models.DateTimeField(("created on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)


    class Meta:
        verbose_name = ("RoleSetting")
        verbose_name_plural = ("RoleSettings")

    def __str__(self):
        return self.role_name

    def get_absolute_url(self):
        return reverse("RoleSetting_detail", kwargs={"pk": self.pk})


class PermissionSettings(models.Model):
    permission_name = models.CharField("Permission Name", max_length=50)
    permission_description = models.TextField("Permission Description", max_length=150)
    created_on = models.DateTimeField(("created on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)

    class Meta:
        verbose_name = ("PermissionSettings")
        verbose_name_plural = ("PermissionSettings")

    def __str__(self):
        return self.permission_name

    def get_absolute_url(self):
        return reverse("PermissionSettings_detail", kwargs={"pk": self.pk})
    
    
class RolePermissions(models.Model):
    role_id = models.ForeignKey(RoleSettings, on_delete=models.CASCADE)
    permission_id = models.ManyToManyField(PermissionSettings, verbose_name="Permission id")

    class Meta:
        verbose_name = ("RolePermissions")
        verbose_name_plural = ("RolePermissions")

    def __str__(self):
        return f"{self.role_id}"

    def get_absolute_url(self):
        return reverse("RolePermissions_detail", kwargs={"pk": self.pk})
