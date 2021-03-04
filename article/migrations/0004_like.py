# Generated by Django 3.1.7 on 2021-03-03 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20210303_1310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.post')),
            ],
            options={
                'unique_together': {('post', 'session_key')},
            },
        ),
    ]