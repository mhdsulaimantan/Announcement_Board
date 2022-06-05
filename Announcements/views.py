from datetime import datetime, timedelta

from django.http import HttpResponseBadRequest
from django.shortcuts import render

""" Announcements dictionary
keys -> announcement ID || values -> [announcement text , announcement date] 
"""
announcements = {0: ["Hi, I have a question. Where i could find dancing courses?", datetime.now() - timedelta(days=50)],
                 1: ["Good Morning :), Anyone up to do some hiking on the weekend?",
                     datetime.now() - timedelta(days=44)],
                 2: ["Help, I lost my credit card on my way to work. Should I contact and inform my bank?",
                     datetime.now() - timedelta(days=10)],
                 3: ["hey, I want to get a cat. Where could I find a place to adopt one, thank you ^_^",
                     datetime.now() - timedelta(days=5)],
                 4: ["Would like to find someone interested in taking cooking lessons, Anybody?",
                     datetime.now() - timedelta(days=3)],
                 5: ["Hello, Where I could find a place to buy new furniture for my apartment?",
                     datetime.now() - timedelta(hours=18)],
                 6: ["Found a wallet in my way home, Anyone lost one recently?", datetime.now() - timedelta(hours=8)],
                 }


def Announcement_Page(request, *args, **kwargs):
    # default value for period (date filter)
    period = "all"

    try:
        if request.method == "POST":
            period = request.POST["period"]
            # if there is a POST request passing a delete statement
            if request.POST.get("delete"):
                delete_announcement(request)
            # if there is a POST request passing a create statement
            elif request.POST.get("create"):
                create_announcement(request)

        elif request.method == "GET":
            # passing a specific period with GET request
            if request.GET.get("period"):
                period = request.GET["period"]

    except HttpResponseBadRequest as err:
        raise err

    return render(request, "index.html", {"announcements": show_based_on_period(period), "period": period})


def create_announcement(request, *args, **kwargs):
    # exist announcements
    if announcements:
        # next announcement id -> get last announcement id and add 1
        announcement_id = list(announcements.keys())[-1] + 1

    # there is no announcements
    else:
        announcement_id = 0

    # get the current date when the announcement is created
    current_date = datetime.now()
    # add new announcement to the announcements dictionary
    announcements[announcement_id] = [request.POST["announcement_text"], current_date]


def delete_announcement(request, *args, **kwargs):
    announcements.pop(int(request.POST["announcement_id"]))


def show_based_on_period(period):
    announcements_list = []
    # sort announcements by key (reverse) from the newest announcement to the oldest
    for key, value in sorted(announcements.items(), reverse=True):
        if period == "all":
            announcements_list.append({"id": key,
                                       "text": value[0],
                                       "date": value[1]})

        elif period == "today":
            if value[1] >= datetime.now() - timedelta(hours=24):
                announcements_list.append({"id": key,
                                           "text": value[0],
                                           "date": value[1]})

        elif period == "week":
            if value[1] >= datetime.now() - timedelta(days=7):
                announcements_list.append({"id": key,
                                           "text": value[0],
                                           "date": value[1]})

        elif period == "month":
            if value[1] >= datetime.now() - timedelta(days=30):
                announcements_list.append({"id": key,
                                           "text": value[0],
                                           "date": value[1]})

    return announcements_list
