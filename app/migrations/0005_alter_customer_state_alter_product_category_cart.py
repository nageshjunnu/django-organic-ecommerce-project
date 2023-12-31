# Generated by Django 4.2.4 on 2023-08-18 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0004_alter_product_category_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.CharField(
                choices=[
                    ("AN", "Andaman and Nicobar Islands"),
                    ("DN", "Dadra and Nagar Haveli"),
                    ("CG", "Chhattisgarh"),
                    ("GJ", "Gujarat"),
                    ("MH", "Maharashtra"),
                    ("JK", "Jammu and Kashmir"),
                    ("UK", "Uttarakhand"),
                    ("HR", "Haryana"),
                    ("ML", "Meghalaya"),
                    ("LD", "Lakshadweep"),
                    ("AR", "Arunachal Pradesh"),
                    ("MP", "Madhya Pradesh"),
                    ("MZ", "Mizoram"),
                    ("LA", "Ladakh"),
                    ("AP", "Andhra Pradesh"),
                    ("DL", "Delhi"),
                    ("OD", "Odisha"),
                    ("MN", "Manipur"),
                    ("TN", "Tamil Nadu"),
                    ("PB", "Punjab"),
                    ("UP", "Uttar Pradesh"),
                    ("TS", "Telangana"),
                    ("DD", "Daman and Diu"),
                    ("BR", "Bihar"),
                    ("SK", "Sikkim"),
                    ("KA", "Karnataka"),
                    ("TR", "Tripura"),
                    ("PY", "Pondicherry"),
                    ("KL", "Kerala"),
                    ("AS", "Assam"),
                    ("NL", "Nagaland"),
                    ("RJ", "Rajasthan"),
                    ("GA", "Goa"),
                    ("WB", "West Bengal"),
                    ("CH", "Chandigarh"),
                    ("HP", "Himachal Pradesh"),
                    ("JH", "Jharkhand"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("FR", "Fresh Fruits"),
                    ("FM2", "Fresh Milk"),
                    ("BS", "Biscuits Snack"),
                    ("SF", "Sea Foods"),
                    ("FD", "Fruit Drinks"),
                    ("FB", "Fresh Bakery"),
                    ("FM", "Fresh Meat"),
                    ("VG", "Vegetables"),
                ],
                max_length=25,
            ),
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
