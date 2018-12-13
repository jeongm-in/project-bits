# miscellaneous-bits
Repository for miscellaneous projects

# contents
## 음력 날짜 계산기 | Lunar Date Converter
  - A program to easily convert lunar dates to solar dates. Can also export results to .ics file.
  - Supports dates upto lunar year 2050.
  - 매년 반복되는 음력 생일을 일일히 검색해서 달력에 넣기 귀찮아서 몇년치를 한번에 검색해서 [.ics파일](https://en.wikipedia.org/wiki/ICalendar)로 내보낼 수 있는 프로그램을 만들었습니다. 
  - [공공데이터포털](https://data.go.kr)의 음양력 정보제공 서비스를 이용해서 제작하였습니다. 
  - 사용하실 때는 공공데이터포털에서 인증키를 발급받아서 코드 안에 넣어주세요. 
  - 공공데이터포털에서는 2050년 음력 달력까지만 제공하므로, 이 프로그램 역시 2050년까지 날짜만 출력됩니다.
  - Build Environment : Python 3.7 / PySide2 5.11.1 / requests-xml 0.2.3
  
  - ![LDTGUI](https://raw.githubusercontent.com/jeongm/miscellaneous-bits/master/lunar_date_converter/lunar_date_converter.png)
