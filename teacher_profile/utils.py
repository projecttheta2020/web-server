from teacher_profile.models import TeacherProfileDetails, TeacherStatus


def create_teacher(user, email):
    teacher_profile = TeacherProfileDetails.objects.create(user=user, email=email)
    teacher_profile.save()
    teacher_status = TeacherStatus.objects.create(user=user)
    teacher_status.save()
    return


def update_teacher_profile_details(user, **kwargs):
    try:
        TeacherProfileDetails.objects.filter(user=user).update(kwargs)
    except Exception as e:
        print('error: ', e)
    return

