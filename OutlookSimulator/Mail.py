# Outlook Simulator - Base Mail class
# All email types (normal, confidential, personal) come from this

class Mail:
    """Basic email structure used throughout the simulator."""

    def  __init__(self,m_id,frm,to,date,subject,tag,body):
        # Store all fields for the email
        self._m_id = m_id
        self._frm = frm
        self._to = to
        self._subject = subject
        self._date = date
        self._tag = tag
        self._body = body
        self._flag = False
        self._read = False

    # Step 1: Compact string version used in mailbox listings
    def __str__(self):
        return (
            f"m_id:{self.m_id}\tfrom:{self.frm}\t|{self.to}\t|"
            f"{self.date}|{self.subject}|{self.tag}|{self.read}|{self.flag}"
        )

    # Step 2: Property getters
    @property
    def m_id(self):
        return self._m_id

    @property
    def frm(self):
        return self._frm

    @property
    def to(self):
        return self._to

    @property
    def date(self):
        return self._date

    @property
    def body(self):
        return self._body

    @property
    def subject(self):
        return self._subject

    @property
    def tag(self):
        return self._tag

    @property
    def read(self):
        return self._read

    @property
    def flag(self):
        return self._flag

    # Step 3: Property setters
    @tag.setter
    def tag(self, value):
        self._tag = value

    @read.setter
    def read(self,value):
        self._read = value

    @flag.setter
    def flag(self,value):
        self._flag = value

    # Step 4: Full pretty print for displaying emails
    def show_email(self):
        return (
            f"Message ID: {self._m_id}\n"
            f"From: {self._frm}\n"
            f"To: {self._to}\n"
            f"Date: {self._date}\n"
            f"Subject: {self._subject}\n"
            f"Tag: {self._tag}\n"
            f"Read: {'Yes' if self.read else 'No'}\n"
            f"Flagged: {'Yes' if self.flag else 'No'}\n"
            f"Body: {self._body}\n"
        )