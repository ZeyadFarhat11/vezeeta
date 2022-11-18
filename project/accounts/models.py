from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify


# Create your models here.
class Profile(models.Model):
    """Model definition for Profile."""
    user = models.OneToOneField(User,verbose_name='user', on_delete=models.CASCADE)
    name=models.CharField(('الاسم '),max_length=70)
    who_i=models.TextField(('من انا '),max_length=200)
    price=models.IntegerField(('سعر الكشف'),blank=True,null=True)
    image=models.ImageField(("الصوره الشخصيه"), upload_to='profile',blank=True,null=True)
    doctor=models.CharField(('التخصص'),max_length=20)
    Specialist_doctor=models.CharField(("القسم"), max_length=50)
    address=models.CharField(("المحافظه"), max_length=50)
    address_detail=models.CharField(("العنوان بالتفاصيل"), max_length=70)
    Waiting_time =models.IntegerField(("مده الانتظار"))
    working_hours =models.IntegerField(("عدد ساعات العمل"))
    phone = models.CharField(("رقم الهاتف"),max_length=20)
    facebook=models.CharField(("فيس بوك"), max_length=70)
    slug=models.SlugField(("slug"),blank=True,null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = (slugify(self.user.username))
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return '%s' %self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile, sender=User)