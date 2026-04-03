from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required

from main.models import WebStyle


from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from main.models import WebStyle

def home(request):
    style = WebStyle.get_settings()
    is_anggota = request.user.is_authenticated and request.user.email in settings.ALLOWED_EMAILS

    anggota_kelompok = [
        {
            "id": 1,
            "nama": "Anggota Pertama",
            "npm": "2206123451",
            "role": "Hustler / PM",
            "bio": "Mengatur jalannya proyek dan memastikan semua selesai tepat waktu.",
            "prodi": "Ilmu Komputer",
            "foto": "img/anggota1.png",
            "linkedin": "https://linkedin.com/in/username1",
            "github": "https://github.com/username1"
        },
        {
            "id": 2,
            "nama": "Anggota Kedua",
            "npm": "2206123452",
            "role": "Hipster / UI/UX",
            "bio": "Mendesain antarmuka yang cantik menggunakan Tailwind dan Figma.",
            "prodi": "Sistem Informasi",
            "foto": "img/anggota2.png",
            "linkedin": "https://linkedin.com/in/username2",
            "github": "https://github.com/username2"
        },
        {
            "id": 3,
            "nama": "Anggota Ketiga",
            "npm": "2206123453",
            "role": "Hacker / Backend",
            "bio": "Membangun sistem autentikasi dan integrasi database Django.",
            "prodi": "Ilmu Komputer",
            "foto": "img/anggota3.png",
            "linkedin": "https://linkedin.com/in/username3",
            "github": "https://github.com/username3"
        },
        {
            "id": 4,
            "nama": "Anggota Keempat",
            "npm": "2206123454",
            "role": "Hacker / Frontend",
            "bio": "Mengubah desain menjadi kode HTML dan Tailwind yang responsif.",
            "prodi": "Sistem Informasi",
            "foto": "img/anggota4.png",
            "linkedin": "https://linkedin.com/in/username4",
            "github": "https://github.com/username4"
        }
    ]

    context = {
        'style': style,
        'is_anggota': is_anggota,
        'anggota_kelompok': anggota_kelompok
    }
    return render(request, 'home.html', context)

@login_required
def edit_style(request):
    if request.user.email not in settings.ALLOWED_EMAILS:
        return HttpResponseForbidden("Akses Ditolak: Anda bukan anggota kelompok ini.")

    style = WebStyle.get_settings()
    if request.method == "POST":
        style.bg_color = request.POST.get('bg_color')
        style.font_family = request.POST.get('font_family')
        style.save()
        return redirect('home')

    return render(request, 'edit_style.html', {'style': style})