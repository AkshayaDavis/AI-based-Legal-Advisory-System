from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re
from django.forms import ClearableFileInput

class RegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(
        max_length=20,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'id':'password','name':'password'}),
        )
    class Meta:
        model=Register
        fields=['first_name','username','email','phone','password']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email'}),
            'phone':forms.NumberInput(attrs={'id':'phone','name':'phone'}),
            'password':forms.PasswordInput(attrs={'id':'password','name':'password'}),
        }
        labels={
            'first_name':'Name',
            'username':'Username',
            'email':'E-Mail',
            'phone':'Phone Number',
            'password':'Password',
        }
        help_texts={
            'username':None
        }

    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
            
        return username
    
    # Custom Validation for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    # Custom Validation for contact
    def clean_phone(self):
        phone = str(self.cleaned_data.get('phone'))
        if len(phone) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not phone.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return phone
    
    # Custom Validation for password
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r'[A-Za-z]', password):
            raise ValidationError("Password must contain at least one letter.")
        return password
    
    # Custom Validation for confirm_password
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if confirm_password != password:
            raise ValidationError("Password and confirm password do not match.")
        return confirm_password


class LoginForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        label='UserName',
        widget=forms.TextInput(attrs={'id':'username','name':'username'}),
    )
    password=forms.CharField(
        max_length=20,
        label="Password",
        widget=forms.PasswordInput(attrs={'id':'password','name':'password'}),
        )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=['first_name', 'username', 'email', 'phone','image']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email',}),
            'phone':forms.TextInput(attrs={'id':'phone','name':'phone'}),
            'image':forms.FileInput(attrs={'id':'image','name':'image'}),
        }
        labels={
            'first_name':'NAME',
            'username':'USERNAME',
            'email':'EMAIL',
            'phone':'PHONE NUMBER',
            'image':'PROFILE PICTURE',
        }
        help_texts={
            'username':None
        }
    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise ValidationError("This username is already taken.")

        return username
    
    
    
    # Custom Validation for contact
    def clean_phone(self):
        phone = str(self.cleaned_data.get('phone'))  # Ensure contact is a string
        if len(phone) != 10:
            raise ValidationError("Phone number must be exactly 10 digits.")
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits.")

        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("An account with this email already exists.")
        return email


class ForgotPasswordForm(forms.Form):
    email=forms.CharField(max_length=50,label='',widget=forms.EmailInput(attrs={'id':'email','name':'email','placeholder':'Enter your E-mail'}))

class ResetPasswordForm(forms.Form):
    otp=forms.CharField(max_length=6,label="",widget=forms.TextInput(attrs={'id':'otp','name':'otp','placeholder':'Enter OTP'}))
    email=forms.CharField(max_length=50,label="",widget=forms.EmailInput(attrs={'id':'email','name':'email','placeholder':'Enter your E-mail'}))
    newpassword=forms.CharField(max_length=50,label="",widget=forms.PasswordInput(attrs={'id':'newpassword','name':'newpassword','placeholder':'Enter new password'}))
    confirmpassword=forms.CharField(max_length=50,label="",widget=forms.PasswordInput(attrs={'id':'confirmpassword','name':'confirmpassword','placeholder':'Please confirm password'}))

class LawyerRegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(
        max_length=20,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'id':'password','name':'password'}),
        )
    
    class Meta:
        model=Register
        fields=['first_name','username','email','phone','barcouncil_number','password']
        widgets={
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email'}),
            'phone':forms.NumberInput(attrs={'id':'phone','name':'phone'}),
            'barcouncil_number': forms.TextInput(attrs={
                'id': 'barcouncil_number',
                'name': 'barcouncil_number',
                'pattern': '[A-Z]{2}/\d{4}/\d{4}',  # Example: UP/1234/2022
                'title': 'Format: XX/1234/2022 (State Code / Serial Number / Year)'
            }),
            'password':forms.PasswordInput(attrs={'id':'password','name':'password'}),
        }
        labels={
            'first_name':'Name',
            'username':'Username',
            'email':'E-Mail',
            'phone':'Phone Number',
            'barcouncil_number':'Bar Council Number',
            'password':'Password',
        }
        help_texts={
            'username':None
        }

    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
            
        return username
    
    # Custom Validation for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    # Custom Validation for contact
    def clean_phone(self):
        phone = str(self.cleaned_data.get('phone'))
        if len(phone) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not phone.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return phone
    
    # Custom Validation for password
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r'[A-Za-z]', password):
            raise ValidationError("Password must contain at least one letter.")
        return password
    
    # Custom Validation for confirm_password
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if confirm_password != password:
            raise ValidationError("Password and confirm password do not match.")
        return confirm_password

    def clean_barcouncil_number(self):
        barcouncil_number = self.cleaned_data.get('barcouncil_number')

        # Define a regex pattern for Bar Council Number (Example: UP/1234/2022)
        pattern = r'^[A-Z]{2}/\d{4}/\d{4}$'

        if not re.match(pattern, barcouncil_number):
            raise ValidationError("Invalid Bar Council Number format. Use format: 'XX/1234/2022'.")

        return barcouncil_number

