from django.db import models

class Books(models.Model):
    title=models.CharField('Заголовок',max_length=100)
    subtitle=models.CharField('Подзаголовок',max_length=100)
    description=models.TextField('Описание')

    price=models.CharField('Цена',max_length=100)
    genre=models.CharField('Жанр',max_length=20)
    author=models.CharField('Автор',max_length=20)

    year=models.CharField('Год издания',max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    is_favorite=models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Create your models here.
