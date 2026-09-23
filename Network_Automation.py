#Requirements
"""
•	Store data for at least 8 devices. The device data must be hard-coded directly inside the script.
•	Include fields such as hostname, device type, management IP, location, status, CPU usage, memory usage, uptime, and backup status.
•	Print a clear operational report (You may refer to our Week 3 Python class activity for ideas).
•	Include totals by device type and location.
•	Flag devices needing attention based on reasonable rules, such as high CPU, high memory, failed backup, low uptime, or non-operational status.
•	Use lists, dictionaries, loops, conditionals, and at least one function.
"""
import json
import yaml

with open('Network_Automation_config.json','r') as json_file:
    ourjson = json.load(json_file)

#print(ourjson)
#print("The access token is: {}".format(ourjson['api_token']))
#print("The token expires in {} seconds.".format(ourjson['expires_in']))

#print("\n\n---")
#print(yaml.dump(ourjson))

#Requirement 1 stores data of at least 8 devices
network_inventory = [
    #index 0
    {
        "hostname": "Router-01",
        "device_type": "Router",
        "management_ip": "192.168.100.10",
        "location": "Basement",
        "status": "operational",
        "CPU_usage": 50,
        "memory_usage": 67,
        "uptime_days": 131,
        "backup_status": "completed"
    },

    #index 1
    {
        "hostname": "Router-02",
        "device_type": "Router",
        "management_ip": "192.168.100.11",
        "location": "Lobby",
        "status": "operational",
        "CPU_usage": 25,
        "memory_usage": 32,
        "uptime_days": 32,
        "backup_status": "completed"
    },

    #index 2
    {
        "hostname": "Router-03",
        "device_type": "Router",
        "management_ip": "192.168.100.12",
        "location": "Cafeteria",
        "status": "warning",
        "CPU_usage": 62,
        "memory_usage": 71,
        "uptime_days": 67,
        "backup_status": "completed"
    },    

    #index 3
    {
        "hostname": "Router-04",
        "device_type": "Router",
        "management_ip": "192.168.100.13",
        "location": "First Floor Office",
        "status": "operational",
        "CPU_usage": 61,
        "memory_usage": 82,
        "uptime_days": 311,
        "backup_status": "completed"
    },    

    #index 4
    {
        "hostname": "Router-05",
        "device_type": "Router",
        "management_ip": "192.168.100.14",
        "location": "Administration",
        "status": "operational",
        "CPU_usage": 21,
        "memory_usage": 19,
        "uptime_days": 121,
        "backup_status": "completed"
    },   

    #index 5
    {
        "hostname": "ProdServer",
        "device_type": "Server",
        "management_ip": "192.168.100.15",
        "location": "Basement",
        "status": "warning",
        "CPU_usage": 72,
        "memory_usage": 88,
        "uptime_days": 81,
        "backup_status": "completed"
    },     

    #index 6
    {
        "hostname": "DevServer",
        "device_type": "Server",
        "management_ip": "192.168.100.16",
        "location": "Basement",
        "status": "operational",
        "CPU_usage": 25,
        "memory_usage": 32,
        "uptime_days": 2,
        "backup_status": "incomplete"
    },     

    #index 7
    {
        "hostname": "TestServer",
        "device_type": "Server",
        "management_ip": "192.168.100.17",
        "location": "Basement",
        "status": "offline",
        "CPU_usage": 0,
        "memory_usage": 0,
        "uptime_days": 0,
        "backup_status": "completed"
    }
]

def generate_network_report(inventory):
    print("=== NETWORK INFRASTRUCTURE REPORT ===")
    print(f"Total devices monitored:{len(network_inventory)}")
    print("\n--- DEVICE STATUS SUMMARY---")

    for device in network_inventory:
        status_indicator = "OK" if device["status"] == "operational" else "NOK"
        print(f"{status_indicator} {device['hostname']:15} | {device['device_type']:8} | {device['location']:12} | CPU: {device['CPU_usage']:5}%")

    print("\n--- DEVICES BY LOCATION---")
    location_counts = {}
    for device in network_inventory:
        loc = device["location"]

        if loc in location_counts:
            location_counts[loc] += 1
        else:
            location_counts[loc] = 1

    for loc, count in location_counts.items():
        print(f"{loc}: {count}")

    print("\n--- TOTALS BY DEVICE TYPE ---")
    type_loc_counts = {}
    for device in network_inventory:
        device_type = device["device_type"]
        
        if device_type in type_loc_counts:
            type_loc_counts[device_type] += 1
        else:
            type_loc_counts[device_type] = 1

    for device_type, count in type_loc_counts.items():
        print(f"Number of {device_type}s: {count}")

    print("\n--- DEVICES NEEDING ATTENTION ---")
    for device in network_inventory:
        if device["CPU_usage"] > 30 or device["memory_usage"] > 60:
            print(f" Check {device['hostname']}: CPU {device['CPU_usage']}%, Memory {device['memory_usage']}%")

    print("\n--- UPTIME ANALYSIS ---")
    total_uptime = sum(device["uptime_days"] for device in network_inventory)
    average_uptime = total_uptime / len(network_inventory)
    print(f"Average uptime across all devices: {average_uptime:.1f} days")

generate_network_report(network_inventory)