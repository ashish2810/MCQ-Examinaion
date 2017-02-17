from django.shortcuts import render,redirect
from MCQ.models import Student,Faculty,Credentials,Exam,QuestionPaper,Question,AnswerKey,Exam,Result
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
	try:
		already=Exam.objects.get(exam_name=exam_name)
		exam=Exam.objects.get(exam_name=exam_name)
		end_time=exam.exam_time+timedelta(minutes=exam.exam_duration)
		ques_paper=exam.question_paper
		questions=list(ques_paper.question_set.all())
	except Exception as e:
		qp=QuestionPaper(no_of_question=2)
		qp.save()
		q=Question(question="Formula of water",option_a="H2O",option_b="HCL",option_c="N2O",option_d="WAT",question_paper=qp)
		q.save()
		q1=Question(question="2+2=",option_a="4",option_b="0",option_c="1",option_d="3",question_paper=qp)
		q1.save()
		ak=AnswerKey(answers="aa")
		ak.save()
		d=date(2017,2,17)
		t=time(21,0)
		dt=datetime.combine(d,t)
		exam=Exam(exam_name=exam_name,question_paper=qp,answer_key=ak,exam_time=dt,exam_duration=120)
		exam.save()
		end_time=exam.exam_time+timedelta(minutes=exam.exam_duration)
		questions=list(qp.question_set.all())
		
	'''exam=Exam.objects.get(exam_name=exam_name)
	end_time=exam.exam_time+timedelta(minutes=exam.exam_duration)
	ques_paper=exam.question_paper
	questions=list(ques_paper.question_set.all())'''
	print end_time
	return render(request,'exam.html',{'end_time':(mktime(end_time.timetuple())-(19800)),'questions':questions,'exam_name':exam_name})

def submit_exam(request,exam_name):
	#to protect direct access
	exam=Exam.objects.get(exam_name=exam_name)
	ans_key=exam.answer_key
	answers=ans_key.answers
	answers=answers.lower()
	no_of_questions=len(answers)	
	score=0
	for x in xrange(1,no_of_questions+1):
		query="Question"+str(x)
		try:
			if answers[x-1]==request.POST[query]:
				score+=1
		except Exception as e:
			pass
	creds=Credentials.objects.get(username=request.user.get_username())
	student=Student.objects.get(credentials=creds)
	result=Result(student=student,score=score,exam=exam)
	result.save()
	return render(request,"score.html",{'score':score})