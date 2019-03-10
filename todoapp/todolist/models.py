from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model): #this category table name that inherits model.Model
    name = models.CharField(max_length=100) #like a varchar
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name #name to be shown when called

class TodoList(models.Model): #todolist able name that inherits models.Model
    title = models.CharField(max_length=250) # a varchar
    content = models.TextField(blank=True) # a text field
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) #a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # date
    category = models.ForeignKey(Category, default="general", on_delete=models.CASCADE) # this is a foreignkey

    class Meta:
        ordering = ["-created"] #order by the created field

    def __str__(self):
        return self.title # name to be shown when called

