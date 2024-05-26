from datetime import datetime

def view_current_date():
    return f'Data atual: {datetime.now()}'

print(view_current_date())