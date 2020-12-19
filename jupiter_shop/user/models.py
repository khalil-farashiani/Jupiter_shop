from django.db import models
from django.contrib.auth.models import User



# from django.db.models.signals import pre_save
# from django.dispatch.dispatcher import receiver

# @receiver(pre_save,sender= Profile)
# def create_user_before_profile_saves(instance,*args, **kwargs):
#     try:
#         user = User.objects.create(username = f'{instance.ful_name} - {instance.phonenumber}',password=instance.password) 
#         instance.id = user
#     except Exception:
#         raise Exception



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.RESTRICT,primary_key=True,blank=True)
    password = models.CharField(max_length=128,blank=True, null=True)
    ful_name = models.CharField(max_length=40, null=False)

    phonenumber = models.CharField(max_length=12, null=False,unique=True)
    address = models.OneToOneField(
        'address.Address', on_delete=models.SET_NULL, null=True,blank=True)
    postal_code = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='./res/profile_photo',blank=True, null=True)

    USER_TYPE = [("A", 'customer'), ("B", 'staff')]
    user_join_date = models.DateField(auto_now_add=True)
    user_type = models.CharField(max_length=1, choices=USER_TYPE, default="A")

    user_last_login = models.DateTimeField(auto_now_add = True,blank=True, null=True)

    
    # def save(self, force_insert: bool, force_update: bool, using: Optional[str], update_fields: Optional[Iterable[str]]) -> None:
    #     return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def save(self,*args, **kwargs):
        
        try:
            is_staff = False
            if not self.password:
                password = User.objects.make_random_password()
                print(password)
            else:
                password = self.password
            
            if self.user_type== 'B':
                is_staff = True
            

            user = User.objects.create(username = f'{self.ful_name} - {self.phonenumber}',password=password, is_staff= is_staff) 
            self.user_id = user
        except Exception as e:
            raise e
        return super().save(*args, **kwargs)

    # def update_user_login_date(sender,*args, **kwargs):
        

    def __str__(self):
        if self.ful_name:
            return f'{self.ful_name} - {self.phonenumber}'
        else:
            return str(self.id)

# class User(models.Model):
#     user_id = models.OneToOneField(User,on_delete=models.RESTRICT,primary_key=True)
#     phonenumber = models.IntegerField(null=False)
#     passcode = models.CharField(max_length=64, null=False)
#     User_Type = [("A", 'user'), ("B", 'staff')]
#     user_type = models.CharField(max_length=1, choices=User_Type, default="A")
#     profile = models.ForeignKey(
#         Profile, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)

#     def __str__(self):
#         if self.profile:
#             return str(self.profile)
#         else:
#             return str(f'{self.id} - {self.phonenumber}')

#     def save(self,*args, **kwargs):
#             if 
#         return super().save(args, kwargs)

