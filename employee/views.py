import io
import uuid
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.http import FileResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus.flowables import DocAssign, DocExec, DocPara, DocIf, DocWhile
from company.models import UserCompanyModel

from employee.models import EmployeeModel
from employee.forms import AddEmployeeForm, EditEmployeeForm
# Create your views here.
class EmployeeListView(TemplateView):
    template_name ='employee/employee_index.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        data = EmployeeModel.objects.filter(company=self.request.user.default_company_key).order_by('-add_date')

        p = Paginator(data, 8)
        
        try:
            page_number = self.request.GET.get('page')

        
            page_obj = p.get_page(page_number)
        

            context['employees']  = page_obj
        except:
            context['employees'] = p.get_page(1)

        
        return context


class EmployeeCreateView(TemplateView):
    template_name = 'employee/employee_create.html'
    form_class = AddEmployeeForm
    success_url = reverse_lazy('gen-employees')
    model = EmployeeModel

    def post(self, request, **kwargs):

        form = AddEmployeeForm(request.POST )

        if form.is_valid():
            form.save(self.request.user)

            return redirect(reverse_lazy('gen-employees'))
        


    def get_context_data(self, **kwargs) :

        context = super().get_context_data(**kwargs)


        context['form'] = AddEmployeeForm()
        return context
    # def get_success_url(self) :
    #     return reverse_lazy('gen-employees')

class EmployeeUpdateView(UpdateView):
    template_name = 'employee/employee_update.html'
    form_class = EditEmployeeForm
    success_url = reverse_lazy('gen-employees')
    model = EmployeeModel

    def form_valid(self, form):

        form.save(self.request.user)
        return super().form_valid(form)
    
    

class EmployeeDeleteView(DeleteView):
    model = EmployeeModel
    template_name = 'employee/employee_delete.html'
    success_url = reverse_lazy('gen-employees')

class EmployeeToggleView(View):

    def get(self,request, *args, **kwargs):
        
        pk = kwargs.get('pk')
        print("pk",pk)
        employee = EmployeeModel.objects.get(pk=pk)
        employee.toggleupdate()

        return redirect(reverse_lazy('gen-employees'))

class EmployeeDownloadActive(View):

    # def post(self, request, *args, **kwargs):
    #     pass

    

    def get(self, request):
        
        buffer = io.BytesIO()
        #p  = canvas.Canvas(buffer)

        company = UserCompanyModel.objects.get(id=request.user.default_company)

        employees = EmployeeModel.objects.filter(company=self.request.user.default_company, is_active=True).values(
             'unique_id','first_name', 'middle_name','last_name' )

        employee_list = list(employees)

        emp_tup = self.to_tuple(employee_list)

        print(emp_tup)

        print(employee_list)
        doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=72, leftMargin=72, bottomMargin=18)
        
        #p.drawString(100,100, str(company.company_name))

        #p.showPage()
        #p.save()

        cscreen_info = 'Covered Screen Company ActiveList'

        company_name = company.company_name

        header_text =  cscreen_info.capitalize()

        header_company = company_name.capitalize()

        header_table = Table([(header_text, header_company)], colWidths=[8*cm], rowHeights=[5*cm])

        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'), 
            ('ALIGN', (3,0), (-1,-1), 'LEFT'),
            ('ALIGN', (1,0),(1,0), 'RIGHT')
        ]))


        content_table = Table(data=emp_tup)

        content_table.setStyle(TableStyle([('INNERGRID', (0,0), (1, -1), 0.25, colors.gray), 
                    ('ALIGN', (3,0), (1,-1), 'RIGHT')
        ]))


        p_data = [(header_table, ), (content_table, )]
        layout_table = Table(p_data)
        layout_table.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER')]))

        doc.build([layout_table])

        buffer.seek(0)

        name = uuid.uuid4().hex + ".pdf"

        return FileResponse(buffer, as_attachment=True, filename=name)


    def to_tuple(self, list_in):

        out_tup = []
        for val in list_in:

            pre = []
            for k,v in val.items():
                out = pre.append(v)
            
            out_tup.append(tuple(pre))
        
        return out_tup




            

