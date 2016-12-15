from django.forms import ModelForm
from django.shortcuts import render, redirect

from directory.models import Doctor


def doctor_list(request):
    doctors = Doctor.objects.all().order_by('last_name')
    # doctors_str = "; ".join([str(doctor) for doctor in doctors])
    # return HttpResponse(doctors_str)
    return render(request, "directory/doctor_list.html",
                  {"doctors": doctors})


def doctor_details(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    return render(request, "directory/doctor_detail.html",
                  {"doctor": doctor})


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


def doctor_add(request):
    form = DoctorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, "directory/doctor_add.html",
                  {"form": form})
