from django.views.generic import TemplateView
from django.views.generic import View
from django.http import JsonResponse

class SqlStandardsView(TemplateView):
    template_name = "sql_standards.html"

class SqlStandardsResultView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        return JsonResponse({'a': 1})