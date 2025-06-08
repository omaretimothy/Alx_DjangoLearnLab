from datetime import datetime, timedelta
#getting the current date and time from the datetime module
def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

#calculate future date
def calculate_future_date(current_date):
    days_in_future = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days_in_future)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    current = display_current_datetime()
    calculate_future_date(current)

if __name__ == "__main__":
    main()