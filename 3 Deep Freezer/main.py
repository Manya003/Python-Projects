# Deep Freezer Automation

REQUIRED_TEMP = -28

temp = int(input("🌡️ Enter current temperature (°C): "))

print("\n🔄 Starting Freezer...")

while True:
    
    if temp > REQUIRED_TEMP:
        print(f"Freezer ON | Temp: {temp}°C")
        temp -= 1   # cooling

    else:
        print(f"❄️ Freezer OFF | Temp: {temp}°C (Ideal reached)")
        break