# --- DATA VARIABLES
# ---

# -- PROGRAM DATA:
version = "(0.0.1)"

# -- DETECTOR DATA:

# - STANDARD SYMPTOMS
standard_symptoms = {
    0: False,  # fever
    1: False,  # dry-cough
    2: False,  # fatigue
}

standard_smpt_weight = [
    1,
    2,
    1
]

# - RARE SYMPTOMS
rare_symptoms = {
    0: False,  # muscle-pain
    1: False,  # sore-throat
    2: False,  # diarrhea
    3: False,  # conjunctivitis
    4: False,  # headache
    5: False,  # taste-smell-loss
    6: False  # skin-rash-discoloration
}

rare_smpt_weight = [
    3,
    3,
    2,
    3,
    3,
    4,
    3
]

# - SERIOUS SYMPTOMS
serious_symptoms = {
    0: False,  # breathing-difficulty-shortness-of-breath
    1: False,  # tightness-chest-pain
    2: False  # speech-motor-skills-loss
}

serious_smpt_weight = [
    6,
    6,
    5
]

# - DETECTOR QUESTIONS
standard_questions = [
    "Have you had a fever in the last two weeks? ",
    "If you cough, have you cough dry? ",
    "Are you tired? Do you feel fatigue? "
]

rare_questions = [
    "Do you have muscle pain? ",
    "Do you have sore throat? ",
    "Do you have diarrhea? ",
    "Do you feel like you could have conjunctivitis? (Common symptoms of conjunctivitis: itch, eye baking, tearing, "
    "eye reddening) ",
    "Do you have a headache? ",
    "Have you lost your taste or smell recently? ",
    "Did you observe skin rash or discoloration of the fingers and toes lately? ",
]

serious_questions = [
    "Do you have difficulty in breathing or shortness of breath? ",
    "Do you have chest pain or tightness? ",
    "Did you lost skill to speech or to move? "
]

