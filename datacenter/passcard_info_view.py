from datacenter.models import Passcard, Visit
from datacenter.visit_calculations import (
    format_duration,
    get_duration,
    is_visit_long,
)
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(
        Passcard,
        passcode=passcode,
    )

    passcard_visits = Visit.objects.filter(
        passcard=passcard,
    )

    visits_information = []

    for visit in passcard_visits:
        visits_information.append(
            {
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(
                    get_duration(visit)
                ),
                'is_strange': is_visit_long(visit),
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': visits_information,
    }

    return render(
        request,
        'passcard_info.html',
        context,
    )