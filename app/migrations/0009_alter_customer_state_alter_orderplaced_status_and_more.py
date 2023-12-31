# Generated by Django 4.2.4 on 2023-08-20 08:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("app", "0008_alter_customer_state_alter_product_category_payments_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.CharField(
                choices=[
                    ("JH", "Jharkhand"),
                    ("ML", "Meghalaya"),
                    ("MP", "Madhya Pradesh"),
                    ("GA", "Goa"),
                    ("AN", "Andaman and Nicobar Islands"),
                    ("HP", "Himachal Pradesh"),
                    ("KA", "Karnataka"),
                    ("AR", "Arunachal Pradesh"),
                    ("NL", "Nagaland"),
                    ("HR", "Haryana"),
                    ("AS", "Assam"),
                    ("DD", "Daman and Diu"),
                    ("MN", "Manipur"),
                    ("DL", "Delhi"),
                    ("MZ", "Mizoram"),
                    ("AP", "Andhra Pradesh"),
                    ("WB", "West Bengal"),
                    ("TR", "Tripura"),
                    ("CH", "Chandigarh"),
                    ("TS", "Telangana"),
                    ("RJ", "Rajasthan"),
                    ("DN", "Dadra and Nagar Haveli"),
                    ("KL", "Kerala"),
                    ("TN", "Tamil Nadu"),
                    ("BR", "Bihar"),
                    ("LD", "Lakshadweep"),
                    ("GJ", "Gujarat"),
                    ("JK", "Jammu and Kashmir"),
                    ("UP", "Uttar Pradesh"),
                    ("UK", "Uttarakhand"),
                    ("LA", "Ladakh"),
                    ("SK", "Sikkim"),
                    ("PY", "Pondicherry"),
                    ("CG", "Chhattisgarh"),
                    ("OD", "Odisha"),
                    ("PB", "Punjab"),
                    ("MH", "Maharashtra"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="orderplaced",
            name="status",
            field=models.CharField(
                choices=[
                    ("Cancel", "Cancel"),
                    ("Packed", "Packed"),
                    ("Delivered", "Delivered"),
                    ("On The Way", "On The Way"),
                    ("Accepted", "Accepted"),
                    ("Pending", "Pending"),
                ],
                default="Pending",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("BS", "Biscuits Snack"),
                    ("FM", "Fresh Meat"),
                    ("SF", "Sea Foods"),
                    ("FD", "Fruit Drinks"),
                    ("FB", "Fresh Bakery"),
                    ("FM2", "Fresh Milk"),
                    ("VG", "Vegetables"),
                    ("FR", "Fresh Fruits"),
                ],
                max_length=25,
            ),
        ),
        migrations.CreateModel(
            name="WhishlistAdminModel",
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
