import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect

#..........

def welcome(request):
    return render(request, 'welcome.html')

def galery_of_day(request):
    date = dt.date.today()
    return render(request, 'all_galery/today_galery.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_galery(request,past_date):
        try:
        # Converts data from the string Url
            date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

        except ValueError:
        # Raise 404 error when ValueError is thrown
            raise Http404()
            assert False

        if date == dt.date.today():
            return redirect(galery_of_day)

        return render(request, 'all_galery/today_galery.html', {"date": date})