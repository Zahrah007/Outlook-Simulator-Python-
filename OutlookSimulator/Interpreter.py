# Outlook Simulator - Command-line interpreter
# Handles the user input and passes commands to the MailboxAgent

from MailboxAgent import *
import random
import string

# Step 1: Generate random bodies for the auto-generated emails
def gen_bdy():
    snt = ''
    for i in range(random.randint(1,10)):
        snt += ''.join(random.choices(string.ascii_lowercase, k=random.randint(3,10)))+' '
    return f"Body{str(random.randint(0, 140))}. {snt.capitalize()[:-1]}."

# Step 2: Generate raw email strings that MailboxAgent will convert into Mail objects
def gen_emails():
    msgs, msg_id = [], 0
    for i in range(40):
        msg = ''
        for j in range(30):
            msg += f"ID:{str(msg_id)}"+"\n"
            msg += f"From:email{random.randint(0, 15)}@gre.ac.uk\n"
            msg += f"To:email{random.randint(0, 80)}@gre.ac.uk\n"
            msg += f"Date:{random.randint(1, 29)}/{random.randint(0, 12)}/2025\n"
            msg += f"Subject:subject{random.randint(0, 100)}\n"
            msg += f"Tag:tag{random.randint(0, 6)}\n"
            msg += f"Body:{gen_bdy()}\n"
            msg += "Flag:False\n"
            msg += "Read:False\n"
        msgs.append(msg)
        msg_id += 1
    return msgs

# Step 3: Show available commands
def display_command_help():
    print('Interpreter Commands:')
    print('get <m_id> | lst | mv <m_id> <tag> | del <m_id> | mrkr <m_id> | mrkf <m_id> | '
          'flt <frm> | fnd <date> | add <email>')

# Step 4: Main loop that reads the commands and calls MailboxAgent
def loop():
    mba = MailboxAgent(gen_emails())
    display_command_help()

    line = input('mba > ')
    words = line.split(' ')
    command, args = words[0],words[1:]

    while command != 'end':
        match command:

            # Add new mail
            case 'add':
                try:
                    body_index = line.index('%%')
                    body = line[body_index + 2:]
                    parts = line[:body_index].split(' ')
                    frm, to, date, subject, tag = parts[1:6]
                    mba.add_mail(frm, to, date,subject,tag,body)
                except Exception as e:
                    print(f"Error adding email: {e}")

            # Delete (move to bin)
            case 'del':
                try:
                    m_id = int(args[0])
                    mba.del_mail(m_id)
                except Exception as e:
                    print(f"Error deleting email: {e}")

            # Filter by sender
            case 'flt':
                try:
                    sender = args[0]
                    mails = mba.filter_by_sender(sender)
                    for m in mails:
                        print(m.show_email())
                except Exception as e:
                    print(f"Error filtering emails: {e}")

            # Find by date
            case 'fnd':
                try:
                    date = args[0]
                    mails = mba.find_by_date(date)
                    for m in mails:
                        print(m.show_email())
                except Exception as e:
                    print(f"Error finding emails: {e}")

            # Get single email
            case 'get' :
                try:
                    m_id = int(args[0])
                    mail = mba.get_mail(m_id)
                    print(mail.show_email() if mail else "Email not found.")
                except Exception as e:
                    print(f"Error retrieving email: {e}")

            # List mailbox
            case 'lst' :
                try:
                    mba.list_mailbox()
                except Exception as e:
                    print(f"Error listing mailbox: {e}")

            # Mark read
            case 'mrkr':
                try:
                    m_id = int(args[0])
                    mba.mark_read(m_id)
                except Exception as e:
                    print(f"Error marking as read: {e}")

            # Mark flagged
            case 'mrkf':
                try:
                    m_id = int(args[0])
                    mba.mark_flagged(m_id)
                except Exception as e:
                    print(f"Error marking as flagged: {e}")

            # Move email to another tag
            case 'mv':
                try:
                    m_id = int(args[0])
                    tag = args[1]
                    mba.move_mail(m_id, tag)
                except Exception as e:
                    print(f"Error moving mail: {e}")

        line = input('mba > ')
        words = line.split(' ')
        command, args = words[0], words[1:]

if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        print("\nSession interrupted. Goodbye!")