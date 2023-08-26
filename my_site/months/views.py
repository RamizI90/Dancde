
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

month_dict = {
    'January': 'месяц январь  31 день',
    'February': 'месяц февраль 28-29 дней',
    'March': 'месяц март 31 день',
    'April': 'месяц апрель 30 дней',
    'May': 'месяц май 31 день',
    'June': 'месяц июнь 30 дней',
    'July': 'месяц июль 31 день',
    'August': 'месяц август 31 день',
    'September': 'месяц сентябрь 30 дней',
    'October': 'месяц октябрь 31 день',
    'November': 'месяц ноябрь 30 дней',
    'December': 'месяц декабрь 31 день',
}

seasons_dict = {
    'winter': ['December', 'January', 'February'],
    'spring': ['March', 'April', 'June'],
    'summer': ['June', 'July', 'August'],
    'autumn': ['September', 'October', 'November'],
}


def index(request):
    list_month = list(month_dict)

    li_elements = ''
    for mon in list_month:
        redirect_path = reverse('month_name', args=[mon])
        li_elements += f"<li> <a href='{redirect_path}'>{mon.title()} </a> </li>"

    response = f"""
    <ol>
        {li_elements}
    </ol>
    """
    return HttpResponse(response)


def get_info_month(request, month: str):
    response = render_to_string('months/info_months.html')
    return HttpResponse(response)


def get_info_month_by_number(request, month: str):
    list_month = month_dict
    if month > len(list_month):
        return HttpResponseNotFound(f'Неправильный порядковый номер месяца - {month}')
    name_month = list_month[month-1]
    redirect_url = reverse('month_name', args=(name_month,))
    return HttpResponseRedirect(redirect_url)


def index_season(request):
    li_elements = ''
    for seas in seasons_dict:
        li_elements += f'<li> <a href="{seas}/"> {seas.title()} </a> </li>'
    return HttpResponse(f'<ol> {li_elements} </ol>')


def get_season(request, season):
    li_elements = ''
    for seas in seasons_dict[season]:
        redirect_path = reverse('month_name', args=[seas])
        li_elements += f'<li> <a href = "{redirect_path}"> {seas.title()} </a> </li>'
    return HttpResponse(f'<ol> {li_elements} </ol>')
