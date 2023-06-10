import pytest
from .models import Member, Group

@pytest.mark.django_db
def test_generate_member_code():
    member = Member()
    member_code = member.generate_member_code()
    assert member_code.isalnum()
    assert len(member_code) == 8
    assert not Member.objects.filter(member_code=member_code).exists()

@pytest.mark.django_db
def test_generate_group_code():
    group = Group()
    group_code = group.generate_group_code()
    assert group_code.isalnum()
    assert len(group_code) == 8
    assert not Group.objects.filter(group_code=group_code).exists()
