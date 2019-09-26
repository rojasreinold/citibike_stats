import pprint
from gbfs.client import GBFSClient

def main():
  client = GBFSClient('https://gbfs.citibikenyc.com/gbfs/gbfs.json', 'en')
  station_names = all_stations_basic_info(client)

  pp = pprint.PrettyPrinter(indent=2)
  #pp.pprint(all_station_information)
  #print(stations_information)
  pp.pprint(station_names)

def live_status_for(station):
  all_statuses = client.request_feed('station_status').get('data').get('stations')
  return next(filter(lambda x: x.get('station_id') == station.get('station_id'), all_statuses))


def all_stations_basic_info(client):
  all_station_information = client.request_feed('station_information')
  stations_list = all_station_information.get('data').get('stations') 
  station_list = []
  current_station = []
  for station_all_info in stations_list :
      current_station = []
      current_station.append(station_all_info['station_id'])
      current_station.append(station_all_info['name'])
      station_list.append(current_station)
  return station_list

if __name__ == "__main__":
  main()
      

