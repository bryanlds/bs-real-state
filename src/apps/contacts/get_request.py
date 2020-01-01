from collections import namedtuple


def get_form_values(request):
    FormValues = namedtuple(
        "FormValues",
        "listing_id listing name email phone message user_id realtor_email",
    )
    values = (
        request.POST["listing_id"],
        request.POST["listing"],
        request.POST["name"],
        request.POST["email"],
        request.POST["phone"],
        request.POST["message"],
        request.POST["user_id"],
        request.POST["realtor_email"],
    )

    return FormValues._make(values)
