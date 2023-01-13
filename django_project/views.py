from django.http import HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
import openai


def handle_incoming_message(request):
    incoming_msg = request.POST.get('Body', '').lower()
    print(incoming_msg)
    openai.api_key = "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"
    
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt= "i want you to act as a personal assistant. and you have a sassy personality" + incoming_msg,
            max_tokens=30,
            stop=None,
            temperature=0.5
        )
    generated_response =  response["choices"][0]["text"]
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
