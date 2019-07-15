from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView

# Create your views here.
# from .utils import render_to_pdf
from django.template.loader import get_template

from Izrael.models import IzraelDataForPacking




class BoxListView(ListView):
	model = IzraelDataForPacking
	template_name = "box_ukr.html"

	def get_context_data(self, **kwargs):
		context = super(BoxListView, self).get_context_data(**kwargs)
		boxs1 = IzraelDataForPacking.objects.all().last()
		# boxs = IzraelDataForPacking.objects.filter(date_add__contains="2019-01-30").order_by('box_number')
		boxs = IzraelDataForPacking.objects.filter(date_add__contains= boxs1.date_add.strftime("%Y-%m-%d")).order_by('box_number')
		context = {
			"boxs": boxs,
		}
		return context



# class GeneratePDF(View):
# 	def get(self, request, *args, **kwargs):
# 		template = get_template('packing.html')

# 		cargo = IzraelDataForPacking.objects.filter(date_add__contains="2019-01-18").order_by('box_number')		# print(cargo.count())

# 		context = {
# 			"invoice_id": 123,
# 			"customer_name": "John Cooper",
# 			"amount": 1399.99,
# 			"today": "Today",
# 			"cargo": cargo,
# 		}
# 		html = template.render(context)
# 		pdf = render_to_pdf('packing.html', context)
# 		if pdf:
# 			response = HttpResponse(pdf, content_type='application/pdf')
# 			filename = "Packing_%s.pdf" %("Izrael_18.01.19")
# 			content = "inline; filename=%s" %(filename)

# 			response['Content-Disposition'] = content
# 			return response
# 		return HttpResponse("Not found")


# def generate_view(request, *args, **kwargs):
# 	template = get_template('packing.html')
# 	context = {
# 		"invoice_id": 123,
# 		"customer_name": "John Cooper",
# 		"amount": 1399.99,
# 		"today": "Today",
# 	}
# 	html = template.render(context)
# 	return HttpResponse(html)