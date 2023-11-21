
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afisha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('time_watch', models.TimeField()),
                ('area', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'verbose_name': 'Книга', 'verbose_name_plural': 'Книга'},
        ),
    ]
