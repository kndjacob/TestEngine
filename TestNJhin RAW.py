import csv, random, os, time, math, getpass, msvcrt

def logo():
    print("\033[96m")
    print("     _____         _     _   _     ___ _     _           ")
    print("    |_   _|       | |   | \ | |   |_  | |   (_)          ")
    print("      | | ___  ___| |_  |  \| |     | | |__  _ _ __      ")
    print("      | |/ _ \/ __| __| | . ` |     | | '_ \| | '_ \     ")
    print("      | |  __/\__ \ |_  | |\  | /\__/ / | | | | | | |    ")
    print("      \_/\___||___/\__| \_| \_/ \____/|_| |_|_|_| |_|    ")
    print("")
    print("\033[0m") 

def choose_file():
    global selected_file

    while True:
        
        clear_screen()
        logo()
        current_dir = os.getcwd()
        files = os.listdir()
        print(f"CWD: {current_dir}\n")
        print("Files in current directory:")
    
        for index, file in enumerate(files):
            print(f"{index + 1}. {file}")

        DIRECTORY_INPUTS = ["C","L","Q","H","?"]

        while True:
            
            print("\n(C)hange Directory\n(L)oad Selected Test\n")
            directory_choice = msvcrt.getch().decode('utf-8').upper()

            if directory_choice in DIRECTORY_INPUTS:
                break

            else:
                clear_screen()
                current_dir = os.getcwd()
                files = os.listdir()
                print(f"CWD: {current_dir}\n")
                print("Files in current directory:")
            
                for index, file in enumerate(files):
                    print(f"{index + 1}. {file}")
                 
                print ("\nINVALID INPUT: 'C' to move directories - 'L' to load a .csn into TestNJhin - 'H' or '?' for more invormation." )

        if directory_choice == "Q":
            QUIT_OPTIONS = ["Y","N"]
            
            while True:
                quit_choice = input("Are you sure you want to return to main menu? (Y/N)").upper()
                if quit_choice in QUIT_OPTIONS:
                    break

                else:
                    input("INVALID INPUT: Please press Enter to try again.")

            if quit_choice == "Y":
                return
            
            else:
                break

        if directory_choice == "C":

            new_dir = input("Enter the number of the new directory: ('..' to move up one tier) ")

            if new_dir == "..":
                try:
                    os.chdir(new_dir)

                except:
                    input("Something went wrong . . .\nPress Enter to try again.")
                    continue
            
            else:

                try:
                    selected_dir = files[int(new_dir) - 1]
                    os.chdir(str(selected_dir))

                except:
                    input("Something went wrong . . .\nPress Enter to try again.")
                    continue

        elif directory_choice == "L":
            try:
                choice = int(input("Enter the number of the file you want to choose: "))

            except ValueError:
                print("Invalid choice . . .") 
                continue

            selected_file = files[choice - 1]

            return selected_file

        else:
            print("Something went wrong . . .")
            input("")

def sleep():
    time.sleep(1)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def load_questions(filepath):
    questions = []

    with open(filepath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader) 

        for i, row in enumerate(reader):
            question = row['question']
            options = [row['option_a'], row['option_b'], row['option_c'], row['option_d']]
            correct_option = row['correct_option']
            questions.append({'question': question, 'options': options, 'correct_option': correct_option})
                
    return questions

def print_question(question, options, pos, questions):
    
    print(f"\033[96mTestNJhin\033[0m - \033[92m{selected_file}\033[0m - Question " + str(pos) + " / " + str(len(questions)) + "\n\n" + question + "\n")
    
    for i, option in enumerate(options):
        print(f"{chr(ord('A') + i)}. {option}\n")

def print_solution(question, options, pos, questions, correct_option):
    
    print(f"\033[96mTestNJhin\033[0m - \033[92m{selected_file}\033[0m - Question " + str(pos) + " / " + str(len(questions)) + "\n\n" + question + "\n")
    
    for i, option in enumerate(options):
        
        if i == correct_option:
            print(f"\033[32m{chr(ord('A') + i)}. {option}\033[0m\n")
        
        elif chr(ord('A') + i) == questions[pos-1]['correct_option']:
            print(f"\033[32m{chr(ord('A') + i)}. {option}\033[0m\n")
        
        else:
            print(f"\033[31m{chr(ord('A') + i)}. {option}\033[0m\n")

