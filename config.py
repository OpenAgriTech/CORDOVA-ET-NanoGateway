""" LoPy LoRaWAN Nano Gateway configuration options """

import machine
import ubinascii
from network import LoRa

WIFI_MAC = ubinascii.hexlify(machine.unique_id()).upper()
# Set  the Gateway ID to be the first 3 bytes of MAC address + 'FFFE' + last 3 bytes of MAC address
GATEWAY_ID = WIFI_MAC[:6] + "FFFE" + WIFI_MAC[6:12]

SERVER = 'router.eu.thethings.network'
PORT = 1700

NTP = "pool.ntp.org"
NTP_PERIOD_S = 3600

WIFI_SSID = 'MeteoNet'
WIFI_PASS = 'xxx'

# for EU868
LORA_FREQUENCY = 867500000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5
LORA_REGION = LoRa.EU868

# for AU915
#LORA_FREQUENCY = 917200000
#LORA_GW_DR = "SF7BW125" # DR_5
#LORA_NODE_DR = 5
#LORA_REGION = LoRa.AU915

# for US915
# LORA_FREQUENCY = 903900000
# LORA_GW_DR = "SF10BW125" # DR_0
# LORA_NODE_DR = 0
#LORA_REGION = LoRa.US915
