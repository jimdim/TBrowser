from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128, primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=64)
    prefTheme = models.PositiveSmallIntegerField()

class Dashboard(models.Model):
    displayName = models.CharField(max_length=128)
    previewImgPath = models.ImageField(upload_to='dash')
    textExtract = models.CharField(max_length=255)
    url = models.URLField()

class Category(models.Model):
    category = models.CharField(max_length=64, primary_key=True)

class PinnedDashboard(models.Model):
    usernamePD = models.ForeignKey('User', on_delete=models.CASCADE)
    dashboardPD = models.ForeignKey('Dashboard', on_delete=models.CASCADE)

class UserMatchedCategory(models.Model):
    usernameUMC = models.ForeignKey('User', on_delete=models.CASCADE)
    categoryUMC = models.ForeignKey('Category', on_delete=models.CASCADE)
    scoreUMC = models.IntegerField()
    favourited = models.BooleanField(default=False)

class DashMatchedCategory(models.Model):
    dashboardDMC = models.ForeignKey('Dashboard', on_delete=models.CASCADE)
    categoryDMC = models.ForeignKey('Category', on_delete=models.CASCADE)
    scoreDMC = models.IntegerField()

class CategorySimilarityCategory(models.Model):
    category1 = models.ForeignKey('Category', on_delete=models.CASCADE)
    category2 = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category2')
