#Name Generator
#Amelie Lynde
#10/17/24

#Init

#Functions
print("Welcome to your Fairy Name 2000")
print("Answer the questions to find out your fairy name")
ans = input("pink (p) or blue (b) ?")
if ans == "p":
    ans = input("dessert (dess) or fruit (fru) ?")
    if ans == "dess":
        ans = input("cookies (cook) or cake (cake) ?")
        if ans == "cook":
            print("Your name is SugarSweet")
        else:
            print("Your name is Shortcake")
    if ans == "fru":
        ans = input("raspberries (rasp) or blueberries (blu) ?")
        if ans == "rasp":
            print("Your name is Rose")
        else:
            print("Your name is Sugarplum")
if ans == "b":
    ans = input("Winter (win) or Summer (sum) ?")
    if ans == "win":
        ans = input("Night (n) or day (d) ?")
        if ans == "n":
            print("Your name is Celeste")
        else:
            print("Your name is Holly")
    if ans == "sum":
        ans = input("Ocean (oce) or Mountain (mount) ?")
        if ans == "oce":
            print("Your name is Silvermist")
        else:
            print("Your name is Poppy")

#Main
