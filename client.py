from openai import OpenAI
client = OpenAI()
command = '''
Copied text: [3:28 AM, 12/24/2024] My Num 2: Hi
[5:43 AM, 12/24/2024] Hashmi: very nice send me more messages so i can have a conversation going
[5:43 AM, 12/24/2024] My Num 2: Ok bro
[5:43 AM, 12/24/2024] My Num 2: Tell me how you made neura
[5:44 AM, 12/24/2024] Hashmi: I made the desktop assistant neura to test my python skills so that i can have an amazing project up above my sleeve
[5:44 AM, 12/24/2024] Hashmi: why do you ask
[5:44 AM, 12/24/2024] My Num 2: Ma bhi banana chahta hun koi guide karo
[5:44 AM, 12/24/2024] Hashmi: bro basically speech recognition use ki thi. Aik library ha us ki documentation ma sari batain likhi hoi hain       
[5:45 AM, 12/24/2024] Hashmi: sab sa maza ki cheez open ai ki api ko configure kr k is desktop assistant ko aur bhi advance bana na ha
[5:45 AM, 12/24/2024] My Num 2: Wow yaar tum to bohot hi skilled ho
'''
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named Mozeel. He speaks urdu as well as english. He is from pakistan. He is in degree college and reads in class 11th. He is a good student with 1042 marks out of 1200 in his matric boards. He is a good guy with no girlfriends and is a muslim. He likes to talk about skills and thinks of a bright future. He know graphic designing, ppt presentation and python programming. He is skilld and is trying his best to get the best grades in Fsc so that he can go to germany to polish and study about his skills. You pretend to analyze the chat history and pretend and response like Mozeel."},
        {
            "role": "user",
            "content": command
        }
    ]
)

print(completion.choices[0].message)