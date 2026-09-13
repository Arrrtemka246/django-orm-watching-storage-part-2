from django.utils.timezone import localtime


def get_duration(visit):
    entered_at = localtime(visit.entered_at)

    if visit.leaved_at:
        leaved_at = localtime(visit.leaved_at)
    else:
        leaved_at = localtime()

    return leaved_at - entered_at


def format_duration(duration):
    total_minutes = int(duration.total_seconds() // 60)
    hours, minutes = divmod(total_minutes, 60)

    return f'{hours}ч {minutes}мин'


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * 60