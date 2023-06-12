from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
                                     related_name="followed_by",
                                     symmetrical=False,
                                     blank=True)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

        # Have User follow themselves
        # user_profile.follows.set([instance.profile.id])
        # user_profile.save()


post_save.connect(create_profile, sender=User)


# Homepage Start HEre
class Welcome(models.Model):
    wel_title = models.CharField('WELCOME SPEECH TITLE', max_length=77)
    wel_speech = models.TextField('WELCOME SPEECH')

    def __str__(self):
        return self.wel_title


class HomeSecondSection(models.Model):
    title = models.CharField('SECOND TITLE', max_length=77)
    speech = models.TextField('SECOND SPEECH')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'INVESTMENT SPEECH'


class HomeThird(models.Model):
    img = models.ImageField(upload_to='home')
    title = models.CharField('SECOND SPEECH', max_length=77)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'SHACKLES'


# Home Ends Here ======================>>


class Team(models.Model):
    img = models.ImageField(upload_to='team')
    name = models.CharField(max_length=77)
    des = models.CharField('DESIGNATION', max_length=77)
    fb_URL = models.URLField('FACEBOOK URL', blank=True, null=True)
    tw_URL = models.URLField('TWITTER URL', blank=True, null=True)
    lk_URL = models.URLField('LINKEDIN URL', blank=True, null=True)
    insta_URL = models.URLField('INSTAGRAM URL', blank=True, null=True)

    def __str__(self):
        return self.name


class TK(models.Model):
    title = models.CharField(max_length=35)
    speech = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'TOKENIZE'


class RoadMap(models.Model):
    title = models.CharField(max_length=77)
    speech = models.TextField()

    def __str__(self):
        return self.title


class RoadmapR1(models.Model):
    hone = models.CharField(max_length=77)
    h_two = models.CharField(max_length=77, blank=True, null=True)
    h_three = models.CharField(max_length=77, blank=True, null=True)
    h_four = models.CharField(max_length=77, blank=True, null=True)
    h_five = models.CharField(max_length=77, blank=True, null=True)
    h_six = models.CharField(max_length=77, blank=True, null=True)
    Quarter = models.CharField(max_length=3)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.Quarter


class RoadmapL1(models.Model):
    hone = models.CharField(max_length=77)
    h_two = models.CharField(max_length=77, blank=True, null=True)
    h_three = models.CharField(max_length=77, blank=True, null=True)
    h_four = models.CharField(max_length=77, blank=True, null=True)
    h_five = models.CharField(max_length=77, blank=True, null=True)
    h_six = models.CharField(max_length=77, blank=True, null=True)
    Quarter = models.CharField(max_length=3)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.Quarter


class RoadmapR2(models.Model):
    hone = models.CharField(max_length=77)
    h_two = models.CharField(max_length=77, blank=True, null=True)
    h_three = models.CharField(max_length=77, blank=True, null=True)
    h_four = models.CharField(max_length=77, blank=True, null=True)
    h_five = models.CharField(max_length=77, blank=True, null=True)
    h_six = models.CharField(max_length=77, blank=True, null=True)
    Quarter = models.CharField(max_length=3)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.Quarter


class RoadmapL2(models.Model):
    hone = models.CharField(max_length=77)
    h_two = models.CharField(max_length=77, blank=True, null=True)
    h_three = models.CharField(max_length=77, blank=True, null=True)
    h_four = models.CharField(max_length=77, blank=True, null=True)
    h_five = models.CharField(max_length=77, blank=True, null=True)
    h_six = models.CharField(max_length=77, blank=True, null=True)
    Quarter = models.CharField(max_length=3)
    year = models.CharField(max_length=4)

    def __str__(self):
        return self.Quarter


class News(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    h2 = models.CharField(max_length=77)
    p1 = models.TextField('First Paragraph')
    p2 = models.TextField('Second Paragraph')
    document = models.FileField('WHITEPAPER', upload_to='media/pdf')

    def __str__(self):
        return self.h2


class FAQ(models.Model):
    question = models.CharField(max_length=77)
    answer = models.TextField()

    def __str__(self):
        return self.question


# class tokenVideo(models.Model):
#     name = models.CharField(max_length=12)
#     video = models.FileField('Video', upload_to='media/video')


#     def __str__(self):
#         return self.video
