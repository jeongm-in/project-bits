# project-bits
Repository for miscellaneous projects

# contents
## 음력 날짜 계산기 | Lunar Date Converter
### Overview
  - A program to easily convert lunar calendar to Gregorian calendar. Can also export results to .ics file.
  - 매년 반복되는 음력 생일을 일일히 검색해서 달력에 넣기 귀찮아서 몇년치를 한번에 검색해서 [.ics파일](https://en.wikipedia.org/wiki/ICalendar)로 내보낼 수 있는 프로그램을 만들었습니다. 
  - Lunar dates in Gregorian calendar change every year, and it can be tedious to keep track of different dates every year. This program will create .ics file with multiple years' lunar-Gregorian date events. Add once and forget about it for decades!
  - ![LDTGUI](https://raw.githubusercontent.com/jeongm/miscellaneous-bits/master/lunar_date_converter/lunar_date_converter.png)

### Important Information
  - [공공데이터포털](https://data.go.kr)의 음양력 정보제공 서비스를 이용해서 제작하였습니다. 
  - Utilizes Lunar-Gregorian information service from [South Korea Public Data Portal](https://data.go.kr).
  - 사용하실 때는 공공데이터포털에서 인증키를 발급받아서 코드 안에 넣어주세요. 
  - API Key from Public Data Portal is required.
  - 공공데이터포털에서는 2050년 음력 달력까지만 제공하므로, 이 프로그램 역시 2050년까지 날짜만 출력됩니다.
  - Public Data Portal only provides lunar calendar upto year 2050, so this program only supports dates upto year 2050.
### requirements
  - Python 3.7 / PySide2 5.11.1 / requests-xml 0.2.3
  - API key from [Public Data Portal](https://data.go.kr)

## Windows Lockscreen Image Crawler

## Multi-Tools Page
