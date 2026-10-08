# Outlook-Simulator (Python)
This project was inspired by my curiosity on the inner workings of an everyday utility. Rather than building a basic, surface-level project, I wanted to build something that I would help me practice building real-world systems rather than a single script and would also feel like an accomplishment.


It runs in the command-line, generates a mailbox, and allows you to interact with emails the way you would in a simplified version of Outlook. It also has added features such as custom email types, a basic encryption feature, and some little analytics for personal messages.

-----
## What This Project Does ##
- Creates a fake mailbox that's filled with generated emails

- Lets you interact with the mailbox through a simple command-line prompt

- Supports several types of emails:

   - Normal Mail
   - Confidential Mail (hidden body and custom encryption)
   - Personal Mail (extra stats like a word count)
- This project lets you:
  
  - List emails
  - Open an email
  - Filter by sender
  - Search by date
  - Mark emails as flagged or read
  - Move emails to different tags
  - Soft-delete emails (moving them to the "bin")
  - Add your own emails directly through the command-line interface
-----
## What I Learned ##
While building this project I learned to:
- Work with several Python files and classes
- Parse data and turn it into structured objects
- Design a system with different components that communicate with each other
- Build something that feels like a proper application
-----
## How It's Structured ##
The structure is simple and easy to read and follow
```
Outlook_Simulator/
│
├─ Mail.py             # Base email class
├─ Confidential.py     # Confidential email type (hidden body and custom encryption)
├─ Personal.py         # Personal email type (analytics)
├─ MailboxAgent.py     # Mailbox controller (searching, tagging, and parsing)
└─ Interpreter.py      # Command-line interface
```

Each file has its own responsibility, and collectively the simulator will run

-----
## How To Use It ##
1. Clone the repo
2. Open in your chosen IDE (I used PyCharm)
3. Run `Interpreter.py`
4. You will see this prompt:
```
mba>
```
After that, you can use the different commands:
```
lst                    # List all the emails
get 3                  # Open email with ID 3
flt email10@gre.ac.uk   # Filter emails by sender
fnd 12/5/2025          # Find emails by date
add sender receiver date subject tag %% message body here
del 7                  # Move email with ID 7 to bin folder
mrkr 4                 # Mark email with ID 4 as read
mv 2 work              # Move email with ID 2 with "work" tag
end                    # Exit the simulator
```
-----
## Programs Demonstration ##
https://github.com/user-attachments/assets/6485f9e6-caba-4dd4-a45d-aab805f7b391

-----
## Future Expansions ##
- Reply/ Forward feature
- A small GUI (PyQT or Tinker)
- Saving the mailbox data per session
-----
## Final Thoughts ## 
This project was challenging and really helped me apply what I had I learned to build something that would be used daily in a real-world scenario  
