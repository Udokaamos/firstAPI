# Generated by Django 3.2.11 on 2022-02-07 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_playlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='date_created',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='date_created',
            new_name='date_added',
        ),
        migrations.RemoveField(
            model_name='song',
            name='publish_date',
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('pop', 'POP'), ('blues', 'Blues'), ('rap', 'Rap'), ('afro_beat', 'Afro beat'), ('gospel', 'Gospel')], default=django.utils.timezone.now, max_length=355),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='main.song'),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
