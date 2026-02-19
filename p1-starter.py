# Name: Ashni Pothineni
# Student ID: 4559 8385
# Email: apothine@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.
# e.g.:
# Asked ChatGPT hints for debugging and suggesting the general structure of the code
# Did your use of GenAI on this assignment align with your goals and guidelines in
# your Gen AI contract? If not, why?

import unittest

def read_input(file):
    pass

# Calculation 1:
# For each species, what is the average body mass of penguins that have a bill length greater than 45 mm?
# Columns used: species, body_mass_g, bill_length_mm
def calc_1(penguins_list):
    pass

# Calculation 2:
# How many penguins are there for each sex on each island that have a flipper length greater than 200 mm?
# Columns used: sex, island, flipper_length_mm
def calc_2(penguins_list):
    pass

def write_output():
    pass


# Testing
class TestCalc(unittest.TestCase):
    def setUp(self):
        # read in subset dataset to list of dictionaries
        self.penguins_list = read_input("penguins_subset.csv")

    def test_calc1(self):
        avg_dict = calc_1(self.penguins_list)
        self.assertEqual(avg_dict["Adelie"], 4175)
        self.assertEqual(avg_dict["Gentoo"], 4850)
        self.assertEqual(avg_dict["Chinstrap"], 3475)

    def test_calc1_edge(self):
        update_penguins_list = []

        # Removing the only qualifying Gentoo penguin for calc 1 from the list
        for penguin in self.penguins_list:
            if not (penguin["species"] == "Gentoo" and penguin["bill_length_mm"] > 45):
                update_penguins_list.append(penguin)

        avg_dict = calc_1(update_penguins_list)
        self.assertEqual(avg_dict["Adelie"], 4175)
        self.assertEqual(avg_dict["Chinstrap"], 3475)
        self.assertNotIn("Gentoo", avg_dict)    # Gentoo should not exist since no penguins qualify

    def test_calc2(self):
        count_dict = calc_2(self.penguins_list)
        self.assertEqual(count_dict["Torgersen"]["M"], 0)
        self.assertEqual(count_dict["Torgersen"]["F"], 0)
        self.assertEqual(count_dict["Dream"]["M"], 1)
        self.assertEqual(count_dict["Dream"]["F"], 0)
        self.assertEqual(count_dict["Biscoe"]["M"], 1)
        self.assertEqual(count_dict["Biscoe"]["F"], 2)

    def test_calc2_edge(self):
        update_penguins_list = []

        # Removing the only male penguin on Biscoe for calc 2 from the list
        for penguin in self.penguins_list:
            if not (penguin["island"] == "Biscoe" and penguin["flipper_length_mm"] > 200):
                update_penguins_list.append(penguin)

        count_dict = calc_2(update_penguins_list)
        self.assertEqual(count_dict["Torgersen"]["M"], 0)
        self.assertEqual(count_dict["Torgersen"]["F"], 0)
        self.assertEqual(count_dict["Dream"]["M"], 1)
        self.assertEqual(count_dict["Dream"]["F"], 0)
        self.assertEqual(count_dict["Biscoe"]["M"], 0)  # Count should be 0 since no male penguins qualify
        self.assertEqual(count_dict["Biscoe"]["F"], 2)


if __name__ == '__main__':
    unittest.main()