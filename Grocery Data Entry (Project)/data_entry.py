from datetime import datetime
#prompt bakal nanyain  ada spesifik prompt akan nanya ke user apa yang pengen diinput sebelum minta tanggal nya.
#allow_default bakal secara otomatis akan milih hari ini, kalau gak masukin tanggal

date_format = "%d-%m-%Y"
CATEGORIES = {"I":"Income", "E":"Expense"}
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, "%d-%m-%Y")
        return valid_date.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format, Please enter the date in dd-mm-yyyy format")
        return get_date(prompt,allow_default)
    
def get_amount():
    try:
        amount = float(input("Enter the amount:"))
        if amount <= 0:
            raise ValueError("Amount must be a non- negative , non-zero number")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
    
def get_category():
    category = input("Enter category('I' for Income, 'E' for Expense):").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("INvalid Category. Please Enter 'I' for Income and 'E' for Expense")
    return get_category()

def get_description():
    return input("Enter Anything you want as a description (OPTIONAL)")
