from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
# importing the EmailMessage class
from email.message import EmailMessage
# Importing the smtplib libaray to send email
import smtplib
import zomatopy
import json
from concurrent.futures import ThreadPoolExecutor
d_email	 = []

config = { "user_key":"Enter your Zomato API Key here"}

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'mexican':73,'american':1,'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			response = self.RestaurantBasedOnBudget(budget,d['restaurants'])
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]
	def RestaurantBasedOnBudget(self,userbudget,allRestaurants):
		rangeMin = 0
		rangeMax = 100000
		price = int(userbudget)
		if price == 1:
			rangeMax = 299
		elif price == 2:
			rangeMin = 300
			rangeMax = 699
		elif price == 3:
			rangeMin = 700
		elif price < 500:
			rangeMax = 299
		elif price < 700 and price >= 300:
			rangeMin = 300
			rangeMax = 699
		else:
			# default budget 
			rangeMin = 300
			rangeMax = 699
		index = 0
		count = 0
		response = ""
		global result_of_last_query
		result_of_last_query = ""
		for restaurant in allRestaurants:
			++count
			res = "[" + restaurant['restaurant']['user_rating']['aggregate_rating'] + "/5] " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address']

			# price_range = str(restaurant['restaurant']['price_range'])
			avg_c_2 = restaurant['restaurant']['average_cost_for_two']

			# if price_range == "1":
			
			if avg_c_2 <= rangeMax and avg_c_2 >= rangeMin:
				
				# mapbybudget["1"].append(restaurant)
				# if userbudget == price_range:
				
				res = restaurant['restaurant']['currency'] + str(restaurant['restaurant']['average_cost_for_two']) + " " + res + "\n"
				if(index < 5):
					response = response + res

				if(index < 10):
					result_of_last_query = result_of_last_query + res
				index = index + 1
		# modifying the search results
		# if the no. of result fall short, appending the results of other price range
		if index == 0:
			response = "Oops! no restaurant found for this query. " + " search results = " + str(count)
		elif index < 5:
			# we can add restaurants from the higher range but for now i am appending an extra message 
			response = response + "\n \nFor more results please search in higher budget range...\n \n"
		elif index < 10:
			result_of_last_query = result_of_last_query + "\n \nFor more results please search in higher budget range...\n \n"
		global d_email
		d_email = response
		return response

tier1_tier2 = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune","Agra","Ajmer","Aligarh","Amravati","Amritsar",
"Asansol","Aurangabad","Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar","Bikaner","Bilaspur","Bokaro Steel City","Chandigarh",
"Coimbatore","Cuttack","Dehradun","Dhanbad","Durg-Bhilai Nagar","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad","Gorakhpur","Gulbarga",
"Guntur","Gurgaon","Guwahati","Gwalior","Hamirpur","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur",
"Jhansi","Jodhpur","Kannur","Kanpur","Kakinada","Kochi","Kolhapur","Kollam","Kozhikode","Kurnool","Lucknow","Ludhiana","Madurai","Malappuram",
"Mathura","Goa","Mangalore","Meerut","Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Patna","Pondicherry","Purulia","Prayagraj",
"Raipur","Rajkot","Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri","Shimla","Solapur","Srinagar","Surat","Thiruvananthapuram","Thrissur",
"Tiruchirappalli","Tiruppur","Ujjain","Vellore","Vadodara","Varanasi","Bijapur","Vasai-Virar City","Vijayawada","Visakhapatnam","Warangal"]

operating_cities = [x.lower() for x in tier1_tier2]

# To Check if the given location exists. using zomato api.if found then save it, else inform the foodie don't have service currently in the given location.
class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc)
		# dispatcher.utter_message(city)

		if city.lower() in operating_cities:
			return [SlotSet('location_match',"one")]
		else:
			return [SlotSet('location_match',"zero")]

class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
        
    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global d_email
        email_rest_count = len(d_email)
        # Construct the email 'subject' and the contents.
        d_email_subj = "Top " + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n"
        d_email_msg = d_email_msg + d_email

        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("Enter your email_id here", "Enter your email_password")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = d_email_subj
        msg['From'] = "Enter your email ID"

        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("**** THE DETAILS HAVE BEEN SENT! HAPPY A GREAT TIME:) ****")
        return []