from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from .forms import * 
import os


def index(request):
    w = Welcome.objects.all()
    hss = HomeSecondSection.objects.all()
    ht = HomeThird.objects.all()
    document = About.objects.all()
    context = {
        'nav': 'index',
        'w': w,
        'hss': hss,
        'ht': ht,
        'document': document
    }
    return render(request, 'ews_app/home.html', context)


def about(request):
    about = About.objects.all()
    context = {
        'nav': 'about',
        'about': about
    }
    return render(request, 'ews_app/about.html', context)


def token(request):
    tk = TK.objects.all()
    # tkv = tokenVideo.objects.all()
    context = {
        'nav': 'ts',
        'tk': tk,
        # 'tkv':tkv
    }
    return render(request, 'ews_app/ts.html', context)


def team(request):
    tm = Team.objects.all()
    context = {
        'nav': 'team',
        'tm': tm
    }
    return render(request, 'ews_app/team.html', context)


def roadmap(request):
    rm = RoadMap.objects.all()
    rmr1 = RoadmapR1.objects.all()
    rml1 = RoadmapL1.objects.all()
    rmr2 = RoadmapR2.objects.all()
    rml2 = RoadmapL2.objects.all()
    context = {
        'nav': 'road',
        'rm': rm,
        'rmr1': rmr1,
        'rml1': rml1,
        'rmr2': rmr2,
        'rml2': rml2,
    }
    return render(request, 'ews_app/roadmap.html', context)


