
# 💰 SoylaBudgeterV2 - CLI Enhanced Edition
# Built by 👨‍🔧🌍 Han aka gone2soon

import pandas as pd
import os
import getpass
from datetime import datetime

BUDGET_FILE = 'budget_data.csv'
LOG_FILE = 'soyla_budget_log.rpl'
PIN_CODE = '6502'  # Change this to your secure PIN

# Splash Screen
def splash():
    print("""
   _____             _        _         _             _            
  / ____|           | |      | |       | |           (_)           
 | (___  _ __   ___ | |_ __ _| |__  ___| |_ _ __ __ _ _ _ __   __ _ 
  \___ \| '_ \ / _ \| __/ _` | '_ \/ __| __| '__/ _` | | '_ \ / _` |
  ____) | | | | (_) | || (_| | |_) \__ \ |_| | | (_| | | | | | (_| |
 |_____/|_| |_|\___/ \__\__,_|_.__/|___/\__|_|  \__,_|_|_| |_|\__, |
                                                              __/ |
                                                             |___/ 
            CLI Budgeting System // Myth.OS Protocol
    """)

# PIN Check
def verify_pin():
    for _ in range(3):
        pin = getpass.getpass("🔐 Enter your PIN: ")
        if pin == PIN_CODE:
            print("✅ Access granted.")
            return True
        else:
            print("❌ Incorrect PIN.")
    print("🔒 Too many failed attempts. Exiting.")
    exit()

# Load existing data
if os.path.exists(BUDGET_FILE):
    df = pd.read_csv(BUDGET_FILE)
else:
    df = pd.DataFrame(columns=['Date', 'Description', 'Amount', 'Category'])

# Append to log
def log_action(action):
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{datetime.now()}] {action}\n")

# Save
def save():
    df.to_csv(BUDGET_FILE, index=False)
    log_action("💾 Saved budget to file.")
    print("✅ Budget saved.")

# Add entry
def add_entry():
    date = input("📅 Date (YYYY-MM-DD): ")
    desc = input("📝 Description: ")
    amount = float(input("💰 Amount: "))
    category = input("📂 Category (Income/Expense): ").capitalize()
    entry = {
        'Date': date,
        'Description': desc,
        'Amount': amount,
        'Category': category
    }
    global df
    df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    log_action(f"➕ Added entry: {entry}")
    print("➕ Entry added.")

# Show entries
def show_entries():
    print("\n--- 📋 All Budget Entries ---")
    print(df)
    log_action("📋 Viewed entries.")

# Summary
def summary():
    income = df[df['Category'] == 'Income']['Amount'].sum()
    expense = df[df['Category'] == 'Expense']['Amount'].sum()
    balance = income - expense
    print(f"📈 Income: £{income:.2f}")
    print(f"📉 Expenses: £{expense:.2f}")
    print(f"💎 Balance: £{balance:.2f}")
    log_action("📈 Viewed summary.")

# Remove entry
def remove_entry():
    print(df[['Date', 'Description', 'Amount', 'Category']])
    idx = int(input("Enter index to remove: "))
    global df
    if 0 <= idx < len(df):
        log_action(f"🗑️ Removed entry: {df.iloc[idx].to_dict()}")
        df = df.drop(index=idx).reset_index(drop=True)
        print("🗑️ Entry removed.")
    else:
        print("❌ Invalid index.")

# Main program
def main():
    splash()
    verify_pin()
    print("💸 Welcome to SoylaBudgeter CLI Enhanced")
    while True:
        print("\n[1] Add Entry  [2] View Entries  [3] Summary  [4] Remove Entry  [5] Save  [0] Exit")
        choice = input("Choose: ")
        if choice == '1':
            add_entry()
        elif choice == '2':
            show_entries()
        elif choice == '3':
            summary()
        elif choice == '4':
            remove_entry()
        elif choice == '5':
            save()
        elif choice == '0':
            save()
            print("🔚 Exiting... Log saved.")
            log_action("🔚 Exited program.")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
