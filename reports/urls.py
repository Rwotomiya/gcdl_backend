from django.urls import path
from .views import export_sales_pdf, export_sales_excel, export_procurement_excel
from .views import (
    export_credit_sales_excel, export_credit_sales_pdf,
    export_stock_excel, export_monthly_summary_excel
)

urlpatterns = [
    path('sales/pdf/', export_sales_pdf, name='export_sales_pdf'),
    path('sales/excel/', export_sales_excel, name='export_sales_excel'),
    path('procurement/excel/', export_procurement_excel, name='export_procurement_excel'),
    path('credit-sales/excel/', export_credit_sales_excel, name='export_credit_sales_excel'),
    path('credit-sales/pdf/', export_credit_sales_pdf, name='export_credit_sales_pdf'),
    path('stock/excel/', export_stock_excel, name='export_stock_excel'),
    path('summary/excel/', export_monthly_summary_excel, name='export_monthly_summary_excel'),
]
