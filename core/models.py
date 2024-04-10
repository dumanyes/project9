from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

CATEGORY_CHOICES = [
    ('featured', 'Избранные'),
    ('politics', 'Политика'),
    ('business_economy', 'Бизнес и экономика'),
    ('culture', 'Культура'),
    ('technology', 'Технологии'),
    ('sports', 'Спорт'),
    ('education', 'Образование'),
    ('environment', 'Окружающая среда'),
    ('travel_tourism', 'Путешествия и туризм'),
    ('local_news', 'Местные новости'),
    ('international_news', 'Мировые новости'),
]

class Category(models.Model):
    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.get_name_display()

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок поста')
    categories = models.ManyToManyField(Category, verbose_name='Категории')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    body = RichTextUploadingField(verbose_name='Содержание поста')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
