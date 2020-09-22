# - COVID-19 PROBABILITY DETECTOR
# - Coded by Adriskk | 2020
import data
import detector


# - MAIN FUNCTION
def main():
    print("============================")
    print("|       CORONA VIRUS       |")
    print("|--------------------------|")
    print("|   PROBABILITY DETECTOR   |")
    print("============================")
    print(" > Beta version (0.0.1)")
    print("|")
    raise_detector_data()


def weight_by_age(age):
    if age > 65:
        data.standard_smpt_weight[0] += 1
        data.standard_smpt_weight[1] += 1
        data.standard_smpt_weight[2] += 1

        data.rare_smpt_weight[0] += 1
        data.rare_smpt_weight[1] += 1
        data.rare_smpt_weight[2] += 1
        data.rare_smpt_weight[3] += 1
        data.rare_smpt_weight[4] += 1
        data.rare_smpt_weight[5] += 1
        data.rare_smpt_weight[6] += 1

        data.serious_smpt_weight[0] += 1
        data.serious_smpt_weight[1] += 1
        data.serious_smpt_weight[2] += 1

        # print(data.standard_smpt_weight)
        # print(data.rare_smpt_weight)
        # print(data.serious_smpt_weight)


def raise_detector_data():
    y_n_question = "Type [Y/y - yes | N/n - No] "

    print("|")
    print("To find out if you are possibly infected with the coronavirus(COVID-19) ")
    print("Answer to some questions: ")

    # IF AGE IS MORE THAN 65 THEN ADD ONE POINT TO ALL SYMPTOMS WEIGHTS LISTS
    age = input("Type your age: ")
    weight_by_age(int(age))

    index = 0
    # - STANDARD QUESTION LOOP:
    for standard_q in data.standard_questions:
        print("\n", standard_q)
        # print(y_n_question)
        answer = input(y_n_question)

        if answer == "Y" or answer == "y":
            data.standard_symptoms[index] = True
        elif answer == "N" or answer == "n":
            pass
        else:
            while answer != "Y" or answer != "y" or answer != "N" or answer != "n":
                print("> Unknown char - answer again <")
                print(standard_q)
                # print(y_n_question)
                answer = input(y_n_question)
            else:
                continue
        index += 1
    result = detector.detector(type="standard")

    if not result:
        print("You probably don't have COVID-19, but you should take some medicines ")
    else:
        # - RARE QUESTION LOOP
        index = 0
        for rare_q in data.rare_questions:
            print("\n", rare_q)
            # print(y_n_question)
            answer = input(y_n_question)

            if answer == "Y" or answer == "y":
                data.rare_symptoms[index] = True
            elif answer == "N" or answer == "n":
                pass
            else:
                while answer != "Y" or answer != "y" or answer != "N" or answer != "n":
                    print("> Unknown char - answer again <")
                    print(rare_q)
                    # print(y_n_question)
                    answer = input(y_n_question)
                else:
                    continue
            index += 1
        result = detector.detector(type="rare")

        if not result:
            print("You probably don't have COVID-19, but you should take a visit with a doctor anyways ")
        elif result == "probably":
            print("You can have the coronavirus, but it is not so harmful ")
        elif result:
            # - SERIOUS QUESTION LOOP
            index = 0
            for serious_q in data.serious_questions:
                print("\n", serious_q)
                # print(y_n_question)
                answer = input(y_n_question)

                if answer == "Y" or answer == "y":
                    data.serious_symptoms[index] = True
                elif answer == "N" or answer == "n":
                    pass
                else:
                    while answer != "Y" or answer != "y" or answer != "N" or answer != "n":
                        print("> Unknown char - answer again <")
                        print(serious_q)
                        # print(y_n_question)
                        answer = input(y_n_question)
                    else:
                        continue
                index += 1
            result = detector.detector(type="serious")

            if result == "dead":
                print("You have to call the emergency insurance now! You have the COVID-19! ")
                # -- LIST OF ALL NUMBERS IN THE COUNTRIES
            elif result == "fast-hospital":
                print("You have to take a visit with a doctor as fast as you can or call the emergency insurance! "
                      "You have the COVID-19! ")
            elif result == "hospital":
                print("You have the COVID-19, Stay at home and do not go anywhere! You can call the emergency "
                      "insurance ")
    # works -- print(data.standard_symptoms)


if __name__ == "__main__":
    main()
