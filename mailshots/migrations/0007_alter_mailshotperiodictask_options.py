# Generated by Django 5.0.4 on 2024-04-24 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailshots', '0006_client_unique_client_for_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailshotperiodictask',
            options={'ordering': ['-created_at'], 'permissions': [('can_disable', 'can disable mailshots')], 'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
    ]