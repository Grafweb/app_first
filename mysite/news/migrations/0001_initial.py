from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='news/')),
                ('excerpt', models.TextField(help_text='Short description shown in news listing')),
                ('content', models.TextField()),
                ('published_date', models.DateField()),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-published_date', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='NewsSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_per_page', models.PositiveIntegerField(
                    default=10,
                    help_text='Number of articles per page in the news list',
                )),
            ],
            options={
                'verbose_name': 'News Settings',
                'verbose_name_plural': 'News Settings',
            },
        ),
    ]
