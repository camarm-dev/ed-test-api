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
        response['data'].extends(timetable[str(day_number)])
        start_datetime += datetime.timedelta(days=1)

    return response
