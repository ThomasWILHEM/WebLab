from django.db import models

# Create your models here.


class Techno(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()

    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name="frameworks")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateField()
    image = models.URLField()
    deployment_link = models.URLField(null=True)
    github_link = models.URLField(null=True)
    status = models.CharField(
        max_length=20,
        choices=[('finished', 'Finished'), ('in_progress', 'In Progress'), ('on_hold', 'On Hold')])

    languages = models.ManyToManyField(Language, related_name="projects_using_language", blank=True)
    frameworks = models.ManyToManyField(Framework, related_name="projects_using_framework", blank=True)


class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)

    languages = models.ManyToManyField(Language, related_name="jobs_using_language", blank=True)
    frameworks = models.ManyToManyField(Framework, related_name="jobs_using_framework", blank=True)


class Education(models.Model):
    institution_name = models.CharField(max_length=100)
    formation_name = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.TextField()

    languages = models.ManyToManyField(Language, related_name="educations_using_language", blank=True)
    frameworks = models.ManyToManyField(Framework, related_name="educations_using_framework", blank=True)


class OnlineCourse(models.Model):
    course_name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    completion_date = models.DateField()
    course_link = models.URLField()
    description = models.TextField()

    languages = models.ManyToManyField(Language, related_name="courses_using_language", blank=True)
    frameworks = models.ManyToManyField(Framework, related_name="courses_using_framework", blank=True)
    technos = models.ManyToManyField(Techno, related_name="courses_using_tech", blank=True)