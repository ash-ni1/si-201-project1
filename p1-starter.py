# Name: Ashni Pothineni
# Student ID: 4559 8385
# Email: apothine@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): No teammates
# If you worked with generative AI also add a statement for how you used it.
    # I used Python docs and the lecture slides for help with reading files and writing files
# Asked ChatGPT hints for debugging and suggesting the general structure of the code
# Did your use of GenAI on this assignment align with your goals and guidelines in
# your Gen AI contract? If not, why?
    # My use of GenAI on this assignment aligned with my goals and guidelines in my GenAI contract.

import csv
import unittest

def read_input(csv_file):
    '''
    Reads input .csv file into a list of dictionaries
    '''
    penguins_list = []
    
    # Open and read csv file, use 'with open' for automatic close
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)

        # Get keys for individual dictionaries of penguins
        key_sp = headers[1]
        key_is = headers[2]
        key_bl = headers[3]
        key_bd = headers[4]
        key_fl = headers[5]
        key_bm = headers[6]
        key_sx = headers[7]
        key_yr = headers[8]

        for row in reader:
            # Empty dictionary for single penguin object  
            penguin = {}      

            # Get each individual value
            species = row[1]
            island = row[2]
            # Account for 'NA' value in the dataset, set None if value equals 'NA' else get true value
            bill_length = None if row[3] == 'NA' else float(row[3])
            bill_depth = None if row[4] == 'NA' else float(row[4])
            flipper_length = None if row[5] == 'NA' else int(row[5])
            body_mass = None if row[6] == 'NA' else int(row[6])
            sex = None if row[7] == 'NA' else row[7]
            year = int(row[8])

            # Insert value into dictionary
            penguin[key_sp] = species
            penguin[key_is] = island
            penguin[key_bl] = bill_length
            penguin[key_bd] = bill_depth
            penguin[key_fl] = flipper_length
            penguin[key_bm] = body_mass
            penguin[key_sx] = sex
            penguin[key_yr] = year

            # Add penguin to list
            penguins_list.append(penguin)

    return penguins_list

def calc_1(penguins_list):
    '''
    For each species, calculates the average body mass of penguins that have a bill length greater than 45 mm
    Columns used: species, body_mass_g, bill_length_mm
    '''
    averages = {}

    # Keep track of the sum and count for each species
    adelie_sum = 0
    a_count = 0
    gentoo_sum = 0
    g_count = 0
    chinstrap_sum = 0
    c_count = 0

    # Loop through each penguin
        # 1) Get the bill length of the penguin and check if bill length is None
            # 1.5) If true, continue to next penguin
        # 2) Check if the bill length is greater than 45 mm
        # 3) If true, get the species and body_mass of the penguin
            # 3.5) If body_mass is None, continue to next penguin
        # 4) Filter by species using if/elif, add to respective sum and count
    for penguin in penguins_list:
        bill_length = penguin["bill_length_mm"]
        if bill_length is None:
            continue

        if bill_length > 45:
            species = penguin["species"]
            body_mass = penguin["body_mass_g"]
            if body_mass is None:
                continue

            if species == 'Adelie':
                adelie_sum += body_mass
                a_count += 1
            elif species == 'Gentoo':
                gentoo_sum += body_mass
                g_count += 1
            elif species == "Chinstrap":
                chinstrap_sum += body_mass
                c_count += 1

    # Calculate the averages, prevent divide by 0 by checking count value
    averages["Adelie"] = 0 if a_count == 0 else adelie_sum / a_count
    averages["Gentoo"] = 0 if g_count == 0 else gentoo_sum / g_count
    averages["Chinstrap"] = 0 if c_count == 0 else chinstrap_sum / c_count

    write_output(averages, 1)
    return averages

