from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Certification

@login_required
def certification_list(request):
    certifications = Certification.objects.filter(user=request.user)
    return render(request, 'certifications/certification_list.html', {'certifications': certifications})

@login_required
def certification_detail(request, id):
    certification = get_object_or_404(Certification, id=id, user=request.user)
    return render(request, 'certifications/certification_detail.html', {'certification': certification})
