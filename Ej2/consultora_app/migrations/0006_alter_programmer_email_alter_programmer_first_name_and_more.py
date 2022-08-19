# Generated by Django 4.1 on 2022-08-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultora_app', '0005_alter_programmer_email_alter_programmer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='programmer',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='programmer',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='programmer',
            name='nick',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='programmer',
            name='program_lang',
            field=models.CharField(blank=True, choices=[('js', 'Javascript'), ('python', 'Python'), ('c', 'C'), ('java', 'Java'), ('php', 'PHP')], max_length=32),
        ),
    ]
