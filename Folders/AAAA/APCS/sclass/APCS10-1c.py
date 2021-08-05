import sys

for s in sys.stdin:
    if type(s[0]) == str and len(s)==11:
        try:
            digit = int(s[1:])
        except BaseException:
            print("Fake")
            continue
        print("True")
    else:
        print("Fake")