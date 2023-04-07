# Generated by Django 4.1.1 on 2023-02-11 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products_module', '0001_initial'),
        ('user_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_push', models.BooleanField(default=True, verbose_name='Send Push')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_settings', to='products_module.currency', verbose_name='Currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_settings', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
