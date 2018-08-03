import sys
import requests
import re
from PySide2.QtCore import Qt
from PySide2.QtWidgets import (QPushButton, QLineEdit,
                             QApplication, QLabel, QMessageBox,
                             QMainWindow, QListWidget, QListWidgetItem)



class MainFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Define buttons
        # Button to calculate lunar dates
        self.calculate_lunar = QPushButton('음력날짜 계산', self)
        self.calculate_lunar.clicked.connect(self.calculate_lunar_date)
        self.calculate_lunar.setGeometry(20, 260, 130, 35)
        self.calculate_lunar.setStatusTip('음력 날짜를 계산합니다.')
        self.calculate_lunar.setShortcut('Return')

        # Button to save ICS file to local directory
        self.ICS_save_button = QPushButton('ICS 파일 저장', self)
        self.ICS_save_button.clicked.connect(self.create_ics_file)
        self.ICS_save_button.setGeometry(175, 260, 130, 35)
        self.ICS_save_button.setStatusTip('ICS 파일을 컴퓨터에 저장합니다.')

        # Define labels
        # Define label for lunar date to convert
        lunar_date_text = QLabel(self)
        lunar_date_text.setText('계산할 음력 날짜')
        lunar_date_text.setGeometry(25, 15, 240, 25)

        # Define label for name of event
        event_name_text = QLabel(self)
        event_name_text.setText('이벤트 이름 입력')
        event_name_text.setGeometry(25, 50, 240, 25)

        # Define label for repetition
        event_name_text = QLabel(self)
        event_name_text.setText('몇년치나 할까요?')
        event_name_text.setGeometry(25, 85, 240, 25)

        # Define ListWidget to display results
        self.result_console = QListWidget(self)
        self.result_console.setGeometry(25, 118, 275, 133)
        self.result_console.setStatusTip('올해부터 매년 양력날짜가 출력됩니다.')

        # Define user input areas
        # Define lunar date to convert to solar date
        self.user_date_input = QLineEdit(self)
        self.user_date_input.setGeometry(180, 15, 120, 27)
        self.user_date_input.setAlignment(Qt.AlignCenter)
        self.user_date_input.setPlaceholderText('YYYYMMDD')
        self.user_date_input.setStatusTip('날짜를 YYYYMMDD로 입력하세요.')

        # Define name of event to use in ICS file
        self.user_event_name = QLineEdit(self)
        self.user_event_name.setGeometry(180, 50, 120, 27)
        self.user_event_name.setAlignment(Qt.AlignCenter)
        self.user_event_name.setPlaceholderText('이벤트 이름')
        self.user_event_name.setStatusTip('이벤트 이름을 입력하세요.')

        # Define number of years to convert
        self.user_repetition = QLineEdit(self)
        self.user_repetition.setGeometry(180, 84, 120, 27)
        self.user_repetition.setAlignment(Qt.AlignCenter)
        self.user_repetition.setText('10')
        self.user_repetition.setStatusTip('생성할 햇수를 입력하세요.')

        # Define size of main window
        self.setGeometry(200, 320, 325, 330)
        self.setWindowTitle('날짜')
        self.statusBar()
        self.show()

    # Define functions
    # Function to parse lunar date from openAPI website using user input
    def calculate_lunar_date(self):
        if len(self.user_date_input.text()) != 8:
            reply = QMessageBox.question(self, 'Error',
                                         "YYYYMMDD로 정확한 날짜를 입력해 주십시오.", QMessageBox.Close)
            return

        url = 'http://apis.data.go.kr/B090041/openapi/service/LrsrCldInfoService/getSolCalInfo'
        personal_key = 'your_user_key_here' 	
        lunar_input = self.user_date_input.text()
        lunar_month = lunar_input[4:6]
        lunar_day = lunar_input[6:]
        repeat = int(self.user_repetition.text()) + 1

        for i in range(0, repeat):
            lunar_year = int(lunar_input[:4]) + int(i)
            query_params = '?lunYear={}&lunMonth={}&lunDay={}&ServiceKey={}'.format(lunar_year, lunar_month,
                                                                                    lunar_day, personal_key)

            # TODO: parse xml file as a whole for better performance
            r = requests.get(url + query_params)
            raw_text = r.text

            # TODO: use different method to extract date from xml, or at least use better regex
            solar_day = re.search('<solDay>(\d\d)<\/solDay>', raw_text).group(1)
            solar_month = re.search('<solMonth>(\d\d)<\/solMonth>', raw_text).group(1)
            solar_week = re.search('<solWeek>(.+?)</solWeek>', raw_text).group(1)
            solar_year = re.search('<solYear>(\d\d\d\d)<\/solYear>', raw_text).group(1)
            solar_date_text = '   {}년 {}월 {}일 {}요일 '.format(solar_year, solar_month, solar_day, solar_week)

            QListWidgetItem(solar_date_text, self.result_console)

    def create_ics_file(self):
        event_name = self.user_event_name.text()
        # TODO: use different method to extract date from QListWidgetItem, or at least use better regex
        ics_date_capture = re.compile('(\d\d\d\d).+?(\d\d).+?(\d\d)')
        ics_content = 'BEGIN:VCALENDAR\nVERSION:2.0\nCALSCALE:GREGORIAN\nBEGIN:VTIMEZONE\nTZID:Asia/Tokyo\n' \
                      'TZURL:http://tzurl.org/zoneinfo-outlook/Asia/Tokyo\nX-LIC-LOCATION:Asia/Tokyo\n' \
                      'BEGIN:STANDARD\nTZOFFSETFROM:+0900\nTZOFFSETTO:+0900\nTZNAME:JST\n' \
                      'DTSTART:19700101T000000\nEND:STANDARD\nEND:VTIMEZONE\n'

        if len(self.user_event_name.text()) == 0:
            reply = QMessageBox.question(self, 'Error', "이벤트 이름을 입력해 주십시오.", QMessageBox.Close)
            return
        elif self.result_console.count() == 0:
            reply = QMessageBox.question(self, 'Error', "날짜 계산을 먼저 해주십시오.", QMessageBox.Close)
            return

        # https://stackoverflow.com/a/34479509
        converted_dates = [str(self.result_console.item(i).text()) for i in range(self.result_console.count())]
        for i in converted_dates:
            event_string = 'BEGIN:VEVENT\nDTSTAMP:20180802T115053z\nDTSTART;TZID="Asia/Tokyo":{0}T120000' \
                           '\nDTEND;TZID="Asia/Tokyo":{0}T120000\nSUMMARY:{1}\nBEGIN:VALARM\n' \
                           'TRIGGER:-PT14H\nREPEAT:1\nACTION:DISPLAY\nDESCRIPTION:Reminder\nEND:VALARM\nEND:VEVENT\n'
            result = ics_date_capture.search(i)
            date_string = result.group(1) + result.group(2) + result.group(3)
            ics_content += event_string.format(date_string, event_name)

        ics_content += 'END:VCALENDAR'

        # This program cannot read existing .ics files, so if user creates a new ics event with existing file name,
        # the program would crash.
        new_ics = open(event_name.replace(' ', '') + '.ics', 'w')
        new_ics.write(ics_content)
        new_ics.close()

        success = QMessageBox.question(self, 'Success', "ICS 파일 생성 완료!", QMessageBox.Close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainFrame()
    sys.exit(app.exec_())
