from collections import namedtuple


def get_form_values(request):
    FormValues = namedtuple(
        "FormValues", "first_name last_name username email password password2"
    )
    values = (
        request.POST["first_name"],
        request.POST["last_name"],
        request.POST["username"],
        request.POST["email"],
        request.POST["password"],
        request.POST["password2"],
    )

    return FormValues._make(values)


def get_username_and_password(request):
    User = namedtuple("User", "username password")
    values = (request.POST["username"], request.POST["password"])

    return User._make(values)
