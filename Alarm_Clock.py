# • current_second (a value in the range of 0–59)
# • current_minute (a value in the range of 0–59)
# • current_hour (a value in the range of 1–12)
# • alarm_time (a valid hour and minute)
# • alarm_is_set (True or False)

class AlarmClock:

    __current_minute = 0        #(a value in the range of 0–59)
    __current_hour   = 1        #(a value in the range of 1–12)
    __alarm_is_set   = False    #  (True or False)

    def setMinute(self,m):
        if m>=0 and m<=59:
            self.__current_minute = m
        else:
            print("enter is wrong")
    def getMinute(self):
        print(self.__current_minute)

am = AlarmClock()
am.setMinute(60)
am.getMinute()
