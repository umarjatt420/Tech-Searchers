# Generated by Django 4.2.4 on 2023-09-13 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('AI', 'Artificial Intelligence'), ('IT', 'Information Technology'), ('CN', 'Computer Network'), ('PROGRAMMING', 'Programming'), ('Operating System', 'Operating Systems'), ('ROBOTICS', 'Robotics'), ('QC', 'Quantum Computing'), ('DS', 'Data Science'), ('AUTOMATION', 'Automation'), ('VR', 'Virtual Reality')], default=None, max_length=20),
        ),
    ]
