from termios import TIOCSERSETMULTI
from django.db import models

#Have an array with first index being module code and then continue
#to add ratings as they come in for the professor in that modules
"""
class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
"""

#Poll the ratings model for every 
class Rating(models.Model):
    class_id = models.CharField(max_length=10)
    professor_id = models.CharField(max_length=10)
    rating = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)

    def __str__(self):
        return u'%s %s %s' % (self.class_id, self.proffesor_id, self.rating)

class Professor(models.Model):
    professor_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    rating = models.ManyToManyField(Rating)
    
    def __str__(self):
        return u'%s %s' % (self.professor_id, self.name)

class Module(models.Model):
    module_code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    professors = models.ManyToManyField(Professor)

    def __str__(self):
        return u'%s %s %s %s' % (self.module_code, self.name, self.year, self.semester)

    def listview(self):
        return u'| %s | %s | %s | %s | ' % (self.module_code, self.name, self.year, self.semester)
"""
class Enrollment(models.Model):
    professors = models.ForeignKey(Professor, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    year = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.professors, self.module, self.year, self.semester)


class Rater(models.Model):
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    professors = models.ForeignKey(Professor, on_delete=models.CASCADE)
    
"""
