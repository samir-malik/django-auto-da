from django.views.generic import TemplateView

class SqlStandardsView(TemplateView):
    template_name = "sql_standards.html"

class SqlStandardsResultView(TemplateView):
    template_name = "sql_standards_results.html"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)