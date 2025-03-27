def worker_salary(weekly_work):
    return sum(weekly_work) * 10

def bonus_money(weekly_work):
    weekly_work = sum(weekly_work)
    if weekly_work <= 24:
        return 0
    elif weekly_work >= 30 < 42:
        return 20
    elif weekly_work >= 42 < 48:
        return 50
    elif weekly_work >= 48:
        return 100

def worker_status(weekly_work):
    weekly_work = sum(weekly_work) / 6 
    if weekly_work < 5:
        return "Bad"
    if weekly_work >= 5 < 6:
        return "Normal"
    if weekly_work >= 7 < 8:
        return "Good"
    if weekly_work >= 8:
        return "Perfect"

def main():
    weekly_work = []

    for day in range(6):
        while True:
            try:
                daily_work = input(f"Enter the number of working hours per {day+1} day: ")
                daily_work = int(daily_work)
                weekly_work.append(daily_work)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            
    status = worker_status(weekly_work)
    bonus = bonus_money(weekly_work)
    salary = worker_salary(weekly_work)
    
    print(f"Yorn salary is: {salary}$")
    print(f"Your status is: {status}")
    print(f"Your bonus money is: {bonus}$")
    print(f"Your total salary is: {salary + bonus}$")

main()
