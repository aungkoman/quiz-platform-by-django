from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import  authenticate #add this

from django.contrib.auth.models import User # Built-in user model
from django.contrib.auth import login # Built-in login function
from django.contrib.auth import logout # Built-in logout function
from django.contrib.auth.decorators import login_required # for login protected routes
from django.shortcuts import get_object_or_404 # select လုပ်တဲ့ function
from app.models import Quiz, Question, Answer
from django.urls import reverse # redirect url တည်ဆောက်ဖို့

def helloWorld(request):
    return HttpResponse("Hello, world. You're at the money app -> index method")

def index(request):
    #return HttpResponse("Hello, world. You're at the money app -> index method")
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    return render(request, 'index.html',{'person_list': person_list, 'title' : 'Person List' })

def login_page(request):
    #return HttpResponse("Hello, world. You're at the money app -> index method")
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    return render(request, 'login.html',{'person_list': person_list, 'title' : 'Person List' })

def register_page(request):
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    return render(request, 'register.html',{'person_list': person_list, 'title' : 'Person List' })

@login_required
def dasbhoard(request):
    # get authenticated user
    user = request.user 
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    title = "This is title"
    display_name = user.first_name # "Display Name"
    data = {
        'person_list' : person_list,
        'title' : title,
        'display_name' : display_name,
    }
    return render(
        request, 
        'dashboard.html',
        data
    )

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username= username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return redirect("dashboard")
    else:
        # No backend authenticated the credentials
        return HttpResponse("credential does not match " + username + ", " + password) #render(request, 'user_management/login.html')
    # person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    # return render(request, 'dashboard.html',{'person_list': person_list, 'title' : 'Person List' })

def register_check(request):
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    first_name = request.POST['display_name']
    
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = first_name
    user.save()

    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return redirect("dashboard")
    else:
        # No backend authenticated the credentials
        return HttpResponse("register failed :  " + username + ", " + password) #render(request, 'user_management/login.html')
    # person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    # return render(request, 'dashboard.html',{'person_list': person_list, 'title' : 'Person List' })

def logout_page(request):
    logout(request)
    return redirect("index")

# Quiz Business Logic

@login_required
def quiz_store(request):
    if request.method == 'POST':
        # Access form data using request.POST
        title = request.POST.get('title')
    else:
        # Handle non-POST requests as needed
        return HttpResponse('This view only handles POST requests')
    # Article.objects.create(user_profile_info=user_profile, description= description, media = media )
    user = request.user
    title = request.POST['title']
    description = request.POST['description']
    quiz = Quiz.objects.create(user=user, title=title, description=description)
    return redirect('quiz_list_page')

def quiz_update(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    title = request.POST['title']
    description = request.POST['description']
    quiz.title = title
    quiz.description = description
    quiz.save()

    return redirect('quiz_list_page')

def quiz_delete(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    quiz.delete()
    return redirect('quiz_list_page')

# Quiz UI
@login_required
def quiz_list_page(request):
    user = request.user
    # Article.objects.filter(user_profile_info = user_profile)
    quiz_list = Quiz.objects.filter(user=user)
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    
    data = {
        'person_list': person_list, 
        'title' : 'Person List',
        'quiz_list' : quiz_list
    }

    return render(request, 'quiz/quiz_list.html', data)

def quiz_create_page(request):
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    data = {'person_list': person_list, 'title' : 'Person List' }
    return render(request, 'quiz/quiz_create.html', data)

def quiz_edit_page(request, quiz_id):
    person_list = ['Aung Aung', 'Ma Ma', 'Mg Mg']
    quiz = get_object_or_404(Quiz, id=quiz_id)
    data = {
        'person_list': person_list, 
        'title' : 'Person List' ,
        'quiz' : quiz
    }
    return render(request, 'quiz/quiz_edit.html', data)

def quiz_detail_page(request, quiz_id):
    # Using get_object_or_404 to raise a 404 error if the object is not found
    # your_object = get_object_or_404(YourModel, id=object_id)
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question_list = Question.objects.filter(quiz = quiz)
    data = {
        'title' : 'Quiz Detail' , 
        'quiz' : quiz,
        'question_list': question_list
    }
    return render(request, 'quiz/quiz_detail.html', data)

# Question Business Logic
def question_store(request):
    # user = request.user
    title = request.POST['title']
    priority = request.POST['priority']
    quiz_id = request.POST['quiz_id']
    quiz = get_object_or_404(Quiz,id = quiz_id)
    question = Question.objects.create(quiz=quiz, title=title, priority=priority)
    # go to quiz detail

    # Using reverse to build the URL for 'quiz_detail_page' and including the 'quiz_id' parameter
    redirect_url = reverse('quiz_detail_page', kwargs={'quiz_id': quiz_id})
    return redirect(redirect_url)

def question_update(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    title = request.POST['title']
    question.title = title
    # description = request.POST['description']
    # quiz.description = description
    question.save()
    # Go to question detail
    # Redirect to the 'question_detail_page' with the specified 'question_id'
    return redirect(reverse('question_detail_page', args=[question_id]))

def question_delete(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    quiz_id = question.quiz.id
    question.delete()
    # Where we go? go to quiz page 
    return redirect(reverse('quiz_detail_page', args=[quiz_id]))
# Question UI
def question_create_page(request):
    quiz_id = request.GET['quiz_id']
    quiz = get_object_or_404(Quiz, id=quiz_id)
    data = {
        'title' : 'Person List',
        'quiz' : quiz
    }
    return render(request, 'question/question_create.html', data)

def question_detail_page(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answer_list = Answer.objects.filter(question = question)
    data = {
        'title' : 'Answer Detail' , 
        'question' : question,
        'answer_list': answer_list
    }
    return render(request, 'question/question_detail.html', data)

def question_edit_page(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    data = {
        'title' : 'Question Edit' ,
        'question' : question
    }
    return render(request, 'question/question_edit.html', data)


# Answer Business Logic
def answer_store(request):
    # user = request.user
    title = request.POST['title']
    priority = request.POST['priority']
    question_id = request.POST['question_id']
    correct = request.POST['correct']
    question = get_object_or_404(Question,id = question_id)
    question = Answer.objects.create(question=question, title=title, priority=priority, correct=correct)
    # go to upper level -> question detail
    # Using reverse to build the URL for 'quiz_detail_page' and including the 'quiz_id' parameter
    redirect_url = reverse('question_detail_page', kwargs={'question_id': question_id})
    return redirect(redirect_url)
