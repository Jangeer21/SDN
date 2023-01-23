from netmiko import (ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException)
import xlrd

wb = xlrd.open_workbook(r"MB_Routers.xls")

core_rtr_sheet = wb.sheet_by_name("Core Routers")
preagg_rtr_sheet = wb.sheet_by_name("Pre-Aggregation Routers")
access_rtr_sheet = wb.sheet_by_name("Access Routers")

ip_list = access_rtr_sheet.col_values(1,start_rowx = 1, end_rowx = None)
USERNAME = access_rtr_sheet.cell_value(1,2)
PASSWORD = access_rtr_sheet.cell_value(1,3)

for ip in ip_list:
    try:
        mb_routers = {'device_type': 'cisco_xr','ip': ip,'username': USERNAME,'password': PASSWORD}
        controller = ConnectHandler(**mb_routers)
        print("Connecting to -> " + ip)
        #cfg = ['xml agent tty iteration off']

        #controller.send_config_from_file('config_content')
        #controller.commit()
        output1 = controller.send_command('show run hostname')
        print(output1)
    except(NetmikoTimeoutException, NetmikoAuthenticationException):
        print("Failed to connect to -> " + ip)
    

