from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    descriptions =models.TextField(
        verbose_name="Описание"
    )
    logo = models.ImageField(
        upload_to="logo",
        verbose_name="Логотип сайта"
    )
    phone = models.CharField(
        max_length=255,
        verbose_name="Тел.номер"
    )
    email = models.EmailField(
        verbose_name="Почта"
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook"
    )
    instagram = models.URLField(
        verbose_name="Ссылка на Instagram"
    )
    youtube = models.URLField(
        verbose_name="Ссылка на Youtube"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = "Настройка"
        
class About(models.Model):
    image = models.ImageField(
        upload_to="about_image",
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    decriptions = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"