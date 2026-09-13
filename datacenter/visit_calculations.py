from django.utils.timezone import localtime


SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60


def get_duration(visit):
    entered_at = localtime(visit.entered_at)

    if visit.leaved_at:
        leaved_at = localtime(visit.leaved_at)
    else:
        leaved_at = localtime()

    return leaved_at - entered_at


def format_duration(duration):
    total_minutes = int(
        duration.total_seconds() // SECONDS_IN_MINUTE
    )
    hours, minutes = divmod(
        total_minutes,
        MINUTES_IN_HOUR,
    )

    return f'{hours}ч {minutes}мин'


def is_visit_long(visit, minutes=MINUTES_IN_HOUR):
    duration = get_duration(visit)
    return (
        duration.total_seconds()
        > minutes * SECONDS_IN_MINUTE
    )