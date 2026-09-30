class IPReports:
    def __init__(self):
        self.ip_logins = {}

    def add_report(self):
        ip = input("Enter IP:")     
        failed_logins = input("Enter Failed Logins")
        total_attempts = input("Enter Total Attempts")
        if "quit" in (ip, failed_logins, total_attempts):
            print("Exiting")
            return False
        try:
            failed_logins = float(failed_logins)
            total_attempts = float(total_attempts)
        except ValueError:
            print("Error. Invalid Entry. Not a Valid Number")
            return True
        
        self.ip_logins[ip] = failed_logins, total_attempts
        print(f"Added entry for {ip}")
        return True

    def call_report(self):
        if vals is None:
            print("No Ips Added.")
            return None
        
        try:
            # key = input("Search IP:")
            key = "10.0.0.5" 
            vals = self.ip_logins.get(key)
        except:
            print("Invalid IP. Try again.")

        failed_logins, total_attempts = vals
        succesful_logins = total_attempts - failed_logins
        percent_fail = (failed_logins/total_attempts)*100
        percent_succeed = (succesful_logins/total_attempts)*100

        if percent_fail > 100:
            status = "OVER LIMIT"
        elif percent_fail >= 90:
            status = "WARNING"
        else:
            status = "OK"

        return key, failed_logins, total_attempts, succesful_logins, percent_fail, percent_succeed, status


    def print_report(self, ip, failed_logins, total_attempts, succesful_logins, percent_fail, percent_succeed, status):
        print("=" * 34)
        print(f"  RECORD CHECK  -  {ip}")
        print("=" * 34)
        print(f"  Total Login Attempts: {total_attempts:>8}")
        print(f"  Failed Logins: {failed_logins:>15}")
        print(f"  Successful Attempts: {succesful_logins:>9}\n")
        print(f"  Failed Login Percent: {percent_fail:>8.0f}%")
        print(f"  Succesful Login Percent: {percent_succeed:>5.0f}%")
        print(f"  Status: {status:>22}")
        print("=" * 34)

    def test(self):
        result = self.call_report()
        if result:
            self.print_report(*result)
        

report = IPReports()

running = True
while running:
    running = report.add_report()

report.test()