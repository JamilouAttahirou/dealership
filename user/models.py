from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()  # Set the custom UserManager


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    exterior_color = models.CharField(max_length=15, blank=True, null=True)
    interior_color = models.CharField(max_length=15, blank=True, null=True)
    mileage = models.IntegerField()
    engine = models.CharField(max_length=10, blank=True, null=True)
    vin_number = models.CharField(max_length=17, unique=True)
    transmission = models.CharField(max_length=25, blank=True, null=True)
    stock_number = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=255, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True,)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.make
    

class Photo(models.Model):
    car = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='cars_photos/')

    def __str__(self):
        return f"Photo for {self.car.make} {self.car.model}"
    


class Financing(models.Model):

     # Defining a list of US states as choices
    STATE_CHOICES = [
        ('0', 'Alabama'),
        ('1', 'Alaska'),
        ('2', 'Arizona'),
        ('3', 'Arkansas'),
        ('4', 'California'),
        ('5', 'Colorado'),
        ('6', 'Connecticut'),
        ('7', 'Delaware'),
        ('8', 'Florida'),
        ('9', 'Georgia'),
        ('10', 'Hawaii'),
        ('11', 'Idaho'),
        ('12', 'Illinois'),
        ('13', 'Indiana'),
        ('14', 'Iowa'),
        ('15', 'Kansas'),
        ('16', 'Kentucky'),
        ('17', 'Louisiana'),
        ('18', 'Maine'),
        ('19', 'Maryland'),
        ('20', 'Massachusetts'),
        ('21', 'Michigan'),
        ('22', 'Minnesota'),
        ('23', 'Mississippi'),
        ('24', 'Missouri'),
        ('25', 'Montana'),
        ('26', 'Nebraska'),
        ('27', 'Nevada'),
        ('28', 'New Hampshire'),
        ('29', 'New Jersey'),
        ('30', 'New Mexico'),
        ('31', 'New York'),
        ('32', 'North Carolina'),
        ('33', 'North Dakota'),
        ('34', 'Ohio'),
        ('35', 'Oklahoma'),
        ('36', 'Oregon'),
        ('37', 'Pennsylvania'),
        ('38', 'Rhode Island'),
        ('39', 'South Carolina'),
        ('40', 'South Dakota'),
        ('41', 'Tennessee'),
        ('42', 'Texas'),
        ('43', 'Utah'),
        ('44', 'Vermont'),
        ('45', 'Virginia'),
        ('46', 'Washington'),
        ('47', 'West Virginia'),
        ('48', 'Wisconsin'),
        ('49', 'Wyoming'),
    ]

    STATE_CHOICES_2 = [
        ('0', 'Alabama'),
        ('1', 'Alaska'),
        ('2', 'Arizona'),
        ('3', 'Arkansas'),
        ('4', 'California'),
        ('5', 'Colorado'),
        ('6', 'Connecticut'),
        ('7', 'Delaware'),
        ('8', 'Florida'),
        ('9', 'Georgia'),
        ('10', 'Hawaii'),
        ('11', 'Idaho'),
        ('12', 'Illinois'),
        ('13', 'Indiana'),
        ('14', 'Iowa'),
        ('15', 'Kansas'),
        ('16', 'Kentucky'),
        ('17', 'Louisiana'),
        ('18', 'Maine'),
        ('19', 'Maryland'),
        ('20', 'Massachusetts'),
        ('21', 'Michigan'),
        ('22', 'Minnesota'),
        ('23', 'Mississippi'),
        ('24', 'Missouri'),
        ('25', 'Montana'),
        ('26', 'Nebraska'),
        ('27', 'Nevada'),
        ('28', 'New Hampshire'),
        ('29', 'New Jersey'),
        ('30', 'New Mexico'),
        ('31', 'New York'),
        ('32', 'North Carolina'),
        ('33', 'North Dakota'),
        ('34', 'Ohio'),
        ('35', 'Oklahoma'),
        ('36', 'Oregon'),
        ('37', 'Pennsylvania'),
        ('38', 'Rhode Island'),
        ('39', 'South Carolina'),
        ('40', 'South Dakota'),
        ('41', 'Tennessee'),
        ('42', 'Texas'),
        ('43', 'Utah'),
        ('44', 'Vermont'),
        ('45', 'Virginia'),
        ('46', 'Washington'),
        ('47', 'West Virginia'),
        ('48', 'Wisconsin'),
        ('49', 'Wyoming'),
    ]

    STATE_CHOICES_3 = [
        ('0', 'Alabama'),
        ('1', 'Alaska'),
        ('2', 'Arizona'),
        ('3', 'Arkansas'),
        ('4', 'California'),
        ('5', 'Colorado'),
        ('6', 'Connecticut'),
        ('7', 'Delaware'),
        ('8', 'Florida'),
        ('9', 'Georgia'),
        ('10', 'Hawaii'),
        ('11', 'Idaho'),
        ('12', 'Illinois'),
        ('13', 'Indiana'),
        ('14', 'Iowa'),
        ('15', 'Kansas'),
        ('16', 'Kentucky'),
        ('17', 'Louisiana'),
        ('18', 'Maine'),
        ('19', 'Maryland'),
        ('20', 'Massachusetts'),
        ('21', 'Michigan'),
        ('22', 'Minnesota'),
        ('23', 'Mississippi'),
        ('24', 'Missouri'),
        ('25', 'Montana'),
        ('26', 'Nebraska'),
        ('27', 'Nevada'),
        ('28', 'New Hampshire'),
        ('29', 'New Jersey'),
        ('30', 'New Mexico'),
        ('31', 'New York'),
        ('32', 'North Carolina'),
        ('33', 'North Dakota'),
        ('34', 'Ohio'),
        ('35', 'Oklahoma'),
        ('36', 'Oregon'),
        ('37', 'Pennsylvania'),
        ('38', 'Rhode Island'),
        ('39', 'South Carolina'),
        ('40', 'South Dakota'),
        ('41', 'Tennessee'),
        ('42', 'Texas'),
        ('43', 'Utah'),
        ('44', 'Vermont'),
        ('45', 'Virginia'),
        ('46', 'Washington'),
        ('47', 'West Virginia'),
        ('48', 'Wisconsin'),
        ('49', 'Wyoming'),
    ]

    STATE_CHOICES_4 = [
        ('0', 'Alabama'),
        ('1', 'Alaska'),
        ('2', 'Arizona'),
        ('3', 'Arkansas'),
        ('4', 'California'),
        ('5', 'Colorado'),
        ('6', 'Connecticut'),
        ('7', 'Delaware'),
        ('8', 'Florida'),
        ('9', 'Georgia'),
        ('10', 'Hawaii'),
        ('11', 'Idaho'),
        ('12', 'Illinois'),
        ('13', 'Indiana'),
        ('14', 'Iowa'),
        ('15', 'Kansas'),
        ('16', 'Kentucky'),
        ('17', 'Louisiana'),
        ('18', 'Maine'),
        ('19', 'Maryland'),
        ('20', 'Massachusetts'),
        ('21', 'Michigan'),
        ('22', 'Minnesota'),
        ('23', 'Mississippi'),
        ('24', 'Missouri'),
        ('25', 'Montana'),
        ('26', 'Nebraska'),
        ('27', 'Nevada'),
        ('28', 'New Hampshire'),
        ('29', 'New Jersey'),
        ('30', 'New Mexico'),
        ('31', 'New York'),
        ('32', 'North Carolina'),
        ('33', 'North Dakota'),
        ('34', 'Ohio'),
        ('35', 'Oklahoma'),
        ('36', 'Oregon'),
        ('37', 'Pennsylvania'),
        ('38', 'Rhode Island'),
        ('39', 'South Carolina'),
        ('40', 'South Dakota'),
        ('41', 'Tennessee'),
        ('42', 'Texas'),
        ('43', 'Utah'),
        ('44', 'Vermont'),
        ('45', 'Virginia'),
        ('46', 'Washington'),
        ('47', 'West Virginia'),
        ('48', 'Wisconsin'),
        ('49', 'Wyoming'),
    ]

    # Defining a list of residence status
    RESIDENCE_STATUS = [
        ('0', 'Rent'),
        ('1', 'Own'),
    ]

    PREVIOUS_RESIDENCE_STATUS = [
        ('0', 'Rent'),
        ('1', 'Own'),
    ]

    # Defining a list of time at current residence
    TIME_CURRENT_RESIDENCE = [
        ('0', '0 years'),
        ('1', '1 years'),
        ('2', '2 years'),
        ('3', '3 years'),
        ('4', '4 years'),
        ('5', '5 years'),
        ('6', '6 years'),
        ('7', '7 years'),
        ('8', '8 years'),
        ('9', '9 years'),
        ('10', '10 years'),
        ('11', '11 years'),
        ('12', '12 years'),
        ('13', '13 years'),
        ('14', '14 years'),
        ('15', '15 years'),
        ('16', '16 years'),
        ('17', '17 years'),
        ('18', '18 years'),
        ('19', '19 years'),
        ('20', '20 years'),
        ('21', '21 years'),
        ('22', '22 years'),
        ('23', '23 years'),
        ('24', '24 years'),
        ('25', '25 years'),
        ('26', '26 years'),
        ('27', '27 years'),
        ('28', '28 years'),
        ('29', '29 years'),
        ('30', '30 years'),
        ('31', '31 years'),
        ('32', '32 years'),
        ('33', '33 years'),
        ('34', '34 years'),
        ('35', '35 years'),
        ('36', '36 years'),
        ('37', '37 years'),
        ('38', '38 years'),
        ('39', '39 years'),
        ('40', '40 years'),
        ('41', '41 years'),
        ('42', '42 years'),
        ('43', '43 years'),
        ('44', '44 years'),
        ('45', '45 years'),
        ('46', '46 years'),
        ('47', '47 years'),
        ('48', '48 years'),
        ('49', '49 years'),
        ('45', '50 years'),
    ]

    TIME_CURRENT_EMPLOYER = [
        ('0', '0 years'),
        ('1', '1 years'),
        ('2', '2 years'),
        ('3', '3 years'),
        ('4', '4 years'),
        ('5', '5 years'),
        ('6', '6 years'),
        ('7', '7 years'),
        ('8', '8 years'),
        ('9', '9 years'),
        ('10', '10 years'),
        ('11', '11 years'),
        ('12', '12 years'),
        ('13', '13 years'),
        ('14', '14 years'),
        ('15', '15 years'),
        ('16', '16 years'),
        ('17', '17 years'),
        ('18', '18 years'),
        ('19', '19 years'),
        ('20', '20 years'),
        ('21', '21 years'),
        ('22', '22 years'),
        ('23', '23 years'),
        ('24', '24 years'),
        ('25', '25 years'),
        ('26', '26 years'),
        ('27', '27 years'),
        ('28', '28 years'),
        ('29', '29 years'),
        ('30', '30 years'),
        ('31', '31 years'),
        ('32', '32 years'),
        ('33', '33 years'),
        ('34', '34 years'),
        ('35', '35 years'),
        ('36', '36 years'),
        ('37', '37 years'),
        ('38', '38 years'),
        ('39', '39 years'),
        ('40', '40 years'),
        ('41', '41 years'),
        ('42', '42 years'),
        ('43', '43 years'),
        ('44', '44 years'),
        ('45', '45 years'),
        ('46', '46 years'),
        ('47', '47 years'),
        ('48', '48 years'),
        ('49', '49 years'),
        ('45', '50 years'),
    ]

    TIME_PREVIOUS_EMPLOYER = [
        ('0', '0 years'),
        ('1', '1 years'),
        ('2', '2 years'),
        ('3', '3 years'),
        ('4', '4 years'),
        ('5', '5 years'),
        ('6', '6 years'),
        ('7', '7 years'),
        ('8', '8 years'),
        ('9', '9 years'),
        ('10', '10 years'),
        ('11', '11 years'),
        ('12', '12 years'),
        ('13', '13 years'),
        ('14', '14 years'),
        ('15', '15 years'),
        ('16', '16 years'),
        ('17', '17 years'),
        ('18', '18 years'),
        ('19', '19 years'),
        ('20', '20 years'),
        ('21', '21 years'),
        ('22', '22 years'),
        ('23', '23 years'),
        ('24', '24 years'),
        ('25', '25 years'),
        ('26', '26 years'),
        ('27', '27 years'),
        ('28', '28 years'),
        ('29', '29 years'),
        ('30', '30 years'),
        ('31', '31 years'),
        ('32', '32 years'),
        ('33', '33 years'),
        ('34', '34 years'),
        ('35', '35 years'),
        ('36', '36 years'),
        ('37', '37 years'),
        ('38', '38 years'),
        ('39', '39 years'),
        ('40', '40 years'),
        ('41', '41 years'),
        ('42', '42 years'),
        ('43', '43 years'),
        ('44', '44 years'),
        ('45', '45 years'),
        ('46', '46 years'),
        ('47', '47 years'),
        ('48', '48 years'),
        ('49', '49 years'),
        ('45', '50 years'),
    ]

    # Defining the list of finace method choices
    FINANCE_METHOD = [
        ('0' ,'Finance'),
        ('1' ,'Lease'),
    ]

    # Defining list of loan length choices
    LOAN_LENGTH = [
        ('0', '0 years'),
        ('1', '1 year'),
        ('2', '2 years'),
        ('3', '3 years'),
        ('4', '4 years'),
        ('5', '5 years'),
    ]


    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    work_phone = models.CharField(max_length=15, null=True, blank=True)
    last_four_digits_social_security_number = models.IntegerField(blank=False, null=False)

    street = models.CharField(max_length=255, blank=False, null=False)
    apartment = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, choices=STATE_CHOICES, blank=False, null=False)
    zip_code = models.IntegerField(blank=False, null=False)
    residence_status = models.CharField(max_length=4, choices=RESIDENCE_STATUS, null=True, blank=True)
    landlord_mortgage_holder = models.CharField(max_length=100, null=True, blank=True)
    rent_mortgage_monthly_amount = models.IntegerField(blank=False, null=False)
    time_at_current_residence = models.CharField(max_length=10, choices=TIME_CURRENT_RESIDENCE, blank=False, null=False)
    previous_residence = models.CharField(max_length=4, choices=PREVIOUS_RESIDENCE_STATUS, null=True, blank=True)
    previous_street = models.CharField(max_length=255, null=True, blank=True)
    previous_apartment = models.CharField(max_length=255, null=True, blank=True)
    city_2 = models.CharField(max_length=100, null=True, blank=True)
    state_2 = models.CharField(max_length=100, choices=STATE_CHOICES_2, null=True, blank=True)
    zip_code_2 = models.IntegerField(null=True, blank=True)


    place_of_employment = models.CharField(max_length=100, null=True, blank=True)
    street_3 = models.CharField(max_length=255, null=True, blank=True)
    city_3 = models.CharField(max_length=100, null=True, blank=True)
    state_3 = models.CharField(max_length=100, choices=STATE_CHOICES_3, null=True, blank=True)
    zip_code_3 = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=100, blank=False, null=False)
    business_phone = models.CharField(max_length=15, null=True, blank=True)
    time_at_current_employer = models.CharField(max_length=10, choices=TIME_CURRENT_EMPLOYER, blank=False, null=False)
    gross_salary = models.IntegerField(null=True, blank=True)
    net_salary = models.IntegerField(blank=False, null=False)
    other_income = models.IntegerField(null=True, blank=True)
    previous_employment = models.CharField(max_length=100, null=True, blank=True)
    street_4 = models.CharField(max_length=255, null=True, blank=True)
    city_4 = models.CharField(max_length=100, null=True, blank=True)
    state_4 = models.CharField(max_length=100 ,choices=STATE_CHOICES_4, null=True, blank=True)
    zip_code_4 = models.IntegerField(null=True, blank=True)
    previous_occupation = models.CharField(max_length=100, null=True, blank=True)
    previous_employer_phone = models.CharField(max_length=15, null=True, blank=True)
    time_at_previous_employer = models.CharField(max_length=10, choices=TIME_PREVIOUS_EMPLOYER, null=True, blank=True)

    name_of_bank = models.CharField(max_length=100, null=True, blank=True)
    account_types = models.CharField(max_length=100, null=True, blank=True)
    name_of_bank_2 = models.CharField(max_length=100, null=True, blank=True)
    account_types_2 = models.CharField(max_length=100, null=True, blank=True)
    lender = models.CharField(max_length=100, null=True, blank=True)
    finance_method = models.CharField(max_length=10, choices=FINANCE_METHOD, blank=False, null=False)
    monthly_payment = models.IntegerField(blank=False, null=False)
    total_debt = models.IntegerField(null=True, blank=True)
    length_of_loan = models.CharField(max_length=10, choices=LOAN_LENGTH, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f""
    

class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    body = models.TextField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return f" {self.first_name} - {self.get_state_display()}"
    
