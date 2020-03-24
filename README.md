# Restaurant-Chatbot-using-RASA
Building a conversational bot which can help users discover restaurants across several Indian cities. The main purpose of the bot here is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.
Some of the important characterisitcs of the Chatbot ->
- The Chatbot works only in Tier-1 and Tier-2 cities. Hence for any other city it responds with - "We do not operate in that area yet"  <br>
- The bot displays the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest) for any restaurant search by users.  <br>
- Our foodie chatbot can also share the details of the top 10 restaurants over email if needed, with the following details: <br>
Restaurant Name <br>
Restaurant locality address <br>
Average budget for two people <br>
Zomato user rating. <br>
Some of the steps taken care while building this Chatbot -> <br>
- NLU training: Created many training examples for entities and intents. Have tried regex and synonym features for extracting entities.<br>
- Build actions for the Bot: Functions to extract the features such as the average price for two people and restaurant’s user rating by going through Zomato Documentation <br>
Also function for sending emails from Python<br>
- Stories: Building complete path,happy path and also as many interactive stories as possible so that Chatbot can handle any possible user input <br>
- Deployment: The above chatbot was deployed through Slack and with the help of Webhook. The bot is connected to Slack through ngrok as the webhook. <br>

NOTE: Ngrok is a command-line application with which you can connect your chatbot to the Internet. Basically, ngrok connects your local server (on which you have built your chatbot) to a public URL securely so that you can share your bot over the Internet. 
