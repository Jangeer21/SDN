from netmiko import (ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException)
import xlrd

wb = xlrd.open_workbook(r"MB_Routers.xls")

core_rtr_sheet = wb.sheet_by_name("Core Routers")
preagg_rtr_sheet = wb.sheet_by_name("Pre-Aggregation Routers")
access_rtr_sheet = wb.sheet_by_name("Access Routers")

ip_list = access_rtr_sheet.col_values(1,start_rowx = 1, end_rowx = None)
# host_list = access_rtr_sheet.col_values(0,start_rowx = 1, end_rowx = None)
# user_list = access_rtr_sheet.col_values(2,start_rowx = 1, end_rowx = None)
# passwd_list = access_rtr_sheet.col_values(3,start_rowx = 1, end_rowx = None)

for ip in ip_list:
    try:
        mb_routers = {'device_type': 'cisco_xr','ip': ip,'username': 'admin','password': 'admin1234'}
        controller = ConnectHandler(**mb_routers)
        print("Connecting to -> " + ip)
        #cfg = ['xml agent tty iteration off']

        controller.send_config_from_file('config_content')
        controller.commit()
        output1 = controller.send_command('show access-lists IPv4_VTY_ACCESS 11')
        print(output1)
    except(NetmikoTimeoutException, NetmikoAuthenticationException):
        print("Failed to connect to -> " + ip)
    

