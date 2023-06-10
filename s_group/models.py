from django.db import models
from s_members.models import Member
from s_admin.models import CustomUser, RolePermissions


ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"
PENDING = "PENDING"
DELETED = "DELETED"
STATUS = ((ACTIVE, "ACTIVE"), (INACTIVE, "INACTIVE"), (PENDING, "PENDING"), (DELETED, "DELETED"))

# Create your models here.
class GroupSetting(models.Model):
    """ Group Code, Group Name, Group description"""
   
    group_name = models.CharField(("group_name"), max_length=50)
    group_description = models.TextField(("group_description"), max_length=120)
    group_code = models.CharField(("group_code"), max_length=10)
    created_on = models.DateTimeField(("created_on"), auto_now=False, auto_now_add=True)
    updated_on  = models.DateTimeField(("updated_on"), auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(("status"), choices=STATUS, default=ACTIVE)
    
    class Meta:
        verbose_name = ("GroupSetting")
        verbose_name_plural = ("GroupSettings")

    def __str__(self):
        return (str(self.group_name))

    def get_absolute_url(self):
        return reverse("GroupSetting_detail", kwargs={"pk": self.pk})
    
    def generate_group_code(self):
        pass
    
    
class GroupMembers(models.Model):
    group_setting_id = models.ForeignKey(GroupSetting, on_delete=models.CASCADE)
    member_id = models.ManyToManyField(Member, verbose_name=("Member"))

    
    class Meta:
        verbose_name = ("GroupMembers")
        verbose_name_plural = ("GroupMembers")

    def __str__(self):
        return f"{self.group_setting_id}"

    def get_absolute_url(self):
        return reverse("GroupMembers_detail", kwargs={"pk": self.pk})
    

class Membership(models.Model):
    group_members = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)


class GroupMemberRole(models.Model):
    group_id = models.ForeignKey(GroupSetting, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    role_permission_id = models.ForeignKey(RolePermissions, on_delete=models.CASCADE)


    class Meta:
        verbose_name = ("GroupMemberRole")
        verbose_name_plural = ("GroupMemberRoles")

    def __str__(self):
        return f"({self.member_id}, {self.role_permission_id})"

    def get_absolute_url(self):
        return reverse("GroupMemberRole_detail", kwargs={"pk": self.pk})


