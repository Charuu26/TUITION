from django.shortcuts import render,get_object_or_404
from django.contrib import messages
# Create your views here.
from tuition.models import *
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .models import Student 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from .models import Standard 

# Create your views here.
#View Pages
def home(request):
    return render(request,"home.html")

def index(request):
    return render(request,"index.html")

def index1(request):
    return render(request,"index1.html")

def About(request):
    return render(request,"About.html")

def Contact(request):
    return render(request,"Contact.html")

def service(request):
    return render(request,"service.html")

def addstudent(request):
    return render(request,"addstudent.html")

def faculty(request):
    return render(request,"faculty.html")

def dashboard(request):
    return render(request,"dashboard.html")



def dashboard(request):
    student_count = Student.objects.count()
    faculty_count = Faculty.objects.count()
    standard_count = Standard.objects.count()
    subject_conut=Subject.objects.count()
    stastudent_count=Stastudent.objects.count()
    stasubject_count=Stasubject.objects.count()
    context = {
        'student_count':student_count,
        'faculty_count':faculty_count,
        'standard_count':standard_count,
        'subject_conut':subject_conut,
        'stastudent_count':stastudent_count,
        'stasubject_count':stasubject_count
    }
    return render(request,"dashboard.html",context)


#Show Table Detials.
def st(request):
    stundents =Student.objects.all()
    context ={
        'student' : stundents
    }
    return render(request,"student.html",context)

def standard(request):
    standards =Standard.objects.all()
    context = {
        'standards':standards
    }
    print(standards)
    return render(request,"standard.html",context)

def Facu(request):
    facultys = Faculty.objects.all()
    context = {
        'facultys' : facultys
    }
    return render(request,"faculty.html",context)

def subj(request):
    subjects = Subject.objects.all()
    context = {
        'subjects' : subjects
        }
    return render(request,"subject.html",context)

def timetab(request):
    timetable = Timetable.objects.all()
    context = {
        'timetable' : timetable
        }
    return render(request,"timetable.html",context)

def studatt(request):
    studentattendence = AttedenceStudent.objects.all()
    context = {
        'studentattendence' : studentattendence
        }
    return render(request,"atten_student.html",context)

def attenfac(request):
    facultyattendence = AttedenceFaculty.objects.all()
    context = {
        'facultyatten' : facultyattendence
        }
    return render(request,"atten_faculty.html",context)
    
#Adding data
def addstandard(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)

        s = Standard()
        s.sta_name = request.POST.get('staname')
        s.sta_code = request.POST.get('stacode')
        s.image1 = request.FILES.get('standard_img')

        print("Standard Name:", s.sta_name)
        print("Standard Code:", s.sta_code)
        print("Image:", s.image1)

        if s.image1:  # Check if an image was uploaded
            s.save()
            return redirect('/standard')
        else:
            print("No image uploaded")
            # Optionally, handle the case where no image was uploaded
    else:
        return render(request, 'addstandard.html')

    
def addsubject(request):
    if request.method=='POST':
        s=Subject()
        s.sub_name=request.POST.get('subname')
        s.sub_code=request.POST.get('subcode')
        s.save()
        return redirect('/subject')
    else:
        return render(request,'addsubject.html')
    
def addstudent(request):
    if request.method=='POST':
        s=Student()
        s.s_name=request.POST.get('sname')
        s.address=request.POST.get('address')
        s.email=request.POST.get('email')
        s.password=request.POST.get('password')
        s.con_no=request.POST.get('conno')
        s.username=request.POST.get('username')
        s.save()
        print()
        return redirect('/student')
    else:
        return render(request,'addstudent.html')
    
def addfaculty(request):
    if request.method=='POST':
        s=Faculty()
        s.f_name=request.POST.get('f_name')
        s.address=request.POST.get('address')
        s.email=request.POST.get('email')
        s.password=request.POST.get('password')
        s.con_no=request.POST.get('conno')
        s.joining_date=request.POST.get('joining_date')
        s.save()
        return redirect('/faculty')
    else:
        return render(request,'addfaculty.html')
    
def addattfac(request):
    f=Faculty.objects.all()
    fac={'fac':f}
    if request.method=='POST':
        
        s=AttedenceFaculty()
        
        s.f_id=request.POST.get('fid')
        s.att_date=request.POST.get('date')
        s.status=request.POST.get('status')
        s.save()
        return redirect('/atten_faculty')
    else:
        return render(request,'addattfac.html',fac)
    
