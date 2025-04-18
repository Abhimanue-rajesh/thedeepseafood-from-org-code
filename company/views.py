# from django.shortcuts import render
from django.urls import reverse_lazy
from company.models import (
    CompanyTestimonial,
    AboutUs,
    ManagementTeam,
    SEO,
    BlogDetails,
    Certification,
    Brand,
)
from company.forms import (
    CompanyTestimonialForm,
    AboutUsForm,
    ManagementTeamForm,
    SeoForm,
    # BlogForm,
    CertificationForm,
    BrandForm,
)
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib import messages


class CompanyTestimonialListView(ListView):
    model = CompanyTestimonial
    template_name = "company/list_testimonial.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_testimonial"] = CompanyTestimonial.objects.filter(status=True)
        context["page_title"] = "List Testimonial"
        return context


class CompanyTestimonialCreateView(CreateView):
    model = CompanyTestimonial
    template_name = "create_update.html"
    form_class = CompanyTestimonialForm
    success_url = reverse_lazy("view_company_testimonial")
    extra_context = {
        "page_title": "Create Testimonial",
    }

    def form_valid(self, form):
        messages.success(self.request, "Testimonial Added Successfully...!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class CompanyTestimonialUpdateView(UpdateView):
    model = CompanyTestimonial
    form_class = CompanyTestimonial
    template_name = "create_update.html"
    success_url = reverse_lazy("view_company_testimonial")
    extra_context = {
        "page_title": "Update Testimonial",
    }

    def form_valid(self, form):
        messages.success(self.request, "Testimonial Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# About
class AboutListView(ListView):
    model = AboutUs
    template_name = "company/list_about.html"
    extra_context = {"page_title": "About List"}
    # paginate_by=2
    # ordering=["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_about"] = AboutUs.objects.filter(status=True)
        return context


class AboutCreateView(CreateView):
    model = AboutUs
    template_name = "create_update.html"
    form_class = AboutUsForm
    success_url = reverse_lazy("view_about_us")
    extra_context = {
        "page_title": "Create About Us",
    }

    def form_valid(self, form):
        messages.success(self.request, "About Us Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class AboutUpdateView(UpdateView):
    model = AboutUs
    template_name = "create_update.html"
    form_class = AboutUsForm
    success_url = reverse_lazy("view_about_us")
    extra_context = {
        "page_title": "Update About Us",
    }

    def form_valid(self, form):
        messages.success(self.request, "About Us Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# Team Member


class TeamListView(ListView):
    model = ManagementTeam
    template_name = "company/list_team_member.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_team_member"] = ManagementTeam.objects.filter(status=True)
        context["page_title"] = "Team Member List"
        return context


class TeamCreateView(CreateView):
    model = ManagementTeam
    template_name = "create_update.html"
    form_class = ManagementTeamForm
    success_url = reverse_lazy("view_team")
    extra_context = {
        "page_title": "Create Team",
    }

    def form_valid(self, form):
        messages.success(self.request, "Team Added Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class TeamUpdateView(UpdateView):
    model = ManagementTeam
    template_name = "create_update.html"
    form_class = ManagementTeamForm
    success_url = reverse_lazy("view_team")
    extra_context = {
        "page_title": "Update Team",
    }

    def form_valid(self, form):
        messages.success(self.request, "Team Updated Successfully...!!")

        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# SEO
class SeoListView(ListView):
    model = SEO
    template_name = "company/list_seo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "SEO List"
        context["seo"] = SEO.objects.all()
        return context


class SeoCreateView(CreateView):
    model = SEO
    template_name = "create_update.html"
    form_class = SeoForm
    extra_context = {"page_title": "Create SEO"}
    success_url = reverse_lazy("list_seo")

    def form_valid(self, form):
        messages.success(self.request, "SEO added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class SeoUpdateView(UpdateView):
    model = SEO
    template_name = "create_update.html"
    form_class = SeoForm
    extra_context = {"page_title": "Update SEO"}
    success_url = reverse_lazy("list_seo")

    def form_valid(self, form):
        messages.success(self.request, "SEO Updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# Brand
class BrandListView(ListView):
    model = Brand
    template_name = "company/list_brand.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Brand List"
        context["all_brand"] = Brand.objects.filter(status=True)
        return context


class BrandCreateView(CreateView):
    model = Brand
    template_name = "create_update.html"
    form_class = BrandForm
    extra_context = {"page_title": "Create Brand"}
    success_url = reverse_lazy("list_brand")

    def form_valid(self, form):
        messages.success(self.request, "Brand added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


class BrandUpdateView(UpdateView):
    model = Brand
    template_name = "create_update.html"
    form_class = BrandForm
    extra_context = {"page_title": "Update Brand"}
    success_url = reverse_lazy("list_brand")

    def form_valid(self, form):
        messages.success(self.request, "Brand Updated successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)
        return super().form_invalid(form)


# blog
class BlogListView(ListView):
    model = BlogDetails
    template_name = "company/list_blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "Blog List"
        context["all_blogs"] = BlogDetails.objects.filter(status=True)
        return context


# class BlogCreateView(CreateView):
#     model = BlogDetails
#     template_name = "create_blog.html"
#     form_class = BlogForm
#     success_url = reverse_lazy("list_blog")
#     extra_context = {"page_title": "Create Blog"}

#     def form_valid(self, form):
#         messages.success(self.request, "Blog created Successfully")
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         for error_list in form.errors.values():
#             for errors in error_list:
#                 messages.error(self.request, errors)
#         return super().form_invalid(form)


# class BlogUpdateView(UpdateView):
#     model = BlogDetails
#     template_name = "create_update.html"
#     form_class = BlogForm
#     success_url = reverse_lazy("list_blog")
#     extra_context = {"page_title": "Update Blog"}

#     def form_valid(self, form):
#         messages.success(self.request, "Blog UpdatedSuccessfully")
#         return super().form_valid(form)

#     def form_invalid(self, form):
#         for error_list in form.errors.values():
#             for errors in error_list:
#                 messages.error(self.request, errors)
#         return super().form_invalid(form)


class CertificationsListView(ListView):
    model = Certification
    template_name = "company/list_certification.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_certification"] = Certification.objects.filter(status=True)
        context["page_title"] = "List Certification"

        return context


class CertificationCreateView(CreateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy("list_certification")
    extra_context = {"page_title": "Create a Certification"}

    def form_valid(self, form):
        messages.success(self.request, "Certification Added Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)


class CertificationUpdateView(UpdateView):
    model = Certification
    form_class = CertificationForm
    success_url = reverse_lazy("list_certification")
    extra_context = {"page_title": "Update Certification"}

    def form_valid(self, form):
        messages.success(self.request, "Certification Updated Successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        for error_list in form.errors.values():
            for errors in error_list:
                messages.error(self.request, errors)

        return super().form_invalid(form)
