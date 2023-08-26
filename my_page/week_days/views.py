
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

week_dict = {
    'monday': 'день недели понедельник',
    'tuesday': 'день недели вторник',
    'wednesday': 'день недели среда',
    'thursday': 'день недели четверг',
    'friday': 'день недели пятница',
    'saturday': 'день недели суббота',
    'sunday': 'день недели воскресенье'
}


def index(request):
    list_day = list(week_dict)
    """
    <ol>
        <li>monday</li>
        <li>tuesday</li>
        <li>wednesday</li>
        ...
    <ol>
    """
    li_elements = ''
    for day in list_day:
        redirect_path = reverse('week_name', args=[day])
        li_elements += f"<li> <a href='{redirect_path}'>{day.title()} </a> </li>"

    response = f"""
    <ol>
        {li_elements}
    </ol>
    """
    return HttpResponse(response)


def get_info_about_days(request, days: str):
    description = week_dict.get(days, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'Неизвестный день недели - {days}')


def get_info_about_days_by_number(request, days: str):
    list_day = list(week_dict)
    if days > len(list_day):
        return HttpResponseNotFound(f'Неправильный порядковый номер дня недели - {days}')
    name_day = list_day[days-1]
    redirect_url = reverse('week_name', args=(name_day,))
    return HttpResponseRedirect(redirect_url)
