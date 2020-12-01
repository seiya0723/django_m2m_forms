from django.db import models
import uuid


class Category(models.Model):
    class Meta:
        db_table    = "category"

    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(verbose_name="カテゴリ名",max_length=10)

    def __str__(self):
        return self.name

class Allergy(models.Model):
    class Meta:
        db_table    = "allergy"

    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(verbose_name="アレルギー名",max_length=10)

    def __str__(self):
        return self.name

class Menu(models.Model):
    class Meta:
        db_table    = "menu"

    category    = models.ForeignKey(Category,verbose_name="カテゴリ名",on_delete=models.PROTECT)
    name        = models.CharField(verbose_name="品名",max_length=20)
    breakfast   = models.BooleanField(verbose_name="朝メニュー",default=True)
    lunch       = models.BooleanField(verbose_name="昼メニュー",default=True)
    dinner      = models.BooleanField(verbose_name="夜メニュー",default=True)
    takeout     = models.BooleanField(verbose_name="テイクアウト",default=True)
    price       = models.IntegerField(verbose_name="価格")
    allergy     = models.ManyToManyField(Allergy,verbose_name="含むアレルギー",blank=True)

    def __str__(self):
        return self.name



