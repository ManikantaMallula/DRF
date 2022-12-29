from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

# @receiver(user_logged_in,sender=User)
# def login(sender,request,user,**kwargs):
#     print(".....................")
#     print('logged-in signal')
#     print('sender: ',sender)
#     print('request:',request)
#     print('User: ',user)
#     print("User Password:", user.password)
#     print(f'Kwargs: {kwargs}')




#
# @receiver(user_logged_out, sender=User)
# def logout(sender, request, user, **kwargs):
#  print("----------------------------")
#  print("Logged-out Signal")
#  print("Sender:", sender)
#  print("Request:", request)
#  print("User:", user)
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(user_login_failed)
# def loginfailed(sender, credentials, request, **kwargs):
#  print("----------------------------")
#  print("Login Failed Signal")
#  print("Sender:", sender)
#  print("Credentials:", credentials)
#  print("Request:", request)
#  print(f'Kwargs: {kwargs}')
# # user_login_failed.connect(login_failed)
#
# @receiver(pre_save, sender=User)
# def atbeginningsave(sender, instance, **kwargs):
#  print("----------------------------")
#  print("Pre Save Signal")
#  print("Sender:", sender)
#  print("Instance:", instance)
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(post_save, sender=User)
# def atendingsave(sender, instance, created, **kwargs):
#  if created:
#   print("----------------------------")
#   print("Post Save Signal")
#   print("New Record")
#   print("Sender:", sender)
#   print("Instance:", instance)
#   print("Created:", created)
#   print(f'Kwargs: {kwargs}')
#  else:
#   print("--------------------------")
#   print("Post Save Signal")
#   print("Update")
#   print("Sender:", sender)
#   print("Instance:", instance)
#   print("Created:", created)
#   print(f'Kwargs: {kwargs}')
#
#
# @receiver(pre_delete, sender=User)
# def atbeginningdelete(sender, instance, **kwargs):
#  print("-----------------------------------")
#  print("Pre Delete Signal")
#  print('Sender:', sender)
#  print('Instance:', instance)
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(post_delete, sender=User)
# def atendingdelete(sender, instance, **kwargs):
#  print("----------------------------------")
#  print("Post Delete Signal")
#  print('Sender:', sender)
#  print('Instance:', instance)
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(pre_init, sender=User)
# def atbeginninginit(sender, *args, **kwargs):
#  print("-----------------------------------------")
#  print("Pre Init Signal......")
#  print('Sender:', sender)
#  print(f'Args: {args}')
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(post_init, sender=User)
# def atendinginit(sender, *args, **kwargs):
#  print("----------------------------")
#  print("Post Init Signal..")
#  print('Sender:', sender)
#  print(f'Args: {args}')
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(request_started)
# def atbeginningrequest(sender, environ, **kwargs):
#  print("-----------------------------------------")
#  print("At Beginning Request.")
#  print('Sender:', sender)
#  print('Environ:', environ)
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(request_finished)
# def atendingrequest(sender, **kwargs):
#  print("-----------------------------------------")
#  print("At Ending Request")
#  print('Sender:', sender)
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(got_request_exception)
# def atreqexception(sender, request, **kwargs):
#  print("-----------------------------------------")
#  print("At Request Exception......")
#  print('Sender:', sender)
#  print('Request:', request)
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(pre_migrate)
# def beforeinstallapp(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
#  print("-----------------------------------------")
#  print("before_install_app......")
#  print('Sender:', sender)
#  print('App_config:', app_config)
#  print('Verbosity:', verbosity)
#  print('Interactive:', interactive)
#  print('Using:', using)
#  print('Plan:', plan)
#  print('App:', apps)
#  print(f'Kwargs: {kwargs}')
#
#
# @receiver(post_migrate)
# def atendmigrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
#  print("-----------------------------------------")
#  print("at_end_migrate_flush......")
#  print('Sender:', sender)
#  print('App_config:', app_config)
#  print('Verbosity:', verbosity)
#  print('Interactive:', interactive)
#  print('Using:', using)
#  print('Plan:', plan)
#  print('App:', apps)
#  print(f'Kwargs: {kwargs}')
#
#
@receiver(connection_created)
def conndb(sender, connection, **kwargs):
 print("-----------------------------------------")
 print("Initial connection to the database......")
 print('Sender:', sender)
 print('Connection:', connection)
 print(f'Kwargs: {kwargs}')

