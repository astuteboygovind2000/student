"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app2.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_reg/', admin_reg),
    path('accountant_reg/', accountant_reg),
    path('student_reg/', student_reg),
    path('course_reg/', course_reg),
    path('allcourses/', allcourses),
    path('', login),
    path('logout/', logout),
    path('autherror/', autherror),
    path('admin_home/', admin_home),
    path('accountant_home/', accountant_home),
    path('editacntprofile/', editacntprofile),
    path('editacntprofile1/', editacntprofile1),
    path('accountant_pass_change/', accountant_pass_change),
    path('accountant_pass_change1/', accountant_pass_change1),
    path('student_home/', student_home),
    path('alladmins/', alladmins),
    path('allaccountants/', allaccountants),
    path('edit_ac_data/', edit_ac_data),
    path('edit_ac_data1/', edit_ac_data1),
    path('delete_ac_data/', delete_ac_data),
    path('delete_ac_data1/', delete_ac_data1),
    path('edit_course/', edit_course),
    path('edit_course1/', edit_course1),
    path('delete_course/', delete_course),
    path('delete_course1/', delete_course1),
    path('editstprofile/', editstprofile),
    path('editstprofile1/', editstprofile1),
    path('student_pass_change/', student_pass_change),
    path('student_pass_change1/', student_pass_change1),
    path('uploadphoto/', uploadphoto),
    path('chngephoto/', chngephoto),
    path('chngephoto1/', chngephoto1),
    path('deletephoto/', deletephoto),
    path('deletephoto1/', deletephoto1),
    path('editadminprofile/', editadminprofile),
    path('editadminprofile1/', editadminprofile1),
    path('admin_pass_change/', admin_pass_change),
    path('admin_pass_change1/', admin_pass_change1),
    path('allstudentsAD/', allstudentsAD),
    path('ADviewstudent/', ADviewstudent),
    path('deletestudentprofile/', deletestudentprofile),
    path('deletestudentprofile1/', deletestudentprofile1),
    path('studentcourseadd/', studentcourseadd),
    path('studentcourseadd1/', studentcourseadd1),
    path('studentinstallmentadd/', studentinstallmentadd),
    path('studentinstallmentadd1/', studentinstallmentadd1),
    path('allstudentsACC/', allstudentsACC),
    path('viewstudentACC/', viewstudentACC),
    path('studentcourseadd_acc/', studentcourseadd_acc),
    path('studentcourseadd_acc1/', studentcourseadd_acc1),
    path('studentinstallmentadd_acc/', studentinstallmentadd_acc),
    path('studentinstallmentadd_acc1/', studentinstallmentadd_acc1),
    path('studentuploadphoto/', studentuploadphoto),
    path('studentchngephoto/', studentchngephoto),
    path('studentchngephoto1/', studentchngephoto1),
    path('studentdeletephoto/', studentdeletephoto),
    path('studentdeletephoto1/', studentdeletephoto1),
    path('editstudentcoursedata/', editstudentcoursedata),
    path('editstudentcoursedata1/', editstudentcoursedata1),
    path('deletestudentcoursedata/', deletestudentcoursedata),
    path('deletestudentcoursedata1/', deletestudentcoursedata1),
    path('editstdata/', editstdata),
    path('editstdata1/', editstdata1),
    path('student_course_info/', student_course_info),
    path('editstudentinstdata/', editstudentinstdata),
    path('editstudentinstdata1/', editstudentinstdata1),
    path('deletestudentinstdata/', deletestudentinstdata),
    path('deletestudentinstdata1/', deletestudentinstdata1),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)