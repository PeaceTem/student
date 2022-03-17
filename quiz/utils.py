import random

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, link_callback=fetch_resources)
     if not pdf.err:
          return HttpResponse(result.getvalue(), content_type='application/pdf')
     return None

def fetch_resources(uri, rel):
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    return path





def sortKey(e):
    return e[0]




def randomCoin():
     value = (1,2,3,4,5)
     goal = random.choices(value, weights=[22,10,5,2,1], k=1)
     return goal
print(randomCoin()[0])



def quizRandomCoin():
     value=(3,5,7)
     goal = random.choices(value, weights=[100,10,1], k=1)
     return goal[0]

print(quizRandomCoin())








