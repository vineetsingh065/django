from main.models import Main


def render_header_footer():
    site = Main.objects.get(pk=2)
    return site
