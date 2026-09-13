from datacenter.models import Visit
from datacenter.visit_calculations import (
    format_duration,
    get_duration,
    is_visit_long,
)
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(
        leaved_at__isnull=True,
    ).select_related('passcard')

    visits_information = []

    for visit in non_closed_visits:
        visits_information.append(
            {
                'who_entered': visit.passcard.owner_name,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(
                    get_duration(visit)
                ),
                'is_strange': is_visit_long(visit),
            }
        )

    context = {
        'non_closed_visits': visits_information,
    }

    return render(
        request,
        'storage_information.html',
        context,
    )