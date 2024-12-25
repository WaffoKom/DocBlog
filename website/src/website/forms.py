from django import forms


CHOICES =[
    ("Flutter" ,"Developpeur Mobile"),
    ("JavaScript", "Developpeur JavaScript"),
    ("Python","Developpeur Python")
]


class SignUpForms(forms.Form):
    pseudo =forms.CharField(required=False, strip=True, max_length=200, label="Pseudo")
    password =forms.CharField(widget=forms.PasswordInput() , label="Mot de Passe", min_length=6)
    jobs =forms.MultipleChoiceField(choices=CHOICES ,widget=forms.SelectMultiple())
    cgu_accept =forms.BooleanField(initial=True, label="Accepter les CGU")
