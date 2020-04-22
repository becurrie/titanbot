# Generated by Django 2.2.10 on 2020-04-22 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titandash', '0045_globalsettings_rate_screen_checks_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalsettings',
            name='pihole_ads_settings',
            field=models.CharField(choices=[('on', 'On'), ('off', 'Off')], default='off', help_text="Enable or disable the ability to watch and collect ads without vip while using pihole to prevent ads from running within tap titans 2. This allows users to basically get the benefits of VIP, without a VIP enabled account. <strong>Note:</strong> This setting will only work if you have properly installed and setup a <a href='https://pi-hole.net/'>pihole</a> server. Titandash does <strong>not</strong> handle this process for you.", max_length=255, verbose_name='Enable PI-Hole Ads'),
        ),
    ]
