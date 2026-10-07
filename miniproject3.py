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

over_limit = 0
while True:
    ip = input("Enter IP: ")
    failed_logins = input("Enter Failed Logins: ")
    total_attempts = input("Enter Total Attempts: ")
    # ip = "10.0.0.1"
    # failed_logins = 40
    # total_attempts = 12
    if "quit" in (ip, failed_logins, total_attempts):
        print("Exiting")
        break
    
    failed_logins = float(failed_logins)
    total_attempts = float(total_attempts)


    if total_attempts == 0:
        print("Error. Total Attempts can't be 0")
        continue

    difference, percent = check(failed_logins, total_attempts)
    status = status_of(percent)
    print_report(ip=ip, failed_logins=failed_logins, total_attempts=total_attempts, succesful_logins=difference, percent_fail=percent, status=status)
    if status == "OVER LIMIT":
        over_limit += 1

print(f"OVER LIMIT COUNT : {over_limit}")
