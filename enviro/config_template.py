# enviro config file

# you may edit this file by hand but if you enter provisioning mode
# then the file will be automatically overwritten with new details

provisioned = False

# enter a nickname for this board
nickname = None

# network access details
wifi_ssid = None
wifi_password = None

# how often to wake up and take a reading (in minutes)
reading_frequency = 15

# where to upload to ("http", "mqtt", "adafruit_io", "influxdb")
destination = None

# how often to upload data (number of cached readings)
upload_frequency = 5

# web hook settings
custom_http_url = None
custom_http_url2 = None
header_content = None
header_xpin1 = None
header_xpin2 = None
header_id = None

# mqtt broker settings
mqtt_broker_address = None
mqtt_broker_username = None
mqtt_broker_password = None

# adafruit ui settings
adafruit_io_username = None
adafruit_io_key = None

# influxdb settings
influxdb_org = None
influxdb_url = None
influxdb_token = None
influxdb_bucket = None

# grow specific settings
auto_water = False
moisture_target_a = 50
moisture_target_b = 50
moisture_target_c = 50