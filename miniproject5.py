class Record:
    def __init__(self, label, value, limit):
        self.label = label            # source IP
        self.value = value            # failed logins
        self.limit = limit            # total attempts
        self.difference = limit - value          # successful logins
        self.percent = (value / limit) * 100     # failed login percent
 
    def status(self):
        """Return OVER LIMIT, WARNING or OK based on the failed login percent."""
        if self.percent >= 100:
            return "OVER LIMIT"
        elif self.percent >= 90:
            return "WARNING"
        return "OK"
 
    def print_report(self, status):
        """Print a bordered report for this record using an already-computed status."""
        print("=" * 34)
        print(f"    RECORD CHECK  -  {self.label}")
        print("=" * 34)
        print(" Name : Karan")
        print(" Lane : Cyber")
        print(" Date : 09/23/26")
        print("=" * 34)
        print(f" Failed Logins          : {self.value:>7.2f}")
        print(f" Total Login Attempts   : {self.limit:>7.2f}\n")
        print(f" Successful Attempts    : {self.difference:>7.2f}")
        print(f" Failed Login Percent   : {self.percent:>6.2f}%\n")
        print(f" Status                 : {status}")
        print("=" * 34)
 
    def to_line(self):
        """Return this record as a label,value,limit line for the data file."""
        return f"{self.label},{self.value},{self.limit}\n"


class RecordBook:
    def __init__(self, path, results_path):
        self.path = path                  
        self.results_path = results_path  
        self.records = []                 
 
    def load(self):
        """Replace self.records with every Record read from the data file."""
        self.records = load_records(self.path)
 
    def find(self, label):
        """Return the first loaded Record whose label matches, or None."""
        for record in self.records:
            if record.label == label:
                return record
        return None
 
    def add(self, record, status):
        """Save a new record or update an existing one. Returns True if updated."""
        existing = self.find(record.label)
        if existing:
            self.records[self.records.index(existing)] = record
            self.save_all()
            return "updated"
        with open(self.path, "a") as f:
            f.write(record.to_line())
        with open(self.results_path, "a") as f:
            f.write(f"{record.label},{status}\n")
        self.records.append(record)
        return "added"

    def list_all(self):
        """Print a summary list of all IPs and their status from the results file."""
        with open(self.results_path) as f:
            for line in f:
                if line.strip():
                    label, status = line.strip().split(",")
                    print(f"{label}: {status}")

    def save_all(self):
        """Rewrite both files from the current in-memory record list."""
        with open(self.path, "w") as f:
            for record in self.records:
                f.write(record.to_line())
        with open(self.results_path, "w") as f:
            for record in self.records:
                f.write(f"{record.label},{record.status()}\n")


def load_records(path):
    """Read label,value,limit lines from path and return a list of Record objects."""
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                label, value, limit = line.strip().split(",")
                records.append(Record(label, float(value), float(limit)))
    return records
 
def ask_for_record():
    """Prompt for IP, failed logins and total attempts; return a Record or None."""
    ip = input("Enter IP: ")
    failed = input("Enter Failed Logins: ")
    total = input("Enter Total Attempts: ")
    if "quit" in (ip, failed, total):
        print("Exiting")
        return None
    try:
        failed = float(failed)
        total = float(total)
    except ValueError:
        print("Error: failed logins and total attempts must be numbers")
        return None
    if total <= 0:
        print("Total attempts must be greater than 0")
        return None
    return Record(ip, failed, total)

def main():
    """add / view / all / quit menu loop."""
    book = RecordBook("ip_records.txt", "login_results.txt")
    try:
        book.load()
    except FileNotFoundError:
        pass
 
    over_limit = 0
    while True:
        choice = input("add a record (add), view one IP (view), report all (all), or quit: ")

        if choice == "quit":
            print("Exiting")
            break
 
        if choice == "add":
            record = ask_for_record()
            if record:
                result = book.add(record, record.status())
                print(f"Record {result.upper()}")
                continue
 
        if choice == "view":
            record = book.find(input("Enter the IP you want to check: "))
            if record is None:
                print("IP not found")
                continue
            to_report = [record]

        elif choice == "all":
            try:
                book.list_all()
            except FileNotFoundError:
                print("No records yet - add one first")
            continue

        else:
            print("Not an option")
            continue
 
        for record in to_report:
            status = record.status()
            record.print_report(status)
            if status == "OVER LIMIT":
                over_limit += 1
 
    print(f"OVER LIMIT COUNT : {over_limit}")


if __name__ == "__main__":
    main()
