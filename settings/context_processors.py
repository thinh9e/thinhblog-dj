from settings.models import Setting


def settings_context(request):
    settings = {}
    for setting in Setting.objects.all():
        if setting.category not in settings:
            settings[setting.category] = {}
        settings[setting.category][setting.key] = setting.value
    return {"settings": settings}
