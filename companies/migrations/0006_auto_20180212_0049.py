# Generated by Django 2.0.2 on 2018-02-12 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_auto_20180211_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('have_raised_fund_before', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('medium_of_fund_raising', models.CharField(blank=True, max_length=100, null=True)),
                ('do_you_have_fund_raising_plan', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('have_you_taking_a_loan_in_the_past', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('company_bank_account', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('financial_personnel', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('financial_record_updated', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('average_monthly_revenue', models.CharField(blank=True, max_length=100, null=True)),
                ('average_monthly_expenditure', models.CharField(blank=True, max_length=100, null=True)),
                ('future_year_forecast_financial_statement', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('cashflow_statement', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'StartUps Finance ',
                'verbose_name': 'StartUp Finance',
                'db_table': 'Finance',
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_long_have_you_known_your_market', models.CharField(blank=True, choices=[('1 - 5 years', '1 - 5 years'), ('6 - 13 years', '6 - 13 years'), ('14 - 20 years', '14 - 20 years'), ('20 years and above', '20 years and above')], max_length=100, null=True)),
                ('how_big_is_the_market_value', models.CharField(blank=True, default='$500,000', max_length=100, null=True)),
                ('what_is_your_standout_point', models.CharField(blank=True, default='Mode Of Service Delivery', max_length=100, null=True)),
                ('do_you_know_your_competitors', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('do_you_have_a_strategic_business_plan', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('mode_of_getting_target_audience', models.TextField()),
                ('social_media_presence', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'StartUps Market ',
                'verbose_name': 'StartUp Market',
                'db_table': 'Market',
            },
        ),
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'StartUps Pitch ',
                'verbose_name': 'StartUp Pitch',
                'db_table': 'Pitch',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('CEO', 'CEO'), ('CTO', 'CTO'), ('CFO', 'CFO'), ('COO', 'COO'), ('Engineer', 'Engineer'), ('Legal Adviser', 'Legal Adviser'), ('Manager', 'Manager'), ('Finance', 'Finance'), ('Business Developer', 'Business Developer'), ('Operator', 'Operator'), ('Others', 'Others')], max_length=100, null=True)),
                ('do_you_have_a_cofounder', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('how_many_cofounders', models.CharField(blank=True, choices=[('1 - 5', '1 - 5'), ('6 - 10', '6 - 10'), ('Above 11+', 'Above 11+')], max_length=100, null=True)),
                ('do_you_have_an_communication_system', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('how_long_have_you_worked_together', models.CharField(blank=True, choices=[('1 - 5 years', '1 - 5 years'), ('6 - 13 years', '6 - 13 years'), ('14 - 20 years', '14 - 20 years'), ('20 years and above', '20 years and above')], max_length=100, null=True)),
                ('do_you_have_a_legal_agreement_for_shareholders', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('list_the_functioning_units_in_your_business', models.TextField()),
                ('do_you_have_human_resource_policy', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'StartUps Team',
                'verbose_name': 'StartUp Team',
                'db_table': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('does_your_business_require_technology', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('do_you_have_proprietor_technology_in_place', models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'StartUps Technology ',
                'verbose_name': 'StartUp Technology',
                'db_table': 'Technology',
            },
        ),
        migrations.AlterModelOptions(
            name='investor',
            options={'ordering': ['-timestamp', '-updated'], 'verbose_name': 'Investor Data', 'verbose_name_plural': 'Investors Data'},
        ),
        migrations.AlterModelOptions(
            name='startup',
            options={'ordering': ['-timestamp', '-updated'], 'verbose_name': 'StartUp', 'verbose_name_plural': 'StartUps'},
        ),
        migrations.AddField(
            model_name='startup',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='do_you_have_a_3_to_5_year_plan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='how_do_you_measure_growth',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='how_many_customers',
            field=models.CharField(blank=True, choices=[('1 - 10', '1 - 10'), ('11 - 50', '51 - 150'), ('151 - 500', '151 - 500'), ('501 - 1,500', '501 - 1,500'), ('1,501 - 10,000', '1,501 - 10,000'), ('10,001 - More', '10,001 - More')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='number_of_staffs',
            field=models.CharField(blank=True, choices=[('1 - 5', '1 - 5'), ('6 - 10', '6 - 10'), ('Above 11+', 'Above 11+')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='resgistered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='startup',
            name='stage',
            field=models.CharField(blank=True, choices=[('idea', 'idea'), ('research', 'research'), ('market validation', 'market validation'), ('revenue generation', 'revenue generation'), ('early growth', 'early growth'), ('expansion', 'expansion')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='users_or_customers',
            field=models.CharField(blank=True, choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='startup',
            name='why_are_you_in_business',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='technology',
            name='startup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.StartUp'),
        ),
        migrations.AddField(
            model_name='team',
            name='startup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.StartUp'),
        ),
        migrations.AddField(
            model_name='pitching',
            name='startup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.StartUp'),
        ),
        migrations.AddField(
            model_name='market',
            name='startup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.StartUp'),
        ),
        migrations.AddField(
            model_name='finance',
            name='startup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.StartUp'),
        ),
    ]
