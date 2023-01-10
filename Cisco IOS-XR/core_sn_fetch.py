from napalm import get_network_driver
import xlrd
from pprint import pprint

wb = xlrd.open_workbook(r"./Documents/Azerconnect/IOS-XR Automation/MB_Routers.xls")

core_rtr_sheet = wb.sheet_by_name("Core Routers")
ip_list = core_rtr_sheet.col_values(1,start_rowx = 1, end_rowx = None)

for ip in ip_list:
    try:
        driver = get_network_driver('iosxr')
        print("Connecting to -> " + ip)
        device = driver(ip,'jahangir','Teconfio@22')

        device.open()
        sn = device.get_facts()
        print(sn['serial_number'])
    except:
        print("Failed to connect to -> " + ip)
        continue
