
decibel_level = int(input("Enter a sound level in decibels: "))

if decibel_level > 130:
        print("The sound level is louder than a jackhammer")
elif decibel_level == 40:
        print("The sound level is equivalent to a quiet room")
elif decibel_level > 40 and decibel_level < 70:
        print("The sound level is between a quiet room and an alarm clock")
elif decibel_level == 70:
        print("The sound level is equivalent to an alarm clock")
elif decibel_level > 70 and decibel_level < 106:
        print("The sound level is between an alarm clock and a gas lawnmower")
elif decibel_level == 106:
        print("The sound level is equivalent to a gas lawnmower")
elif decibel_level > 106 and decibel_level < 130:
        print("The sound level is between a gas lawnmower and a jackhammer")
else:
        print("The sound level is quieter than a quiet room")


