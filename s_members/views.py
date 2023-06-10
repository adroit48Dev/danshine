# # views.py
# import csv
# import openpyxl

# from django.shortcuts import render
# from django.contrib import messages
# from .models import Member

# def upload_data(request):
#     if request.method == 'POST':
#         file = request.FILES['file']
#         if file.name.endswith('.csv'):
#             reader = csv.reader(file)
#             next(reader)  # Skip the header row if needed
#             for row in reader:
#                 # Assuming your CSV file has columns in the following order:
#                 # first_name, last_name, member_code, date_of_birth, age, gender, is_old_member,
#                 # shg_name, marital_status, father_name, mother_name, religion, community,
#                 # disability, mobile_number, email, referred_by_id, created_by_id, status
#                 obj = Member(
#                     first_name=row[0],
#                     last_name=row[1],
#                     member_code=row[2],
#                     date_of_birth=row[3],
#                     age=row[4],
#                     gender=row[5],
#                     is_old_member=row[6],
#                     shg_name=row[7],
#                     marital_status=row[8],
#                     father_name=row[9],
#                     mother_name=row[10],
#                     religion=row[11],
#                     community=row[12],
#                     disability=row[13],
#                     mobile_number=row[14],
#                     email=row[15],
#                     referred_by_id=row[16],
#                     created_by_id=row[17],
#                     status=row[18]
#                 )
#                 obj.save()
#         elif file.name.endswith('.xlsx'):
#             workbook = openpyxl.load_workbook(file)
#             sheet = workbook.active
#             for row in sheet.iter_rows(min_row=2):
#                 # Assuming your Excel file has columns in the following order:
#                 # first_name, last_name, member_code, date_of_birth, age, gender, is_old_member,
#                 # shg_name, marital_status, father_name, mother_name, religion, community,
#                 # disability, mobile_number, email, referred_by_id, created_by_id, status
#                 obj = Member(
#                     first_name=row[0].value,
#                     last_name=row[1].value,
#                     member_code=row[2].value,
#                     date_of_birth=row[3].value,
#                     age=row[4].value,
#                     gender=row[5].value,
#                     is_old_member=row[6].value,
#                     shg_name=row[7].value,
#                     marital_status=row[8].value,
#                     father_name=row[9].value,
#                     mother_name=row[10].value,
#                     religion=row[11].value,
#                     community=row[12].value,
#                     disability=row[13].value,
#                     mobile_number=row[14].value,
#                     email=row[15].value,
#                     referred_by_id=row[16].value,
#                     created_by_id=row[17].value,
#                     status=row[18].value
#                 )
#                 obj.save()
#         else:
#             messages.error(request, 'Invalid file format. Please upload a CSV or Excel file.')
#             return render(request, 'Success')

#         messages.success(request, 'Data uploaded successfully.')
#         return render(request, 'Success')

#     return


# from django.shortcuts import render, redirect
# from s_members.models import Member
# from .forms import MemberForm, GroupForm

# def member_list(request):
#     members = Member.objects.all()
#     return render(request, 'member_list.html', {'members': members})

# def member_create(request):
#     if request.method == 'POST':
#         form = MemberForm(request.POST)
#         if form.is_valid():
#             member = form.save(commit=False)
#             member.member_code = member.generate_member_code()  # Generate member code
#             member.save()
#             return redirect('member_list')
#     else:
#         form = MemberForm()
#     return render(request, 'member_create.html', {'form': form})

# def member_update(request, pk):
#     member = Member.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = MemberForm(request.POST, instance=member)
#         if form.is_valid():
#             member = form.save()
#             return redirect('member_list')
#     else:
#         form = MemberForm(instance=member)
#     return render(request, 'member_update.html', {'form': form, 'member': member})

# def member_delete(request, pk):
#     member = Member.objects.get(pk=pk)
#     member.delete()
#     return redirect('member_list')

# def group_list(request):
#     groups = Group.objects.all()
#     return render(request, 'group_list.html', {'groups': groups})

# def group_create(request):
#     if request.method == 'POST':
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             group = form.save(commit=False)
#             group.group_code = group.generate_group_code()  # Generate group code
#             group.save()
#             return redirect('group_list')
#     else:
#         form = GroupForm()
#     return render(request, 'group_create.html', {'form': form})

# Additional views for group update and delete similar to member_update and member_delete


from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .templates import *

from .bulk_import import bulk_import
from .bulk_export import bulk_export
from .forms import (StepperFormWizard, 
                    MemberForm, 
                    MemberAddressForm, 
                    MemberEducationForm, 
                    MemberOccupationForm, 
                    MemberRegistrationForm)

def stepper_form_view(request):
    form = StepperFormWizard([MemberForm, MemberAddressForm, MemberEducationForm, MemberOccupationForm, MemberRegistrationForm])
    if request.method == "POST":
        form = StepperFormWizard(request.POST, [MemberForm, MemberAddressForm, MemberEducationForm, MemberOccupationForm, MemberRegistrationForm])
        if form.is_valid():
            form.save()
    return render(request, 'stepper_form.html', {'form':form})



        



def member_list(request):
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'member_list.html', context)

def member_details(request, pk):
    member = get_object_or_404(Member, pk=pk)
    context = {
        'member': member
    }
    return render(request, 'member_details.html', context)

def member_create(request):
    if request.method == 'POST':
        form = member_create(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('member_details', pk=member.pk)
    else:
        form = MemberForm()
    
    context = {
        'form': form
    }
    return render(request, 'member_create.html', context)

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_details', pk=pk)
    else:
        form = MemberForm(instance=member)
    
    context = {
        'form': form,
        'member': member
    }
    return render(request, 'member_update.html', context)

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    
    context = {
        'member': member
    }
    return render(request, 'member_delete.html', context)



def import_data(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            # Assuming the file is uploaded via a form with input name 'file'
            filename = file.temporary_file_path()
            bulk_import(filename)
            # Redirect or display success message
            return 
        else:
            # Handle file not found error
            return 
            
    else:
        # Render the import form
        return 
        
def export_data(request):
    filename = 'data_export.csv'
    bulk_export(filename)
    # Download the file or provide a link to download
