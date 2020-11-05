from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

api_v1_docs = [
    path('openapi', get_schema_view(
        title="Pizzapi",
        description="Pizza APIs",
        version="1.0.0"
    ), name='openapi-schema'),
    path('docs/',TemplateView.as_view(
        template_name='swagger-docs.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui')
]


urlpatterns = [
    path('api/v1/', include(api_v1_docs)),
    path('api/v1/', include('products.urls'))
]
