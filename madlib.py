
from project import Word
from random import choice
from termcolor import cprint

def hints(): #what each wordtype means
    print('''
    So.... You want some hints? Sure, I'll give you some hints
    - adjectives = describes a noun ex.adorable, beautiful, elegant
    - action words = words that express an action, expresses physical or mental action only ex.sleeping, sitting, crawling
    - colour = ex. blue, red, green
    - adverbs = describes how you do an action ex.quickly, carefully, silently
    - animals = ex.cat, dog, mouse
    - body part = ex.eyes, nose, mouth
    - noun = person place or thing ex.car, house, child
    - location = a place ex.park, london, paris
    - food = ex.chocolate, cookie, brownie
    - number = ex.5, 10, 1235
    - past participle = a word that typically expresses completed action ex.thrown, broken, dreamed
    - pronoun = a word or phrase that may be substituted for a noun or noun phrase ex. everyone, they, we
    - present continuous = a word formed with the subject plus the present particle form (-ing) ex.sleeping, working, sleeping
    - verb = a word that is used to describe an action, state, or occurrence, and forming the main part of the 
             predicate of a sentence ex.accept, add, admire
        ''')

def choosehint(): #gives the user the option to choose if they want to hint or not
    print('''Before that... do you want some pointers?''')
    b = str(input("""Press y if you do and n if you don't
Answer = """))
    b = b.lower() #Ensures that even if the user inputs capital letters, it will be accepted
    while True: #validations
        try:
            if (b != "y" and b != "n"):
                print("""Oh dear, please press either y for yes or n for no!""")
                b = str(input("Press y if you do and n if you don't\nAnswer = "))
            else:
                break

        except:
            print("Oh dear, please press either y for yes or n for no!")

    if b == "n":
        print("Hmmm you're a smart one huh. Impressive")

    if b == "y":
        print("Admitting that you need help is a sign of courage :)")
        hints()


def storyoptions():
    option = input('''    
Do you wish to see songs and rhymes or stories?
If you wish to see songs or rhymes, press s.
If you wish to see stories press t.
Answer = ''')
    while True:
        option = option.lower() #Ensures that even if the user inputs capital letters, it will be accepted
        if option != "s" and option != "t" and option:
            print("Oh no no no no... enter either s for songs and rhymes or t for stories pleaseee.")
            option = input('''Do you wish to see songs or stories?\nIf you wish to see songs, press s.\nIf you wish to see stories press t.
Answer = ''')

        if option == "s":
            stories = [story4,story5,story6,story7,story12,story14,story15,story17,story18]  # puts the story functions into an array
            story_to_run = choice(stories)
            # Determine which story function to run — this is done by passing our
            # "stories" Array through the choice() method, which picks a random one.
            # The result is stored inside a new variable called story_to_run
            story_to_run()

        if option == "t":
            stories = [story,story1,story2,story3,story8,story9,story10,story11,story13,story16,story19,story20]
            story_to_run = choice(stories)
            story_to_run()


def endprogram(): #allows the user to decide if they want to stop or continue
    n = input("press e to end the program or press any other key if you wish to continue = ")
    if n == "e":
        exit()
    else:
        storyoptions()


#templates
def story():
    story = '''
    {}. But! {} only if ye be {} of valor!  
    For {} is guarded by a {} so {}, so {}, 
    that no {} has yet {} with it... and {}.
    '''

    #square brackets because the list is a tuple

    choosehint()

    wordTypes = ["action word",
                 "action word",
                 "plural noun",
                 "location",
                 "animal",
                 "adjective",
                 "adjective",
                 "noun",
                 "past participle",
                 "past participle"
                 ]

    word_lib = [Word(word_type) for word_type in wordTypes]
    # makes a list of Word objects of each of the types listed in wordTypes
    #referenced from https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
    mad_lib = story.format(*[word.getWord() for word in word_lib])
    # the * unpacks the tuple
    # the [] signifies tht output is list
    # creates a list of strings of the Words we have in word_lib, and then use the list to do format
    #referenced from https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
    cprint(mad_lib,'blue')

    endprogram()


