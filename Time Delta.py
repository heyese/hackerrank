import datetime

def time_delta(t1, t2):
    # Date format is: Day dd Mon yyyy hh:mm:ss +xxxx
    format_str = '%a %d %b %Y %H:%M:%S %z'
    a = datetime.datetime.strptime(t1, format_str)
    b = datetime.datetime.strptime(t2, format_str)
    if a > b:
        return (a-b).days*60*60*24 + (a-b).seconds
    return (b-a).days*60*60*24 + (b-a).seconds

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(f'{delta}')


