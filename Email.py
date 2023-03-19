from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ssl import create_default_context
from smtplib import SMTP
from typing import List, Any
from re import match


class Email:
    def __init__(self, email, password) -> None:
        self.sender: str = email
        self.password: str = password
        self._message: Any = ''
        self._attachment: List[str] = []

    @property
    def message(self) -> Any:
        return self._message

    @message.setter
    def message(self, message: str) -> None:
        self._message = message

    @property
    def attachment(self) -> List[str]:
        return self._attachment

    @attachment.setter
    def attachment(self, attachment: List[str]) -> None:
        self._attachment = attachment

    def send(self, recipient: str) -> None:
        if match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', recipient) is None:
            raise Exception('Not a valid email')
        elif self.message is None:
            raise Exception('Message empty')

        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = recipient
        msg.attach(MIMEText(self.message, 'plain'))

        for file in self.attachment:
            with open(file, 'rb') as f:
                attachment = MIMEApplication(f.read(), _subtype='pdf')
                attachment.add_header('Content-Disposition', 'attachment', filename=file)
                msg.attach(attachment)

        smtp_server: str = 'smtp.gmail.com'
        port: int = 587

        context = create_default_context()
        server = SMTP(smtp_server, port)

        try:
            server.starttls(context=context)
            server.login(self.sender, self.password)
            server.send_message(msg)
        except Exception as err:
            print(err)
        finally:
            server.quit()

    # def send(self, recipient: str) -> None:
    #     if self.message is None:
    #         raise Exception('Message empty')
    #
    #     smtp_server: str = 'smtp.gmail.com'
    #     port: int = 587
    #
    #     context = create_default_context()
    #     server = SMTP(smtp_server, port)
    #
    #     try:
    #         server.starttls(context=context)
    #         server.login(self.sender, self.password)
    #         server.sendmail(self.sender, recipient, self.message)
    #     except Exception as err:
    #         print(err)
    #     finally:
    #         server.quit()