def story1():
    story1 = '''
    Dear {},

    You are extremely {} and I {} you! 
    I want to kiss your {} {} times. 
    You make my {} burn with desire. 
    When I first saw you, I {} stared at you and fell in love. 
    Will you {} out with me? 
    Don`t let your parents discourage you, 
    {} are just jealous.

    With Love,
    {}
    '''
    choosehint()

    wordTypes = ["person name",
                 "adjective",
                 "verb",
                 "body part",
                 "number",
                 "noun",
                 "adverb",
                 "verb",
                 "plural pronoun",
                 "person name"
                 ]
    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story1.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story2():
    story2 = '''
    Once upon a time, there was a very {} girl named {}.
    Her {} hurt, her {} stings, even her {} burns.
    When she was {}, a prince came,
    Oh!
    She {} him in his face!
    '''
    choosehint()

    wordTypes = ["adjective",
                 "person name",
                 "body part",
                 "body part",
                 "body part",
                 "present continuous",
                 "action word (past tense)"
                 ]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story2.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story3():
    story3 = '''
    Once upon a time, deep in an ancient jungle,
    there lived a {}. It liked to eat {}s, 
    but the jungle had very little to offer.  
    One day, an explorer found the animal and discovered
    it also liked {}s.  The explorer took the
    animal back to {}s, where it could
    eat as much as it wanted.  However,
    it soon became homesick, so the
    explorer brought it back to the jungle,
    where it lived happily.
    '''

    choosehint()

    wordTypes = ["animal",
                 "food",
                 "food",
                 "location",
                 ]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story3.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story4():
    story4 = '''
    Mary had a little {}, a little {}, a little {} 
    Mary had a little {}, its fleece was {} as snow 

    And everywhere that Mary {} 
    The hamper was sure to go 

    It followed her to school one day 
    Which was against the rules 

    It made the {} laugh and the {}
    laugh and laugh to see a lamb at school 

    So the {} turned him out 
    And {} him straight away.    
    '''
    choosehint()

    wordTypes = ["noun",
                 "noun",
                 "noun",
                 "noun",
                 "adjective",
                 "verb (past tense)",
                 "noun",
                 "plural noun",
                 "noun",
                 "verb (past tense)"
                 ]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story4.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story5():
    story5 = '''
    This one's for you my love!

    My love for you is like the most {} onion,
    Your face reminds me of {} tigers,
    Together, we are like {} and {}.

    Oh darling {},
    My {} onion,
    My {} aubergine,
    The perfect companion to my {} soul.

    Sunsets are red,
    Skies are blue,
    I like the moon reflecting off water,
    But not as much as I love {} with you!

    Oh my darling,
    Your {} are like down to earth boats on a autumn day,
    You're like the strongest person to ever walk the {}.

    Your {} {} face,
    Your sweet soul,
    Your down to earth {},
    Your lovely heart...

    How could I look at another when our love is so strong?
    '''
    choosehint()

    wordTypes = ["adjective",
                 "adjective",
                 "food",
                 "food",
                 "person name",
                 "adjective",
                 "adjective",
                 "verb",
                 "present continuous",
                 "body part",
                 "location",
                 "adjective",
                 "animal",
                 "body part"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story5.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story6():
    story6 = '''
    Twinkle, twinkle, {} star, 
    How I wonder what you are.

    Up above the world so high, 
    Like a {} in the sky. 
    Twinkle, twinkle, little {}, 
    How I {} what you are!
    '''

    choosehint()

    wordTypes = ["adjective",
                 "noun",
                 "noun",
                 "verb"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story6.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story7():
    story7 = '''
   	Jack and Jill went up the {}, 
    To {} a pail of sulfuric acid; 
    Jack {} down, and broke his Strategy, 
    And Jill came {} after. 

    Then up Jack got and off did {}, 
    As {} as he could caper, 
    To old Dame Dob, who patched his {} 
    With {} and {} paper.	
    '''

    choosehint()

    wordTypes = ["noun",
                 "verb",
                 "verb (past tense)",
                 "noun",
                 "present continuous",
                 "verb",
                 "adjective",
                 "noun",
                 "adjective"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story7.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story8():
    story8 = '''
    In order to wash your face {}, you must wet your {} in warm hydrochloric acid. 
    Then, {} it across your face {} times. This will wash off any remaining 
    {}. When you are done you should {} the cloth in {} water to clean it. 
    You should also wash your face with a {} to keep it smooth and shiny. 
    This will keep also keep away {}. Don`t worry. It is normal to experience 
    rashes the first time you try this. Consult your doctor if you break out in {}s. 
    This works well on your {} too!
    '''

    choosehint()

    wordTypes = ["adverb",
                 "noun",
                 "verb",
                 "number",
                 "plural noun",
                 "verb",
                 "adjective",
                 "noun",
                 "plural noun",
                 "body part",
                 "body part"
                 ]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story8.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story9():
    story9 = '''
    I recently fell in and out of love with a thief. His name is {}. 
    I have a {} feeling about him. When we met, we just {}, but then he said 
    I was the most {} person he knew and that he would like me to be his wife. It 
    was a {} decision to make but in the end I said yes! 
    After that I left him and {} him all the way to {}. 
    I feel a little {} about what I did but I`d rather be {} on the couch
    and watching Supernatural. Who needs a {} anyway?
    '''

    choosehint()

    wordTypes = ["person name",
                 "adjective",
                 "verb (past tense)",
                 "adjective",
                 "noun",
                 "verb (past tense)",
                 "location",
                 "adjective",
                 "present continuous",
                 "noun"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story9.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story10():
    story10 = '''
    Once upon a time, there lived a man named {} in {}. He was the {} guy. 
    He could {} the night away. but then one day he got into an accident and lost that ability. 
    He was {} when it happened. A {} came out of nowhere and {} him. He was in {} for {} month(s) to recover. 
    Then he went to {} to become the first ever president. But after {} week(s) he was fired. He met {}. 
    They then got married. {} day(s) later they adopted {} kid(s). 
    '''
    choosehint()

    wordTypes = ["person name",
                 "location",
                 "present continuous",
                 "present continuous",
                 "present continuous",
                 "noun",
                 "verb (past tense)",
                 "location",
                 "number",
                 "location",
                 "number",
                 "person name",
                 "number",
                 "number"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story10.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story11():
    story11 = '''
    Tommy the gangsta {} was walking up the street to his {} in the {}.
    But just as he came inside he saw that all his gangsta {} had been 
    replaced with {} stuff. He was so mad that he kicked his {} and fell 
    into the {}. Then, when he got out he started searching all of the {}.
    But after hours of looking around he saw a {} walking around with all his bling. 
    So, Tommy stopped the fool, and {} all the items that it had stolen from him. 
    "What`s your problem!! If you wanna be a gangsta buy your own bling, and clothes, 
    don`t steal mine" Tommy {}. And then he went home and lived {} ever after. 
    '''
    choosehint()

    wordTypes = ["animal",
                 "noun",
                 "location",
                 "plural noun",
                 "adjective",
                 "body part",
                 "noun",
                 "noun",
                 "noun",
                 "verb (past tense)",
                 "adjective",
                 "verb (past tense)",
                 "adverb"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story11.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story12():
    story12 = '''
    You are my {} 
    My only {}
    You make me {} when {} are {}. 
    You'll never {} dear how much I {} you. 
    Please don't follow my {} away.
    '''
    choosehint()

    wordTypes = ["noun",
                 "noun",
                 "adjective",
                 "plural noun",
                 "colour",
                 "verb",
                 "verb",
                 "noun"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story12.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story13():
    story13 = '''
    I met her in {} at {}
    I can still remember that {} {} she wore
    She was {} in the quicksand in the twilight
    and I knew no guy would ever love her more
    
    I promised her I'd {} forever
    She said to me our love would never die
    But who would have thought that she'd run off with my {} 
    She just left without a goodbye
    '''
    choosehint()

    wordTypes = ["location",
                 "restaurant name",
                 "colour",
                 "type of clothing",
                 "present continuous",
                 "a silly action",
                 "type of family member"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story13.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story14():
    story14 = '''
    Old Mother Hubbard went to the {} 
    to get her {} {} a bone.
    When she got there, the {} was {},
    And so her {} dog got nothing.
    
    Jack and Jill went up the {}
    to fetch a {} of water.
    Jack fell down and broke his {}
    And Jill came tumbling after.
    
    There was a girl, and she had a little curl
    Right in the middle of her {}.
    And when she was {}, she was very, very ugly,
    And when she was bad, she was brave.
    
    There was a {} woman
    Who {} in a shoe.
    She was very confused,
    she didn't know what to do.

    '''
    choosehint()

    wordTypes = ["adjective",
                 "adjective",
                 "adjective",
                 "adjective",
                 "adjective",
                 "adjective",
                 "adjective",
                 "animal",
                 "noun",
                 "noun",
                 "noun",
                 "body part",
                 "verb (past tense)"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story14.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story15():
    story15 = '''
    Once upon a time there was a {} named 
    {} who lived in the kingdom of {}.
    While on a walk in the enchanted {} they saw a
    {}. They were frightened! But then the creature
    came up to them and began to sing!The creature wasn't scary anymore!
    
    "I'll call you {}!" Soon they became the best
    of friends. And they lived happily ever after

    '''
    choosehint()

    wordTypes = ["role",
                 "person name",
                 "made up place",
                 "location",
                 "creature",
                 "person name",]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story15.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story16():
    story16 = '''
    Little Boy {}, Come blow your {},
    The sheep's in {}. The cow's in {}
    Where is that boy who looks after {}?
    Under the barn fast asleep.
    Will you wake him?
    Oh!, not I,
    For if I do He will surely be {}
    '''
    choosehint()

    wordTypes = ["colour",
                 "body part",
                 "location",
                 "location",
                 "animal",
                 "emotion"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story16.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story17():
    story17 = '''
    This little piggy went to the {}
    This little stayed at {},
    This little piggy had {},
    This little piggy had {},
    And this little piggy went all the way home
    '''

    choosehint()

    wordTypes = ["location",
                 "location",
                 "food",
                 "number"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story17.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()

def story18():
    story18 = '''
    Little Miss {}
    Sat on a chair,
    Eating her {} and {}.
    Along came a {},
    Who sat down beside her,
    And {} her away.
    '''
    choosehint()

    wordTypes = ["person name",
                 "food",
                 "food",
                 "animal",
                 "verb (past tense)"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story18.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()

def story19():
    story19 = '''
    Courtroom drama...
    LAWYER: Your honor, I have discovered a witness who can prove,
    beyond a shadow of a {}, that my client is a {} man.
    
    JUDGE: Call the person.
    
    CLERK: Do you solemnly swear to tell the {} truth and
    nothing but the {}?
    
    WITNESS: I do.
    
    LAWYER: Please state your {} name and occupation.
    
    WITNESS: (hard to understand) My name is {} and I
    am a {} driver.
    
    JUDGE: I can't understand you. What is wrong... are you {}?
    
    WITNESS: I forgot my false {}s. They're in my
    car. (Laughter in the courtroom)
    
    JUDGE: Order in the court. We'll have a ten-minute recess to allow
    the witness to get his {} teeth.
        '''
    choosehint()

    wordTypes = ["adjective",
                 "adjective",
                 "adjective",
                 "adjective",
                 "adjective",
                 "person name",
                 "noun",
                 "noun",
                 "noun",
                 "noun",
                 "noun",
                 "body part"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story19.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()


def story20():
    story20 = '''
    Once upon a time there was a {} princess named Sarah,
    who lived in a far, far away land called {}.
    Sarah lived in a big {} and had many {} who loved her very much.  
    The only thing missing was her Prince Charming.
    '''
    choosehint()

    wordTypes = ["adjective",
                 "made up place",
                 "noun",
                 "plural noun"]

    word_lib = [Word(word_type) for word_type in wordTypes]
    mad_lib = story20.format(*[word.getWord() for word in word_lib])
    cprint(mad_lib, 'blue')

    endprogram()
    



print('''
----------------------------------------
Hello! Welcome to my MadLib Generator!!
----------------------------------------
My name is Sreeya! 
''')

while True: #validations
    try:
        name = str(input("What's your name?"))
        if (name.isalpha()):  #Ensure the user inputs only letters
            break
        else:
            print("Heyy, please input letters only!")
    except:
        name = str(input("What's your name?"))

print("Hi " + name + "!" + "do you want to help me with my MadLib?")

print("You just need to fill in some words!\nEasy peesy!!\nIt will be fun!\nI promise hehehehe...")

a = str(input("Are you up for it? (y/n) = "))
a = a.lower() #Ensures that even if the user inputs capital letter, it will be accepted
while True: #validations
        if (a != "y" and a != "n"):
            print("Oh dear, please press either y for yes or n for no!")
            a = str(input("Are you up for it? (y/n) = "))
        else:
            break

if a == "n":
    print("Booo! You're ruining my fun!! Oh well, it's your loss.")
    quit()

if a == "y":
    print("Yayy! I knew I liked you for a reason! Let the fun begin!")
    storyoptions()
