from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank =True,null=True)
    updated_at = models.DateTimeField(auto_now=True,blank =True,null=True)
    # is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class MainPage(TimeStamp):
    '''hold home pae set up variables for sohyo website'''
    titleup = models.CharField(
        max_length=100,
        default='Healthy,Developed',
        blank=True, null=True)

    titledown = models.CharField(
        max_length=100,
        default='and focused community.',
        blank=True, null=True)

    small_description = models.TextField(max_length=200,default='Vision: To Create a healhy and focused community.', blank=True, null=True)
    donate = models.CharField(max_length=100,default="Donate", blank=True, null=True)
    mobile_no = models.CharField(max_length=100,default="+254 722 259 264", blank=True, null=True)
    email = models.EmailField(max_length=100,default="sohyo.sohyo@gmail.com", blank=True, null=True)
    address = models.CharField(max_length=100,default="P O BoX 94 Mulot,Bomet", blank=True, null=True)

    what_we_are_doing = models.CharField(max_length=300,default="Our Mission", blank=True, null=True)

    mission1 = models.CharField(max_length=300,default="Protect Youth's Heath", blank=True, null=True)
    mission1_desc = models.TextField(
        max_length=300,
        default="* Fight against drugs and substance abuse among the youth.* Promote youth 's health  through reproductive education & HIV/AIDS awareness.* Guidance & counselling to the youth.",
        blank=True, null=True)

    mission2 = models.CharField(max_length=300,default="Promote Career,Talent & Skills", blank=True, null=True)
    mission2_desc = models.TextField(
        max_length=300,
        default="*Promote capacity building on entrepreneurship skills .*Empowers and enhance leadership skills", blank=True, null=True)

    mission4 = models.CharField(max_length=300,default="Environmental Conservation", blank=True, null=True)
    mission4_desc = models.TextField(
        max_length=300,
        default="*Planting trees in public places which include schools,churches etc.", blank=True, null=True)

    about_our_foundation_header = models.CharField(max_length=300,default="About the Organization", blank=True, null=True)
    about_our_foundation_sub_header = models.CharField(max_length=300,default="Our Mission", blank=True, null=True)
    about_our_foundation_desc1 = models.TextField(
        max_length=300,
        default="To equip the young people with life skills and impact knowledge to promote health and development in achieving their full physical ,intellectual,morals and social potential as members of the community.",
        blank=True, null=True)
    about_our_foundation_desc2 = models.TextField(max_length=300,default="", blank=True, null=True)

    exlore_causes = models.CharField(max_length=300,default="Explore Our Latest Causes", blank=True, null=True)
    events_plans = models.CharField(max_length=300,default="We arrange many social events for charity", blank=True, null=True)
    dev_mobile = models.CharField(max_length=300,default="-0712 478 566", blank=True, null=True)

    change = models.CharField(max_length=300,default="At SOHYO We Serve To Save", blank=True, null=True)

    active = models.BooleanField(default=False, blank=True, null=True)
    about1_image= models.ImageField(upload_to='images/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    about2_image= models.ImageField(upload_to='images/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
class Common(TimeStamp):
    '''hold footer and header settup for sohyo website'''

    mobile_no = models.CharField(
        max_length=100,
        default="+254 722 259 264",
        blank=True, null=True)

    email = models.EmailField(
        max_length=100,
        default="sohyo.sohyo@gmail.com",
        blank=True, null=True)

    address = models.CharField(
        max_length=100,
        default="P O BoX 94 Mulot,Bomet ,Nairobi -Kenya",
        blank=True, null=True)
    
    newsletter = models.CharField(
        max_length=300,
        default="Newsletter",
        blank=True, null=True)

    newsletter_dec = models.TextField(
        max_length=300,
        default="Subsctibe to our newsletter to get updated\
             on our current events.We love seeing around.",
        blank=True, null=True)

    twitter = models.URLField(
        max_length=100,
        default="http://www.twitter.com/",
        blank=True, null=True)

    facebook = models.URLField(
        max_length=100,
        default="https://www.facebook.com/",
        blank=True, null=True)

    instagram = models.URLField(
        max_length=100,
        default="http://www.instagram.com/",
        blank=True, null=True)

    youtube = models.URLField(
        max_length=100,
        default="http://www.youtube.com/",
        blank=True, null=True)

    linkedin = models.URLField(
        max_length=100,
        default="http://www.linkedin.com/",
        blank=True, null=True)

    google_plus = models.URLField(
        max_length=100,
        default="http://www.google_plus.com/",
        blank=True, null=True)

    town = models.CharField(
        max_length=300,
        default="Mulot",
        blank=True, null=True)

    disrict = models.CharField(
        max_length=300,
        default="Nairobi",
        blank=True, null=True)

    street = models.CharField(
        max_length=300,
        default="Mulot-Sunset , Kipsete BLD",
        blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    title = models.CharField(max_length=300,default="Fit Druds", blank=True, null=True)
    startime =models.DateTimeField(blank=True, null=True)
    
    endtime =models.DateTimeField(blank=True, null=True)

    date =models.DateField(blank=True, null=True)
    venuetitle= models.CharField(max_length=300,default="Bomet", blank=True, null=True)

    town=models.CharField(max_length=300,default="Bomet", blank=True, null=True) 

    donate = models.CharField(max_length=100,default="Donate", blank=True, null=True) 
    event_header =  models.CharField(max_length=300,default="We Arrange Many Social Events to promote our mission", blank=True, null=True)   

    def __str__(self):
        return 'Footer & header Setup'

class Cause(TimeStamp):
    image = models.ImageField(upload_to='images/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    # image = models.FileField(upload_to='files/%Y/%m/%d/') #max_length=2000,blank=True ,null =True
    description = models.TextField(max_length=400,default="Soyo :Ensure Education For Every Poor Children", blank=True, null=True)
    donation_progress = models.FloatField(blank=True, null=True)
    raised = models.DecimalField(max_digits=12, decimal_places=2,default=1,blank =True,null=True)
    goal = models.DecimalField(max_digits=12, decimal_places=2,default=1,blank =True,null=True)

    


    @property
    def donation_prog(self):
        return round(self.raised/self.goal *100,1)


class Event(TimeStamp):    
    # image = models.FileField(upload_to='files/%Y/%m/%d/') #max_length=2000,blank=True ,null =True
    # header = models.TextField(max_length=400,default="We as Soyo Arrange Many Social Events For Charity Donations", blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    description = models.TextField(max_length=400,default="We as Soyo Arrange Many Social Events For Charity Donations", blank=True, null=True)
    startime =models.DateTimeField(blank=True, null=True)    
    endtime =models.DateTimeField(blank=True, null=True)
    date =models.DateField(blank=True, null=True)
    venuetitle= models.CharField(max_length=300,default="Bomet", blank=True, null=True)

    town=models.CharField(max_length=300,default="Bomet", blank=True, null=True) 



class Feedback(TimeStamp):
    message =  models.TextField(max_length=400, blank=True, null=True)
    full_name = models.CharField(max_length=300, blank=True, null=True)
    email =models.EmailField(max_length=300, blank=True, null=True)
    subject = models.CharField(max_length=300, blank=True, null=True)



#Join Us
class User(AbstractUser):
    """Add three fields to existing Django User model.
      : daru_code  and my_code for reference
    """
    JOIN_AS = [
        ('Member', 'member'),
        ('Sponser', 'sponser'),
        ('Volunteer', 'volunteer'),
        ('Others', 'others'),

    ]
    member_type = models.CharField(
        max_length=20,
        choices=JOIN_AS,
        default='Member',
        blank=True, null=True
    )
    others = models.CharField(
        max_length=255,
        help_text='If others specify here',
        blank=True, null=True)

    phone_number = models.CharField(max_length=150, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    @staticmethod
    def format_mobile_no(mobile): # hard coded for kenya # need refactor
        mobile = str(mobile)
        if (
            mobile.startswith("07") or mobile.startswith("01"))\
                and len(mobile) == 10:
            return "254"+mobile[1:]
        elif mobile.startswith("254") and len(mobile) == 12:
            return mobile
        elif (
            mobile.startswith("7") or mobile.startswith("1"))\
                and len(mobile) == 9:
            return "254"+mobile
        else:
            return mobile+"-invalid"

    def save(self, *args, **kwargs):
        try:
            self.phone_number = self.format_mobile_no(self.phone_number)
        except Exception as e:
            print(e)
            pass

        super(User, self).save(*args, **kwargs)



class Leader(TimeStamp):
    image = models.ImageField(upload_to='images/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    name =models.TextField(max_length=200,default="Jon Doe", blank=True, null=True)
    # image = models.FileField(upload_to='files/%Y/%m/%d/') #max_length=2000,blank=True ,null =True
    title = models.CharField(max_length=100,default="Volunteer leader", blank=True, null=True)


class Testimomial(TimeStamp):
    image = models.ImageField(upload_to='images/%Y/%m/%d/',max_length=2000,blank=True ,null =True)
    name =models.CharField(max_length=200,default="Gama'liel", blank=True, null=True)
    # image = models.FileField(upload_to='files/%Y/%m/%d/') #max_length=2000,blank=True ,null =True
    title = models.CharField(max_length=100,default="CEO", blank=True, null=True) 
    description = models.TextField(max_length=300,default="“Stop asking what the country can do  for you ,instead ask what you can do for the country for a better tomorrow.” am at an age where I just want to be fit and healthy our bodies are our responsibility!”", blank=True, null=True)  


class Statistic(TimeStamp):
    value = models.FloatField(default=0)
    type =models.CharField(max_length=50,default="Donation", blank=True, null=True)   