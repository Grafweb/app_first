from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_article_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='show_contact_form',
            field=models.BooleanField(default=False),
        ),
    ]
