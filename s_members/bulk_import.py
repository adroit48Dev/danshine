import csv
from .models import Member, MemberAddress, Education, Occupation

def bulk_import(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            member_data = {
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                # Add more fields for the Member model
            }
            member = Member.objects.create(**member_data)

            address_data = {
                'member_id': member.id,
                'address_ln_one': row['address_ln_one'],
                'address_ln_two': row['address_ln_two'],
                # Add more fields for the MemberAddress model
            }
            MemberAddress.objects.create(**address_data)

            education_data = {
                'member_id': member.id,
                'education_name': row['education_name'],
                'education_description': row['education_description'],
                # Add more fields for the Education model
            }
            Education.objects.create(**education_data)

            occupation_data = {
                'member_id': member.id,
                'occupation_name': row['occupation_name'],
                'occupation_description': row['occupation_description'],
                # Add more fields for the Occupation model
            }
            Occupation.objects.create(**occupation_data)
