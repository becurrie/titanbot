# Generated by Django 2.2.8 on 2019-12-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titandash', '0036_fix_artifact_purchase_help_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalsettings',
            name='pihole_ads_settings',
            field=models.CharField(choices=[('on', 'On'), ('off', 'Off')], default='off', help_text='Enable or disable the ability to watch and collect ads without vip while using pihole to prevent ads from running within tap titans 2. This allows users to basically get the benefits of VIP, without a VIP enabled account.', max_length=255, verbose_name='Enable PI-Hole Ads'),
        ),
    ]
