from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
import string
import random
from datetime import datetime




from s_admin.models import CustomUser, FeeSettings

ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"
PENDING = "PENDING"
DELETED = "DELETED"
STATUS = ((ACTIVE, "ACTIVE"), (INACTIVE, "INACTIVE"), (PENDING, "PENDING"), (DELETED, "DELETED"))



# Create your models here.

class Member(models.Model):
    
    """Customer Model where customer onboarding fields are available
    Fields = name, date_of_birth, age, gender, occupation, marital_status, father_name, 
    mother_name, religion, community, disability, address(one-to-one), mobile, email,
    aadhaar_number, pan_number, voter_number, ration_card_number, education, aadhaar_file,
    pan_file, voter_file, ration_file, referred_by, joined_on, updated_on
    
    """
    MALE = "M"
    FEMALE = "F"
    OTHERS = "O"
    GENDER_CHOICES = ((MALE, "MALE"), (FEMALE, "FEMALE"), (OTHERS, "OTHERS"))

    MARRIED = "MARRIED"
    SINGLE = "SINGLE"
    DIVORCED = "DIVORCED"
    WIDOWED = "WIDOWED"
    
    MARITAL_CHOICES = (
        (MARRIED, "MARRIED"), 
        (SINGLE, "SINGLE"), 
        (DIVORCED, "DIVORCED"), 
        (WIDOWED, "WINDOWED"), 
        )
    
    SC = "SC"
    ST = "ST"
    MBC = "MBC"
    BC = "BC"
    OC = "OC"
    COMMUNITY_CHOICES = (
        (SC, "SC"), 
        (ST, "ST"), 
        (MBC, "MBC"), 
        (BC, "BC"), 
        (OC, "OC")
        )
    
    PAID = "PAID"
    UNPAID = "UNPAID"
    ONHOLD = "ON-HOLD"

    PAYMENT_STATUS = ((PAID, "PAID"), (UNPAID, "UNPAID"), (ONHOLD, "ON-HOLD"),)
    
    first_name = models.CharField(("first name"), max_length=50)
    last_name = models.CharField(("last_name"), max_length=50)
    member_code = models.CharField("member_code", max_length=10, default="SHMXXXXXX")
    date_of_birth = models.DateField(("date_of_birth"), max_length=8)
    age = models.IntegerField(("age"), max_length=3)
    gender = models.CharField(("gender"), choices=GENDER_CHOICES)
    is_old_member = models.BooleanField(("is_old_member"), default=False)
    shg_name = models.CharField(("shg_name"), max_length=50, null=True, default="NA")
    marital_status = models.CharField(("marital_status"), choices=MARITAL_CHOICES, max_length=15)
    father_name = models.CharField(("father_name"), max_length=50)
    mother_name = models.CharField(("mother_name"), max_length=50)
    religion = models.CharField(("religion"), max_length=20)
    community = models.CharField(("community"), choices=COMMUNITY_CHOICES, max_length=3)
    disability = models.BooleanField(("disabled"), default=False)
    mobile_number = models.CharField(("mobile_number"), max_length=11, unique=True)
    email = models.EmailField(("email"), max_length=50, null=True, unique=True)
    referred_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    registration_fees = models.FloatField("Registration Fees", default=500.00)
    payment_status = models.CharField("Payment Status", choices=PAYMENT_STATUS, default=UNPAID)
    joined_on = models.DateTimeField(("joined_on"), auto_now=False, auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, verbose_name=("created_by"), on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)
    
    # def generate_member_code(self):
    #     # Generate a unique alphanumeric member code
    #     code_length = 10
    #     prefix = 'SHM'
    #     characters = string.ascii_uppercase + string.digits
    #     member_code = prefix + ''.join(random.choice(characters) for _ in range(code_length))
    #     while Member.objects.filter(member_code=member_code).exists():
    #         member_code = ''.join(random.choice(characters) for _ in range(code_length))
    #     # self.member_code = member_code                                                                                                                                                         =
    #     return member_code
    
    
    class Meta:
        verbose_name = ("Member")
        verbose_name_plural = ("Members")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("member_details", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        code_length = 7
        prefix = 'SHM'
        year = self.date_of_birth.year
        current_year = datetime.now().year
        self.age = int(current_year - year)
        characters = string.ascii_uppercase + string.digits
        # while Member.objects.filter(member_code=member_code).exists():
        #     member_code = ''.join(random.choice(characters) for _ in range(code_length))
        self.member_code = prefix + ''.join(random.choice(characters) for _ in range(code_length))
        super(Member, self).save(*args, **kwargs)

# Member Address model
class MemberAddress(models.Model):
    """ Address details of Member"""
    member_id = models.ForeignKey(Member, verbose_name=("member"), on_delete=models.CASCADE)
    address_ln_one = models.CharField(("address_line_one"), max_length=50)
    address_ln_two = models.CharField(("address_line_two"), max_length=50)
    address_ln_three = models.CharField(("address_line_three"), max_length=50, null=True)
    country = models.ForeignKey('cities_light.Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey("cities_light.City", on_delete=models.SET_NULL, null=True, blank=True)
    district = models.CharField(("district"), max_length=50)
    state = models.CharField(("state"), max_length=50, default="Tamil Nadu")
    taluk = models.CharField(("taluk"), null=True, max_length=50)
    local_body = models.CharField(("local_body"), null=True, max_length=50)    
    pincode = models.IntegerField(("pincode"), max_length=6)

    class Meta:
        verbose_name = ("Member Address")
        verbose_name_plural = ("Member Addresss")

    def __str__(self):
        return str(self.member_id)

    def get_absolute_url(self):
        return reverse("MemberAddress_detail", kwargs={"pk": self.pk})

# Education Meta
class Education(models.Model):
    """Education deatails"""
    education_name = models.CharField(("education_name"), max_length=50)
    education_description = models.TextField(("education_desciprtion"))
    created_on = models.DateTimeField(("created_on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated_on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)

    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Educations")

    def __str__(self):
        return self.education_name

    def get_absolute_url(self):
        return reverse("Education_detail", kwargs={"pk": self.pk})


# Member Education
class MemberEducation(models.Model):
    """Education details of menber"""
    member_id = models.ForeignKey(Member, verbose_name=(""), on_delete=models.CASCADE)
    education_id = models.ForeignKey(Education, verbose_name=("education_id"), on_delete=models.CASCADE)
    is_completed = models.BooleanField(("is_completed"), default=True)
    completed_year  = models.IntegerField(("course_completed_year"), max_length=4, null=True)


    class Meta:
        verbose_name = ("Member Education")
        verbose_name_plural = ("Member Educations")

    def __str__(self):
        return str(self.member_id)

    def get_absolute_url(self):
        return reverse("MemberEducation_detail", kwargs={"pk": self.pk})
    
# Occupation
class Occupation(models.Model):
    """Occupation list"""
    occupation_name = models.CharField(("occupation_name"), max_length=50)
    occupation_description = models.TextField(("occupation_description"))
    occupation_type = models.CharField(("occupation_type"), max_length=50)
    created_on = models.DateTimeField(("created_on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated_on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)

    class Meta:
        verbose_name = ("Occupation")
        verbose_name_plural = ("Occupations")

    def __str__(self):
        return self.occupation_name

    def get_absolute_url(self):
        return reverse("Occupation_detail", kwargs={"pk": self.pk})


#Member Occupation data
class MemberOccupation(models.Model):
    """ member occupation"""
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    occupation_id = models.ForeignKey(Occupation, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("Member Occupation")
        verbose_name_plural = ("Member Occupations")

    def __str__(self):
        return str(self.member_id)

    def get_absolute_url(self):
        return reverse("MemberOccupation_detail", kwargs={"pk": self.pk})



# Member Registration model
class MemberRegistration(models.Model):
    """Member registration table"""
    #PAYMENT STATUS
    PAID = "PAID"
    UNPAID = "UNPAID"
    ONHOLD = "ON-HOLD"

    PAYMENT_STATUS = ((PAID, "PAID"), (UNPAID, "UNPAID"), (ONHOLD, "ON-HOLD"),)
    
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    
    PAYMENT_MODE = ((ONLINE, "ONLINE"), (OFFLINE, "OFFLINE"))
    
    member_id = models.ForeignKey(Member, verbose_name=("member"), on_delete=models.CASCADE)
    registration_fee_id = models.ForeignKey(FeeSettings, verbose_name=("Fee Name"), on_delete=models.CASCADE)
    transaction_number = models.CharField(("txn_number"), max_length=50)
    payment_mode = models.CharField(("payment_mode"), choices=PAYMENT_MODE, default=ONLINE)
    payment_through = models.CharField(("payment_through"), max_length=50)
    payment_status = models.CharField("Payment Status", choices=PAYMENT_STATUS, default=UNPAID)
    

    class Meta:
        verbose_name = ("Member Registration Status")
        verbose_name_plural = ("Member Registrations status")

    def __str__(self):
        return f"{self.member_id} - Payment Status: {self.payment_status}"

    def get_absolute_url(self):
        return reverse("MemberRegistration_detail", kwargs={"pk": self.pk})
