# Define functions that can be used by the `action` field !
import datetime

from main import read_json

# id: number;
# text: string;
# matiere: string;
# codeMatiere: string;
# typeCours: string;
# start_date: string;
# end_date: string;
# color: string;
# dispensable: boolean;
# dispense: number;
# prof: string;
# salle: string;
# classe: string;
# classeId: number;
# classeCode: string;
# groupe: string;
# groupeCode: string;
# isFlexible: boolean;
# groupeId: number;
# icone: string;
# isModifie: boolean;
# contenuDeSeance: boolean;
# devoirAFaire: boolean;
# isAnnule: boolean;

# TODO: fill timetable !
timetable = read_json('data/timetable.json')
# TODO: fill homeworks
homeworks = read_json('data/homeworks.json')


def get_timetable(response, data):
    start_date = data['dateDebut']
    end_date = data['dateFin']
    with_gaps = data['avecTrous']

    # Parsing
    start_year, start_month, start_day = start_date.split("-")
    end_year, end_month, end_day = end_date.split("-")

    # Datetime objects
    start_datetime = datetime.datetime(int(start_year), int(start_month), int(start_day))
    end_datetime = datetime.datetime(int(end_year), int(end_month), int(end_day))

    # Fill EDT by weekday
    while start_datetime <= end_datetime:
        day_number = start_datetime.weekday()
        response['data'].extend(timetable[str(day_number)])
        start_datetime += datetime.timedelta(days=1)
    # TODO; need to sort ?
    return response


def get_week(date):
    """Return the full week (Sunday first) of the week containing the given date.

    'date' may be a datetime or date instance (the same type is returned).
    """
    monday = date - datetime.timedelta(days=date.weekday())
    date = monday
    for n in range(7):
        yield date
        date += datetime.timedelta(days=1)


def get_homeworks(response):
    week = get_week(datetime.datetime.now())
    for day in week:
        weekday = day.weekday()
        key = day.strftime("%Y-%m-%d")
        response['data'][key] = homeworks[str(weekday)]
    print(response)
    return response


def get_homeworks_day(request, response):
    day = request.path_params.get('day')
    year, month, day = day.split("-")
    date = datetime.datetime(int(year), int(month), int(day))
    day_number = date.weekday()

    response['data']['matieres'] = homeworks[str(day_number)]
    return response
