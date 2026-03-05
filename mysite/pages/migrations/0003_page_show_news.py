from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_news',
            field=models.CharField(
                choices=[
                    ('none', 'No news'),
                    ('featured', 'Featured - 3 latest articles'),
                    ('full', 'Full list with pagination'),
                ],
                default='none',
                max_length=20,
            ),
        ),
    ]
