print("""

List of Menu Functions
Select a function below

1. Phone Book
2. Media
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM Services

""")

menu = int(input("Choose Option: "))

match menu:

    case 1:
        print("""
1. Search
2. Service Nos.
3. Add Name
4. Erase
5. Edit
6. Assign Tone
7. Send b'card
8. Options
9. Speed Dials
10. Voice Tags
""")

        sub_menu = int(input("Choose Option: "))

        match sub_menu:
            case 1:
                print("""
NOT FOUND!!
""")
            case 2:
                print("""
NOT FOUND!!
""")
            case 3:
                print("""
NOT FOUND!!
""")
            case 4:
                print("""
NOT FOUND!!
""")
            case 5:
                print("""
NOT FOUND!!
""")
            case 6:
                print("""
NOT FOUND!!
""")
            case 7:
                print("""
NOT FOUND!!
""")
            case 8:
                print("""
1. Type of View
2. Memory Status
""")
                sub_menu = int(input("Choose Option: "))
                match sub_menu:
                    case 1:
                        print("""
NOT FOUND!!
""")
                    case 2:
                        print("""
NOT FOUND!!
""")
            case 9:
                print("""
NOT FOUND!!
""")
            case 10:
                print("""
NOT FOUND!!
""")


    case 2:
        print("""
1. Write Messages
2. Inbox
3. Outbox
4. Picture Messages
5. Templates
6. Smileys
7. Message Settings
8. Info Service
9. Voice Mailbox Number
10. Service Command Editor
""")
        sub_menu = int(input("Choose Option: "))
        match sub_menu:
            case 1:
                print("""
NOT FOUND!!
""")
            case 2:
                print("""
NOT FOUND!!
""")
            case 3:
                print("""
NOT FOUND!!
""")
            case 4:
                print("""
NOT FOUND!!
""")
            case 5:
                print("""
NOT FOUND!!
""")
            case 6:
                print("""
NOT FOUND!!
""")
            case 8:
                print("""
NOT FOUND!!
""")
            case 9:
                print("""
NOT FOUND!!
""")
            case 10:
                print("""
NOT FOUND!!
""")
            case 7:
                print("""
1. Set 1
2. Common
""")
                sub_menu = int(input("Choose Option: "))
                match sub_menu:
                    case 1:
                        print("""
1. Message Centre Number
2. Message Sent as
3. Message Validity
""")
                        sub_menu = int(input("Choose Option: "))
                        match sub_menu:
                            case 1:
                                print("""
NOT FOUND!!
""")
                            case 2:
                                print("""
NOT FOUND!!
""")
                            case 3:
                                print("""
NOT FOUND!!
""")
                    case 2:
                        print("""
1. Delivery Reports
2. Reply via Same Centre
""")
                        sub_menu = int(input("Choose Option: "))
                        match sub_menu:
                            case 1:
                                print("""
NOT FOUND!!
""")
                            case 2:
                                print("""
NOT FOUND!!
""")
        
    case 3:
        print("""
NOT FOUND!!
""")

    case 4:
        print("""
1. Missed Calls
2. Recieved Calls
3. Dialled Numbers
4. Erasw Recent Call Lists
5. Show Call Duration
6. Show Call Costs
7. Call Cost Settings
8. Prepaid Credit
""") 
        sub_menu = int(input("Choose Option: "))
        match sub_menu:
            case 1:
                print("""
NOT FOUND!!
""")
            case 2:
                print("""
NOT FOUND!!
""")
            case 3:
                print("""
NOT FOUND!!
""")
            case 4:
                print("""
NOT FOUND!!
""")
            case 5:
                print("""
1. Last Call Duration
2. All Calls' Duration
3. Recieved Calls' Duration
4. Dialled Calls' Duration
5. Clear Timers
""")
                sub_menu = int(input("Choose Option: "))
                match sub_menu:
                    case 1:
                        print("""
NOT FOUND!!
""")
                    case 2:
                        print("""
NOT FOUND!!
""")
                    case 3:
                        print("""
NOT FOUND!!
""")
                    case 4:
                        print("""
NOT FOUND!!
""")
                    case 5:
                        print("""
NOT FOUND!!
""")
            case 6:
                print("""
1. Last Call Cost
2. All Calls' Costs
3. Clear Counters
""")
                sub_menu = int(input("Choose Option: "))
                match sub_menu:
                    case 1:
                        print("""
NOT FOUND!!
""")
                    case 2:
                        print("""
NOT FOUND!!
""")
                    case 3:
                        print("""
NOT FOUND!!
""")
            case 7:
                print("""
1. Call Cost Limit
2. Show Costs in
""")
                sub_menu = int(input("Choose Option: "))
                match sub_menu:
                    case 1:
                        print("""
NOT FOUND!!
""")
                    case 2:
                        print("""
NOT FOUND!!
""")
            case 8:
                print("""
NOT FOUND!!
""")
       
    case 5:
        print("""
1. Ringing Tone
2. Ringing Volume
3. Incoming Call Alerts
4. Composer
5. Message Alert Tone
6. Keypad Tones
7. Warning and Game Tones
8. Viberating Alert
9. Screen Saver
""")    
        sub_menu = int(input("Choose Option: "))
        match sub_menu:
            case 1:
                print("""
NOT FOUND!!
""")
            case 2:
                print("""
NOT FOUND!!
""")
            case 3:
                print("""
NOT FOUND!!
""")
            case 4:
                print("""
NOT FOUND!!
""")
            case 5:
                print("""
NOT FOUND!!
""")
            case 6:
                print("""
NOT FOUND!!
""")
            case 7:
                print("""
NOT FOUND!!
""")
            case 8:
                print("""
NOT FOUND!!
""")
            case 9:
                print("""
NOT FOUND!!
""")

      
    case 6:
        print("""
1. Call Settings
2. Phone Settings
3. Security Settings
4. Restore Factory Seetings
""")      

        sub_menu = int(input("Choose Option: "))
        match sub_menu:
            case 1:
                print("""
1. Automatic Redail
2. Speed Dialling
3. Call Waiting Options
4. Own Number Sending
5. Phone Line in Use
6. Automatic Answer
""")
                sub_menu = int(input("Choose Option: "))
                match sub_menu:
                    case 1:
                        print("""
NOT FOUND!!
""")
                    case 2:
                        print("""
NOT FOUND!!
""")
                    case 3:
                        print("""
NOT FOUND!!
""")
                    case 4:
                        print("""
NOT FOUND!!
""")
                    case 5:
                        print("""
NOT FOUND!!
""")
                    case 6:
                        print("""
NOT FOUND!!
""")
            case 2:
                print("""
1. Language
2. Cell Info Display
3. Welcome Note
4. Network Selection
5. Lights
6. Confirm SIM Service Actions
""")
                sub_menu = int(input("Choose Option: "))
                match sub_menu:
                    case 1:
                        print("""
NOT FOUND!!
""")
                    case 2:
                        print("""
NOT FOUND!!
""")
                    case 3:
                        print("""
NOT FOUND!!
""")
                    case 4:
                        print("""
NOT FOUND!!
""")
                    case 5:
                        print("""
NOT FOUND!!
""")
                    case 6:
                        print("""
NOT FOUND!!
""")
            case 3:
                print("""
1. PIN Code Request
2. Call Barring Service
3. Fixed Dialling
4. Closed User Group
5. Phone Security
6. Change Access Codes
""")
                sub_menu = int(input("Choose Option: "))
                match sub_menu:
                    case 1:
                        print("""
NOT FOUND!!
""")
                    case 2:
                        print("""
NOT FOUND!!
""")
                    case 3:
                        print("""
NOT FOUND!!
""")
                    case 4:
                        print("""
NOT FOUND!!
""")
                    case 5:
                        print("""
NOT FOUND!!
""")
                    case 6:
                        print("""
NOT FOUND!!
""")
            case 4:
                print("""
NOT FOUND!!
""")

    case 7:
        print("""
NOT FOUND!!
""")

    case 8:
        print("""
NOT FOUND!!
""")

    case 9:
        print("""
NOT FOUND!!
""")

    case 10:
        print("""
NOT FOUND!!
""")
   
    case 11:
        print("""
1. Alarm Clock
2. Clock Settings
3. Date Setting
4. Stopwatch
5. Countdown Timer
6. Auto-Update of Date and Time
""")        
        sub_menu = int(input("Choose Option: "))
        match sub_menu:
            case 1:
                print("""
NOT FOUND!!
""")
            case 2:
                print("""
NOT FOUND!!
""")
            case 3:
                print("""
NOT FOUND!!
""")
            case 4:
                print("""
NOT FOUND!!
""")
            case 5:
                print("""
NOT FOUND!!
""")
            case 6:
                print("""
NOT FOUND!!
""")

    case 12:
        print("""
NOT FOUND!!
""")

    case 13:
        print("""
NOT FOUND!!
""")
