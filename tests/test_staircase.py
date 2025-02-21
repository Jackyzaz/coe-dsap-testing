from program.staircase import staircase
import unittest


class StairCaseTest(unittest.TestCase):
    # case 1: Below Min-Boundary by 1
    def test_give_minus_0_is_empty(self):
        # arrange
        n = 0
        pattern = "#"
        expected_output = ""

        # act
        result = staircase(n, pattern)
        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    # case 2: At Min Boundary
    def test_give_1_should_be_h(self):
        # arrange
        n = 1
        pattern = "#"
        expected_output = "#\n"

        # act
        result = staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    # case 3: Above Min-Boundary by 1
    def test_give_2_should_be_hh(self):
        # arrange
        n = 2
        pattern = "#"
        expected_output = " #\n##\n"
        # act
        result = staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be  {expected_output}")

        # arrange
        n = 1

    # case 4: average case
    def test_give_15_is_correctly(self):
        # arrange
        n = 15
        pattern = "#"
        expected_output = """              #
             ##
            ###
           ####
          #####
         ######
        #######
       ########
      #########
     ##########
    ###########
   ############
  #############
 ##############
###############
"""
        # act
        result = staircase(n, pattern)

        # arrange
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    # case 5: Below Max-Boundary by 1
    def test_give_29_is_correctly(self):
        # arrange
        n = 29
        pattern = "#"
        expected_output = """                            #
                           ##
                          ###
                         ####
                        #####
                       ######
                      #######
                     ########
                    #########
                   ##########
                  ###########
                 ############
                #############
               ##############
              ###############
             ################
            #################
           ##################
          ###################
         ####################
        #####################
       ######################
      #######################
     ########################
    #########################
   ##########################
  ###########################
 ############################
#############################
"""
        # act
        result = staircase(n, pattern)

        # arrange
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    # case 6: At Max-Boundary
    def test_give_30_is_correctly(self):
        # arrange
        n = 30
        pattern = "#"
        expected_output = """                             #
                            ##
                           ###
                          ####
                         #####
                        ######
                       #######
                      ########
                     #########
                    ##########
                   ###########
                  ############
                 #############
                ##############
               ###############
              ################
             #################
            ##################
           ###################
          ####################
         #####################
        ######################
       #######################
      ########################
     #########################
    ##########################
   ###########################
  ############################
 #############################
##############################
"""
        # act
        result = staircase(n, pattern)

        # arrange
        self.assertEqual(result, expected_output, f"Should be {expected_output}")

    # case 7: Above Max-Boundary by 1
    def test_give_31_is_empty(self):
        # arrange
        n = 31
        pattern = "#"
        expected_output = ""
        # act
        result = staircase(n, pattern)

        # arrange
        self.assertEqual(result, expected_output, f"Should be {expected_output}")
