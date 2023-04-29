from django.shortcuts import render, redirect
from .forms import ProjectForm, AchievementForm, ContactForm
from .models import Project, Achievement, Contact
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages

# [GET]	http://127.0.0.1:8000/
# sehife yuklenir, comments-ler secilir bazadan
@require_http_methods(["GET"])
def index(request):
    comments = Project.objects.all()
    form = ProjectForm()
    comments_ach = Achievement.objects.all()
    form_ach = AchievementForm()
    contacts = Contact.objects.all()
    contacts_form = ContactForm()
    context = {
        'form': form,
        'comments': comments,
        'comments_ach': comments_ach,
        'form_ach': form_ach,
        'contacts': contacts,
        'contacts_form': contacts_form
    }
    return render(request, 'index.html', context )

# [POST]	http://127.0.0.1:8000/projects
# comment save edir db-e, redirect yuxardaki [GET]-e
@require_http_methods(["POST"])
def save_comments(request):
    form = ProjectForm(data=request.POST)

    if form.is_valid():
        comment_save = form.save(commit=False)
        comment_save.save()
        # subject = 'Comment added'
        # body = {
        #     'message': form.cleaned_data['message']
        # }
        # message = "\n".join(body.values())
        #
        # send_mail(subject, message, 'test@gmail.com', ['mahammad.muradd@gmail.com'])



    return redirect('index')

@require_http_methods(["POST"])
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return redirect('index')

@require_http_methods(["POST"])
def edit_comment(request, pk):
    # comment_edit = Project.objects.get(id=pk)
    # comment_edit.c
    return redirect('index')



@require_http_methods(["POST"])
def save_comments_ach(request):
    # h = request.POST["message"]
    # print(f'Your commont {h}')
    form_ach = AchievementForm(data=request.POST)
    if form_ach.is_valid():
        comment_ach_save = form_ach.save(commit=False)
        comment_ach_save.save()
        # subject = 'Comment added'
        # body = {
        #     'message': form_ach.cleaned_data['message']
        # }
        # message = "\n".join(body.values())
        #
        # send_mail(subject, message, 'test@gmail.com', ['mahammad.muradd@gmail.com'])

    return redirect('index')

@require_http_methods(["POST"])
def save_contacts(request):
    contacts_form = ContactForm(data=request.POST)

    if contacts_form.is_valid():
        # contact = contacts_form.save(commit=False)
        # contact.save()
        subject = 'Contact form submitted'
        body = {
            'name': contacts_form.cleaned_data['name'],
            'email': contacts_form.cleaned_data['email'],
            'number': contacts_form.cleaned_data['number'],
            'message': contacts_form.cleaned_data['message']
        }
        message = "\n".join(body.values())

        send_mail(subject, message, 'test@gmail.com', ['mahammad.muradd@gmail.com'])



    return redirect('index')

