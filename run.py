from chatbot.greetings import greeting
from chatbot.response import response
from chatbot.data_processing import sent_tokens

flag=True
print("C3PO: My name is C3PO, I am a protocol droid.")
print("C3PO: Ask me anything about Star Wars. If you want to exit, type Bye!")
while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("C3PO: You are most welcome, Sir.")
        else:
            if(greeting(user_response)!=None):
                print("C3PO: "+greeting(user_response))
            else:
                print("C3PO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("C3PO: May the Force be with you!")
