from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {datetime.strftime(current_date, '%Y-%m-%d %H:%M:%S')}")


def calculate_future_date():
    days_ahead  = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_ahead)
    print(f"Future date: {datetime.strftime(future_date, '%Y-%m-%d')}")



def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()