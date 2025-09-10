# Create a dictionary of 3 servers with their IPs

servers = {
    "web-server" : "192.168.1.10",
    "db-server": "192.168.1.20",
    "cache-server": "192.168.1.30"
}

#update db-servers IP
servers["db-server"] = "192.168.1.25"

#add new server
servers["api-server"] = "192.168.1.40"

#print only updated IPs
for ip in servers.values():
    print(ip)


#print final dictionary
print(servers)