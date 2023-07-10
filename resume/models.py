from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.position

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=100)
    completion_date = models.DateField()

    def __str__(self):
        return self.degree

class Developer(models.Model):
    name = models.CharField(max_length=100)
    profile_name = models.CharField(max_length=100)
    career_objective = models.CharField(max_length=1000)
    contact_location = models.CharField(max_length=100)
    contact_mobile = models.CharField(max_length=20)
    contact_email = models.EmailField()
    contact_linkedin = models.URLField()
    education = models.ForeignKey(Education, on_delete=models.CASCADE)
    experiences = models.ManyToManyField(Experience)
    skills = models.ManyToManyField(Skill)
    certifications = models.ManyToManyField(Certification)

    def __str__(self):
        return self.name
