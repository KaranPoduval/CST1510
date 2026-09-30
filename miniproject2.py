while True:
    ip = input("Enter IP: ")
    failed_logins = input("Enter Failed Logins: ")
    total_attempts = input("Enter Total Attempts: ")

    if "quit" in (ip, failed_logins, total_attempts):
        print("Exiting")
        break
    
    failed_logins = float(failed_logins)
    total_attempts = float(total_attempts)


    if total_attempts == 0:
        print("Error. Total Attempts can't be 0")
        continue



    difference = (total_attempts - failed_logins) 
    percent = (failed_logins/total_attempts)*100   
    
    if percent > 100: #The instructions I believe include 100 but it makes no sense for 100/100 to be over limit
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {ip}")
    print("=" * 34)

    print("  Name : Karan")
    print("  Lane : Cyber")
    print("  Date : 09/23/26")
    # : your report lines go here
    print("=" * 34)

    print(f"  Failed Logins: {failed_logins:>15.2f}")
    print(f"  Total Login Attempts: {total_attempts:>8.2f}")
    print(f"  Successful Attempts: {difference:>+9.2f}")
    print(f"  Failed Login Percent: {percent:>8.2f}%")
    print(f"  Status: {status:>22}")

    print("=" * 34)


