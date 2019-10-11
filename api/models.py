from django.db import models
from django.core.validators import validate_email, validate_ipv4_address, MinLengthValidator

class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, validators=[validate_email])
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])

class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.CharField(max_length=39, validators=[validate_ipv4_address])

class Event(models.Model):
    CHOICES = (
        ('C', 'CRITICAL'),
        ('D','DEBUG'),
        ('E','ERROR'),
        ('W', 'WARNING'),
        ('I', 'INFO')
    )
    level = models.CharField(max_length=20, choices=CHOICES)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.deletion.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING)

class Group(models.Model):
    name = models.CharField(max_length=50)

class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.deletion.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.deletion.DO_NOTHING)