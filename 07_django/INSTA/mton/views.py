from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Student, Lecture, Enrollment


@require_http_methods(['GET'])
def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'mton/enrollment_list.html', {
        'enrollments': enrollments,
    })


@require_http_methods(['GET'])
def search_lecture(request):
    enrollments = Enrollment.objects.all()
    lectures_id = []
    for enrollment in enrollments:
        if 'student_id' == enrollment.student_id:
            lectures_id.append(enrollment.lecture_id)
    if lectures_id:
        return redirect('mton:lecture_list', lectures_id=lectures_id)


@require_http_methods(['GET'])
def lecture_list(request, lectures_id):
    return render(request, '')