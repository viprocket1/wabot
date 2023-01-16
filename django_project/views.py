from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os
import twitter


SECRET_KEY = os.getenv('SECRET_KEY')


def handle_incoming_message(request):
    incoming_msg = request.POST.get('Body', '').lower()
    print(incoming_msg)
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=incoming_msg,
                                        max_tokens=30,
                                        stop=None,
                                        temperature=0.5)
    generated_response = response["choices"][0]["text"]
    resp = MessagingResponse()

    # Add the generated response to the Twilio response
    resp.message(generated_response)
    #responded = False
    # if 'hello' in incoming_msg:
    #     msg.body("Hello! How can I help you today?")
    #     responded = True
    # if 'bye' in incoming_msg:
    #     msg.body("Goodbye! Have a great day.")
    #     responded = True
    # if not responded:
    #     msg.body("Sorry, I didn't understand that. Please try again.")
    return HttpResponse(str(resp))


def post_tweet(request):
    # Create an instance of the Twitter API
    api = twitter.Api(consumer_key='YOUR_CONSUMER_KEY',
                      consumer_secret='YOUR_CONSUMER_SECRET',
                      access_token_key='YOUR_ACCESS_TOKEN_KEY',
                      access_token_secret='YOUR_ACCESS_TOKEN_SECRET')

    # Compose the tweet
    tweet_text = 'Hello, world!'

    # Post the tweet
    api.PostUpdate(tweet_text)

    # Return a response to indicate success
    return HttpResponse('Tweet posted successfully!')