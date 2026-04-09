import random
import time

def qna(question):

    while True:
        start_time = time.time()
        ans = input(question + " (yes/no): ").lower().strip()
        end_time = time.time()

        if ans in ("yes", "no"):
            break
        print("Please answer yes or no.")

    resp_time = end_time - start_time
    #=========================================================

    #chance of telling truth is 54% before starting
    lie_chance = 0.40                                             
    #========================================================

    # increasing lie chance acc to response time
    if resp_time < 1.5:
        lie_chance += 0.08      #too fast to be true
    elif resp_time < 4:
        lie_chance -= 0.08      #honest range
    elif resp_time < 7:
        lie_chance += 0.07      #too slow
    else:
        lie_chance += 0.12
    #==========================================================

    # if ans == "yes":
    #     lie_chance -= 0.05
    #                                     yes/no bias. cant decide to add it or not
    # elif ans == "no":
    #     lie_chance += 0.05

    #=========================================================

    #random num between -0.05 and 0.05
    lie_chance += random.uniform(-0.05, 0.05)

    #==========================================================
    if lie_chance < 0:
        lie_chance = 0
                                        #keeps it between 0 and 1
    if lie_chance > 1:
        lie_chance = 1

    #=========================================================
    print("\nAnalysing", end="", flush=True )    #fake ahh analysis effect

    for watever in range(4):          
        time.sleep(0.4)
        print(".", end="", flush=True)
                                        #cool animating dot
    print("\r", end="")
    #=========================================================

    lie_perc = int(lie_chance * 100)    #turns lie chance into percantage
    print(f"Hypothesis: Estimated lying probability is {lie_perc}%")

    if lie_perc < 50:
        print("you seem honest")

    elif lie_perc > 50:
        print("you seem sus")
    
    return lie_perc, ans
    #=========================================================
    
questions = [
    "1. Have you lied recently?",                       #0
    "2. Did you ever pretend to laugh at a joke you didn't understand?",
    "3. Are you confident in yourself?",                #2
    "4. Have you ever faked being sick to skip school?",           
    "5. Have you ever (accidentally) stepped on animal poo?",
    """6. Have you ever said "I'm fine" when you were clearly not?""",
    "7. Do you often doubt your decisions?",             #6
    "8. Have you stayed up past 3 am for no reason?",
    "9. Do you consider yourself an honest person?",    #8
    "10. have you forgotten someone's name right after the told you?",
    "11. Do you enjoy 67 jokes?",
    ]

answers = {}
total_lie_per = 0
cont_score = 0
triggered = set()

print("\nDisclaimer: This game, The 'lie detector' is completely made up. Plz don't sue me.")

print("\n---=== Lie Detector Test ===---\n")
    
for q in questions:
    result, ans = qna(q)
    total_lie_per += result
    answers[q] = ans

    #contradiction 1. lied recently vs being honest
    if questions[0] in answers and questions[8] in answers:
        if answers[questions[0]] == "yes" and answers[questions[8]] == "yes":
            if "cont1" not in triggered:
                print("⚠ CONTRADICTION DETECTED. You lied. But you're honest. Okay bro.")
                cont_score += 5
                triggered.add("cont1")

    #contradiction 2. confident vs doubts decisions
    if questions[2] in answers and questions[6] in answers:
        if answers[questions[2]] == "yes" and answers[questions[6]] == "yes":
            if "cont2" not in triggered:
                print("⚠ CONTRADICTION DETECTED. Bro is confident and indecisive at the same time. Nice")
                cont_score += 5
                triggered.add("cont2")

print("========================================================")

average = total_lie_per / len(questions)
average += cont_score

print("\n--==FINAL RESULT==--:")
print(f"Lie probability: {int(average)}%")

if average > 65:
    print("Verdict: You're lying, right?\n")
elif average > 45:
    print("Verdict: You're Suspicious. But not enough to call it\n ")
else:
    print("Verdict: Either you're honest.. or really good at this.\n")