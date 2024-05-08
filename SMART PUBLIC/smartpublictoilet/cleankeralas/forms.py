from django import forms
from .models import books,reports
class booksForm(forms.ModelForm):
    
    class Meta:
        model = books
        fields = "__all__"
        labels={"toilet_by_serial":"SERIAL NUMBER",
                
                "s_email":"EMAIL",
                 "s_name":"TOILET PLACE",
                 "s_phone":"MOBILE NUMBER",
                  "c_name":"NAME"
            
        }

class complaintForm(forms.ModelForm):
    
    class Meta:
        model = reports
        fields = "__all__"
        labels={'r_name':'NAME',
                'r_phone':" MOBILE NUMBER",
                's_name':"TOILET PLACE",
                't_by_serial':"SERIAL NUMBER",
                    'r_email':"EMAIL",
                    "t_report":"REPORT",
        }
