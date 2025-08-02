from groq import Groq
import speech_recognition as sr
import random

#STT
g=Groq(api_key="your_API_key")

#func to listen and convert voice commands to text
def listen():
    rec=sr.Recognizer()
    mic=sr.Microphone()

    with mic as x:
        print("Say your move...")

        #Reduuce background noise
        rec.adjust_for_ambient_noise(x)

        #listen for speech
        audio=rec.listen(x)
    try:
        #Send audio to groq
        data=audio.get_wav_data()
        response=g.audio.transcriptions.create(model="whisper-large-v3" ,
                                                         file=("speech.wav",data))
        text=response.text.strip()
        print(f"You said : {text}")
        return text 
    except Exception as e:
        print("Couldn't process speech : " ,e)
        return None


#Racer Class >> handles attacks ,defenses and stats
class Racer:
    def __init__(self,name,offensive,defensive):
        self.name=name
        self.tireHealth=100
        self.fuel=500
        self.offensive=offensive
        self.defensive=defensive
        self.defense_uses={move: info['uses']for move ,info in defensive.items()}

    #Attack
    def attack(self,move_name,opponent):
        move=self.offensive[move_name]
        if self.fuel>=move['fuel']:
            self.fuel-=move['fuel']
            opponent.take_damage(move['tire_damage'])
            print(f"{self.name} used {move_name} (-{move['fuel']} fuel)")
        else:
            print(f"{self.name} wanted {move_name} but ran out of fuel..")


    #Defend from an incoming attack
    def defend(self,move_name,incoming_damage):
        move=self.defensive[move_name]
        if self.fuel >=move['fuel'] and (self.defense_uses[move_name] > 0 or move['uses']==float('inf')):
            self.fuel-=move['fuel']
            if move['uses'] != float('inf'):
                self.defense_uses[move_name] -=1
            red_damage=incoming_damage * (1-move['reduction'])
            print(f"{self.name} used {move_name}. damage reduced to {red_damage:.1f}")
            return red_damage

        else:
            print(f"{self.name} could not defend..") 
            return incoming_damage

    #Apply damage to tries
    def take_damage(self,amount):
        self.tireHealth-=amount
        if self.tireHealth<0:
            self.tireHealth=0

    #Show current tire health and fuel
    def status(self):
        print(f"{self.name} >> tire : {self.tireHealth} / fuel : {self.fuel}")

    #Check if racer is out of the race
    def out(self):
        return self.tireHealth<=0


#Moves for VERSTAPPEN & MOSTAFA
verstappen_offense = {
    "DRS Boost": {"fuel": 45, "tire_damage": 12},
    "Red Bull Surge": {"fuel": 80, "tire_damage": 20},
    "Precision Turn": {"fuel": 30, "tire_damage": 8}
}
verstappen_defense = {
    "Brake Late": {"fuel": 25, "reduction": 0.3, "uses": float('inf')},
    "ERS Deployment": {"fuel": 40, "reduction": 0.5, "uses": 3}
}

mostafa_offense = {
    "Turbo Start": {"fuel": 50, "tire_damage": 10},
    "Mercedes Charge": {"fuel": 90, "tire_damage": 22},
    "Corner Mastery": {"fuel": 25, "tire_damage": 7}
}
mostafa_defense = {
    "Slipstream Cut": {"fuel": 20, "reduction": 0.4, "uses": float('inf')},
    "Aggressive Block": {"fuel": 35, "reduction": 1.0, "uses": 2}
}

#Create racers
verstappen=Racer("MAX VERSTAPPEN" ,verstappen_offense ,verstappen_defense)
mostafa=Racer("HASSAN MOSTAFA" ,mostafa_offense,mostafa_defense)


#Start the race
print("The Final Race - Verstappen vs Mostafa")

turn=0
while not verstappen.out() and not mostafa.out():
    #Determine attacker and defender
    attacker=verstappen if turn %2==0 else mostafa
    defender=mostafa if turn %2==0 else verstappen

    #if it's mostafa turn , listen for voice command
    if attacker==mostafa:
        y=listen()
        if y is None:
            print("Did not catch that. Skipping your turn. ")
        else:
            #format text
            y=y.title()    

            if y in mostafa_offense:
                mostafa.attack(y,verstappen)
            elif y in mostafa_defense:
                print("You can only use defendse if someone attacks you ")
            else:
                print("Unknown command!! Try again next turn")

    else:
        #VERSTAPPEN Plays Randomly
        move_name=random.choice(list(verstappen_offense.keys()))
        damage=move_name
        verstappen.attack(move_name ,mostafa)

    #Show updated status for both racers
    verstappen.status()
    mostafa.status()
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    turn+=1                        

#Winner Announcment
w=verstappen if not verstappen.out() else mostafa
print(f"AAAND THE WINNER IS : {w.name} ")