# Generated by Django 3.0.5 on 2020-04-18 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0002_auto_20200418_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloggerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('desc', models.CharField(default='', max_length=300)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='base/avatar/image/%y/%m')),
                ('background', models.ImageField(blank=True, null=True, upload_to='base/background/image/%y/%m')),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NavigationLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='base/friendlink/image/%y/%m')),
                ('url', models.CharField(max_length=200)),
                ('target', models.CharField(blank=True, choices=[('_blank', 'Next Page'), ('_self', 'in same Frame'), ('_parent', 'parent'), ('_top', 'top')], max_length=10, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('desc', models.CharField(default='', max_length=150)),
                ('keywords', models.CharField(default='', max_length=300)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='base/site/image/%y/%m')),
                ('background', models.ImageField(blank=True, null=True, upload_to='base/site/image/%y/%m')),
                ('api_base_url', models.URLField(max_length=30)),
                ('copyright', models.CharField(default='', max_length=100)),
                ('copyright_desc', models.CharField(default='', max_length=300)),
                ('icp', models.CharField(default='', max_length=20)),
                ('is_live', models.BooleanField(default=False)),
                ('is_force_refresh', models.BooleanField(default=False)),
                ('force_refresh_time', models.DateTimeField(blank=True, null=True)),
                ('access_password', models.CharField(blank=True, max_length=20, null=True)),
                ('access_password_encrypt', models.CharField(blank=True, max_length=100, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfoNavigation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('index', models.IntegerField(default=0)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('navigation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.NavigationLink')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.SiteInfo')),
            ],
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='navigations',
            field=models.ManyToManyField(through='base.SiteInfoNavigation', to='base.NavigationLink'),
        ),
        migrations.CreateModel(
            name='BloggerSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('index', models.IntegerField(default=0)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.BloggerInfo')),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.Social')),
            ],
        ),
        migrations.CreateModel(
            name='BloggerMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('index', models.IntegerField(default=0)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('blogger', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.BloggerInfo')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='root.Master')),
            ],
        ),
        migrations.AddField(
            model_name='bloggerinfo',
            name='masters',
            field=models.ManyToManyField(through='base.BloggerMaster', to='root.Master'),
        ),
        migrations.AddField(
            model_name='bloggerinfo',
            name='socials',
            field=models.ManyToManyField(through='base.BloggerSocial', to='root.Social'),
        ),
    ]
