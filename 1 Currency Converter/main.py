# Currency Converter

rates = [
    ["USD", 83],
    ["EUR", 90],
    ["INR", 1]
]
 
def get_rate(currency, rates):
    for item in rates:
        if item[0] == currency:
            return item[1]
    return None

print("\n" + "="*41)
print("💱🌍  Welcome to Currency Converter  🌍💱")
print("="*41)

amount = float(input("💰 Enter amount: "))
from_currency = input("🔄 From currency: ").upper()
to_currency = input("➡️ To currency: ").upper()

from_rate = get_rate(from_currency, rates)
to_rate = get_rate(to_currency, rates)

if from_rate is None or to_rate is None:
    print("❌ Invalid currency!") 
else:
    converted = amount * (from_rate / to_rate)
    print("\n" + "-"*35)
    print(f"💱 {amount} {from_currency} = {converted:.2f} {to_currency}  🎉") 
    print("-"*35)