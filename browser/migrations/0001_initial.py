# Generated by Django 2.0.2 on 2018-05-08 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category', models.CharField(max_length=64, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CategorySimilarityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Category')),
                ('category2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category2', to='browser.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('displayName', models.CharField(max_length=128)),
                ('previewImgPath', models.FilePathField()),
                ('textExtract', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='DashMatchedCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoreDMC', models.IntegerField()),
                ('categoryDMC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Category')),
                ('dashboardDMC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Dashboard')),
            ],
        ),
        migrations.CreateModel(
            name='PinnedDashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboardPD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Dashboard')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=64)),
                ('prefTheme', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserMatchedCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scoreUMC', models.IntegerField()),
                ('favourited', models.BooleanField(default=False)),
                ('categoryUMC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.Category')),
                ('usernameUMC', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.User')),
            ],
        ),
        migrations.AddField(
            model_name='pinneddashboard',
            name='usernamePD',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browser.User'),
        ),
    ]
