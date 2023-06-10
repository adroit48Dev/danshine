import csv
from .models import Member, MemberAddress, Education, Occupation

def bulk_export(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'first_name', 'last_name', 'address_ln_one', 'address_ln_two',
            'education_name', 'education_description', 'occupation_name', 'occupation_description'
            # Add more headers for additional fields
        ])

        members = Member.objects.all().prefetch_related('address', 'educations', 'occupations')
        for member in members:
            address = member.address
            educations = member.educations.all()
            occupations = member.occupations.all()

            for education in educations:
                for occupation in occupations:
                    writer.writerow([
                        member.first_name, member.last_name,
                        address.address_ln_one, address.address_ln_two,
                        education.education_name, education.education_description,
                        occupation.occupation_name, occupation.occupation_description
                        # Add more fields for additional models
                    ])
