def main():
    s = input()
    print(convert(s))

def convert(s):
    s1 = s.replace(":)", '\N{Slightly Smiling Face}')
    s2 = s1.replace(":(", '\N{Slightly Frowning Face}')
    return s2

main()