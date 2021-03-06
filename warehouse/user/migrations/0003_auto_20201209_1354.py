# Generated by Django 3.1 on 2020-12-09 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201209_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Categories name')),
                ('status', models.BooleanField(verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Categories name')),
                ('status', models.BooleanField(verbose_name='status')),
                ('all_categories', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user.all_categories')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categoriya_id',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='user.categories'),
            preserve_default=False,
        ),
    ]
