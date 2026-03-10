from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_show_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='show_contact_form',
            field=models.BooleanField(default=False),
        ),
    ]
