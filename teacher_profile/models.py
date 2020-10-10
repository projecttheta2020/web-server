from django.db import models
from django.contrib.auth.models import User

from common.utils import get_choices_from_enum
from teacher_profile.enums import Status


class TeacherProfileDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=50, null=True, blank=True)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    email_alternative = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    current_address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    perm_address = models.TextField(null=True, blank=True)
    perm_city = models.CharField(max_length=50, null=True, blank=True)
    perm_state = models.CharField(max_length=50, null=True, blank=True)
    perm_country = models.CharField(max_length=50, null=True, blank=True)
    perm_postal_code = models.CharField(max_length=50, null=True, blank=True)

    objective = models.TextField(null=True, blank=True)
    job_role = models.CharField(max_length=200, null=True, blank=True)
    preferred_subjects = models.CharField(max_length=200, null=True, blank=True)
    preferred_city = models.CharField(max_length=200, null=True, blank=True)
    total_experience = models.IntegerField(null=True, blank=True)
    highest_education = models.CharField(max_length=100, null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    cover_letter = models.TextField(null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.email) + ' | ' + str(self.name)

    @property
    def name(self):
        first_name = self.first_name if self.first_name else ""
        middle_name = self.middle_name if self.middle_name else ""
        last_name = self.last_name if self.last_name else ""
        return first_name + middle_name + last_name

    @property
    def education_details(self):
        try:
            return TeacherEducation.objects.filter(user=self.user)
        except Exception as e:
            # log_exception(e)
            pass

    @property
    def experience_details(self):
        try:
            return TeacherExperience.objects.filter(user=self.user)
        except Exception as e:
            # log_exception(e)
            pass

    @property
    def cocurricular_details(self):
        try:
            return TeacherCocurricular.objects.filter(user=self.user)
        except Exception as e:
            # log_exception(e)
            pass

    @property
    def certification_details(self):
        try:
            return TeacherCertification.objects.filter(user=self.user)
        except Exception as e:
            # log_exception(e)
            pass

    @property
    def references_details(self):
        try:
            return TeacherReferences.objects.filter(user=self.user)
        except Exception as e:
            # log_exception(e)
            pass


class TeacherEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    degree = models.CharField(max_length=200, null=True, blank=True)
    institution_name = models.CharField(max_length=200, null=True, blank=True)
    field_of_study = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    start_year = models.CharField(max_length=200, null=True, blank=True)
    end_year = models.CharField(max_length=200, null=True, blank=True)
    grade_obtained = models.CharField(max_length=200, null=True, blank=True)
    marks_obtained = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.user.teacherprofiledata) + ' | ' + str(self.degree)


class TeacherExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    subjects = models.CharField(max_length=200, null=True, blank=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    additional_role = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user.teacherprofiledata) + ' | ' + str(self.position)


class TeacherCocurricular(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    certificate_file = models.FileField(upload_to='uploads/teacher/cocurricular', null=True, blank=True)

    def __str__(self):
        return str(self.user.teacherprofiledata) + ' | ' + str(self.title)


class TeacherCertification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, null=True, blank=True)
    certificate_url = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    certificate_file = models.FileField(upload_to='uploads/teacher/certificates', null=True, blank=True)
    certificate_area = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user.teacherprofiledata) + ' | ' + str(self.title)


class TeacherReferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    job_title = models.CharField(max_length=200, null=True, blank=True)
    institution = models.CharField(max_length=200, null=True, blank=True)
    institution_address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    lor = models.FileField(upload_to='uploads/teacher/lor', null=True, blank=True)

    def __str__(self):
        return str(self.user.teacherprofiledata) + ' | ' + str(self.name)

    @property
    def name(self):
        first_name = self.first_name if self.first_name else ""
        middle_name = self.middle_name if self.middle_name else ""
        last_name = self.last_name if self.last_name else ""
        return first_name + middle_name + last_name


class TeacherStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    onboarding_status = models.CharField(max_length=200, choices=get_choices_from_enum(Status), default=Status.Pending.value)

