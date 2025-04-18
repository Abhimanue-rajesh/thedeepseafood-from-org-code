from django.urls import path
from company import views

urlpatterns = [
    # Company Testimonials
    path(
        "list/company-testimonial",
        views.CompanyTestimonialListView.as_view(),
        name="list_company_testimonial",
    ),
    path(
        "create/testimonial",
        views.CompanyTestimonialCreateView.as_view(),
        name="create_company_testimonial",
    ),
    path(
        "update/testimonial/<slug:slug>",
        views.CompanyTestimonialUpdateView.as_view(),
        name="update_company_testimonial",
    ),
    # About us
    path(
        "list/about",
        views.AboutListView.as_view(),
        name="list_about_us",
    ),
    path(
        "create/about",
        views.AboutCreateView.as_view(),
        name="create_about_us",
    ),
    path(
        "update/about/<slug:slug>",
        views.AboutUpdateView.as_view(),
        name="update_about_us",
    ),
    # Team Member
    path(
        "list/team/",
        views.TeamListView.as_view(),
        name="list_team",
    ),
    path(
        "create/management-team/",
        views.TeamCreateView.as_view(),
        name="create_team",
    ),
    path(
        "update/team/<slug:slug>",
        views.TeamUpdateView.as_view(),
        name="update_team",
    ),
    # SEO
    path(
        "list/seo/",
        views.SeoListView.as_view(),
        name="list_seo",
    ),
    path(
        "create/seo/",
        views.SeoCreateView.as_view(),
        name="create_seo",
    ),
    path(
        "update/seo/<slug:slug>",
        views.SeoUpdateView.as_view(),
        name="update_seo",
    ),
    # brand
    path(
        "list/brand/",
        views.BrandListView.as_view(),
        name="list_brand",
    ),
    path(
        "create/brand/",
        views.BrandCreateView.as_view(),
        name="create_brand",
    ),
    path(
        "update/brand/<slug:slug>",
        views.BrandUpdateView.as_view(),
        name="update_brand",
    ),
    # Blog
    path(
        "list/blog/",
        views.BlogListView.as_view(),
        name="list_blog",
    ),
    # path(
    #     "create/blog/",
    #     views.BlogCreateView.as_view(),
    #     name="create_blog",
    # ),
    # path(
    #     "update/blog/<slug:slug>",
    #     views.BlogUpdateView.as_view(),
    #     name="update_blog",
    # ),
    # certification
    path(
        "list/certification/",
        views.CertificationsListView.as_view(),
        name="list_certification",
    ),
    path(
        "create/certification/",
        views.CertificationCreateView.as_view(),
        name="create_certification",
    ),
    path(
        "update/certification/<slug:slug>",
        views.CertificationUpdateView.as_view(),
        name="update_certifications",
    ),
]