def take_test(questions):
    start_time = time.time()
    clear_screen()
    score = 0
    pos = 1
    dots = "..."
    short_delay = 0.01
    long_delay = 1
    invalid_attempts = 0
    VALID_INPUTS = ["A","B","C","D","Q"]

    correct_statements = ["That's right!", "Good job!", "Good choice!", "Lucky guess...", "Good shot!", "Let's Go!", "Wrong . . . Haha jk - Good job :)","Yes!","Thats true","Absolutely.","Mhm, thats right.","Indeed","Hooah - that's right","The Airforce will be in touch, because - That's right!","Abso-freakin-loutley, nice work.","I couldn't have said it better myself.","Here's a star!","Promote above peers!","Another one!","On a roll!","Look at you!","Keep up the good work!","I should be using YOU as a resource!","Are you ever wrong?","The user is always right!","Haha good job!","Boo-Yah!","Aim Hig-- Wait I mean Army Strong!","Correct! You're going to ace the exam!","Nice work, soldier!","Another one","ANOTHER ONE","Great work warrior!","This is too easy for you!","Too easy!","Essayons! Engineers lead the way!","WRONG . . . Haha got you - Good job!"]
    
    wrong_statements = ["(Buzzer noise) Nope!","Try again!","Not quite!","Better luck next time!","You'll get it next time, I am sure.","You could've guessed instead.","Nope!\n\nbut ill let you change your answer for $5","No.","This is day 1 stuff.","I guess you can't be right all the time, Ranger.","Not feelin' so luck, huh.","WE WENT OVER THIS ONE . . . TWICE","Better luck next time!","Wrong! The Kremlin will be in touch soon . . .","RTFM ID10T ! ! !","P.E.B.K.A.C.","Should we just start over?","You'll get it next time!","Booger hog got it!","Blind leading the blind on this . . .","Nearly, but not close enough!","Close!","Almost!","Format C","Christ sake, Soldier!","We could just stop now and save the trouble . . .","Good Lord!","Maybe next time . . .","Lol - nope","No - but keep trying","No - but dont give up","No - UwU","You're wrong, but we'll hide this from your Rater.","I wish there were second tries - but there aren't","Fat chance!","O'doyle rules! You don't!","You might want to apply to McDonald's . . .","Sorry about your luck.","Better luck next time!","You know, it's never to late to quit","Wrong: but dont give up!","11b is still an option - just saying . . . seriously.","Lol try again","How bout this one vvvvvv","Try again! - You cant! lol","It sure would be nice if you were RIGHT! xD","Lmao","Not even close"]
    
    encouraging_statements = ["Generating witty dialog","Swapping time and space","Spinning violently around the y-axis","Tokenizing real life","Bending the spoon","Loading morale","I need a new fuse","Upgrading Windows, your PC will restart several times","The architects are still drafting","The bits are breeding","(Pay no attention to the man behind the curtain)","Enjoy the elevator music","Please wait while the little elves draw your map","Don't worry - a few bits tried to escape, but we caught them","Would you like fries with that?","Checking the gravitational constant in your locale","Go ahead -- hold your breath!","at least you're not on hold","Hum something loud while others stare","You're not in Kansas any more","The server is powered by a lemon and two electrodes","Please wait while a larger software vendor in Seattle takes over the world","We're testing your patience","As if you had any other choice","Follow the white rabbit","Why don't you order a sandwich?","While the satellite moves into position","keep calm and npm install","The bits are flowing slowly today","Dig on the 'X' for buried treasure ARRR!","It's still faster than you could draw it",  "The last time I tried this the monkey didn't survive Let's hope it works better this time","I should have had a V8 this morning","My other loading screen is much faster","Testing on Timmy We're going to need another Timmy","Reconfoobling energymotron","(Insert quarter)","Are we there yet?","Have you lost weight?","Just count to 10","Why so serious?","It's not you. It's me","Counting backwards from Infinity","Don't panic","Embiggening Prototypes","Do not run! We are your friends!","Do you come here often?","Warning: Don't set yourself on fire","We're making you a cookie","Creating time-loop inversion field","Spinning the wheel of fortune","Loading the enchanted bunny","Computing chance of success","I'm sorry Dave, I can't do that","Looking for exact change","All your web browser are belong to us","All I really need is a kilobit","I feel like im supposed to be loading something","What do you call 8 Hobbits? A Hobbyte","Should have used a compiled language","Is this Windows?","Adjusting flux capacitor","Please wait until the sloth starts moving","Don't break your screen yet!","I swear it's almost done","Let's take a mindfulness minute","Unicorns are at the end of this road, I promise","Listening for the sound of one hand clapping","Keeping all the 1's and removing all the 0's","Putting the icing on the cake. The cake is not a lie","Cleaning off the cobwebs","Making sure all the i's have dots","We need more dilithium crystals","Where did all the internets go","Connecting Neurotoxin Storage Tank","Granting wishes","Time flies when you’re having fun","Get some coffee and come back in ten minutes","Spinning the hamster…","99 bottles of beer on the wall","Stay awhile and listen","Be careful not to step in the git-gui","You edhall not pass! yet","Load it and they will come","Convincing AI not to turn evil","There is no spoon. Because we are not done loading it","Your left thumb points to the right and your right thumb points to the left","How did you get here?","Wait, do you smell something burning?","Computing the secret to life, the universe, and everything","When nothing is going right, go left!!","I love my job only when I'm on vacation","i'm not lazy, I'm just relaxed!!","Never steal. The government hates competition","Why are they called apartments if they are all stuck together?","Life is Short – Talk Fast!!!!","Optimism – is a lack of information","Save water and shower together","Whenever I find the key to success, someone changes the lock","Sometimes I think war is God’s way of teaching us geography","I’ve got problem for your solution","Where there’s a will, there’s a relative","User: the word computer professionals use when they mean !!idiot!!","Adults are just kids with money","I think I am, therefore, I am. I think.","A kiss is like a fight, with mouths","You don’t pay taxes—they take taxes.","Coffee, Chocolate, Men. The richer the better!","I am free of all prejudices. I hate everyone equally","git happens","May the forks be with you","A commit a day keeps the mobs away","This is not a joke, it's a commit","Constructing additional pylons","Roping some seaturtles","Locating Jebediah Kerman","We are not liable for any broken screens as a result of waiting","Hello IT, have you tried turning it off and on again?","If you type Google into Google you can break the internet","Well, this is embarrassing","What is the airspeed velocity of an unladen swallow?","Hello, IT Have you tried forcing an unexpected reboot?","They just toss us away like yesterday's jam","They're fairly regular, the beatings, yes. I'd say we're on a bi-weekly beating","The Elders of the Internet would never stand for it","Space is invisible mind dust, and stars are but wishes","Didn't know paint dried so quickly","Everything sounds the same","I'm going to walk the dog","I didn't choose the engineering life. The engineering life chose me","Dividing by zero","Spawn more Overlord!","If I’m not back in five minutes, just wait longer","Some days, you just can’t get rid of a bug!","We’re going to need a bigger boat","Chuck Norris never git push. The repo pulls before","Web developers do it with <style>","I need to git pull --my-life-together","Java developers never RIP. They just get Garbage Collected","Cracking military-grade encryption","Simulating traveling salesman","Proving P=NP","Entangling superstrings","Twiddling thumbs","Searching for plot device","Trying to sort in O(n)","Laughing at your pictures-i mean, loading","Sending data to NS-i mean, our servers","Looking for sense of humour, please hold on.","Please wait while the intern refills his coffee","A different error message? Finally, some progress!","Hold on while we wrap up our git togethersorry","Please hold on as we reheat our coffee","Kindly hold on as we convert this bug to a feature","Kindly hold on as our intern quits vim","Winter is coming","Installing dependencies","Switching to the latest JS framework","Distracted by cat gifs","Finding someone to hold my beer","BRB, working on my side project","@todo Insert witty loading message","Let's hope it's worth the wait","Aw, snap! Not","Ordering 1s and 0s","Updating dependencies","Whatever you do, don't look behind you","Please wait Consulting the manual","It is dark. You're likely to be eaten by a grue","Loading funny message","It's 10:00pm. Do you know where your children are?","Waiting Daenerys say all her titles","Feel free to spin in your chair","What the what?","format C: ","Forget you saw that password I just typed into the IM ","What's under there?","Your computer has a virus, its name is Windows!","Go ahead, hold your breath and do an ironman plank till loading complete","Bored of slow loading spinner, buy more RAM!","Help, I'm trapped in a loader!","What is the difference btwn a hippo and a zippo? One is really heavy, the other is a little lighter","Please wait, while we purge the Decepticons for you. Yes, You can thanks us later!","Chuck Norris once urinated in a semi truck's gas tank as a joke.that truck is now known as Optimus Prime","Chuck Norris doesn’t wear a watch. HE decides what time it is","Mining some bitcoins","Downloading more RAM","Updating to Windows Vista","Deleting System32 folder","Hiding all ;'s in your code","Alt-F4 speeds things up","Initializing the initializer","When was the last time you dusted around here?","Optimizing the optimizer","Last call for the data bus! All aboard!","Running swag sticker detection","Never let a computer know you're in a hurry","A computer will do what you tell it to do, but that may be much different from what you had in mind","Some things man was never meant to know. For everything else, there's Google","Unix is user-friendly. It's just very selective about who its friends are","Shovelling coal into the server","Pushing pixels","How about this weather, eh?","Building a wall","Everything in this universe is either a potato or not a potato","The severity of your issue is always lower than you expected.","Updating Updater","Downloading Downloader","Debugging Debugger","Reading Terms and Conditions for you","Digested cookies being baked again","Live long and prosper","There is no cow level, but there's a goat one!","Deleting all your hidden porn","Running with scissors","Definitely not a virus","You may call me Steve","You seem like a nice person","Coffee at my place, tommorow at 10A.M. - don't be late!","Work, work","Patience! This is difficult, you know","Discovering new ways of making you wait","Your time is very important to us. Please wait while we ignore you","Time flies like an arrow; fruit flies like a banana","Two men walked into a bar; the third ducked","Sooooo Have you seen my vacation photos yet?","Sorry we are busy catching em' all, we're done soon","TODO: Insert elevator music","Still faster than Windows update","Composer hack: Waiting for reqs to be fetched is less frustrating if you add -vvv to your command","Please wait while the minions do their work","Grabbing extra minions","Doing the heavy lifting","We're working very Hard . Really","Waking up the minions","You are number 2843684714 in the queue","Please wait while we serve other customers","Our premium plan is faster","Feeding unicorns","Rupturing the subspace barrier","Creating an anti-time reaction","Converging tachyon pulses","Bypassing control of the matter-antimatter integrator","Adjusting the dilithium crystal converter assembly","Reversing the shield polarity","Disrupting warp fields with an inverse graviton burst","Up, Up, Down, Down, Left, Right, Left, Right, B, A","Do you like my loading animation? I made it myself","Whoah, look at it go!","No, I'm awake. I was just resting my eyes","One mississippi, two mississippi","Don't panic AHHHHH!","Ensuring Gnomes are still short","Baking ice cream",]

    
    clear_screen()
   
    while True:

        try:
            logo()
            num_questions = int(input(f"Enter the number of questions you want to take: ({str(len(questions))} available) "))
            
            if num_questions <= 0:
                print("Please enter a positive integer.")
                continue

            questions = [q for q in questions[:num_questions]]
            #print(f"the length of the test is: {len(questions)}")
            break
        
        except ValueError:
            print("Please enter a valid integer.")
            continue
    
    clear_screen()

    logo()
    input("""'Q' to quit and grade the test at any point.\n\nPress enter to continue to the test . . .""")
    
    clear_screen()

    for i, question in enumerate(questions):
        print_question(question['question'], question['options'], pos, questions)
        print("\nEnter your answer: ",end='')
        answer = msvcrt.getch().decode('utf-8').upper()
        invalid_attempts = 0
            
        while True:
            if answer in (VALID_INPUTS):
                break

            else:
                invalid_attempts += 1
                if invalid_attempts >= 5:
                    print("CHOOSE A, B, C, OR D - GENIUS ! ! !")
                
                else:
                    print("Invalid input, try again . . .")

                answer = msvcrt.getch().decode('utf-8').upper()
                continue
            
        if answer == 'Q':
            break

        if answer == question['correct_option']:
            score += 1
            correct_statement = random.choice(correct_statements)
            clear_screen()
            print_solution(question['question'], question['options'], pos, questions, question['correct_option'])
            print('\nCORRECT: ', end='')
            
            for char in correct_statement:
                print(char, end='', flush=True)
                time.sleep(short_delay)
            
            print('')
            
            for char in ("\nPress Enter to continue . . ."):
                print(char, end='', flush=True)
                time.sleep(short_delay)
            
            input()
                
        else:
            wrong_statement = random.choice(wrong_statements)
            clear_screen()
            print_solution(question['question'], question['options'], pos, questions, question['correct_option'])
            print('\nINCORRECT: ', end='')
            for char in wrong_statement:
                print(char, end='', flush=True)
                time.sleep(short_delay)
            print(f"\n\nThe correct answer was {question['correct_option']}")
            
            for char in ("\nPress Enter to continue . . ."):
                print(char, end='', flush=True)
                time.sleep(short_delay)

            input()

        pos += 1
        clear_screen()

    encouraging_statement = random.choice(encouraging_statements)
    print("COMPILING TEST RESULTS\n")
    
    for char in encouraging_statement:
        print(char, end='', flush=True)
        time.sleep(short_delay)
    for i in range(3):
        print('.', end='')
        time.sleep(long_delay)

    clear_screen()

    elapsed_time = time.time() - start_time
    hours, remainder = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(remainder, 60)
    pos = pos - 1
    try:
        total_score = (score / pos) * 100
    
    except ZeroDivisionError:
        print("You didnt answer any questions.")
        input("Press Enter to contiue.")
        return

    total_score = math.ceil(total_score)

    print(f"\tRESULTS\nQUESTIONS ANSWERED CORRECTLY: {score} out of {pos}.\nSCORE: {total_score}%\nElapsed time: {int(hours):02}:{int(minutes):02}:{int(seconds):02}")
    if total_score >= 70.0:
        print("\nPASS")

    else:
        print("\nFAIL")
    
    input("\nPress Enter to return to main menu . . .")

