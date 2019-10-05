# Generated by Django 2.2.5 on 2019-10-03 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titandash', '0015_configuration_enable_artifact_discover_enchant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='botstatistics',
            name='premium_ads',
        ),
        migrations.AddField(
            model_name='botstatistics',
            name='ads',
            field=models.PositiveIntegerField(default=0, help_text='How many ads have been earned and tracked by the bot.', verbose_name='Premium Ads'),
        ),
    ]