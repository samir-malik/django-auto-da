from django.views.generic import TemplateView
from django.views.generic import View
from django.http import JsonResponse

class SqlStandardsView(TemplateView):
    template_name = "sql_standards.html"

class SqlStandardsResultView(TemplateView):
    template_name = "sql_standards_results.html"