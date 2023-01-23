from genie.testbed import load
import unicon

testbed = load('./test.yaml')

for device in testbed.devices:
    iosxr = testbed.devices[device]
    print("Connecting to device -> " + device)
    
    try:
        iosxr.connect(init_exec_commands=[],init_config_commands=[],log_stdout=False,learn_hostname=True)         
        iosxr.execute('''
                          logging suppress rule Drop_unnec_log
                           alarm PKT_INFRA FM FAULT_MINOR
                           alarm PKT_INFRA FAULT_MINOR MB-ALTITUDE
                          exit
                          logging suppress apply rule Drop_unnec_log
                           all-of-router
                          exit
                          !
                        ''')
        show_log_supress = iosxr.execute('sh logging suppress rule all')
        print(show_log_supress)
        iosxr.disconnect()

    except unicon.core.errors.ConnectionError:
        print("Connection failed")
        continue

   # cfg = iosxr.configure("netconf agent tty")

