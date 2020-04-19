# Generated by Django 3.0.5 on 2020-04-19 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('root', '0002_auto_20200418_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('postbaseinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='root.PostBaseInfo')),
            ],
            bases=('root.postbaseinfo',),
        ),
        migrations.CreateModel(
            name='ArticleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_content', models.TextField(blank=True)),
                ('formatted_content', models.TextField()),
                ('add_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('article_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='article.ArticleInfo')),
            ],
        ),
    ]
