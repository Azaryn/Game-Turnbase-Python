import random
import csv
import termcolor
import os
import time

stats = []
skill = []

def clear():
    os.system("cls")

def pagar():
    print("="*101)

def red(anu):
    logo()
    termcolor.cprint(anu.center(101), "red")

def green(anu):
    logo()
    termcolor.cprint(anu.center(101), "green")


def logo():
    clear()
    pagar()
    print("""

███████╗ ██████╗ ██╗      ██████╗     ██╗     ███████╗██╗   ██╗███████╗██╗     ██╗███╗   ██╗ ██████╗ 
██╔════╝██╔═══██╗██║     ██╔═══██╗    ██║     ██╔════╝██║   ██║██╔════╝██║     ██║████╗  ██║██╔════╝ 
███████╗██║   ██║██║     ██║   ██║    ██║     █████╗  ██║   ██║█████╗  ██║     ██║██╔██╗ ██║██║  ███╗
╚════██║██║   ██║██║     ██║   ██║    ██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║     ██║██║╚██╗██║██║   ██║
███████║╚██████╔╝███████╗╚██████╔╝    ███████╗███████╗ ╚████╔╝ ███████╗███████╗██║██║ ╚████║╚██████╔╝
╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝     ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                     
          """)
    pagar()

def main():
    while True:
        clear()
        print("WELCOME TO SOLO LEVELING")
        print("1. LOGIN")
        print("2. REGISTER")
        print("3. EXIT GAME")
        try:
            pilih = int(input("Your Answer: "))
        except ValueError:
            red("INVALID, TRY AGAIN")
        if pilih == 1:
            login()
            break
        elif pilih == 2:
            register()
            break
        elif pilih == 3:
            clear
            exit()
        else:
            red("INVALID, TRY AGAIN")

def login():
    while True:
        clear()
        logo()
        print("LOGIN".center(101))
        pagar()
        global username
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")
        anu = 0
        with open(f"user/{username}.csv", mode='r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row == [username,password]:
                    anu += 1
                else:
                    continue
        if anu == 1:
            clear()
            logo()
            green("ACCESS ACCEPTED")
            pagar()
            time.sleep(1)
            main()
            break
        else:
            logo()
            red("ACCESS DENIED")
            pagar()
            time.sleep(1)
            clear()
            continue


def register():
    while True:
        akun = []
        data = []
        
        while True:
            clear()
            logo()
            print("REGISTER")
            pagar()
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            akun.append(username)
            akun.append(password)
            break

        while True:
            clear()
            logo()
            print("CHOOSE YOUR ROLE")
            pagar()
            print("1. 🗡️ Warrior")
            print("2. 🏹 Archer")
            print("3. view information role")

            anu = int(input("Your Answer: "))
            match anu:
                case 1:
                    data.append("Warrior")
                    data.append(1) #Level
                    data.append(0) #exp
                    data.append(15) #base HP
                    data.append(5) #base ATK
                    data.append(5) #CritRate
                    data.append(20) #CritDMG
                    break
                case 2:
                    data.append("Archer")
                    data.append(1) #Level
                    data.append(0) #exp
                    data.append(10) #base HP
                    data.append(10) #base ATK
                    data.append(5) #CritRate
                    data.append(20) #CritDMG
                    break
                case _:
                    print("Pilihan tidak ada")
                    continue
        
        with open("user/user.csv", mode="a", newline='') as f:
            write = csv.writer(f)
            write.writerow(akun)
        with open("user/profile.csv", mode='a', newline='') as f:
            write = csv.writer(f)
            write.writerow(data)
            
        green("REGISTER SUCCESS")



def main():
    pass

# =======================================================================
def inventory():
    pass

def profile():
    pass

def upgrade():
    pass

def skillpoint():
    pass

def shop():
    pass
# =======================================================================
def hunt():
    pass

def attack():
    pass

def heal():
    pass

def dodge():
    pass

def skill():
    pass

# =========================================================================
def gacha():
    pass

if __name__ == "__main__":
    # main()
    register()