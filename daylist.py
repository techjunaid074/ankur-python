#program for accepting  any week and display its name:
d = {"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"satarday":6,"sunday":7}
day=input("enter the day")
if day in d:
    print("{} is  weekday".format(day))
else :
    print("{} is not week day".format(day))

