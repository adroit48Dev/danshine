from django import forms
from formtools.wizard import FormWizard
from .models import Member, MemberAddress, MemberEducation, MemberOccupation, MemberRegistration

# Form for Member model
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ['member_code']
        
# Form for Member Address model
class MemberAddressForm(forms.ModelForm):
    class Meta:
        model = MemberEducation
        fields = '__all__'
        
# Form for Member Education Model
class MemberEducationForm(forms.ModelForm):
    class Meta:
        model = MemberAddress
        fields = '__all__'
        
# Form for Member Occupation Model
class MemberOccupationForm(forms.ModelForm):
    class Meta:
        model = MemberOccupation
        fields = '__all__'   

# Form for the Member Registration Model        
class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = MemberRegistration
        fields = '__all__'
        
class StepperFormWizard(FormWizard):
    def done(self, form_list, **kwargs):
        # Process for stepper form
        member_form, member_address_form, member_education_form, member_occupation_form = form_list
        member = member_form.save()
        member_address = member_address_form.save(commit=False)
        member_address.member_id = member
        member_address.save()
        member_education = member_education_form.save(commit=False)
        member_education.member_id = member
        member_education.save()
        member_occupation = member_occupation_form.save(commit=False)
        member_occupation.member_id = member
        member_occupation.save()
        member_registration = member_registration_form.save(commit=False)
        member_registration.member_id = member
        member_registration.save()
        
        