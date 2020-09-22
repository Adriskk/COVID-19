# --- CORONAVIRUS DETECTOR CORE FILE
import data


# DETECTOR FUNCTION
def detector(type):
    # - STANDARD QUESTION COVID-19 DETECTION
    standard_weight = 0
    if type == "standard":
        if data.standard_symptoms[0] is True:
            standard_weight += data.standard_smpt_weight[0]
        if data.standard_symptoms[1] is True:
            standard_weight += data.standard_smpt_weight[1]
        if data.standard_symptoms[2] is True:
            standard_weight += data.standard_smpt_weight[2]

        # print(standard_weight)
        if standard_weight >= 3:
            return True
        else:
            return False

    # - RARE QUESTION COVID-19 DETECTION
    rare_weight = 0
    if type == "rare":
        if data.rare_symptoms[0] is True:
            rare_weight += data.rare_smpt_weight[0]
        if data.rare_symptoms[1] is True:
            rare_weight += data.rare_smpt_weight[1]
        if data.rare_symptoms[2] is True:
            rare_weight += data.rare_smpt_weight[2]
        if data.rare_symptoms[3] is True:
            rare_weight += data.rare_smpt_weight[3]
        if data.rare_symptoms[4] is True:
            rare_weight += data.rare_smpt_weight[4]
        if data.rare_symptoms[5] is True:
            rare_weight += data.rare_smpt_weight[5]
        if data.rare_symptoms[6] is True:
            rare_weight += data.rare_smpt_weight[6]

        if rare_weight >= 11:
            return True
        elif rare_weight <= 8:
            return "probably"
        else:
            return False

    # - SERIOUS QUESTION COVID-19 DETECTION
    serious_weight = 0
    if type == "serious":
        if data.serious_symptoms[0] is True:
            serious_weight += data.serious_smpt_weight[0]
        if data.serious_symptoms[1] is True:
            serious_weight += data.serious_smpt_weight[1]
        if data.serious_symptoms[2] is True:
            serious_weight += data.serious_smpt_weight[2]

        if serious_weight == 17:
            return "dead"
        elif 11 <= serious_weight < 17:
            return "fast-hospital"
        elif serious_weight < 11:
            return "hospital"
# ---


