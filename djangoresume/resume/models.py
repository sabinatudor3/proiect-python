from django.db import models
from django.forms import ModelForm

# Create your models here.
SKILLS_CHOICES1 = (
    ("1", "Communication"), 
    ("2", "Teamwork"), 
    ("3", "Innovation"), 
    ("4", "Leadership"), 
    ("5", "Motivation"))

SKILLS_CHOICES2 = (
    ("1", "Problem-solving"),
    ("2", "Organisation"),
    ("3", "Perseverance"),
    ("4", "Ability to work under pressure"),
    ("5","Adaptability"))  

SKILLS_CHOICES3 = (
    ("1", "Work Ethic"), 
    ("2", "Flexibility"), 
    ("3", "Time Management"), 
    ("4", "Critical Thinking"), 
    ("5", "Creativity"))

TEMPLATE_CHOICES = (
    ("", "Choose.."),
    ("1", "Template 1"))

LANGUAGE_CHOICES1 = (
    ("", "Choose.."),
    ("1", "English"), 
    ("2", "French"), 
    ("3", "Spanish"), 
    ("4", "German"), 
    ("5", "Italian"))


class Data(models.Model):
    firstname    = models.CharField(max_length=50)
    lastname     = models.CharField(max_length=50)
    email        = models.EmailField()
    phone        = models.IntegerField()

    def __str__(self):
        return '{0} {1}' .format(self.firstname, self.lastname)
    


class Tech(models.Model):
    profile      = models.CharField(max_length=300)
    tech1        = models.CharField(max_length=50)
    tech2        = models.CharField(max_length=50, blank=True, null = True)
    tech3        = models.CharField(max_length=50, blank=True, null = True)
    data         = models.OneToOneField('Data', on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):
        return '{0}, {1}, {2}' .format(self.tech1, self.tech2, self.tech3)


class Skill(models.Model):
    skills1      = models.CharField(max_length=1, choices=SKILLS_CHOICES1)
    skills2      = models.CharField(max_length=1, choices=SKILLS_CHOICES2)
    skills3      = models.CharField(max_length=1, choices=SKILLS_CHOICES3)
    data         = models.OneToOneField('Data', on_delete=models.CASCADE, blank=True, null = True)

class Language(models.Model):
    language1        = models.CharField(max_length=50)
    language2        = models.CharField(max_length=50, blank=True, null = True)
    language3        = models.CharField(max_length=50, blank=True, null = True)
    data             = models.OneToOneField('Data', on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):
        return '{0}, {1}, {2}' .format(self.language1, self.language2, self.language3)


class Work(models.Model):
    position     = models.CharField(max_length=50)
    company      = models.CharField(max_length=50)
    description  = models.CharField(max_length=250)
    data         = models.OneToOneField('Data', on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):
        return '{0}, {1}' .format(self.position, self.company)


class Education(models.Model):
    institution  = models.CharField(max_length=50)
    studies      = models.CharField(max_length=50)
    description  = models.CharField(max_length=250)
    data         = models.OneToOneField('Data', on_delete=models.CASCADE, blank=True, null = True)

    def __str__(self):
        return '{0}, {1}' .format(self.institution, self.studies)

class Template(models.Model):
    type         = models.CharField(max_length=1, choices=TEMPLATE_CHOICES)
    data         = models.OneToOneField('Data', on_delete=models.CASCADE, blank=True, null = True)






