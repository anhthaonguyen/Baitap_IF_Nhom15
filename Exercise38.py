n=int(input("Thang:"))
if n=="4" or n=="6" or n=="9" or n=="11":
    ngay = 30
elif n=="2":
     m="28 hoac 29"
else:
    m = 31
print(f"So ngay trong {n} la {m} ngay.")