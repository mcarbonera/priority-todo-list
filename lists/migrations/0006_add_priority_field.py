import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_alter_item_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='priority',
            field=models.TextField(default=''),
        ),
    ]
