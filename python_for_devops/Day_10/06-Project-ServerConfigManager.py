# """
# 06-Project-ServerConfigManager.py
#  Purpose: Manage server configurations and compare with running servers
#  DevOps Use Case: Detect mismatches between expected (configured) vs actual (running)

# """
# # Step 1: Store server configurations in a dictionary (key = server name, value = details)
# server_configs = {
#     "web-server": {"ip": "192.168.1.10", "os": "Ubuntu", "status": "active"},
#     "db-server": {"ip": "192.168.1.20", "os": "CentOS", "status": "inactive"},
#     "cache-server": {"ip": "192.168.1.30", "os": "Ubuntu", "status": "active"}
# }

# # Step 2: Retrieve specific information from dictionary
# print("DB Server IP:", server_configs["db-server"]["ip"])  
# # Access nested dictionary → get IP of db-server

# # Update a value inside dictionary
# server_configs["db-server"]["status"] = "active"  
# # Changed db-server status from 'inactive' to 'active'


# # Step 3: Convert dictionary keys (configured servers) into a set
# configured = set(server_configs.keys())  
# # {'web-server', 'db-server', 'cache-server'}


# # Assume monitoring tool gives us this set of actually running servers
# running = {"web-server", "cache-server", "api-server"}  
# # api-server is running but not in configs, db-server is missing

# # Step 4: Use set operations to compare
# print("\n--- Server Comparison ---")

# print("Configured Servers:", configured)        # All expected servers
# print("Running Servers:", running)              # All currently active servers

# print("\nMissing Servers (Configured but not running):", configured - running)     #servers missing in real world.
# # Difference (configured - running) → db-server missing


# print("Extra Servers (Running but not configured):", running - configured)          #extra/unauthorized servers.
# # Difference (running - configured) → api-server extra

# print("Healthy Servers (Configured and running):", configured & running)         #healthy servers.
# # Intersection (configured & running) → web-server, cache-server healthy

# print("All Known Servers (Union):", configured | running)                      #full list.
# # Union (configured | running) → all servers combined

# print("Mismatched Servers (Only on one side):", configured ^ running)           # mismatched servers.
# # Symmetric Difference → db-server, api-server (they don’t match)









"""
DevOps View:

This script simulates:

Configured Servers → like Ansible inventory, Kubernetes manifest, or Terraform state.
Running Servers → like AWS EC2 list, kubectl get pods, or monitoring tool output.
Report → helps find drift (mismatch between expected vs real infra).
"""

# 07-CLI-ServerConfigManager.py
# Purpose: CLI tool to manage server configs and compare with running servers
# DevOps Use Case: Infra validation script to detect missing or extra servers

# Step 1: Store server configurations in a dictionary
server_configs = {}

print("=== Server Configuration Manager ===")

# Step 2: Take user input to add servers
num = int(input("How many servers do you want to configure? "))

for i in range(num):
    name = input(f"Enter name of server {i+1}: ")
    ip = input(f"Enter IP address of {name}: ")
    os = input(f"Enter OS of {name}: ")
    status = input(f"Enter status (active/inactive) of {name}: ")
    
    # Save in dictionary
    server_configs[name] = {"ip": ip, "os": os, "status": status}

# Step 3: Ask which servers are actually running
running_input = input("\nEnter running servers (comma separated): ")
running = set(running_input.split(","))  # Convert to set
running = {srv.strip() for srv in running}  # Clean spaces

# Step 4: Convert configured servers to set
configured = set(server_configs.keys())

# Step 5: Generate report
print("\n=== Server Report ===")
print("Configured Servers:", configured)
print("Running Servers:", running)

print("\nMissing Servers (Configured but not running):", configured - running)
print("Extra Servers (Running but not configured):", running - configured)
print("Healthy Servers (Configured and running):", configured & running)
print("All Known Servers:", configured | running)
print("Mismatched Servers:", configured ^ running)
