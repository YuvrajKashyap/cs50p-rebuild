months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    date_str = get_input()
    print(parse(date_str))
        
    
    
def get_input():
    return input("Date: ")
            
def parse(date_str):
    global months
    # if / in string
        # split input by /
        # assign month, day, year
    # elif , in string
        # split by ,
        # extract month name, day, and yaer
        # convert month to number using list
    #else:
        # return None
        
    if "/" in date_str:
        try:
            month, day, year = date_str.split("/")
        
            month = int(month.strip())
            day = int(day.strip())
            year = int(year.strip())
            
            return f"{year}-{month:02}-{day:02}"
        
        except:
            return None
        
    elif "," in date_str:
        try:
            month, day, year = date_str.replace(",", "").split()
            month = int(months.index(month.strip().title()) + 1)
            day = int(day.strip())
            year = int(year.strip())
            return f"{year}-{month:02}-{day:02}"
        except ValueError:
            return None

    
    
main()