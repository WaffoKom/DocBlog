from django import forms
from blog.models import BlogPost

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

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("Le pseudo ne doit pas contenir de symbole $")
        return pseudo


class BlogPostForm(forms.ModelForm):
    class Meta :
        model =BlogPost
        fields =[
            "title",
            "date",
            "category",
            "description",

        ]
        labels ={
            "title":"Titre",
             "category":"Categorie",
        }
        widgets ={"date":forms.SelectDateWidget(years=range(1990, 2040))}




