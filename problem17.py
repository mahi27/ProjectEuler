def to_english(n):
                if 0 <= n < 20:
                                return ONES[n]
                elif 20 <= n < 100:
                                return TENS[n // 10] + (" " + ONES[n % 10] if (n % 10 != 0) else "")
                elif 100 <= n < 1000:
                                return ONES[n // 100] + " Hundred" + ((" " + to_english(n % 100)) if (n % 100 != 0) else "")
 
ONES = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
        "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
 
def complete_english(n):
    n = str(n).zfill(12)
    l = [int(n[0:3]),int(n[3:6]),int(n[6:9]),int(n[9:12])]
    name = ""
    for i in range(len(l)):
        if l[i] > 0:
            if i == 0:
                name = name + to_english(l[i]) + " Billion "
            if i == 1:
                name = name + to_english(l[i]) + " Million "
            if i == 2:
                name = name + to_english(l[i]) + " Thousand "
            if i == 3:
                name = name + to_english(l[i])
    return name
 
for _ in range(int(input())):
    print(complete_english(int(input())))