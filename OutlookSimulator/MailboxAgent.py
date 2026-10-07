# Outlook Simulator - MailboxAgent manages all Mail, Confidential, and Personal objects
# Interpreter calls this class to perform mailbox operations

from Mail import *
from Confidential import *
from Personal import *

class MailboxAgent:
    """Handles storing, searching, sorting, and modifying emails"""

    def __init__(self, email_data):
        # Convert raw email strings into Mail objects
        self._mailbox = self.__gen_mailbox(email_data)

    # Step 1: Build mailbox from raw strings
    @classmethod
    def __gen_mailbox(cls, email_data):
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

    # Step 2: Basic operations
    def get_mail(self, m_id):
        for mail in self._mailbox:
            if str(mail.m_id) == str(m_id):
                return mail
        return None

    def del_mail(self, m_id):
        mail = self.get_mail(m_id)
        if mail:
            mail.tag = "bin"
            return True
        return False

    def filter_by_sender(self, frm):
        return [mail for mail in self._mailbox if mail.frm == frm]

    def find_by_date(self, date):
        return [mail for mail in self._mailbox if mail.date == date]

    # Step 3: Listing emails
    def list_mailbox(self):
        if not self._mailbox:
            print("MailboxAgent is empty")
            return

        lines = [
            "Id|From|To|Subject|Date|body|Tag"
        ]
        for mail in self._mailbox:
            lines.append(
                f"{mail.m_id}|{mail.frm}{mail.to}|{mail.subject}|{mail.date}|{mail.body}|{mail.tag}"
            )
        print("\n".join(lines))

    # Step 4: Modify email status
    def move_mail(self, m_id, tag):
        mail = self.get_mail(m_id)
        if mail:
            mail.tag = tag
            return True
        return False

    def mark_read(self, m_id):
        mail = self.get_mail(m_id)
        if mail:
            mail.read = True
            return True
        return False

    def mark_flagged(self, m_id):
        mail = self.get_mail(m_id)
        if mail:
            mail.flag = True
            return True
        return False

    # Step 5: Sorting
    def sort_by_sender(self):
        self._mailbox.sort(key=lambda x: x.frm)
        return self._mailbox

    # Step 6: Add new mail (normal, confidential, personal)
    def add_mail(self, frm, to, date, subject, tag, body):
        new_id = max(int(mail.m_id) for mail in self._mailbox) + 1 if self._mailbox else 0

        tag_lower = tag.lower()

        if tag_lower == "conf":
            new_mail = Confidential(new_id, frm, to, date, subject, tag, body)
        elif tag_lower == "prsnl":
            new_mail = Personal(new_id, frm, to, date, subject, tag, body)
        else:
            new_mail = Mail(new_id, frm, to, date, subject, tag, body)

        self._mailbox.append(new_mail)
        return new_mail