# Gym Membership System
# Features: Plans, Renewal, Age/Marital discounts, Dynamic Festival Discounts

import datetime
import os

# ─────────────────────────────────────────────────────────────────────────────
# MEMBERSHIP PLANS
# ─────────────────────────────────────────────────────────────────────────────

PLANS = {
    "1": {"name": "Monthly",   "months": 1,  "price": 1000},
    "2": {"name": "Quarterly", "months": 3,  "price": 2700},   # ~10% cheaper
    "3": {"name": "Yearly",    "months": 12, "price": 9000},   # ~25% cheaper
}


# ─────────────────────────────────────────────────────────────────────────────
# FESTIVAL DISCOUNT ENGINE  (Dynamic — based on today's date)
# ─────────────────────────────────────────────────────────────────────────────

FESTIVALS = [
    # (festival_name, month, day_start, day_end, discount%)
    ("🎆 New Year",           1,  1,   7,   20),
    ("🌈 Holi",               3,  20,  28,  15),
    ("🌙 Eid",                4,  1,   7,   15),   # approximate (shifts yearly)
    ("🇮🇳 Independence Day", 8,  13,  17,  12),
    ("🎉 Navratri",           10, 1,   12,  10),
    ("🪔 Diwali",             10, 18,  30,  25),
    ("🎄 Christmas & NYE",    12, 24,  31,  20),
]


def get_festival_discount():
    """Return (festival_name, discount%) if today falls in a festival window, else (None, 0)."""
    today = datetime.date.today()
    for festival, month, d_start, d_end, discount in FESTIVALS:
        if today.month == month and d_start <= today.day <= d_end:
            return festival, discount
    return None, 0


# ─────────────────────────────────────────────────────────────────────────────
# MEMBERSHIP DISCOUNT (Age + Marital Status)
# ─────────────────────────────────────────────────────────────────────────────

def get_member_discount(age, married):
    """Return discount % based on member profile."""
    if married == "yes":
        return 32, "Married Couple"
    elif age < 18:
        return 18, "Junior (under 18)"
    elif 18 <= age <= 45:
        return 35, "Adult (18–45)"
    else:
        return 25, "Senior (45+)"


# ─────────────────────────────────────────────────────────────────────────────
# MEMBERSHIP FILE  (stores renewal history)
# ─────────────────────────────────────────────────────────────────────────────

HISTORY_FILE = "membership_history.txt"


def save_membership(name, plan_name, start_date, end_date, final_price, festival):
    with open(HISTORY_FILE, "a") as f:
        festival_tag = f" [{festival}]" if festival else ""
        f.write(
            f"{name} | {plan_name} | Start: {start_date} | "
            f"End: {end_date} | Paid: ₹{final_price:.2f}{festival_tag}\n"
        )


def load_history(name):
    """Return last membership record for the given name, or None."""
    if not os.path.exists(HISTORY_FILE):
        return None
    last_record = None
    with open(HISTORY_FILE, "r") as f:
        for line in f:
            if line.startswith(name + " |"):
                last_record = line.strip()
    return last_record


# ─────────────────────────────────────────────────────────────────────────────
# DISPLAY HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def print_divider(char="=", width=45):
    print(char * width)


def show_plans():
    print("\n📋 Available Membership Plans:")
    print_divider("-", 45)
    for key, plan in PLANS.items():
        print(f"  {key}. {plan['name']:<12} — ₹{plan['price']} / {plan['months']} month(s)")
    print_divider("-", 45)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN FLOW
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "="*45)
print("🏋️  Welcome to POWER GYM Membership System 💪")
print("="*45)

# --- Member Name ---
name = input("\n👤 Enter your name: ").strip()
if not name:
    print("❌ Name cannot be empty.")
    exit()

# --- Check existing membership ---
history = load_history(name)
if history:
    print(f"\n📂 Found existing record for '{name}':")
    print(f"   {history}")
    action = input("\n🔄 Do you want to RENEW your membership? (yes/no): ").lower().strip()
    is_renewal = action == "yes"
else:
    print(f"\n✅ New member detected. Registering '{name}'...")
    is_renewal = False

# --- Age ---
try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("❌ Age cannot be negative.")
        exit()
except ValueError:
    print("❌ Invalid age entered.")
    exit()

# --- Marital Status ---
married = input("Are you married? (yes/no): ").lower().strip()
if married not in ("yes", "no"):
    married = "no"

# --- Plan Selection ---
show_plans()
plan_choice = input("📌 Choose a plan (1/2/3): ").strip()
if plan_choice not in PLANS:
    print("❌ Invalid plan choice.")
    exit()

selected_plan = PLANS[plan_choice]
base_price    = selected_plan["price"]
plan_name     = selected_plan["name"]
months        = selected_plan["months"]

# --- Discounts ---
member_discount, member_label = get_member_discount(age, married)
festival_name,   fest_discount = get_festival_discount()

# Combine discounts (applied sequentially, not additively, to avoid >100%)
price_after_member   = base_price - (base_price * member_discount / 100)
final_price          = price_after_member - (price_after_member * fest_discount / 100)
total_savings        = base_price - final_price

# Renewal bonus: extra 5% off for returning members
if is_renewal:
    renewal_discount = 5
    final_price  = final_price - (final_price * renewal_discount / 100)
    total_savings = base_price - final_price
else:
    renewal_discount = 0

# --- Membership Dates ---
start_date = datetime.date.today()
end_date   = start_date + datetime.timedelta(days=30 * months)

# --- Save to history ---
save_membership(name, plan_name, start_date, end_date, final_price, festival_name)

# ─────────────────────────────────────────────────────────────────────────────
# OUTPUT RECEIPT
# ─────────────────────────────────────────────────────────────────────────────

print("\n" + "="*45)
print("🧾  MEMBERSHIP RECEIPT")
print("="*45)
print(f"  👤 Name           : {name}")
print(f"  📋 Plan           : {plan_name} ({months} month(s))")
print(f"  📅 Start Date     : {start_date}")
print(f"  📅 End Date       : {end_date}")
print("-"*45)
print(f"  💵 Base Price     : ₹{base_price:.2f}")
print(f"  🎯 Member Discount: -{member_discount}%  ({member_label})")

if festival_name:
    print(f"  {festival_name} Offer : -{fest_discount}%")
else:
    print(f"  🎊 Festival Offer : None (no active festival)")

if is_renewal:
    print(f"  🔄 Renewal Bonus  : -5%")

print("-"*45)
print(f"  💰 Final Price    : ₹{final_price:.2f}")
print(f"  🏷️  Total Savings  : ₹{total_savings:.2f}")
print("="*45)

if is_renewal:
    print("✅ Membership renewed successfully! Stay fit! 💪")
else:
    print("✅ Membership activated! Welcome to POWER GYM! 🎉")
print("="*45)