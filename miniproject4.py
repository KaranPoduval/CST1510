def check(value, limit):
    """returns the difference and percentage of value compared to limit"""
    difference = limit - value
    percent = (value/limit)*100
    return difference, percent

def status_of(percent):
    """returns status based on percent"""
    if percent > 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def print_report(ip, failed_logins, total_attempts, succesful_logins, percent_fail, status):
        """uses ip, failed_logins, total_attempts, successful_logins(difference), percent_fail(percent) and status to print an ordered report"""
        print("=" * 34)
        print(f"    RECORD CHECK  -  {ip}")
        print("=" * 34)
        print(" Name : Karan")
        print(" Lane : Cyber")
        print(" Date : 09/23/26")
        print("=" * 34)
        print(f" Failed Logins {":":>8} {failed_logins:>5.2f}")
        print(f" Total Login Attempts {":":>1} {total_attempts:>5.2f}\n")
        print(f" Successful Attempts {":":>2} {succesful_logins:>5.2f}")
        print(f" Failed Login Percent{":":>2} {percent_fail:>4.2f}%\n")
        print(f" Status {":":>15} {status:>3}")
        print("=" * 34)

def write_record(ip, failed_logins, total_attempts):
    """appends one ip,failed,total line to ip_records.txt"""
    with open("ip_records.txt", "a") as f:
        f.write(f"{ip},{failed_logins},{total_attempts}\n")

def write_result(ip, status):
    """adds a report to login_results.txt"""
    with open("login_results.txt", "a") as f:
        f.write(f"{ip},{status}\n")

def add_report():
    """adds a record to ip_records.txt"""
    ip = input("Enter IP: ")
    failed_logins = input("Enter Failed Logins: ")
    total_attempts = input("Enter Total Attempts: ")
    if "quit" in (ip, failed_logins, total_attempts):
            print("Exiting")
            return
    try:
        failed_logins = float(failed_logins)
        total_attempts = float(total_attempts)
    except ValueError:
        print("Error Invalid Input for failed logins or attempts. Needs to be a number")
        return
    if total_attempts <= 0:
        print("Total attempts must be greater than 0")
        return
    write_record(ip, failed_logins, total_attempts)
    difference, percent = check(failed_logins, total_attempts)
    status = status_of(percent)
    write_result(ip, status)
    return True

def load_record(label):
    """loads a record from the ip_records.txt"""
    with open("ip_records.txt") as f:
        for line in f:
            ip, failed_logins, total_attempts = line.strip().split(",")
            if label == ip:
                return ip, float(failed_logins), float(total_attempts)
            else:
                continue
    return None



over_limit = 0
while True:
    choice = input("Do you want to add a record(add) or view a report(view): ")
    if choice not in ("add", "view", "quit"):
        print("Not an option")
        continue

    if "quit" in choice:
        print("Exiting")
        break

    if choice == "add":
        if add_report():
            print("Report Added")
    else:
        ip_check = input("Enter the Ip you want to check: ")
        try:
            result = load_record(ip_check)
        except FileNotFoundError:
            print("ip_records.txt not found - add a record first")
            continue
        if result is None:
            print("IP not found")
            continue
        ip, failed_logins, total_attempts = result
        difference, percent = check(failed_logins, total_attempts)
        status = status_of(percent)
        print_report(ip=ip, failed_logins=failed_logins, total_attempts=total_attempts, succesful_logins=difference, percent_fail=percent, status=status)
        if status == "OVER LIMIT":
            over_limit += 1

print(f"OVER LIMIT COUNT : {over_limit}")
