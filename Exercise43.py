n=int(input("Gia to tien:"))
m={1: "George Washington",
    2: "Thomas Jefferson",
    5: "Abraham Lincoln",
    10: "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
    100: "Benjamin Franklin"}
if n in m:
    ten=m[n]
    print(f"Nguoi xuat hien tren to tien {n} la {ten}")
else:
    print("Khong co thong tin ve nguoi co xuat hien tren to tien co menh gia nay")
