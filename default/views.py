# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.urls import reverse

from django.conf import settings

from django.contrib.auth.decorators import login_required
# Create your views here.

from django.contrib.auth.decorators import user_passes_test


def home(request):
    return render(request, 'default/home.html')

@login_required(login_url='/accounts/login/')
def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = request.user

    if user.type == 'author':
        output = "welcome author"
        conference_count = user.conference_set.count()
        submission_count = user.submission_set.count()
        review_count = user.submission_set.count()


        submissions = user.submission_set.all().order_by('-id')[:5]
        conferences = user.conference_set.all().order_by('-id')[:5]

        context = {
            'output': output,
            'conference_count' : conference_count,
            'submission_count' : submission_count,
            'review_count' : review_count,
            'submissions' : submissions,
            'conferences' : conferences
        }
        return render(request, 'default/index.html', {'con' : context})

    elif user.type == 'reviewer':
        output = "welcome reviewer"
        context = {'output': output}
        return render(request, 'default/index.html', context)
    elif user.type == 'chair':
        output = "welcome chair"
        context = {'output': output}
        return render(request, 'default/index.html', context)

@login_required(login_url='/accounts/login/')
def profile(request):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return render(request, 'default/profile.html', {})


from django.core.files.storage import FileSystemStorage

@login_required(login_url="/accounts/login")
def profile_update( request ):
    # if this is a POST request we need to process the form
    if request.method == 'POST':

        user = request.user

        user.first_name = request.POST['first_name']

        user.last_name = request.POST['last_name']

        user.email = request.POST['email']

        user.location = request.POST['location']

        user.skype = request.POST['skype']

        user.twitter = request.POST['twitter']

        user.facebook = request.POST['facebook']

        user.interests = request.POST['interests']

        if 'picture' in request.FILES.keys() and request.FILES['picture']:

            picture = request.FILES['picture']

            fs = FileSystemStorage()

            filename = fs.save(picture.name, picture)

            uploaded_file_url = fs.url(filename)

            user.photoURL = uploaded_file_url;

        user.save()

    return HttpResponseRedirect(reverse( "default:profile"))


from .forms import RegisterForm

from default.models import AdminUser, User, AuthorUser

from django.contrib.auth.hashers import PBKDF2PasswordHasher

from django.contrib.auth import authenticate, login

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        #print form
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            cleaned_data = form.cleaned_data

            print "cleaned_data", cleaned_data

            hasher = PBKDF2PasswordHasher()

            password = hasher.encode(password=cleaned_data['password'], salt='salt', iterations=36000)

            user = AuthorUser(id=None,
                                first_name=cleaned_data['fname'],
                                last_name=cleaned_data['lname'],
                                username=cleaned_data['email'],
                                password=password,
                                email=cleaned_data['email'],
                                is_staff=True,
                                type="author"
                            )
            user.save()

            login_user = authenticate(username=user.username, password=cleaned_data['password'])

            print( "login_user is ", login_user )

            if login_user is not None:

                login(request, login_user)
                # redirect to a new URL:
                #return HttpResponseRedirect('/thanks/')
                #return HttpResponseRedirect(reverse( "default:thanks", args=(question.id, )))
                return HttpResponseRedirect(reverse( "default:thanks", args=(login_user.id, )))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegisterForm()

    return render( request, 'default/register.html', {'form': form} )

def thanks( request, user_id ):

    user = User.objects.get(pk=user_id)

    context = {'user': user}

    return render( request, 'default/thanks.html', context )


def papers( request ):

    user = request.user.id

    context = {'user': user}

    return render( request, 'default/papers.html', context )

from .forms import CorrespondenceForm, AuthorForm, PaperForm


from default.models import AuthorUser, User, Conference, Submission

@login_required(login_url='/accounts/login/')
def author_conferences( request ):
    user = request.user
    conferences = user.conference_set.all()
    print conferences.count()

    #onferences = user.conference_set.all()
    return render( request, 'default/authors/conferences.html', {'conferences' : conferences})

def author_submissions( request ):
    user = request.user
    submissions = user.submission_set.all()
    print submissions.count()

    #onferences = user.conference_set.all()
    return render( request, 'default/authors/submissions.html', {'submissions' : submissions})

from .models import Correspondence, Author, Country
from django.http import HttpResponse
from .utils import get_post_dict
from django.shortcuts import get_object_or_404


