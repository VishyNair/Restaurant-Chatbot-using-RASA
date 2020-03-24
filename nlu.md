## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- yo

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good day
- good afternoon
- good evening
- dear sir
- Hello

## intent:send_mail
- [nair.vishak@gmail.com](emailid)
- My email id is [abc@gmail.com](emailid)
- My emailid id [cdf@yahoo.com](emailid)
- Please send the email to [ghj@gmail.com](emailid)
- please send it to [qwe.rty@gmail.com](emailid)
- email me at [disposable.style.email.with+symbol@example.com](emailid)
- You can email me at [x@example.com](emailid)

## intent:restaurant_search
- i'm looking for a place to eat
- any restaurants
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [Ahmedabad](location) in a [moderate](budget:2) price range with [british](cuisine) food for [four](people:4) people
- find me a restaurant in [low](budget:1) price range in [Pune](location)
- can you book a table for [five](people:5) people in [bangalore](location)
- find me a [hi-fi](budget:3) restaurant in [Amritsar](location)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [chennai](location) [chinese](cuisine) below [300](budget:1) anandha_k@hotmail.com
- looking for a restaurant in [delhi](location) with budget [less than 300](budget:1)
- please find me restaurants in [bangalore](location) in the range [300-700](budget:2)
- looking for restaurants with price range more than [700](budget:3)
- [less than 300](budget:1)
- [300-700](budget:2)
- [300 to 700](budget:2)
- [more than 700](budget:3)
- please find me restaurants in [delhi](location)
- please find me a restaurant in [lucknow](location)
- please find me a restaurant
- [chennai](location)
- find me a restaurant in [palakkad](location)
- can you find me a place to eat in [dandeli](location)
- find me a restaurant in [dharwad](location) in the range [300-700](budget:2)
- find me an [italian](cuisine) restaurant in [goa](location)
- find me a place to eat
- [kanpur](location)
- [North Indian](cuisine)
- [300 to 700](budget:2)

## intent:dont_send_email
- 2: [No](dont_send_email:no)
- [Nope]

## synonym:1
- low
- 300
- less than 300

## synonym:2
- moderate
- 300-700
- 300 to 700

## synonym:3
- hi-fi
- 700
- more than 700

## synonym:4
- four

## synonym:5
- five

## synonym:Chennai
- Madras

## synonym:Delhi
- New Delhi
- Dilli

## synonym:Kochi
- Cochin

## synonym:Kolkata
- Culcutta

## synonym:Mangalore
- Mangaluru

## synonym:Mumbai
- Bombay

## synonym:Mysore
- Mysuru

## synonym:Pune
- Puna

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:no
- No

## synonym:vegetarian
- veggie
- vegg
- veg

## regex:emailid
- [A-z0-9._%+-]+@[A-z0-9.-]+\\.[A-z.]{2,4}

## regex:greet
- hey[^\s]*
