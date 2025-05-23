# Generated by Django 5.1.5 on 2025-04-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0006_alter_users_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='op_team',
            field=models.TextField(default='Unknown team', max_length=100),
        ),
        migrations.AddField(
            model_name='match',
            name='our_team',
            field=models.TextField(default='Polyal Suqad'),
        ),
        migrations.AddField(
            model_name='players',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='player_photo'),
        ),
        migrations.AddField(
            model_name='users',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
