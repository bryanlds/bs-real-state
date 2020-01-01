from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from .get_request import get_form_values
from .models import Contact


@require_POST
def contact(request):
    form_values = get_form_values(request)

    if request.user.is_authenticated:
        form_values._replace(user_id=request.user.id)
        has_contacted = Contact.objects.all().filter(
            listing_id=form_values.listing_id, user_id=form_values.user_id
        )
        if has_contacted:
            messages.error(request, "You have already made an inquiry for this listing")
            return redirect("listings:listing", listing_id=form_values.listing_id)

    contact = Contact(
        listing=form_values.listing,
        listing_id=form_values.listing_id,
        name=form_values.name,
        email=form_values.email,
        phone=form_values.phone,
        message=form_values.message,
        user_id=form_values.user_id,
    )

    contact.save()

    messages.success(
        request, "You request has been submitted, a realtor will get back to you soon"
    )
    return redirect("listings:listing", listing_id=form_values.listing_id)
