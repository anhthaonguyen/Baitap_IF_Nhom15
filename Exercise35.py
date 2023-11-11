tuoinguoi=int(input("n="))
if tuoinguoi>0:
    if 0<tuoinguoi<=2:
        tuoiconcho=tuoinguoi*10.5
    elif tuoinguoi>2:
        tuoiconcho=21+(tuoinguoi-2)*4
    print(f"Tuoi cua con cho tuong ung voi {tuoinguoi} nam cua con nguoi la {tuoiconcho} nam")
else:
    print("Error")