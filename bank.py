
accounts = {}

#  ایجاد حساب‌ها 
try:
    count = int(input("چند حساب بانکی می‌خواهید ایجاد کنید؟ "))
    if count <= 0:
        print("تعداد حساب‌ها باید حداقل ۱ باشد.")
    else:
        for i in range(count):
            name = input(f"\nنام صاحب حساب {i + 1}: ").strip().lower()
            if name in accounts:
                print("⚠️ این حساب از قبل وجود دارد! حساب جدیدی ساخته نمی‌شود.")
                continue

            try:
                balance = float(input("موجودی اولیه: "))
                if balance < 0:
                    print("❌ موجودی اولیه نمی‌تواند منفی باشد.")
                    continue
            except ValueError:
                print("❌ ورودی نامعتبر برای موجودی.")
                continue

            accounts[name] = balance
except ValueError:
    print("❌ ورودی نامعتبر برای تعداد حساب‌ها.")


#  منوی اصلی 
while True:
    print("\n===== منوی عملیات بانکی =====")
    print("1. نمایش موجودی همه حساب‌ها")
    print("2. سپرده‌گذاری در حساب")
    print("3. برداشت از حساب")
    print("4. نمایش حساب‌هایی با موجودی بیشتر از میانگین")
    print("5. خروج از برنامه")

    choice = input("گزینه مورد نظر را وارد کنید: ").strip()

    if choice == "1":
        if not accounts:
            print("هیچ حسابی وجود ندارد.")
            continue
        print("\n--- موجودی حساب‌ها ---")
        for n, b in accounts.items():
            print(f"{n.capitalize()}: {b:,.2f} تومان")

    elif choice == "2":
        n = input("نام حساب: ").strip().lower()
        if n not in accounts:
            print("❌ حساب یافت نشد.")