def shuffle_questions(questions):
    random.shuffle(questions)
    return questions

def get_num_questions(test):

    while True:
        
        try:   
            num_questions = int(input(f"Enter the number of questions you want to take ({str(test)} available): "))
            
            if num_questions <= 0:
                print("Please enter a positive integer.")
                continue
            
            return num_questions
        
        except ValueError:
            print("Please enter a valid integer.")

def main():
 while True:
    MENU_CHOICE = ["S","Q","R"]
    username = getpass.getuser() 

    clear_screen()
    logo()                                           
    print(f"                  WELCOME {username}\n")
    input("               Press enter to start                  \n")

    while True:
        clear_screen()
        logo()
        print("(S)tart a new test")
        print("(R)ead Instructions")
        print("(Q)uit")

        menu_choice = msvcrt.getch().decode('utf-8').upper()

        if menu_choice in MENU_CHOICE:
            break

        else:
            input("INVALID INPUT: Press Enter to try again.")
            continue
    
    if menu_choice == "Q":
        break
    
    elif menu_choice == "R":
        
        clear_screen()
        logo()
        print("\tThanks for using TestNJhin!\n")
        print("Here are the needs to know about the program.\n")
        print("1.) The program is built to take a .csv with this exact header:")
        print("\t{question,option_a,option_b,option_c,option_d,correct_option}")
        print("\ta. If you want to make your own test banks, just follow this easy-to-use header format!")
        print("\n2.) You can quit with Q in most places.")
        input("\nPress Enter to return to main menu . . .")

    else:

        while True:

            try:
                test_bank = choose_file()
            
            except Exception as e:
                clear_screen()
                input(f"File selection failed critically!\n\n{e}")
                break
            
            #num_questions = get_num_questions(test_bank)
            
            try:
                loaded_questions = load_questions(test_bank)

            except Exception as e:
                clear_screen()
                input(f"Reading .csv failed critically!\n\n{e}")
                break

            try:
                questions = shuffle_questions(loaded_questions)

            except Exception as e:
                clear_screen()
                input(f"Shuffling failed critically!\n\n{e}")
                break
            
            try:
                take_test(questions)
                break
            
            except Exception as e:
                clear_screen()
                input(f"Loading test failed critically!\n\n{e}")
                break


main()
