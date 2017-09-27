from django import forms

from django.core import validators

# def validate_password(value):
#     if value % 2 != 0:
#         raise ValidationError(
#             _('%(value)s is not an even number'),
#             params={'value': value},
#         )

from .models import Country, Conference

def set_field_html_name(cls, new_name):
    """
    This creates wrapper around the normal widget rendering,
    allowing for a custom field name (new_name).
    """
    old_render = cls.widget.render
    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)

    cls.widget.render = _widget_render_wrapper

class RegisterForm(forms.Form):

    fname = forms.CharField(label='Firstname', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"Firstname",
                                    }
                                ))
    lname = forms.CharField(label='Lastname', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"Lastname",
                                    }
                                ))
    email = forms.CharField(label='Email Address', required=True, max_length=100,
                            validators=[validators.validate_email],
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"Email Address",
                                    }
                                ))
    password = forms.CharField(label='Password', required=True, max_length=100,
                            widget=forms.PasswordInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"Password"
                                    }
                                ))
    confirm_password = forms.CharField(label='Confirm Password',required=True,  max_length=100,
                            widget=forms.PasswordInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"Confirm Password"
                                    }
                                ))
    def clean(self):

        cleaned_data = super(RegisterForm, self).clean()

        password = cleaned_data.get("password")

        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            # Only do something if both fields are valid so far.
            if confirm_password != password:

                raise forms.ValidationError(
                    "Confirm Password is not the same as Password "
                )


class CorrespondenceForm(forms.Form):


    address1 = forms.CharField(label='address1', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"address1",
                                    }
                                ))
    address2 = forms.CharField(label='address2', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"address2",
                                    }
                                ))
    city = forms.CharField(label='city', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"city",
                                    }
                                ))
    state = forms.CharField(label='state', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"state",
                                    }
                                ))

    country = forms.ModelChoiceField(queryset= Country.objects.order_by('country'),
                                        to_field_name='id',
                                        empty_label='Select a Country',
                                        required=True,
                                        widget=forms.Select(
                                            attrs={
                                                'class': 'form-control',
                                                'placeholder':"Country",
                                                }
                                            )
                            )

class AuthorForm(forms.Form):
    title = forms.CharField(label='Title', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                        'class': 'form-control',
                                        'placeholder':"Title",
                                        'data-bind' : 'value: title'
                                    }
                                ))
    # set_field_html_name(title, 'author[title]')

    fname = forms.CharField(label='Firstname', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                        'class': 'form-control',
                                        'placeholder':"Firstname",
                                        'data-bind' : 'value: firstName',
                                    }
                                ))

    lname = forms.CharField(label='Lastname', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                        'class': 'form-control',
                                        'placeholder':"Lastname",
                                        'data-bind' : 'value: lastName',
                                    }
                                ))
    # set_field_html_name(lname, 'author[lname]')

    email = forms.CharField(label='email', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                        'class': 'form-control',
                                        'placeholder':"email",
                                        'data-bind' : 'value: email',
                                    }
                                ))

    organisation = forms.CharField(label='Organisation', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                        'class': 'form-control',
                                        'placeholder':"organisation",
                                        'data-bind' : 'value: organisation',
                                    }
                                ))

    CHECKBOX_CHOICES = ((True, True), (False, False))

    speaker = forms.ChoiceField(label='Speaker', required=False, choices = CHECKBOX_CHOICES,

                            widget=forms.CheckboxInput(
                                attrs={
                                    'class': 'form-control',
                                    'value':"True"
                                    }
                                ))

class PaperForm(forms.Form):

    paper_title = forms.CharField(label='Title', required=True, max_length=100,
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"Title",
                                    }
                                ))

    abstract = forms.CharField(label='Abstract', required=True, max_length=100,
                            widget=forms.Textarea(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"Abstract",
                                    }
                                ))

    keywords = forms.CharField(label='keywords', required=True, max_length=100,
                            widget=forms.Textarea(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder':"keywords",
                                    }
                                ))

    upload = forms.FileField(label='upload', required=True,
                                    widget=forms.FileInput(
                                        attrs={
                                            'class': 'form-control',
                                            }
                                    ))
