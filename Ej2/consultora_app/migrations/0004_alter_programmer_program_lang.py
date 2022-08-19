# Generated by Django 4.1 on 2022-08-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultora_app', '0003_alter_programmer_email_alter_programmer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmer',
            name='program_lang',
            field=models.CharField(blank=True, choices=[('js', 'Javascript'), ('python', 'Python'), ('c', 'C'), ('java', 'Java'), ('php', 'PHP')], max_length=32),
        ),
    ]