class EditLawyerProfileForm(forms.ModelForm):
    SPECIALIZATIONS = [
    ('Criminal', 'Criminal Law'),
    ('Civil', 'Civil Law'),
    ('Corporate', 'Corporate & Business Law'),
    ('Family', 'Family Law'),
    ('Intellectual Property', 'Intellectual Property (IP) Law'),
    ('Labor', 'Labor & Employment Law'),
    ('Tax', 'Taxation Law'),
    ('Immigration', 'Immigration Law'),
    ('Real Estate', 'Real Estate & Property Law'),
    ('Cyber', 'Cyber & Technology Law'),
    ('Environmental', 'Environmental Law'),
    ('Banking', 'Banking & Financial Law'),
    ('Human Rights', 'Human Rights & Constitutional Law'),
    ('Consumer', 'Consumer Protection Law'),
]
    specialization = forms.ChoiceField(choices=SPECIALIZATIONS, widget=forms.Select(attrs={'class': 'form-control'}))

    consultation_mode=[
        ('Online','Online'),
        ('In-Person','In-Person'),
        ('Online & In-Person','Online & In-Person'),
    ]
    consultation_mode = forms.ChoiceField(choices=consultation_mode, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model=Register
        fields=['image','first_name','qualification','bio', 'username', 'email', 'address','phone','barcouncil_number','specialization','experience','consultation_mode']
        widgets={
            'image':forms.FileInput(attrs={'id':'image','name':'image'}),
            'first_name':forms.TextInput(attrs={'id':'first_name','name':'first_name'}),
            'qualification':forms.TextInput(attrs={'id':'qualification','name':'qualification'}),
            'bio':forms.TextInput(attrs={'id':'bio','name':'bio'}),
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email'}),
            'address':forms.TextInput(attrs={'id':'address','name':'address'}),
            'phone':forms.TextInput(attrs={'id':'phone','name':'phone'}),
            'barcouncil_number':forms.TextInput(attrs={'id':'barcouncil_number','name':'barcouncil_number'}),
            'specialization':forms.Select(attrs={'id':'specialization','name':'specialization'}),
            'experience':forms.TextInput(attrs={'id':'experience','name':'experience'}),
            'consultation_mode':forms.Select(attrs={'id':'consultation_mode','name':'consultation_mode'}),
        }
        labels={
            'image':'PROFILE PICTURE',
            'first_name':'NAME',
            'qualification':'Qualification',
            'username':'USERNAME',
            'email':'EMAIL',
            'address':'ADDRESS',
            'phone':'PHONE NUMBER',
            'barcouncil_number':'Bar Council Number',
            'specialization':'Specialization',
            'experience':'Experience',
            'consultation_mode':'Consultation Mode',
        }
        help_texts={
            'username':None
        }
    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise ValidationError("This username is already taken.")

        return username
    
    # Custom Validation for contact
    def clean_phone(self):
        phone = str(self.cleaned_data.get('phone'))  # Ensure contact is a string
        if len(phone) != 10:
            raise ValidationError("Phone number must be exactly 10 digits.")
        if not phone.isdigit():
            raise ValidationError("Phone number must contain only digits.")

        return phone

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise ValidationError("An account with this email already exists.")
        return email

    def clean_barcouncil_number(self):
        barcouncil_number = self.cleaned_data.get('barcouncil_number')
        # Define a regex pattern for Bar Council Number (Example: UP/1234/2022)
        pattern = r'^[A-Z]{2}/\d{4}/\d{4}$'
        if not re.match(pattern, barcouncil_number):
            raise ValidationError("Invalid Bar Council Number format. Use format: 'XX/1234/2022'.")
        return barcouncil_number


class CourtRegisterForm(forms.ModelForm):
    COURT_JURISDICTIONS = [
    ('Federal Jurisdiction', 'Federal Jurisdiction'),
    ('State Jurisdiction', 'State Jurisdiction'),
    ('District Jurisdiction', 'District Jurisdiction'),
    ('Municipal Jurisdiction', 'Municipal Jurisdiction'),
    ('Criminal Jurisdiction', 'Criminal Jurisdiction'),
    ('Civil Jurisdiction', 'Civil Jurisdiction'),
    ('Appellate Jurisdiction', 'Appellate Jurisdiction'),
    ('Special Jurisdiction', 'Special Jurisdiction'),
    ('Exclusive Jurisdiction', 'Exclusive Jurisdiction'),
    ('Concurrent Jurisdiction', 'Concurrent Jurisdiction'),
]
    court_jurisdiction = forms.ChoiceField(
    choices=COURT_JURISDICTIONS, 
    widget=forms.Select(attrs={'class': 'form-control'})
)

    COURT_TYPES = [
    ('Supreme Court', 'Supreme Court'),
    ('High Court', 'High Court'),
    ('District Court', 'District Court'),
    ('Session Court', 'Session Court'),
    ('Magistrate Court', 'Magistrate Court'),
    ('Family Court', 'Family Court'),
    ('Consumer Court', 'Consumer Court'),
    ('Labor Court', 'Labor Court'),
    ('Tribunal Court', 'Tribunal Court'),
    ('Juvenile Court', 'Juvenile Court'),
    ('Cyber Court', 'Cyber Court'),
    ('Small Claims Court', 'Small Claims Court'),
    ('Bankruptcy Court', 'Bankruptcy Court'),
    ('Environmental Court', 'Environmental Court'),
]

    court_type = forms.ChoiceField(
    choices=COURT_TYPES, 
    widget=forms.Select(attrs={'class': 'form-control'})
)


    confirm_password=forms.CharField(
        max_length=20,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'id':'password','name':'password'}),
        )
    class Meta:
        model=Register
        fields=['username','court_jurisdiction','court_type','email','place','password']
        widgets={
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'court_jurisdiction':forms.TextInput(attrs={'id':'court_jurisdiction','name':'court_jurisdiction'}),
            'court_type':forms.TextInput(attrs={'id':'court_type','name':'court_type'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email'}),
            'place':forms.TextInput(attrs={'id':'place','name':'place'}),
            'password':forms.PasswordInput(attrs={'id':'password','name':'password'}),
        }
        labels={
            'username':'Username',
            'court_jurisdiction':'Court Jurisdiction',
            'court_type':'Court Type',
            'email':'E-Mail',
            'place':'Place',
            'password':'Password',
        }
        help_texts={
            'username':None
        }

    # Custom Validation for username
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 5:
            raise ValidationError("Username must be at least 5 characters long.")
        if not username.isalnum():
            raise ValidationError("Username must only contain alphanumeric characters.")
        # Check if the username already exists (assuming you have a model named Register)
        if Register.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
            
        return username
    
    # Custom Validation for email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Register.objects.filter(email=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email
    
    # Custom Validation for contact
    def clean_phone(self):
        phone = str(self.cleaned_data.get('phone'))
        if len(phone) != 10:
            raise ValidationError("Contact number must be exactly 10 digits.")
        if not phone.isdigit():
            raise ValidationError("Contact number must contain only digits.")
        return phone

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'\d', password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r'[A-Za-z]', password):
            raise ValidationError("Password must contain at least one letter.")
        return password
    
    # Custom Validation for confirm_password
    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')
        if confirm_password != password:
            raise ValidationError("Password and confirm password do not match.")
        return confirm_password

class EditCourtProfileForm(forms.ModelForm):
    COURT_JURISDICTIONS = [
    ('Federal Jurisdiction', 'Federal Jurisdiction'),
    ('State Jurisdiction', 'State Jurisdiction'),
    ('District Jurisdiction', 'District Jurisdiction'),
    ('Municipal Jurisdiction', 'Municipal Jurisdiction'),
    ('Criminal Jurisdiction', 'Criminal Jurisdiction'),
    ('Civil Jurisdiction', 'Civil Jurisdiction'),
    ('Appellate Jurisdiction', 'Appellate Jurisdiction'),
    ('Special Jurisdiction', 'Special Jurisdiction'),
    ('Exclusive Jurisdiction', 'Exclusive Jurisdiction'),
    ('Concurrent Jurisdiction', 'Concurrent Jurisdiction'),
]
    court_jurisdiction = forms.ChoiceField(
    choices=COURT_JURISDICTIONS, 
    widget=forms.Select(attrs={'class': 'form-control'})
)

    COURT_TYPES = [
    ('Supreme Court', 'Supreme Court'),
    ('High Court', 'High Court'),
    ('District Court', 'District Court'),
    ('Session Court', 'Session Court'),
    ('Magistrate Court', 'Magistrate Court'),
    ('Family Court', 'Family Court'),
    ('Consumer Court', 'Consumer Court'),
    ('Labor Court', 'Labor Court'),
    ('Tribunal Court', 'Tribunal Court'),
    ('Juvenile Court', 'Juvenile Court'),
    ('Cyber Court', 'Cyber Court'),
    ('Small Claims Court', 'Small Claims Court'),
    ('Bankruptcy Court', 'Bankruptcy Court'),
    ('Environmental Court', 'Environmental Court'),
]

    court_type = forms.ChoiceField(
    choices=COURT_TYPES, 
    widget=forms.Select(attrs={'class': 'form-control'})
)

    class Meta:
        model=Register
        fields=['username','court_jurisdiction','court_type','email','place']
        widgets={
            'username':forms.TextInput(attrs={'id':'username','name':'username'}),
            'court_jurisdiction':forms.TextInput(attrs={'id':'court_jurisdiction','name':'court_jurisdiction'}),
            'court_type':forms.TextInput(attrs={'id':'court_type','name':'court_type'}),
            'email':forms.EmailInput(attrs={'id':'email','name':'email'}),
            'place':forms.TextInput(attrs={'id':'place','name':'place'}),
        }
        labels={
            'username':'Username',
            'court_jurisdiction':'Court Jurisdiction',
            'court_type':'Court Type',
            'email':'E-Mail',
            'place':'Place',
        }
        help_texts={
            'username':None
        }

    # Custom Validation for username

ALLOWED_FILE_TYPES = ['pdf', 'png', 'jpg', 'jpeg', 'docx']
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB
class BookingsForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['content']
        widgets = {
            'content': forms.FileInput(attrs={'id': 'content', 'name': 'content', 'accept': 'application/pdf,image/*,application/vnd.openxmlformats-officedocument.wordprocessingml.document'}),
        }

        labels = {
            'content': 'Upload File',
        }
        help_texts = {
            'content': 'Allowed file types: PDF, PNG, JPG, DOCX, etc.',
        }

    def clean_content(self):
        file = self.cleaned_data.get('content', False)

        if file:
            # Check file type
            ext = file.name.split('.')[-1].lower()
            if ext not in ALLOWED_FILE_TYPES:
                raise ValidationError("Unsupported file type. Allowed types: PDF, PNG, JPG, DOCX.")
            
            # Check file size
            if file.size > MAX_FILE_SIZE:
                raise ValidationError("File size must be less than 5MB.")
        
        return file

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Type your message here...'}),
        }
        labels = {
            'message': '',
        }
        help_texts = {
            'message': '',
        }


class LawForm(forms.ModelForm):
    class Meta:
        model = Law
        fields = ['name', 'ipc', 'description', 'year_of_act']
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'name': 'name'}),
            'ipc': forms.TextInput(attrs={'id': 'ipc', 'name': 'ipc'}),
            'description': forms.Textarea(attrs={'id': 'description', 'name': 'description'}),
            'year_of_act': forms.DateInput(attrs={'id': 'year_of_act', 'name': 'year_of_act', 'type': 'date'}),
        }
        labels = {
            'name': 'Name',
            'ipc': 'IPC Section',
            'description': 'Description',
            'year_of_act': 'Year of Act',
        }
        help_texts = {
            'name': '',
            'ipc': '',
            'description': '',
            'year_of_act': '',
        }