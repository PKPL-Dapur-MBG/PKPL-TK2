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
            "nama": "Ilham Afuw Ghaniy",
            "npm": "2406403495",
            "role": "Member",
            "bio": "nama lengkap Ilham Afuw Ghaniy,biasa dipanggil Ilham. Asal Depok. Hobi nonton film,main game, sama baca buku. Lumayan suka Ama makanan seafood.",
            "prodi": "Ilmu Komputer",
            "foto": "images/ilham.jpg",
            "linkedin": "https://www.linkedin.com/in/ilham-afuw-ghaniy-501576323/",
            "github": "https://github.com/username1"
        },
        {
            "id": 2,
            "nama": "Wildan Muhammad Hafidz",
            "npm": "2406495962",
            "role": "Member",
            "bio": "hobi maen game,pengen ipk gede tapi males",
            "prodi": "Sistem Informasi",
            "foto": "images/wildan.jpg",
            "linkedin": "https://linkedin.com/in/username2",
            "github": "https://github.com/Wildann133"
        },
        {
            "id": 3,
            "nama": "Dzaky Ahmad Trinindito",
            "npm": "2406406351",
            "role": "Member",
            "bio": "aku gampang tertarik dengan hal baru jadi banyak banget interestnya",
            "prodi": "Ilmu Komputer",
            "foto": "images/dzaky.jpg",
            "linkedin": "https://www.linkedin.com/in/dzaky-ahmad-trinindito-37b63a322/",
            "github": "https://github.com/username3"
        },
        {
            "id": 4,
            "nama": "Rexy Adrian Fernando",
            "npm": "2406495666",
            "role": "Member",
            "bio": "6767",
            "prodi": "Ilmu Komputer",
            "foto": "images/rexy.jpg",
            "linkedin": "https://www.linkedin.com/in/rexy-adrian-fernando/",
            "github": "https://github.com/rexyadrian"
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
        style.secondary_color = request.POST.get('secondary_color')
        style.font_family = request.POST.get('font_family')
        style.save()
        return redirect('home')

    return render(request, 'edit_style.html', {'style': style})