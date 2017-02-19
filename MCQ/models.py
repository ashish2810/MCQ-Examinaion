from __future__ import unicode_literals

from django.db import models

from django.contrib.auth import models as mods

# Create your models here.

class Credentials(mods.User):
	role=models.CharField(max_length=10,null=True,choices=[('student', 'student'), ('faculty', 'faculty')])
	class Meta:
		verbose_name="Credential"
		verbose_name_plural="Credentials"

			


class User(models.Model):
	name=models.CharField(max_length=40,null=True)
	credentials=models.OneToOneField(Credentials,null=True)
	
	class Meta:
		abstract=True
	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name


class Faculty(User):
	def sendDcore():
		pass
	def viewPerformance():
		pass


class Course(models.Model):
	code=models.CharField(max_length=10,null=True)
	name=models.CharField(max_length=50,null=True)
	credits=models.IntegerField(default=0)
	faculty=models.ForeignKey(Faculty,null=True)
	def __str__(self):
		return self.name
	def __unicode__(self):
		return self.name

class Student(User):
	courses=models.ManyToManyField(Course,symmetrical=True)

class QuestionPaper(models.Model):
	no_of_question=models.IntegerField(default=0)
	def __str__(self):
		try:
			return "question paper of"+" "+self.exam.exam_name
		except Exception as e:
			return "question paper "
	def __unicode__(self):
		try:
			return "question paper of"+" "+self.exam.exam_name
		except Exception as e:
			return "question paper "

class Question(models.Model):
	question=models.CharField(default="No Question",max_length=1000)
	option_a=models.CharField(default="no_option",max_length=1000)
	option_b=models.CharField(default="no_option",max_length=1000)
	option_c=models.CharField(default="no_option",max_length=1000)
	option_d=models.CharField(default="no_option",max_length=1000)
	question_paper=models.ForeignKey(QuestionPaper,null=True)
	def __str__(self):
		return self.question
	def __unicode__(self):
		return self.question

class AnswerKey(models.Model):		
	answers=models.CharField(default="",max_length=100)
	def __str__(self):
		try:
			return "question paper of"+" "+self.exam.exam_name
		except Exception as e:
			return "question paper "
	def __unicode__(self):
		try:
			return "question paper of"+" "+self.exam.exam_name
		except Exception as e:
			return "question paper "

class Exam(models.Model):
	course=models.ForeignKey(Course,null=True)
	exam_name=models.CharField(default="exam",max_length=100)
	question_paper=models.OneToOneField(QuestionPaper,null=True,related_name='exam')
	answer_key=models.OneToOneField(AnswerKey,null=True)
	exam_time=models.DateTimeField(null=True)
	exam_duration=models.IntegerField(default=60)#in minutes
	def __str__(self):
		return self.exam_name
	def __unicode__(self):
		return self.exam_name
		
class Result(models.Model):
	exam=models.ForeignKey(Exam,null=True)
	score=models.IntegerField(default=0)
	student=models.ForeignKey(Student,null=True)
	class Meta:
		abstract=True
	def __str__(self):
		return self.student.name+" result of "+self.exam.exam_name
	def __unicode__(self):
		return self.student.name+" result of "+self.exam.exam_name


