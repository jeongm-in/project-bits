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
### Overview
  - Windows 10 by default ships with beautiful image slide shows (spotlight). 
  - I wanted to save those images so that I could use them as my desktop background.
  - This is a python script file that saves all windows spotlight lockscreen images into a designated directory in Documents. 
  
### Miscellaneous Details
  - Windows 10 saves miscellaneous image files, including the files for the lockscreen slide show, in a local directory under `Users/name/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager/_cw5n1h2txyewy/LocalState/Assets`
  - Windows 10 spotlight saves both landscape (1920 * 1080) and portrait (1080 * 1920) sized images
  - Windows 10 also saves icon files for __default__ apps such as Candy Crush Saga
  - This script filters out icon files and asks user which image dimensions to save. 
### Todo
  - Create GUI file to get rid of all the commandline interaction
  - Add feature for an one-time installation and regular automatic save
### requirements 
  - Python==3.6.7 or above / Pillow==5.3.0
  - __Windows 10__

## Multi-Tools Page
