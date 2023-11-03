# family_age2.py

fa_age = 39         # 아빠 나이 정보

def up_fa_age():    # 아빠 나이 올라감
    global fa_age
    fa_age += 1

def get_fa_age():   # 아빠 나이는?
    return fa_age

mo_age = 35         # 엄마 나이 정보

def up_mo_age():    # 엄마 나이 올라감
    global mo_age
    mo_age += 1

def get_mo_age():   # 엄마 나이는?
    return mo_age


def main():
    print("2019년...")
    print("아빠:", get_fa_age())
    print("엄마:", get_mo_age())

    
    print("2020년...")
    up_fa_age()
    up_mo_age()
    print("아빠:", get_fa_age())
    print("엄마:", get_mo_age())

main()
