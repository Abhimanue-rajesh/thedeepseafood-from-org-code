from django import forms
from company.models import (
    CompanyTestimonial,
    AboutUs,
    ManagementTeam,
    SEO,
    BlogDetails,
    BlogImage,
    Certification,
    Brand,
)

from django.forms import inlineformset_factory


class CompanyTestimonialForm(forms.ModelForm):
    class Meta:
        model = CompanyTestimonial
        fields = "__all__"


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = "__all__"


class ManagementTeamForm(forms.ModelForm):
    class Meta:
        model = ManagementTeam
        fields = "__all__"


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = "__all__"


class SeoForm(forms.ModelForm):
    class Meta:
        model = SEO
        fields = [
            "page_name",
            "meta_title",
            "meta_author",
            "meta_description",
            "meta_keywords",
            "meta_json_ld",
        ]


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"


class BlogDetailsForm(forms.ModelForm):
    class Meta:
        model = BlogDetails
        fields = "__all__"


class BlogImageForm(forms.ModelForm):
    class Meta:
        model = BlogDetails
        fields = "__all__"


# Inline formset to handle BlogImage with BlogDetails
BlogImageFormSet = inlineformset_factory(
    BlogDetails,
    BlogImage,
    fields=("image",),
    extra=3,  # Number of empty image forms to display
    can_delete=False,
)
