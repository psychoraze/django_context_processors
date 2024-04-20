from django.contrib.auth.models import User, Group


def user_context(request):
    vse_cheliki = User.objects.all()
    gruppi_chelikov = request.user.groups.all() if request.user.is_authenticated else []

    context = {
        "all_users": vse_cheliki,
        "current_user_groups": gruppi_chelikov,
    }

    return context
