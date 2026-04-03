from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required

from main.models import WebStyle


def home(request):
    """
    Dapat diakses oleh siapa saja (tanpa login).
    Menampilkan biodata dan menerapkan style dari database.
    """
    style = WebStyle.get_settings()
    is_anggota = request.user.is_authenticated and request.user.email in settings.ALLOWED_EMAILS
    
    context = {
        'style': style,
        'is_anggota': is_anggota
    }
    return render(request, 'home.html', context)

@login_required
def edit_style(request):
    """
    Hanya bisa diakses jika sudah login DAN merupakan anggota kelompok.
    """
    if request.user.email not in settings.ALLOWED_EMAILS:
        return HttpResponseForbidden("Akses Ditolak: Anda bukan anggota kelompok ini.")

    style = WebStyle.get_settings()
    
    if request.method == "POST":
        style.bg_color = request.POST.get('bg_color')
        style.font_family = request.POST.get('font_family')
        style.save()
        return redirect('home')

    return render(request, 'edit_style.html', {'style': style})