def addattstu(request):
    t=Timetable.objects.all()
    tim={'tim':t}
    if request.method=='POST':

        s=AttedenceStudent()

        s.tt_id=request.POST.get('ttid')
        s.att_date=request.POST.get('date')
        s.status=request.POST.get('status')
        s.save()
        return redirect('/atten_student')
    else:
        return render(request,'addattstu.html',tim)

def addtimetable(request):
    sta=Standard.objects.all()
    
    f=Faculty.objects.all()
    
    su=Subject.objects.all()
    std={'std':sta,
         'sub':su,'fac':f}

    if request.method=='POST':
        s=Timetable()
        s.sta_id=request.POST.get('staid')
        s.f_id=request.POST.get('fid')
        s.sub_id=request.POST.get('subid')
        s.day_of_week=request.POST.get('dofw')
        s.start_time=request.POST.get('st')
        s.end_time=request.POST.get('et')
        s.save()
        return redirect('/timetable')
    else:
        return render(request,'addtimetable.html',std)

    
#Deleting Table Data..

def sta_delete(request,delete_id):
    s=Standard.objects.get(sta_id=delete_id)
    s.delete()
    return redirect('/standard')

def sub_delete(request,delete_id):
    s=Subject.objects.get(sub_id=delete_id)
    s.delete()
    return redirect('/subject')

def s_delete(request,delete_id):
    s=Student.objects.get(s_id=delete_id)
    s.delete()
    return redirect('/student')

def fac_delete(request,delete_id):
    s=Faculty.objects.get(f_id=delete_id)
    s.delete()
    return redirect('/faculty')

def timetable_delete(request,delete_id):
    s=Timetable.objects.get(tt_id=delete_id)
    s.delete()
    return redirect('/timetable')

def attenfac_delete(request,delete_id):
    s=AttedenceFaculty.objects.get(fac_att_id=delete_id)
    s.delete()
    return redirect('/atten_faculty')

def attestu_delete(request,delete_id):
    s=AttedenceStudent.objects.get(stu_att_id=delete_id)
    s.delete()
    return redirect('/atten_student')

#Update Table Data.
def editstandard(request, edit_id):
    standard = get_object_or_404(Standard, sta_id=edit_id)
    
    if request.method == 'POST':
        standard.sta_name = request.POST.get('staname')
        standard.sta_code = request.POST.get('stacode')

        # Handle the image upload
        if request.FILES.get('editImage1'):
            standard.image1 = request.FILES['editImage1']
        if request.FILES.get('editImage1'):
            standard.image1 = request.FILES['editImage1']
            print("New image uploaded:", standard.image1)
        else:
            print("No new image uploaded.")
        standard.save()
        messages.success(request, "Data Updated Successfully.")
        return redirect('/standard')
    
    context = {'stad': standard}
    return render(request, 'standard.html', context)

def editsubject(request,edit_id):
    subject = get_object_or_404(Subject, sub_id=edit_id)
    
    if request.method == 'POST':
        subject.sub_name = request.POST.get('subname')
        subject.sub_code = request.POST.get('subcode')
        subject.save()
        messages.success(request, "Data Updated Successfully.")
        return redirect('/subject')
    
    context = {'sub': subject}
    return render(request, 'subject.html', context)

def editStudent(request, id):
    student = get_object_or_404(Student, s_id=id)

    if request.method == 'POST':
        student.s_name = request.POST.get('sname')
        student.address = request.POST.get('address')
        student.email = request.POST.get('email')
        student.password = request.POST.get('password')
        student.con_no = request.POST.get('conno')
        student.username = request.POST.get('username')
        student.save()
        messages.success(request, "Data Updated Successfully.")
        return redirect('/student')

    context = {'stu': student}
    return render(request, 'student.html', context)

def editfaculty(request, edit_id):
    faculty = get_object_or_404(Faculty, f_id=edit_id)

    if request.method == 'POST':
        faculty.f_id = request.POST.get('f_id')
        faculty.f_name = request.POST.get('faculty_name')
        faculty.address = request.POST.get('address')
        faculty.email = request.POST.get('email')
        faculty.password = request.POST.get('password')
        faculty.con_no = request.POST.get('contact_number')
        faculty.joining_date=request.POST.get('joining_date')
        faculty.save()
        messages.success(request, "Data Updated Successfully.")
        return redirect('/faculty')
    
    context = {'fac': faculty}
    return render(request, 'faculty.html', context)

