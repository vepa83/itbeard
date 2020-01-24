from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(default='special')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    

class Post(models.Model):
    
    KINDS = (
        ('abo', 'About'),
        ('pst', 'Post'),
        ('con', 'Contact'),
    )
    
    kind = models.CharField(max_length=3, choices=KINDS, default='pst')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    link = models.CharField(max_length=255, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    picture = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ImageSpecField( source='picture',
                                processors=[ResizeToFill(120, 120)],
                                format='JPEG',
                                options={'quality': 80}
                            )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(models.Model):
    STATUSES = (
        ('pen', 'Pending'),
        ('pub', 'Published'),
        ('rem', 'Removed'),
    ) 
    status = models.CharField(max_length=3, choices=STATUSES, default='pen')
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class Welcome(models.Model):
    title = models.CharField(max_length=50, default="welcome_title")
    text = RichTextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'welcome text'
        verbose_name_plural = 'welcome texts'


class Menu(models.Model):
    name = models.CharField(max_length=25)
    is_category = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'
