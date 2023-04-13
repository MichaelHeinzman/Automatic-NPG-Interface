from PyQt6.QtWidgets import  QLineEdit

class Input(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.textStyle = '''
            position: absolute;
            width: 122px;
            max-height: 32px;
            padding: 10px;
            left: 700px;
            top: 161px;
            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-size: 16px;
            line-height: 19px;
            text-align: center;
            color: #363C4B;
            background-color: rgba(217, 217, 217, 1);
        '''

        self.setStyleSheet(self.textStyle)