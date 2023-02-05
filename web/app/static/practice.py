#/usr/bin/env python3

def main():
    twelve_hr_time(8,30) #8:30AM
    twelve_hr_time(18,30) #6:30PM
    twelve_hr_time(12,00) #12:00PM
    twelve_hr_time(0,00) #12:00AM

def twelve_hr_time(hour,min):
    #1 ถ้าหลังบ่ายโมงเป็นPMแล้วเอาชม.มาลบ12
    #2 ถ้าเที่ยงพอดีเป็นPMชม.ไม่ต้องทำอะไร
    #3 ถ้าเป็นเที่ยงคืนเป็นAMเอาชม.มาบวก12
    #4 กรณีอื่นๆ ไม่ต้องทำอะไร
    if hour >= 13 :
        print('{:02d}:{:02d}'.format(hour-12,min),'PM')
    elif hour == 12 :
        print('{:02d}:{:02d}'.format(hour,min),'PM')
    elif hour == 0 :
        print('{:02d}:{:02d}'.format(hour+12,min),'AM')
    else:
        print('{:02d}:{:02d}'.format(hour,min),'AM')

if __name__=='__main__':
    main()

