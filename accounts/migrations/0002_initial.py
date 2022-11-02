


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('articles', '0001_initial'),
        ('reviews', '0001_initial'),
        ('accounts', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),

    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='like_reviews',
            field=models.ManyToManyField(related_name='like_it', to='reviews.Review'),
        ),
        migrations.AddField(
            model_name='user',
            name='marker',
            field=models.ManyToManyField(related_name='articles', to='articles.Article'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
