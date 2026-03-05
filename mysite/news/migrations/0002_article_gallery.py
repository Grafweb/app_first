from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='gallery',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='articles',
                to='gallery.gallery',
            ),
        ),
    ]