def edittimetable(request, id):
    timetable = get_object_or_404(Timetable, tt_id=id)
    if request.method == 'POST':
        # timetable.sta = request.POST.get('standard_id')
        # timetable.f = request.POST.get('faculty_id')
        # timetable.sub = request.POST.get('subject_id')
        timetable.day_of_week = request.POST.get('day_of_week')
        timetable.start_time = request.POST.get('start_time')
        timetable.end_time = request.POST.get('end_time')
        timetable.save()
        messages.success(request, "Data Updated Successfully.")
        return redirect('/timetable')
    context = {'tim': timetable}
    return render(request, 'timetable.html', context)


def editattefac(request, id):
    atttefac = get_object_or_404(AttedenceFaculty, fac_att_id=id)
    if request.method == 'POST':
        atttefac.f_id = request.POST.get('f_id')
        atttefac.att_date = request.POST.get('att_date')
        atttefac.status = request.POST.get('status')
        atttefac.save()
        messages.success(request, "Data Updated Successfully.")
        return redirect('/atten_faculty')
    context = {'atte': atttefac}
    return render(request, 'atten_faculty.html', context)

def editattestu(request, id):
    atttestu = get_object_or_404(AttedenceStudent, stu_att_id=id)
    if request.method == 'POST':
        atttestu.att_date = request.POST.get('att_date')
        atttestu.status = request.POST.get('status')
        atttestu.save()
        messages.success(request, "Data Updated Successfully.")
        return redirect('/atten_student')
    context = {'atte': atttestu}
    return render(request, 'atten_student.html', context)        

# def Home(request):
#     return render(request,"Home.html")
def register(request):
    if request.method=='POST':
        s=Student()
        s.s_name=request.POST.get('sname')
        s.address=request.POST.get('address')
        s.email=request.POST.get('email')
        s.password=request.POST.get('password')
        s.con_no=request.POST.get('conno')
        s.username=request.POST.get('username')
        s.save()
        print()
        return redirect('/login')
    return render(request, 'addstudent.html')

def welcome(request):
    if not request.user.is_authenticated:
        return redirect('register')
    return render(request, 'template/welcome.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            admin_data = admin.objects.get(username=username, password=password)
            request.session['admin_id'] = admin_data.admin_id
            return redirect('dashboard')  # Redirect to a home page or dashboard
        except admin.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'admin_login.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            student = Student.objects.get(username=username, password=password)
            request.session['s_id'] = student.s_id
            return redirect('Home')  # Redirect to a home page or dashboard
        except Student.DoesNotExist:
            messages.error(request, 'Invalid username or password')    
    return render(request, 'login.html')

def logout_view(request):
    if 's_id' in request.session:
        del request.session['s_id']
    return redirect('login')  # Redirect to the login page

def Home_view(request):
    if 's_id' not in request.session:
        return redirect('login')
    
    student_id = request.session['s_id']
    try:
        student = Student.objects.get(s_id=student_id)
    except Student.DoesNotExist:
        return redirect('logout')  # Handle case where user is no longer valid
    
    # Fetch all standards
    standards = Standard.objects.all()
    print(standards)  # Print to the console to check if standards are fetched
    
    context = {
        'student': student,
        'standards': standards
    }
    
    return render(request, 'Home.html', context)

#Standard Link Pages
def six_view(request):
    stasubjects = Stasubject.objects.filter(sta__sta_id=1).select_related('sta', 'sub')
    print(stasubjects)
    context = {
        'stasubjects': stasubjects
    }
    return render(request, 'six.html', context)

def seven_view(request):
    # Filter Stasubjects where the related standard is Standard with sta_id 7
    stasubjects = Stasubject.objects.filter(sta__sta_id=2).select_related('sta', 'sub')
    
    context = {
        'stasubjects': stasubjects
    }
    return render(request, 'seven.html', context)

def eight_view(request):
    # Filter Stasubjects where the related standard is Standard with sta_id 7
    stasubjects = Stasubject.objects.filter(sta__sta_id=3).select_related('sta', 'sub')
    
    context = {
        'stasubjects': stasubjects
    }
    return render(request, 'eight.html', context)

def nine_view(request):
    # Filter Stasubjects where the related standard is Standard with sta_id 7
    stasubjects = Stasubject.objects.filter(sta__sta_id=4).select_related('sta', 'sub')
    
    context = {
        'stasubjects': stasubjects
    }
    return render(request, 'nine.html', context)

def ten_view(request):
    # Filter Stasubjects where the related standard is Standard with sta_id 7
    stasubjects = Stasubject.objects.filter(sta__sta_id=5).select_related('sta', 'sub')
    
    context = {
        'stasubjects': stasubjects
    }
    return render(request, 'ten.html', context)   
