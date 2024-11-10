from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime , timedelta
from notification_manager import NotificationManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search =  FlightSearch()
notification_manager = NotificationManager()
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))



ORIGIN_CITY_IATA =  "MAA"
for destination in sheet_data:
     flight = flight_search.check_flights(
       ORIGIN_CITY_IATA ,
       destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today)
     msssg = ("price are down go and check ")
notification_manager.make_notification(msssg)
#  if flight.price < destination["lowestPrice"]:

    #
    # 
    # notification_manager.make_notification(msessage=msssg)
