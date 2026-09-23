#dict with key being the ip and val being failed logins and attempts

class IPReports:
    def __init__(self):
        self.ip_logins = {}

    def add_report(self):
        ip = input("source IP: ")      # : replace with an input() call
        failed_logins = float(input("failed logins: "))     # : replace with an input() call, converted
        login_attempts = float(input("total attempts: "))
        # ip = "10.0.0.5"     # : replace with an input() call
        # failed_logins = int("12")     # : replace with an input() call, converted
        # login_attempts = int("400")
        self.ip_logins[ip] = failed_logins, login_attempts
        print(f"Added entry for {ip}")

    def call_report(self):
        try:
            key = input("Search IP:")
            # key = "10.0.0.5" 
            vals = self.ip_logins.get(key)
        except:
            print("Invalid IP. Try again.")
        try:
            failed_logins, login_attempts = vals
        except:
            print("No Ips Added")
        succesful_logins = (login_attempts - failed_logins)
        percent_fail = (failed_logins/login_attempts)*100
        percent_succeed = (succesful_logins/login_attempts)*100

        return key, failed_logins, login_attempts, succesful_logins, percent_fail, percent_succeed


    def print_report(self, ip, failed_logins, login_attempts, succesful_logins, percent_fail, percent_succeed):
        print("=" * 34)
        print(f"  RECORD CHECK  -  {ip}")
        print("=" * 34)
        print(f"  Total Login Attempts: {login_attempts:>8}")
        print(f"  Failed Logins: {failed_logins:>15}")
        print(f"  Successful Attempts: {succesful_logins:>9}\n")
        print(f"  Failed Login Percent: {percent_fail:>8.0f}%")
        print(f"  Succesful Login Percent: {percent_succeed:>5.0f}%")
        print("=" * 34)

    def test(self):
        self.print_report(*self.call_report())

report = IPReports()

report.add_report()

report.test()