def faq(request):
    fq = FAQ.objects.all()
    context = {
        'nav': 'faq',
        'fq': fq
    }
    return render(request, 'ews_app/faq.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        c = Contact(name=name, email=email, subject=subject, message=message)
        c.save()
        messages.success(request, f'We receive message and we will get back to you on {{email}}, as soon as possible')
        return redirect('ews_app:contact')

    context = {
        'nav': 'contact',
    }
    return render(request, 'ews_app/contact.html', context)


# ========================= ADMIN START HERE


def AdminHome(request):
    return render(request, 'ews_app/ad-home.html')


# HOme Starts Here ======================>>


def WelcomeList(request):
    a = Welcome.objects.all()
    context = {
        'a': a
    }
    return render(request, 'ews_app/wl.html', context)


def DeleteWelcome(request, speech_id):
    speech = Welcome.objects.get(id=speech_id)
    if request.method == 'POST':
        speech.delete()
        return redirect('ews_app:wl')
    context = {
        'item': speech,
    }
    return render(request, 'ews_app/delete_welcome.html', context)


def UpdateWelcome(request, pk):
    speech = Welcome.objects.get(id=pk)
    form = HomeWelcomeForm(instance=speech)
    if request.method == 'POST':
        form = HomeWelcomeForm(request.POST, instance=speech)
        if form.is_valid():
            form.save()
            return redirect('ews_app:wl')
    # else:  delete_welcome
    #     form = HomeWelcomeForm()
    context = {
        'speech': speech,
        'form': form,
    }
    return render(request, 'ews_app/update_welcome.html', context)


def AdminWelcome(request):
    form = HomeWelcomeForm()
    if request.method == 'POST':
        form = HomeWelcomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ews_app:wl')
    context = {
        'form': form,
    }
    return render(request, 'ews_app/index.html', context)


def InvestList(request):
    a = HomeSecondSection.objects.all()
    context = {
        'a': a
    }
    return render(request, 'ews_app/ivb.html', context)


def AdminInvestment(request):
    form = INVESTMENTForm()
    if request.method == 'POST':
        form = INVESTMENTForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('ews_app:il')

    context = {
        'form': form,
    }
    return render(request, 'ews_app/invest.html', context)


def UpdateInvestment(request, invest_pk):
    invest = HomeSecondSection.objects.get(id=invest_pk)
    form = INVESTMENTForm(instance=invest)
    if request.method == 'POST':
        form = INVESTMENTForm(request.POST, instance=invest)
        if form.is_valid():
            form.save()
            return redirect('ews_app:il')
    context = {
        'invest': invest,
        'form': form,
    }
    return render(request, 'ews_app/update_invest.html', context)


def DeleteInvestment(request, invest_pk):
    invest = HomeSecondSection.objects.get(id=invest_pk)
    if request.method == 'POST':
        invest.delete()
        return redirect('ews_app:il')
    context = {
        'item': invest,
    }
    return render(request, 'ews_app/delete_invest.html', context)


def HomeThirdView(request):
    a = HomeThird.objects.all()
    context = {
        'a': a,
    }
    return render(request, 'ews_app/third.html', context)


def CreateHomeThird(request):
    # form = HomeThirdForm() HomeThird
    if request.method == 'POST':
        prod = HomeThird()
        prod.title = request.POST.get('title')
        if len(request.FILES) != 0:
            prod.img = request.FILES['img']

        prod.save()
        messages.success(request, 'Successfully Added')
        return redirect('ews_app:tl')

    return render(request, 'ews_app/create_third.html')  # context


def editHomeThird(request, pk):
    prod = HomeThird.objects.get(id=pk)

    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(prod.img) > 0:
                os.remove(prod.img.path)
            prod.img = request.FILES['img']
        prod.title = request.POST.get('title')
        prod.save()
        messages.success(request, 'Successfully UPDATED')
        return redirect('ews_app:tl')
    context = {
        'prod': prod,
    }
    return render(request, 'ews_app/edit_third.html', context)


def deleteHomeThirdSection(request, pk):
    prod = HomeThird.objects.get(id=pk)
    if request.method == 'POST':
        prod.delete()
        return redirect('ews_app:tl')

    context = {
        'item': prod,
    }
    return render(request, 'ews_app/delete_third.html', context)


# HOme Ends Here ======================>>

# About Starts Here ======================>>


def aboutList(request):
    abt = About.objects.all()
    context = {
        'abt': abt,
    }
    return render(request, 'ews_app/about_list.html', context)


def CreateAbout(request):
    if request.method == 'POST':
        abt = About()
        abt.h2 = request.POST.get('h2')
        abt.p1 = request.POST.get('p1')
        abt.p2 = request.POST.get('p2')
        if len(request.FILES) != 0:
            abt.document = request.FILES['document']
        abt.save()
        return redirect('ews_app:admin-about')

    return render(request, 'ews_app/create_about.html')


def editAbout(request, pk):
    abt = About.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(abt.document) > 0:
                os.remove(abt.document.path)
            abt.document = request.FILES['document']
        abt.h2 = request.POST.get('h2')
        abt.p1 = request.POST.get('p1')
        abt.p2 = request.POST.get('p2')
        abt.save()
        messages.success(request, 'Successfully UPDATED')
        return redirect('ews_app:admin-about')
    context = {
        'abt': abt,
    }
    return render(request, 'ews_app/edit_about.html', context)


def deleteAbout(request, pk):
    abt = About.objects.get(id=pk)
    if request.method == 'POST':
        abt.delete()
        return redirect('ews_app:admin-about')

    context = {
        'item': abt,
    }
    return render(request, 'ews_app/delete_about.html', context)


# About Ends Here ======================>>
# ROADMAP sTARTs Here ======================>>
def AdminRMap(request):
    rm = RoadMap.objects.all()
    rmr1 = RoadmapR1.objects.all()
    rml1 = RoadmapL1.objects.all()
    rmr2 = RoadmapR2.objects.all()
    rml2 = RoadmapL2.objects.all()
    context = {
        'rm': rm,
        'rmr1': rmr1,
        'rml1': rml1,
        'rmr2': rmr2,
        'rml2': rml2,
    }
    return render(request, 'ews_app/admin_roadmap.html', context)


def CreateMap(request):
    if request.method == 'POST':
        rm = RoadMap()
        rm.title = request.POST.get('title')
        rm.speech = request.POST.get('speech')
        rm.save()
        messages.success(request, 'Successfully Added')
        return redirect('ews_app:roadList')

    return render(request, 'ews_app/create_rm.html')


def EditCreateMap(request, pk):
    rm = RoadMap.objects.get(id=pk)
    if request.method == 'POST':
        rm.title = request.POST.get('title')
        rm.speech = request.POST.get('speech')
        rm.save()
        messages.success(request, 'Successfully Added')
        return redirect('ews_app:roadList')
    context = {
        'rm': rm
    }
    return render(request, 'ews_app/editRoad.html', context)


def deleteCreateMap(request, pk):
    rm = RoadMap.objects.get(id=pk)
    if request.method == 'POST':
        rm.delete()
        return redirect('ews_app:roadList')
    context = {
        'rm': rm
    }
    return render(request, 'ews_app/deleteRoad.html', context)


def RoadmapRight1(request):
    if request.method == 'POST':
        rmr = RoadmapR1()
        rmr.Quarter = request.POST.get('rmrQR')
        rmr.year = request.POST.get('rmrYR')
        rmr.hone = request.POST.get('rmrhone')
        rmr.h_two = request.POST.get('rmrh_two')
        rmr.h_three = request.POST.get('rmrh_three')
        rmr.h_four = request.POST.get('rmrh_four')
        rmr.h_five = request.POST.get('rmrh_five')
        rmr.h_six = request.POST.get('rmrh_six')
        rmr.save()
        messages.success(request, 'Successfully Added')
        return redirect('ews_app:roadList')
    return render(request, 'ews_app/create_rmr.html')


def EditRoadmapRight1(request, pk):
    rmr = RoadmapR1.objects.get(id=pk)
    if request.method == 'POST':
        rmr.Quarter = request.POST.get('rmrQR')
        rmr.year = request.POST.get('rmrYR')
        rmr.hone = request.POST.get('rmrhone')
        rmr.h_two = request.POST.get('rmrh_two')
        rmr.h_three = request.POST.get('rmrh_three')
        rmr.h_four = request.POST.get('rmrh_four')
        rmr.h_five = request.POST.get('rmrh_five')
        rmr.h_six = request.POST.get('rmrh_six')
        rmr.save()
        messages.success(request, 'Successfully Updated')
        return redirect('ews_app:roadList')
    context = {
        'rmr': rmr
    }
    return render(request, 'ews_app/edit_rmr.html', context)


def deleteRoadmapR1(request, pk):
    rmr = RoadmapR1.objects.get(id=pk)
    if request.method == 'POST':
        rmr.delete()
        return redirect('ews_app:roadList')
    context = {
        'rmr': rmr
    }
    return render(request, 'ews_app/delete_rmr.html', context)


def RoadmapLeft1(request):
    if request.method == 'POST':
        rml = RoadmapL1()
        rml.Quarter = request.POST.get('rml_QR')
        rml.year = request.POST.get('rml_YR')
        rml.hone = request.POST.get('rml_hone')
        rml.h_two = request.POST.get('rml_h_two')
        rml.h_three = request.POST.get('rml_h_three')
        rml.h_four = request.POST.get('rml_h_four')
        rml.h_five = request.POST.get('rml_h_five')
        rml.h_six = request.POST.get('rml_h_six')
        rml.save()
        messages.success(request, 'Successfully Added')
        return redirect('ews_app:roadList')
    return render(request, 'ews_app/create_rml.html')


def EditRoadmapLeft1(request, pk):
    rmr = RoadmapL1.objects.get(id=pk)
    if request.method == 'POST':
        rmr.Quarter = request.POST.get('rmrQR')
        rmr.year = request.POST.get('rmrYR')
        rmr.hone = request.POST.get('rmrhone')
        rmr.h_two = request.POST.get('rmrh_two')
        rmr.h_three = request.POST.get('rmrh_three')
        rmr.h_four = request.POST.get('rmrh_four')
        rmr.h_five = request.POST.get('rmrh_five')
        rmr.h_six = request.POST.get('rmrh_six')
        rmr.save()
        messages.success(request, 'Successfully Updated')
        return redirect('ews_app:roadList')
    context = {
        'rmr': rmr
    }
    return render(request, 'ews_app/edit_rml.html', context)


def deleteRoadmapLeft1(request, pk):
    rmr = RoadmapL1.objects.get(id=pk)
    if request.method == 'POST':
        rmr.delete()
        return redirect('ews_app:roadList')
    context = {
        'rmr': rmr
    }
    return render(request, 'ews_app/delete_rml.html', context)


def RoadmapRight2(request):
    if request.method == 'POST':
        rmr = RoadmapR2()
        rmr.Quarter = request.POST.get('rmrQR')
        rmr.year = request.POST.get('rmrYR')
        rmr.hone = request.POST.get('rmrhone')
        rmr.h_two = request.POST.get('rmrh_two')
        rmr.h_three = request.POST.get('rmrh_three')
        rmr.h_four = request.POST.get('rmrh_four')
        rmr.h_five = request.POST.get('rmrh_five')
        rmr.h_six = request.POST.get('rmrh_six')
        rmr.save()

        messages.success(request, 'Successfully Added')
        return redirect('ews_app:roadList')

    return render(request, 'ews_app/create_rmrt.html')


def EditRoadmapRight2(request, pk):
    rmr = RoadmapR2.objects.get(id=pk)
    if request.method == 'POST':
        rmr.Quarter = request.POST.get('rmrQR')
        rmr.year = request.POST.get('rmrYR')
        rmr.hone = request.POST.get('rmrhone')
        rmr.h_two = request.POST.get('rmrh_two')
        rmr.h_three = request.POST.get('rmrh_three')
        rmr.h_four = request.POST.get('rmrh_four')
        rmr.h_five = request.POST.get('rmrh_five')
        rmr.h_six = request.POST.get('rmrh_six')
        rmr.save()
        messages.success(request, 'Successfully Updated')
        return redirect('ews_app:roadList')
    context = {
        'rmr': rmr
    }
    return render(request, 'ews_app/edit_rmrt.html', context)


def deleteRoadmapRight2(request, pk):
    rmr = RoadmapR2.objects.get(id=pk)
    if request.method == 'POST':
        rmr.delete()
        return redirect('ews_app:roadList')
    context = {
        'rmr': rmr
    }
    return render(request, 'ews_app/delete_rmrt.html', context)



def RoadmapLeft2(request):
    if request.method == 'POST':
        rml = RoadmapL2()
        rml.Quarter = request.POST.get('rml_QR')
        rml.year = request.POST.get('rml_YR')
        rml.hone = request.POST.get('rml_hone')
        rml.h_two = request.POST.get('rml_h_two')
        rml.h_three = request.POST.get('rml_h_three')
        rml.h_four = request.POST.get('rml_h_four')
        rml.h_five = request.POST.get('rml_h_five')
        rml.h_six = request.POST.get('rml_h_six')
        rml.save()
        messages.success(request, 'Successfully Added')
        return redirect('ews_app:roadList')
    return render(request, 'ews_app/create_rmlt.html')


def EditRoadmapLeft2(request, pk):
    rmr = RoadmapL2.objects.get(id=pk)
    if request.method == 'POST':
        rmr.Quarter = request.POST.get('rmrQR')
        rmr.year = request.POST.get('rmrYR')
        rmr.hone = request.POST.get('rmrhone')
        rmr.h_two = request.POST.get('rmrh_two')
        rmr.h_three = request.POST.get('rmrh_three')
        rmr.h_four = request.POST.get('rmrh_four')
        rmr.h_five = request.POST.get('rmrh_five')
        rmr.h_six = request.POST.get('rmrh_six')
        rmr.save()
        messages.success(request, 'Successfully Updated')
        return redirect('ews_app:roadList')
    context = {
        'rmr': rmr
    }
    return render(request, 'ews_app/edit_rmlt.html', context)


def deleteRoadmapLeft2(request, pk):
    rmr = RoadmapL2.objects.get(id=pk)
    if request.method == 'POST':
        rmr.delete()
        return redirect('ews_app:roadList')
    context = {
        'rmr': rmr
    }
    return render(request, 'ews_app/delete_rmlt.html', context)


# ROADMAP Ends Here ======================>>


# TOKENIZE sTARTs Here ======================>>
def Tokenize(request):
    a = TK.objects.all()
    # b = tokenVideo.objects.all()
    context = {
        'a': a,
        # 'b': b
    }
    return render(request, 'ews_app/tk.html', context)


def TokenCreate(request):
    if request.method == 'POST':
        tk = TK()
        tk.title = request.POST.get('title')
        tk.speech = request.POST.get('speech')
        tk.save()
        messages.success(request, 'Successfully Added')
        return redirect('ews_app:token')
    return render(request, 'ews_app/create_tk.html')


# def tokenVid(request):
#     if request.method == 'POST':
#         tkv = tokenVideo()
#         if len(request.FILES) != 0:
#             tkv.video = request.FILES['video']
#         tkv.save()
#         messages.success(request, 'Successfully Added')
#         return redirect('ews_app:token')
#     return render(request, 'ews_app/create_tkv.html')


def editToken(request, pk):
    prod = TK.objects.get(id=pk)

    if request.method == 'POST':
        prod.title = request.POST.get('title')
        prod.speech = request.POST.get('speech')
        prod.save()
        messages.success(request, 'Successfully UPDATED')
        return redirect('ews_app:token')
    context = {
        'prod': prod,
    }
    return render(request, 'ews_app/edit_token.html', context)


def deleteTokenHome(request, token_pk):
    tkk = TK.objects.get(id=token_pk)
    if request.method == 'POST':
        tkk.delete()
        return redirect('ews_app:token')
    context = {
        'ttk': tkk,
    }
    return render(request, 'ews_app/delete_token.html', context)


# TOKENIZE Ends Here ======================>>


# FAQ Starts Here ======================>>
def AdminFaq(request):
    a = FAQ.objects.all()
    context = {
        'a': a
    }
    return render(request, 'ews_app/adminfaq.html', context)


def CreateAdminFaq(request):
    if request.method == 'POST':
        fq = FAQ()
        fq.question = request.POST.get('question')
        fq.answer = request.POST.get('answer')
        fq.save()
        messages.success(request, 'Successfully Added')
        return redirect('ews_app:faq-admin')
    return render(request, 'ews_app/create_faq.html')


def editFaq(request, pk):
    prod = FAQ.objects.get(id=pk)
    if request.method == 'POST':
        prod.question = request.POST.get('question')
        prod.answer = request.POST.get('answer')
        prod.save()
        messages.success(request, 'Successfully UPDATED')
        return redirect('ews_app:faq-admin')
    context = {
        'prod': prod,
    }
    return render(request, 'ews_app/edit_faq.html', context)


def deleteFaq(request, pk):
    fq = FAQ.objects.get(id=pk)
    if request.method == 'POST':
        fq.delete()
        return redirect('ews_app:faq-admin')
    context = {
        'item': fq,
    }
    return render(request, 'ews_app/delete_faq.html', context)


# FAQ Ends Here ======================>>


# Contact Admin Starts Here ======================>>


def contactAdmin(request):
    cont = Contact.objects.all()
    context = {
        'cont': cont
    }
    return render(request, 'ews_app/contact_admin.html', context)


def deleteContact(request, pk):
    cont = Contact.objects.get(id=pk)
    if request.method == 'POST':
        cont.delete()
        return redirect('ews_app:contactAdmin')
    context = {
        'item': cont,
    }
    return render(request, 'ews_app/delete_contact.html', context)


# Contact Admin Ends Here ======================>>

# Authenticated  Admin starts Here ======================>>


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']

            # LOG IN USER
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Welcome {username} You have Successfully Registered')
            return redirect('ews_app:ad-hm')
    return render(request, 'ews_app/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have been Successfully Logged in ")
            return redirect('ews_app:ad-hm')
        else:
            messages.success(request, "There was an Error logging in. Please Try Again!...")
            return redirect('ews_app:login')

    else:
        return render(request, 'ews_app/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been Logged Out....')
    return redirect('ews_app:index')


# Authenticated  Admin starts Here ======================>>


def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        # if request.method == 'POST':
        #     current_user_profile = request.user.profile

        adeoye = {
            'profile': profile,
            # 'current_user_profile': current_user_profile

        }

        return render(request, 'ews_app/profile.html', adeoye)
    else:
        messages.success(request, "You Must be Logged In to View this User Profile")
        return redirect('ews_app:home')


from django.contrib.auth.models import User


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)

        # Get Forms
        user_form = SignUpForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid and profile_form.is_valid():  #
            user_form.save()
            if len(request.FILES) != 0:
                profile_user.profile_image = request.FILES['profile_image']
            profile_form.save()
            login(request, current_user)
            messages.success(request, "You Profile has been Updated")
            return redirect("ews_app:ad-hm")

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, 'ews_app/update_user.html', context)

    else:
        messages.success(request, "You must be Logged in")
        return redirect("ews_app:home")
