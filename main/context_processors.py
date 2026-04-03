from .models import WebStyle

def web_style_processor(request):
    try:
        style = WebStyle.get_settings()
    except:
        style = None

    return {'style': style}