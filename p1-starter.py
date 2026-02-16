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

# Calculation 1:
# For each species, what is the average body mass of penguins that have a bill length greater than 45 mm?
# Columns used: species, body_mass_g, bill_length_mm

# Calculation 2:
# How many penguins are there for each sex on each island that have a flipper length greater than 200 mm?
# Columns used: sex, island, flipper_length_mm


# Testing
class TestCalc(unittest.TestCase):
    def setUp():
        # read in subset dataset
        pass

    def test_calc1(self):
        pass

    def test_calc1_edge(self):
        pass

    def test_calc2(self):
        pass

    def test_calc2_edge(self):
        pass



if __name__ == '__main__':
    unittest.main()