from teacher_profile.models import TeacherProfileDetails, TeacherStatus


def create_teacher(user, email):
    teacher_profile = TeacherProfileDetails.objects.create(user=user, email=email)
    teacher_profile.save()
    teacher_status = TeacherStatus.objects.create(user=user)
    teacher_status.save()
    return


def update_teacher_profile_details(user, **kwargs):
    TeacherProfileDetails.objects.filter(user=user).update(kwargs)
    return


def get_teacher_status(user):
    try:
        return TeacherStatus.objects.get(user=user)
    except TeacherStatus.DoesNotExist:
        return None

