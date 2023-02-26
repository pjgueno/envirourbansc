from enviro import logging
from enviro.constants import UPLOAD_SUCCESS, UPLOAD_FAILED
import urequests
# import ujson
# import json
import config

def log_destination():
  logging.info(f"> uploading cached readings to url: {config.custom_http_url1} and {config.custom_http_url2}")

def upload_reading(reading):
  url1 = config.custom_http_url1
  url2 = config.custom_http_url2

  out_json1 ={"software_version":"","sensordatavalues":[{"value_type": "P0","value": ""},{"value_type": "P1","value": ""},{"value_type": "P2","value": ""}]}
  out_json1["software_version"] = reading["nickname"]+["uid"]
  [item for item in out_json1["sensordatavalues"] if item["value_type"]=="P0"]["value"]= reading["readings"]["pm1"]
  [item for item in out_json1["sensordatavalues"] if item["value_type"]=="P1"]["value"]= reading["readings"]["pm2_5"]
  [item for item in out_json1["sensordatavalues"] if item["value_type"]=="P2"]["value"]= reading["readings"]["pm10"]

  out_json2 ={"software_version":"","sensordatavalues":[{"value_type": "PMS_P0","value": ""},{"value_type": "PMS_P1","value": ""},{"value_type": "PMS_P2","value": ""}]}
  out_json2["software_version"] = reading["nickname"]+["uid"]
  [item for item in out_json2["sensordatavalues"] if item["value_type"]=="PMS_P0"]["value"]= reading["readings"]["pm1"]
  [item for item in out_json2["sensordatavalues"] if item["value_type"]=="PMS_P1"]["value"]= reading["readings"]["pm2_5"]
  [item for item in out_json2["sensordatavalues"] if item["value_type"]=="PMS_P2"]["value"]= reading["readings"]["pm10"]

  out_json3 ={"software_version":"","sensordatavalues":[{"value_type": "temperature","value": ""},{"value_type": "humidity","value": ""},{"value_type": "pressure","value": ""}]}
  out_json3["software_version"] = reading["nickname"]+["uid"]
  [item for item in out_json3["sensordatavalues"] if item["value_type"]=="temperature"]["value"]= reading["readings"]["temperature"]
  [item for item in out_json3["sensordatavalues"] if item["value_type"]=="humidity"]["value"]= reading["readings"]["humidity"]
  [item for item in out_json3["sensordatavalues"] if item["value_type"]=="pressure"]["value"]= reading["readings"]["pressure"]


  out_json4 ={"software_version":"","sensordatavalues":[{"value_type": "BME280_temperature","value": ""},{"value_type": "BME280_humidity","value": ""},{"value_type": "BME280_pressure","value": ""}]}
  out_json4["software_version"] = reading["nickname"]+["uid"]
  [item for item in out_json4["sensordatavalues"] if item["value_type"]=="BME280_temperature"]["value"]= reading["readings"]["temperature"]
  [item for item in out_json4["sensordatavalues"] if item["value_type"]=="BME280_humidity"]["value"]= reading["readings"]["humidity"]
  [item for item in out_json4["sensordatavalues"] if item["value_type"]=="BME280_pressure"]["value"]= reading["readings"]["pressure"]

  headers1 = {"Content-Type": "application/json", "X-Pin": config.header_xpin1 , "X-Sensor":"raspi-"+ reading["uid"]}
  headers2 = {"Content-Type": "application/json", "X-Pin": config.header_xpin2, "X-Sensor":"raspi-"+reading["uid"]}

  try:
    result1 = urequests.post(url1, headers=headers1, json=out_json1)
    result1.close()

    if result1.status_code not in [200, 201, 202]:
      logging.debug(f"  - upload issue ({result1.status_code} {result1.reason})")
      call1 = False
    else:
      call1 = True
    
    result2 = urequests.post(url2, headers=headers1, json=out_json2)
    result2.close()

    if result2.status_code not in [200, 201, 202]:
      logging.debug(f"  - upload issue ({result2.status_code} {result2.reason})")
      call2 = False
    else:
      call2 = True
 
    result3 = urequests.post(url1, headers=headers2, json=out_json3)
    result3.close()

    if result3.status_code not in [200, 201, 202]:
      logging.debug(f"  - upload issue ({result3.status_code} {result3.reason})")
      call3 = False
    else:
      call3 = True

    result4 = urequests.post(url2, headers=headers2, json=out_json4)
    result4.close()

    if result4.status_code not in [200, 201, 202]:
      logging.debug(f"  - upload issue ({result4.status_code} {result4.reason})")
      call4 = False
    else:
      call4 = True
    
    if call1 & call2 & call3 & call4: 
      return UPLOAD_SUCCESS
      
  except:
    logging.debug(f"  - an exception occurred when uploading")

  return UPLOAD_FAILED
