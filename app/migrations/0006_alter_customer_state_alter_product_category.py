# Generated by Django 4.2.4 on 2023-08-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_customer_state_alter_product_category_cart"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="state",
            field=models.CharField(
                choices=[
                    ("TR", "Tripura"),
                    ("ML", "Meghalaya"),
                    ("AS", "Assam"),
                    ("WB", "West Bengal"),
                    ("AP", "Andhra Pradesh"),
                    ("AR", "Arunachal Pradesh"),
                    ("TN", "Tamil Nadu"),
                    ("HP", "Himachal Pradesh"),
                    ("SK", "Sikkim"),
                    ("UP", "Uttar Pradesh"),
                    ("MN", "Manipur"),
                    ("JK", "Jammu and Kashmir"),
                    ("UK", "Uttarakhand"),
                    ("RJ", "Rajasthan"),
                    ("TS", "Telangana"),
                    ("JH", "Jharkhand"),
                    ("LD", "Lakshadweep"),
                    ("CH", "Chandigarh"),
                    ("BR", "Bihar"),
                    ("PY", "Pondicherry"),
                    ("NL", "Nagaland"),
                    ("HR", "Haryana"),
                    ("DL", "Delhi"),
                    ("CG", "Chhattisgarh"),
                    ("PB", "Punjab"),
                    ("LA", "Ladakh"),
                    ("GJ", "Gujarat"),
                    ("DD", "Daman and Diu"),
                    ("KA", "Karnataka"),
                    ("DN", "Dadra and Nagar Haveli"),
                    ("MZ", "Mizoram"),
                    ("MH", "Maharashtra"),
                    ("KL", "Kerala"),
                    ("OD", "Odisha"),
                    ("GA", "Goa"),
                    ("MP", "Madhya Pradesh"),
                    ("AN", "Andaman and Nicobar Islands"),
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
                    ("SF", "Sea Foods"),
                    ("FM2", "Fresh Milk"),
                    ("FB", "Fresh Bakery"),
                    ("FD", "Fruit Drinks"),
                    ("VG", "Vegetables"),
                    ("FM", "Fresh Meat"),
                    ("BS", "Biscuits Snack"),
                ],
                max_length=25,
            ),
        ),
    ]
