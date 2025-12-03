import datetime

def formatting_magic():
    name = "Alice"
    value = 1234.56789
    date = datetime.datetime.now()

    # >20 aligns right with padding, .2f is float precision, %B is Month name
    print(f"|{name:>20}|")          # Right align within 20 chars
    print(f"|{name:^20}|")          # Center align
    print(f"|{name:*^20}|")         # Center align with '*' fill
    print(f"Currency: ${value:,.2f}") # Comma separator and 2 decimals
    print(f"Date: {date:%B %d, %Y}") # Custom date format inline

formatting_magic()
