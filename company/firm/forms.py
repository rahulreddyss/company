from django import forms

# from pagedown.widgets import PagedownWidget

from .models import Employees


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = [
            "user",
            "department",
            "employee_no",
            "title",
            "mobile",
            "country",
            "state",
            "city",
            "pincode",
            "salary",
        ]
