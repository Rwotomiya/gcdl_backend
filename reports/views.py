from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Q, QuerySet,       Sum, Count
from django.utils.dateparse import parse_date
from xhtml2pdf import pisa
import pandas as pd
from inventory.models import Procurement, Stock, Produce
from sales.models import CreditSale, Sale


def export_sales_excel(request):
    # FILTERING
    filters = Q()
    if start_date := request.GET.get('start_date'):
        filters &= Q(date__date__gte=parse_date(start_date))
    if end_date := request.GET.get('end_date'):
        filters &= Q(date__date__lte=parse_date(end_date))
    if agent := request.GET.get('agent'):
        filters &= Q(sales_agent__username__iexact=agent)

    # FETCH FILTERED DATA
    sales: QuerySet = Sale.objects.select_related('produce', 'buyer').filter(filters)
    sales_data = sales.values_list(
        'produce__name', 'buyer__name', 'tonnage', 'amount_paid', 'date'
    )

    # FORMAT AS EXCEL
    df = pd.DataFrame(list(sales_data))
    df.columns = ['Produce', 'Buyer', 'Tonnage', 'Amount Paid', 'Date']
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="sales_report_filtered.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_sales_pdf(request):    
    sales: QuerySet = Sale.objects.select_related('produce', 'buyer').all()
    html = render_to_string("reports/sales_report.html", {"sales": sales})    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sales_report.pdf"'

    
    pisa_status = pisa.CreatePDF(html, dest=response)
    return response


def export_procurement_excel(request):
    # FILTERING
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    branch = request.GET.get('branch')

    filters = Q()
    if start_date:
        filters &= Q(date__date__gte=parse_date(start_date))
    if end_date:
        filters &= Q(date__date__lte=parse_date(end_date))
    if branch:
        filters &= Q(branch__icontains=branch)

    # FETCH FILTERED DATA
    procurements: QuerySet = Procurement.objects.select_related('produce', 'dealer').filter(filters)
    procurement_data = procurements.values_list(
        'produce__name', 'dealer__name', 'dealer__contact', 'tonnage', 'cost', 'selling_price', 'branch', 'date'
    )    

    # FORMAT AS EXCEL
    df = pd.DataFrame(list(procurement_data))
    df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

    df.columns = ['Produce', 'Dealer', 'Contact', 'Tonnage', 'Cost', 'Selling Price', 'Branch', 'Date']

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="procurement_report_filtered.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_credit_sales_excel(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    filters = Q()
    if start_date:
        filters &= Q(created_on__date__gte=parse_date(start_date))
    if end_date:
        filters &= Q(created_on__date__lte=parse_date(end_date))

    credit_sales: QuerySet = CreditSale.objects.select_related('produce', 'buyer').filter(filters)
    credit_sales_data = credit_sales.values_list(
        'buyer__name', 'buyer__contact', 'buyer__national_id', 'amount_due',
        'due_date', 'produce__name', 'created_on'
    )    

    df = pd.DataFrame(list(credit_sales_data))
    df['created_on'] = pd.to_datetime(df['created_on']).dt.strftime('%Y-%m-%d %H:%M:%S')
    df['Due Date'] = pd.to_datetime(df['Due Date']).dt.strftime('%Y-%m-%d')
    df.columns = ['Buyer Name', 'Contact', 'National ID', 'Amount Due', 'Due Date', 'Produce', 'Recorded On']

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="credit_sales_report.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_stock_excel(request):    
    stock: QuerySet = Stock.objects.select_related('produce')
    stock_data = stock.values_list('produce__name', 'available_tonnage')
    

    df = pd.DataFrame(list(stock_data))
    df.columns = ['Produce', 'Available Tonnage']

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="stock_report.xlsx"'
    df.to_excel(response, index=False)
    return response


def export_monthly_summary_excel(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    procurement_summary = Procurement.objects.filter(date__date__range=[start_date, end_date]).aggregate(
        total_tonnage=Sum('tonnage'),
        total_cost=Sum('cost')
    )
    sales_summary = Sale.objects.filter(date__date__range=[start_date, end_date]).aggregate(
        total_sales=Sum('amount_paid'),
        total_items=Count('id')
    )

    data = {
        "Metric": ["Total Procured (tons)", "Total Procurement Cost", "Total Sales Revenue", "Number of Sales"],
        "Value": [
            procurement_summary['total_tonnage'] or 0,
            procurement_summary['total_cost'] or 0,
            sales_summary['total_sales'] or 0,
            sales_summary['total_items'] or 0,
        ]
    }

    df = pd.DataFrame(data)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="monthly_summary.xlsx"'
    df.to_excel(response, index=False)
    return response
