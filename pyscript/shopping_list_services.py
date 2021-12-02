import requests
import sys
from importlib import reload
if "/config/pyscript_modules" not in sys.path:
    sys.path.append("/config/pyscript_modules")

import write_file
write_file = reload(write_file)

@service
def sort_shopping_list():
    list_items = hass.data["shopping_list"].items
    sorted_items = sorted(list_items, key=lambda x : x['name'].lower())

    task.executor(write_file.write_json, filename = "/config/.shopping_list.json", content=sorted_items)
    hass.data["shopping_list"].async_load()

@event_trigger('shopping_list_updated')
def update_shopping_list(action=None, item=None):
    sort_shopping_list()