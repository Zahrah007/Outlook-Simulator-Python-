# Outlook Simulator - Personal email type
# Extends Mail and adds simple statistics for personal emails

from Mail import *

class Personal(Mail):
    """Represents a personal email message like normal emails but including extra stats."""

    def __init__(self, m_id, frm, to, date, subject, tag, body):
        super().__init__(m_id, frm, to, date, subject, tag, body)

    # Step 1: Short display version
    def display(self):
        return f"[Personal] From: {self.frm}, To: {self.to}, Subject: {self.subject}, Date: {self.date}"

    # Step 2: Generate simple statistics about the body
    def add_stats(self):
        body = self.body.strip()
        words = body.split()

        return {
            "word_count": len(words),
            "char_count": len(body),
            "sent_count": 1
        }