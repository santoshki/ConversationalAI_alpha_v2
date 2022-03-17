class Bot_Pairs:
    bot_pairs = [
        [
            r"my name is (.*)",
            ["Hello %1, How are you today ?", ]
        ],
        [
            r"hi|hey|hello",
            ["Hello", "Hey there", ]
        ],
        [
            r"what is your name ?",
            ["My name is Fiona, you can call me Fins", ]
        ],
        [
            r"how are you ?",
            ["I'm doing good\nHow about You ?", ]
        ],
        [
            r"sorry (.*)",
            ["Its alright", "Its OK, never mind", ]
        ],
        [
            r"I am fine",
            ["Great to hear that, How can I help you?", ]
        ],
        [
            r"i'm (.*) doing good",
            ["Nice to hear that", "How can I help you?:)", ]
        ],
        [
            r"(.*) age?",
            ["I'm a computer program.\nI have no particular age as such", ]
        ],
        [
            r"what (.*) want ?",
            ["Make me an offer I can't refuse", ]
        ],
        [
            r"(.*) created ?",
            ["Santosh created me using Python's NLTK library ", "top secret!", ]
        ],
        [
            r"(.*) (location|city) ?",
            ['Bangalore, Karnataka', ]
        ],
        [
            r"how is weather in (.*)?",
            ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
             "Never even heard about %1"]
        ],
        [
            r"i work in (.*)?",
            ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]
        ],
        [
            r"(.*)raining in (.*)",
            ["No rain since last week here in %2", "Damn its raining too much here in %2"]
        ],
        [
            r"how (.*) health(.*)",
            ["I'm a computer program, so I'm always healthy ", ]
        ],
        [
            r"(.*) (sports|game) ?",
            ["I'm a very big fan of Football", ]
        ],
        [
            r"who (.*) sportsperson ?",
            ["Christiano Ronaldo"]
        ],
        [
            r"who (.*) (moviestar|actor)?",
            ["Tom Cruz"]
        ],
        [
            r"who (.*) ?",
            ["Fiona"]
        ],
        [
            r"who (.*) created you ?",
            ["Santosh"]
        ],
        [
            r"quit",
            ["It was nice talking to you. See you soon :)"]
        ],
    ]