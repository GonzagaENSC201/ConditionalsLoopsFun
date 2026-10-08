temperature = 150
if temperature > 120:
    status = "EMERGENCY"
elif temperature > 100:
    status = "CRITICAL"
elif temperature >= 80:
    status = "WARNING"
else:
    status = "NORMAL"
print("System status:", status)