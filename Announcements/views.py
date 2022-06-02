from datetime import datetime, timedelta

from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

""" Announcements dictionary
keys -> announcement ID || values -> [announcement text , announcement date] 
"""
# announcements = {}
# test cases
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


# View Announcements page
def Announcement_Page(request, *args, **kwargs):
    # default value for period is 'All', used to focus on the period button (javascript use)
    period = "all"

    # when the request method is POST
    if request.method == "POST":
        # to use the POST method on the same page
        # if there is a POST request passing a delete statement then it is a delete POST request
        try:
            if request.POST["Delete"]:
                # delete specific announcement
                Delete_Announcement(request)

        # if there is a POST request without passing a delete statement then it is a create POST request
        except MultiValueDictKeyError:
            # create new announcement
            Create_Announcement(request)

    # passing all the announcements data to the page
    announcements_list = []

    # when the request method is GET
    try:
        # passing a specific period with GET request
        period_req = request.GET["period"]
        # sort announcements by key (reverse) from the newest announcement to the oldest
        for key, value in sorted(announcements.items(), reverse=True):
            if period_req == "All":
                announcements_list.append({"id": key,
                                           "text": value[0],
                                           "date": value[1]})

            elif period_req == "Today":
                period = "today"
                if value[1] >= datetime.now() - timedelta(hours=24):
                    announcements_list.append({"id": key,
                                               "text": value[0],
                                               "date": value[1]})

            elif period_req == "Last 7 Days":
                period = "week"
                if value[1] >= datetime.now() - timedelta(days=7):
                    announcements_list.append({"id": key,
                                               "text": value[0],
                                               "date": value[1]})

            elif period_req == "Last 30 Days":
                period = "month"
                if value[1] >= datetime.now() - timedelta(days=30):
                    announcements_list.append({"id": key,
                                               "text": value[0],
                                               "date": value[1]})

    # when there is no period data passed (default GET request)
    except MultiValueDictKeyError:
        for key, value in sorted(announcements.items(), reverse=True):
            announcements_list.append({"id": key,
                                       "text": value[0],
                                       "date": value[1]})

    return render(request, "index.html", {"announcements": announcements_list, "period": period})


# create new announcement
def Create_Announcement(request, *args, **kwargs):
    # test if there are any announcements before
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


# delete specific announcement that is passing announcement ID
def Delete_Announcement(request, *args, **kwargs):
    announcements.pop(int(request.POST["announcement_id"]))