@login_required(login_url='/accounts/login/')
def author_submissions_upload( request, conf_id ):
    conference = get_object_or_404(Conference, pk = conf_id)
    user = request.user
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CorrespondenceForm(request.POST)
        form3 = PaperForm(request.POST,request.FILES)
        title = request.POST.getlist('title', [])
        fname = request.POST.getlist('fname', [])
        lname = request.POST.getlist('lname', [])
        email = request.POST.getlist('email', [])
        organisation = request.POST.getlist('organisation', [])
        speaker = request.POST.getlist('speaker', [])

        authors = []
        author = {}

        length = len(title)
        for i in range(0, length):
            author['title'] = title[i]
            author['fname'] = fname[i]
            author['lname'] = lname[i]
            author['email'] = email[i]
            author['organisation'] = organisation[i]
            if 0 <= i < len(speaker):
                author['speaker'] = speaker[i]
            form2 = AuthorForm( author )
            if form2.is_valid():
                authors.append( author )


        #print form
        # check whether it's valid:

        if form.is_valid() and form3.is_valid():
            cleaned_data = form3.cleaned_data

            upload = cleaned_data['upload']

            fs = FileSystemStorage()

            filename = fs.save(upload.name, upload)

            paper_url = fs.url(filename)

            submission = Submission.objects.create(
                conference = conference,
                user = user,
                title= cleaned_data['paper_title'] ,
                abstract= cleaned_data['abstract'] ,
                keywords = cleaned_data['keywords'],
                paper_url = paper_url,
                status = "pending"
            )
            submission.save()

            cleaned_data = form.cleaned_data
            country = cleaned_data['country']

            correspondence = Correspondence.objects.create(
                submission = submission,
                address1 = cleaned_data['address1'],
                address2 = cleaned_data['address2'],
                city = cleaned_data['city'],
                state = cleaned_data['state'],
                country = country
            )
            correspondence.save()

            for a in authors:
                author = Author.objects.create(
                    submission = submission,
                    fname = a['fname'],
                    lname = a['lname'],
                    email = a['email'],
                    organisation = a['organisation'],
                    speaker = a['speaker']
                )
                author.save()
            return HttpResponseRedirect(reverse('default:author_submissions_info', kwargs={'submission_id':submission.id}))

    else:
        form = CorrespondenceForm()
        form2 = AuthorForm()
        form3 = PaperForm()

    return render( request, 'default/authors/submission_upload.html', {'conference':conference, 'form': form, 'form2' : form2, 'form3' : form3} )

@login_required(login_url='/accounts/login/')
def author_submissions_info( request, submission_id ):

    submission = get_object_or_404( Submission, pk = submission_id )

    conference = submission.conference

    authors = submission.author_set.all()

    print authors

    correspondence = submission.correspondence_set.all()

    return render( request, 'default/submission_info.html', {'conference':conference, 'submission': submission, 'authors' : authors} )


@login_required(login_url='/accounts/login/')
def support_index(request):
    return render(request, 'default/support.html')

@login_required(login_url='/accounts/login/')
def news_index(request):
    return render(request, 'default/news.html')


def author_reviews( request ):
    return render(request, 'default/maintenance.html')


def conference_register( request ):

    if request.method == 'POST' and 'conf_id' in request.POST:
        conf_id = request.POST['conf_id']
        conference =  Conference.objects.get(pk=conf_id)
        user = request.user
        conference.users.add(user)
        conference.save()
        # return HttpResponseRedirect(reverse( "default:conference_thanks", args=(conference.id, )))
        data = {}
        data['status']= "Success"
        data['url'] = reverse('default:conference_thanks', kwargs={'conf_id':conference.id})

        import json
        json_data = json.dumps(data)

        return HttpResponse(json_data, content_type='application/json')
    return HttpResponse("Error", content_type='application/html')

def conference_info( request, conf_id ):

    conference = Conference.objects.get(pk=conf_id)


    return render(request, 'default/conference_info.html', {'conference' : conference})

def conference_thanks( request, conf_id ):

    conference = Conference.objects.get(pk=conf_id)

    return render(request, 'default/conference_thanks.html', {'conference': conference})


def conference_search( request ):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']
        conferences = Conference.objects.filter(name__icontains=query)
        print conferences
    return render(request, 'default/conference_search.html', {'conferences': conferences})

def site_search( request ):
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET['q']
        conferences = Conference.objects.filter(name__icontains=query)
        print conferences
    return render(request, 'default/conference_search.html', {'conferences': conferences})
