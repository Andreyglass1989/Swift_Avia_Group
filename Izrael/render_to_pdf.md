1. https://www.codingforentrepreneurs.com/blog/html-template-to-pdf-in-django/


A guide to using an HTML template to create a PDF via a render_to_pdf utility function.

   1. Open your Django project or create a blank one

   2. Install xhtml2pdf docs:

    Using Python 3
    	pip install --pre xhtml2pdf 

    Using Python 2	
		pip install xhtml2pdf

	3. Add a utils.py module to your project:

	4. Write the render_to_pdf function(create file utils.py):
---------------------------------------------------
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
-----------------------------------------------------------

	5. Create html template such as invoice.html in templates/pdf Recommended to use internal/inline stylesheets :

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <title>Title</title>
        <style type="text/css">
            body {
                font-weight: 200;
                font-size: 14px;
            }
            .header {
                font-size: 20px;
                font-weight: 100;
                text-align: center;
                color: #007cae;
            }
            .title {
                font-size: 22px;
                font-weight: 100;
               /* text-align: right;*/
               padding: 10px 20px 0px 20px;  
            }
            .title span {
                color: #007cae;
            }
            .details {
                padding: 10px 20px 0px 20px;
                text-align: left !important;
                /*margin-left: 40%;*/
            }
            .hrItem {
                border: none;
                height: 1px;
                /* Set the hr color */
                color: #333; /* old IE */
                background-color: #fff; /* Modern Browsers */
            }
        </style>
    </head>
    <body>
        <div class='wrapper'>
            <div class='header'>
                <p class='title'>Invoice # </p>
            </div>
        <div>
        <div class='details'>
            Bill to: <br/>
            Amount:  <br/>
            Date: 
            <hr class='hrItem' />
        </div>
    </div>
    </body>
</html>


------------------------------------------
6. 
from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
from .utils import render_to_pdf
from django.template.loader import get_template



class GeneratePDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('packing.html')
		context = {
			"invoice_id": 123,
			"customer_name": "John Cooper",
			"amount": 1399.99,
			"today": "Today",
		}
		html = template.render(context)
		return HttpResponse(html)


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


---------------------------------------

7. Final view.py:

from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import View
# Create your views here.
from .utils import render_to_pdf
from django.template.loader import get_template



class GeneratePDF(View):
	def get(self, request, *args, **kwargs):
		template = get_template('packing.html')
		context = {
			"invoice_id": 123,
			"customer_name": "John Cooper",
			"amount": 1399.99,
			"today": "Today",
		}
		html = template.render(context)
		pdf = render_to_pdf('packing.html', context)
		if pdf:
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "Packing_%s.pdf" %("Izrael_4.01.19")
			content = "inline; filename='%s'" %(filename)
			# download = 	request.GET.get("download")
			# if download:
			# 	content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not found")