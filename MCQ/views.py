from django.shortcuts import render,redirect
from MCQ.models import Student,Faculty,Credentials,Exam,QuestionPaper,Question,AnswerKey,Exam,Result,Course
'''from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt'''
from django.contrib.auth import login,logout
from django.http import Http404 
from datetime import datetime,timedelta,date,time
from time import mktime



# Create your views here.


def get_user(credential):
	return {
			"student":Student.objects.filter(credentials=credential),
			"faculty":Faculty.objects.filter(credentials=credential)
			#,"admin":3 #to add admin
			}[credential.role]

def log_in(request):
	if request.user.is_authenticated():
		if(request.user.get_username()=='admin'):
			return redirect('/admin/')
		else:
			creds=Credentials.objects.get(username=request.user.get_username())
			current_user=get_user(creds)
			return redirect('/my_page/')
	else:
		error=request.session.pop('error',False)
		return render(request,"login.html",{'error':error})

def my_page(request):
	if request.user.is_authenticated():
		if request.user.get_username()=='admin':
			return redirect('/admin/')
		else:
			credentials=Credentials.objects.get(username=request.user.get_username())
			print credentials.role+".html"
			return render(request,credentials.role+".html")
	else:
		if request.method=='POST':
			user_name=request.POST['user_name']
			password=request.POST['password']
			role=request.POST['role']
			try:
				credentials=Credentials.objects.get(username=user_name,password=password,role=role)
			except Credentials.DoesNotExist:
				credentials=None
			if credentials is None:
				request.session['error']=True
				return redirect('/')
			else:
				login(request,credentials)
				return render(request,credentials.role+".html")
		else:
			return redirect('/')		

def log_out(request):
	logout(request)
	return redirect('/')

def give_exam(request,exam_name):
	#to protect direct access
	if request.user.is_authenticated():
		if request.user.get_username()=='admin':
			error="You are not elegible to give an exam."
			return render(request,'error.html',{'error':error})
		else:
			credentials=Credentials.objects.get(username=request.user.get_username())
			if credentials.role=="student":
				student=Student.objects.get(credentials=credentials)
				try:
					request.META['HTTP_REFERER']
					exam=Exam.objects.get(exam_name=exam_name)
					course=exam.course
					course.student_set.get(credentials=student.credentials)
					try:
						result=Result.objects.get(exam=exam,student=student)	
						error="You have already submitted this exam."
						return render(request,'error.html',{'error':error})
					except Exception as e:
						end_time=exam.exam_time+timedelta(minutes=exam.exam_duration)
						ques_paper=exam.question_paper
						questions=list(ques_paper.question_set.all())
						return render(request,'exam.html',{'end_time':(mktime(end_time.timetuple())-(19800)),'questions':questions,'exam_name':exam_name,'course':exam.course,'no_of_questions':exam.question_paper.no_of_question})
				except Student.DoesNotExist:
					error="You are not enrolled in course "+course.name
					return render(request,'error.html',{'error':error})
				except Exam.DoesNotExist:
					'''c=Course.objects.get(code="CS223")
					qp=QuestionPaper(no_of_question=5)
					qp.save()
					q=Question(question="Formula of water",option_a="H2O",option_b="HCL",option_c="N2O",option_d="WAT",question_paper=qp)
					q.save()
					q1=Question(question="2+2=",option_a="4",option_b="0",option_c="1",option_d="3",question_paper=qp)
					q1.save()
					q2=Question(question="2*7=",option_a="4",option_b="0",option_c="14",option_d="3",question_paper=qp)
					q2.save()
					q3=Question(question="2-7=",option_a="4",option_b="0",option_c="14",option_d="-5",question_paper=qp)
					q3.save()
					q4=Question(question="2/7=",option_a="4",option_b="0",option_c=".286",option_d="-5",question_paper=qp)
					q4.save()
					ak=AnswerKey(answers="aacdc")
					ak.save()
					d=date(2017,2,19)
					t=time(13,0)
					dt=datetime.combine(d,t)
					exam=Exam(exam_name=exam_name,question_paper=qp,answer_key=ak,exam_time=dt,exam_duration=12000,course=c)
					exam.save()
					end_time=exam.exam_time+timedelta(minutes=exam.exam_duration)
					questions=list(qp.question_set.all())
					#for debugging'''
					error="Exam "+exam_name+" doesn't exist."
					return render(request,'error.html',{'error':error})
				except Exception as e:
					return redirect('/my_page/')
			else:
				error="You are not elegible to give an exam."
				return render(request,'error.html',{'error':error})
	else:
		return redirect('/')

def submit_exam(request,exam_name):
	if request.user.is_authenticated():
		if request.user.get_username()=='admin':
			error="You are not elegible to give an exam."
			return render(request,'error.html',{'error':error})
		else:
			credentials=Credentials.objects.get(username=request.user.get_username())
			if credentials.role=="student":
				try:
					request.META['HTTP_REFERER']
					exam=Exam.objects.get(exam_name=exam_name)
					ans_key=exam.answer_key
					answers=ans_key.answers
					answers=answers.lower()
					no_of_questions=len(answers)
					question_paper=exam.question_paper
					questions=list(question_paper.question_set.all())	
					reply=[]
					score=0
					for x in xrange(1,no_of_questions+1):
						query="Question"+str(x)
						try:
							if answers[x-1]==request.POST[query]:
								score+=1
								reply.append((request.POST[query]+":"+returnOption(questions[x-1],request.POST[query]),1))
							else:
								reply.append((request.POST[query]+":"+returnOption(questions[x-1],request.POST[query]),0))
						except Exception as e:
							print e
							reply.append(("nil",0))
					creds=Credentials.objects.get(username=request.user.get_username())
					student=Student.objects.get(credentials=creds)
					result=Result(student=student,score=score,exam=exam)
					result.save()
					return render(request,"score.html",{'score':score,'reply':reply})
				except Exception as e:
					error="You need to write an exam before submitting it."
					return render(request,'error.html',{'error':error})			
			else:
				error="You are not elegible to give an exam."
				return render(request,'error.html',{'error':error})
	else:
		return redirect('/')

	#to protect direct access

def returnOption(question,option):
	return {
			"a":question.option_a,
			"b":question.option_b,
			"c":question.option_c,
			"d":question.option_d
			}[option]