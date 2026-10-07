# Outlook Simulator - Confidential email type
# Extends Mail and encrypts the body for confidential messages

from Mail import *
import string

class Confidential(Mail):
    """Confidential emails hide their body when displayed and can be encrypted"""

    def __init__(self, m_id,frm,to,date,subject,tag,body):
        # Use the base Mail class to store all normal email field
        super().__init__(m_id,frm,to,date,subject,tag,body)

    # Step 1: Override how the email is shown
    # Confidential emails should not reveal their body
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
            f"Body: [CONFIDENTIAL CONTENT HIDDEN]"
        )

    # Step 2: Encrypt the body using a simple mapping system
    # Encryption uses:
    # - Alphabet position * word_count
    # - Digit position * word_count mapped through digital_maps
    # - Punctuation shifted by word_count
    def encrypt(self):
        body = self.body
        word_count = len(body.split())

        alphabet = string.ascii_lowercase
        digits = "0123456789"
        punct = string.punctuation

        digital_maps = {
            '0':'j', '1':'a', '2':'b', '3':'c', '4':'d',
            '5':'e', '6':'f', '7':'g', '8':'h', '9':'i'
        }

        encrypted = []

        for word in body:
            # Encrypt letters
            if word.lower() in alphabet:
                idx = alphabet.index(word.lower())
                new_idx = (idx * word_count) % len(alphabet)
                new_char = alphabet[new_idx]
                encrypted.append(new_char.upper() if word.isupper() else new_char)

            # Encrypt digits
            elif word in digits:
                idx = digits.index(word)
                new_idx = (idx * word_count) % len(digits)
                encrypted.append(digital_maps[digits[new_idx]])

            # Encrypt punctuation
            elif word in punct:
                idx = punct.index(word)
                new_idx = (idx * word_count) % len(punct)
                encrypted.append(punct[new_idx])

            # Leave spaces and other characters alone
            else:
                encrypted.append(word)

        self._body = "".join(encrypted)
        return self._body