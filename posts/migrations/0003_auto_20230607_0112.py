# Generated by Django 4.2.1 on 2023-06-07 01:12

from django.db import migrations

def populate_status(apps, schemaeditor):
    raw_data = {
        "draft": "Posts that are not ready to be published",
        "published": "Posts that all users can see",
        "archived": "Posts that are archived (only author can see)"
    }
    Status = apps.get_model("posts", "Status")
    for key, val in raw_data.items():
        status_obj = Status(name=key, description=val)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_status_post_status'),
    ]

    operations = [migrations.RunPython(populate_status)
    ]
