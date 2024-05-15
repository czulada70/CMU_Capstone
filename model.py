# define global variables here and give global tag within functions

import json
from collections import OrderedDict

# Question is the raw 'a', 'b' etc. value for the answer
Question1 = "None"
Question2 = "None"
Question3 = "None"
Question4 = "None"
Question5 = "None"
Question6 = "None"
Question7 = "None"
Question8 = "None"
Question9 = "None"
Question10 = "None"
Question11 = "None"
Question12 = "None"
Question13 = "None"
Question14 = "None"
Question15 = "None"
Question16 = "None"
Question17 = "None"
Question18 = "None"
Question19 = "None"
Question20 = "None"
Question21 = "None"
Question22 = "None"
Question23 = "None"
Question24 = "None"
Question25 = "None"
Question26 = "None"
Question27 = "None"
Question28 = "None"
Question29 = "None"
Question30 = "None"
Question31 = "None"
Question32 = "None"
Question33 = "None"
Question34 = "None"
Question35 = "None"
Question36 = "None"
Question37 = "None"
Question38 = "None"
Question39 = "None"
Question40 = "None"
Question41 = "None"
Question42 = "None"

# comment is the additonal comment left with each question
Comment1 = "Enter here"
Comment2 = "Enter here"
Comment3 = "Enter here"
Comment4 = "Enter here"
Comment5 = "Enter here"
Comment6 = "Enter here"
Comment7 = "Enter here"
Comment8 = "Enter here"
Comment9 = "Enter here"
Comment10 = "Enter here"
Comment11 = "Enter here"
Comment12 = "Enter here"
Comment13 = "Enter here"
Comment14 = "Enter here"
Comment15 = "Enter here"
Comment16 = "Enter here"
Comment17 = "Enter here"
Comment18 = "Enter here"
Comment19 = "Enter here"
Comment20 = "Enter here"
Comment21 = "Enter here"
Comment22 = "Enter here"
Comment23 = "Enter here"
Comment24 = "Enter here"
Comment25 = "Enter here"
Comment26 = "Enter here"
Comment27 = "Enter here"
Comment28 = "Enter here"
Comment29 = "Enter here"
Comment30 = "Enter here"
Comment31 = "Enter here"
Comment32 = "Enter here"
Comment33 = "Enter here"
Comment34 = "Enter here"
Comment35 = "Enter here"
Comment36 = "Enter here"
Comment37 = "Enter here"
Comment38 = "Enter here"
Comment39 = "Enter here"
Comment40 = "Enter here"
Comment41 = "Enter here"
Comment42 = "Enter here"

# rec is the recommendation associated with each question
rec1 = rec2 = rec3 = rec4 = rec5 = rec6 = rec7 = rec8 = rec9 = rec10 = rec11 = rec12 = rec13 = rec14 = rec15 = rec16 = rec17 = rec18 = rec19 = rec20 = rec21 = rec22 = rec23 = rec24 = rec25 = rec26 = rec27 = rec28 = rec29 = rec30 = rec31 = rec32 = rec33 = rec34 = rec35 = rec36 = rec37 = rec38 = rec39 = rec40 = rec41 = rec42 = "None"

# ans is the textual answer based on user input ex: a:'yes'
ans1 = ans2 = ans3 = ans4 = ans5 = ans6 = ans7 = ans8 = ans9 = ans10 = ans11 = ans12 = ans13 = ans14 = ans15 = ans16 = ans17 = ans18 = ans19 = ans20 = ans21 = ans22 = ans23 = ans24 = ans25 = ans26 = ans27 = ans28 = ans29 = ans30 = ans31 = ans32 = ans33 = ans34 = ans35 = ans36 = ans37 = ans38 = ans39 = ans40 = ans41 = ans42 = "None"
percentages = []

def calculate_scores():
    # NIST function mapping
    mapping = {
        'Question3': 'Detect',
        'Question4': 'Protect',
        'Question6': 'Identify',
        'Question7': 'Protect',
        'Question8': 'Respond',
        'Question9': 'Respond',
        'Question10': 'Respond',
        'Question11': 'Respond',
        'Question12': 'Govern',
        'Question14': 'Govern',
        'Question15': 'Govern',
        'Question18': 'Respond',  
        'Question20': 'Respond',
        'Question24': 'Govern',
        'Question27': 'Identify',
        'Question28': 'Detect',
        'Question29': 'Protect',
        'Question30': 'Protect',
        'Question32': 'Recover',
        'Question33': 'Recover',
        'Question34': 'Protect',
        'Question37': 'Recover',
        'Question38': 'Recover'
    }
    
    total_questions = {
    'Identify': 2,
    'Protect': 5,
    'Detect': 2,
    'Respond': 6,
    'Recover': 4,
    'Govern': 4
    }
    
    # Initialize scoring
    scores = OrderedDict([('Identify', 0), ('Protect', 0), ('Detect', 0), ('Respond', 0), ('Recover', 0), ('Govern', 0)])

    # Iterate through each question's mapping
    for question, category in mapping.items():
        # Dynamically access the global variable for the question
        answer = globals().get(question)  # Get the answer for the question
        if str(answer) == 'a':
            scores[category] += 1

    # Calculate percentages and convert to a list
    percentages = []
    for category, score in scores.items():
        if total_questions[category] > 0:
           percentage = int((score/total_questions[category]) * 100 )
        percentages.append(percentage)
    return percentages

    
def provide_recs():
    global rec1, rec2, rec3, rec4, rec5, rec6, rec7, rec8, rec9, rec10, rec11, rec12, rec13, rec14, rec15, rec16, rec17, rec18, rec19, rec20, rec21, rec22, rec23, rec24, rec25, rec26, rec27, rec28, rec29, rec30, rec31, rec32, rec33, rec34, rec35, rec36, rec37, rec38, rec39, rec40, rec41, rec42
    global ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10, ans11, ans12, ans13, ans14, ans15, ans16, ans17, ans18, ans19, ans20, ans21, ans22, ans23, ans24, ans25, ans26, ans27, ans28, ans29, ans30, ans31, ans32, ans33, ans34, ans35, ans36, ans37, ans38, ans39, ans40, ans41, ans42  
    
    with open('recommendations.json') as f:
        recs = json.load(f)
        
    with open('answers.json') as f2:
        answers = json.load(f2)
        
    for i in range(1, 43):
        question_key = "Question "+str(i)
        answer = "Question"+str(i)
        record_key = "rec"+str(i)
        ans_key = "ans"+str(i)
        if len(globals()[answer]) > 1 and globals()[answer] != "None":
            globals()[record_key] = "Short answer - Your simulation director will review your answer with you during the debrief."
            globals()[ans_key] = globals()[answer]
        else:    
            globals()[record_key] = recs.get(question_key, {}).get(globals()[answer])
            globals()[ans_key] = answers.get(question_key, {}).get(globals()[answer])
    global percentages
    percentages = calculate_scores()