def calc_2(penguins_list):
    '''
    Calculates how many penguins there are for each sex on each island that have a flipper length greater than 200 mm
    Columns used: sex, island, flipper_length_mm
    '''
    counts = {}

    # Loop through each penguin
        # 1) Get the flipper length of the penguin and check if flipper length is None
            # 1.5) If true, continue to next penguin
        # 2) Check if the flipper length is greater than 200 mm
        # 3) If true, get the island and sex of the penguin
            # 3.5) If sex is None, continue to next penguin
        # 4) Get the inner dictionary of count by sex and add to respective count
    for penguin in penguins_list:
        flipper_length = penguin["flipper_length_mm"]
        if flipper_length is None:
            continue
        
        if flipper_length > 200:
            island = penguin["island"]
            sex = penguin["sex"]
            if sex is None:
                continue
            
            s_dict = counts.get(island, {})
            s_dict[sex] = s_dict.get(sex, 0) + 1
            counts[island] = s_dict

    write_output(counts, 2)
    return counts

def write_output(output, num):
    '''
    Writes output of a calculation into a .txt file
    '''
    # Open and write txt file, use 'with open' for automatic close
    # Mode a to append to file instead of overwritting
    with open('output.txt', mode='a') as file:
        file.write(f"Calculation {num} Output:\n{output}\n\n")


# Testing
class TestCalc(unittest.TestCase):
    def setUp(self):
        open('output.txt', 'w').close() # clear output file at start of run
        # read in subset dataset to list of dictionaries
        self.penguins_list = read_input('penguins_subset.csv')

    def test_calc1(self):
        avg_dict = calc_1(self.penguins_list)
        self.assertEqual(avg_dict["Adelie"], 4175)
        self.assertEqual(avg_dict["Chinstrap"], 3475)
        self.assertEqual(avg_dict["Gentoo"], 4850)

    def test_calc1_edge(self):
        update_penguins_list = []

        # Removing the only qualifying Gentoo penguin for calc 1 from the list
            # Other Gentoo penguins are less than or equal 45 mm bill length (not greater)
        for penguin in self.penguins_list:
            if not (penguin["species"] == "Gentoo" and penguin["bill_length_mm"] > 45):
                update_penguins_list.append(penguin)

        avg_dict = calc_1(update_penguins_list)
        self.assertEqual(avg_dict["Adelie"], 4175)
        self.assertEqual(avg_dict["Chinstrap"], 3475)
        self.assertEqual(avg_dict["Gentoo"], 0)    # Gentoo should average 0 since no penguins qualify

    def test_calc2(self):
        count_dict = calc_2(self.penguins_list)
        self.assertNotIn("Torgersen", count_dict)
        self.assertEqual(count_dict["Dream"]["male"], 1)
        self.assertNotIn("female", count_dict["Dream"])
        self.assertEqual(count_dict["Biscoe"]["male"], 1)
        self.assertEqual(count_dict["Biscoe"]["female"], 2)

    def test_calc2_edge(self):
        update_penguins_list = []

        # Removing the only male penguin on Biscoe for calc 2 from the list
            # Other male penguin on Biscoe that has exactly 200 mm flipper length (not greater)
            # Other penguins on Biscoe are 2 females and 1 NA
        for penguin in self.penguins_list:
            if not (penguin["island"] == "Biscoe" and penguin["flipper_length_mm"] > 200 and penguin["sex"] == "male"):
                update_penguins_list.append(penguin)

        # Check that other male penguin on Biscoe that has exactly 200 mm flipper length still in list
        self.assertEqual(update_penguins_list[1]["island"], "Biscoe")
        self.assertEqual(update_penguins_list[1]["flipper_length_mm"], 200)
        self.assertEqual(update_penguins_list[1]["sex"], "male")

        count_dict = calc_2(update_penguins_list)
        self.assertNotIn("Torgersen", count_dict)
        self.assertEqual(count_dict["Dream"]["male"], 1)
        self.assertNotIn("female", count_dict["Dream"])
        self.assertNotIn("male", count_dict["Biscoe"])  # key of "male" should not exist since no male penguins qualify
        self.assertEqual(count_dict["Biscoe"]["female"], 2)


def main():
    open('output.txt', 'w').close() # clear output file at start of run
    penguins_list = read_input('penguins.csv')
    calc_1(penguins_list)
    calc_2(penguins_list)
    
    # unittest.main()

if __name__ == '__main__':
    main()