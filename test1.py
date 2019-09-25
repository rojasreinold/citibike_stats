import pprint
from gbfs.services import SystemDiscoveryService

ds = SystemDiscoveryService()
client = ds.instantiate_client('NYC')
all_station_information = client.request_feed('station_information')

pp = pprint.PrettyPrinter(indent=2)
pp.pprint(all_station_information)
