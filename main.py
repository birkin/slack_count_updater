import json, os, pathlib
import requests
from dotenv import load_dotenv

load_dotenv()

HH_COUNT_JSON_PATH = os.environ['HH_COUNT_JSON_PATH']

items_url = 'https://repository.library.brown.edu/api/search/?q=rel_is_member_of_collection_ssim:%22bdr:wum3gm43%22&rows=0'
orgs_url = 'https://repository.library.brown.edu/api/search/?q=-rel_is_part_of_ssim:*+rel_is_member_of_collection_ssim:%22bdr:wum3gm43%22&rows=0'

items_jdict = requests.get(items_url).json()
orgs_jdict = requests.get(orgs_url).json()

items_count = items_jdict['response']['numFound']
orgs_count = orgs_jdict['response']['numFound']

data = { 'items_count': items_count, 'orgs_count': orgs_count }
json_data: str = json.dumps( data, indent=2, sort_keys=True )

## write to json file
with open(HH_COUNT_JSON_PATH, 'w') as f:
    f.write(json_data)
