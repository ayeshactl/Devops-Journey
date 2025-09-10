
"""
 05-EX-set.py
 Purpose: Practice sets in Python for server management (DevOps use case)
"""


# Configured servers in system (what we EXPECT to have running)
configured = {"web-server", "db-server", "cache-server", "api-server"}

# Actually running servers (what is REALLY running, imagine from monitoring)
running = {"web-server", "cache-server", "worker-server"}

# Print both sets
print ("Configured-servers: ", configured )               # The planned setup
print ("Running-servers: ", running )                       # The actual running setup

# ----------------------------
# Difference → configured - running
# Shows servers present in configuration but NOT running in reality
print("\nMissing servers (Configured but not running): ", configured - running)   #A - B (elements in A but not in B)


# Difference → running - configured
# Shows servers running in reality but NOT in configuration
print("Extra servers (Running but not configured): ", running-configured)         #B - A (elements in B but not in A)

# Intersection → configured & running
# Shows servers that are BOTH configured AND running (healthy servers)
print("Healthy Servers (Configured and running):", configured & running)           #lements common to both set

# Union → configured | running
# Shows ALL servers (both configured and running) without duplicates
print("All Servers (Union):", configured | running)

# Symmetric Difference → configured ^ running
# Shows servers that are mismatched (only in one set, not in both)
print("Mismatched Servers (Either configured or running but not both):", configured ^ running)