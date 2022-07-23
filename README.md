# <------------------------- SCS2201 - Data Structures and Algorithms  III --------------------------> 
#
# Assignment 1 - String Matching
#
# Contect of Answer Script
#
#           Question - './Assignment01.pdf'
#            Answer code -  './answer.py'
#            Text file - './modules.txt'
#            Explanation of choosing algorithm - ./explanation.pdf'
#            Explanation of the output of the code - ./README.md'
#
#
# -------- Explanation of the output of the code --------------
#
# Above question simply need to,
#
#    Get user input as pattern that they want to search,
#    Find the given pattern is matching with in the given file's content,
#    Print the relvant pattern included sentences and print the number of sentences that pattern include.
#
#
# This is a sample demonstration that How my code works :
#
#
# Example 1 -->
#
#    when the user given pattern is matching with the texts in the text file.(withcase sensitivity)
#
#
#                PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer> cd "e:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer"
#                PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer> python -u "e:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer\answer.py"
#
#                        Enter the Pattern : Home
#
#
#                APL3002 A Home for all  housing vulnerable populations
#                TCP2005 Houses and Homes
#                SEL3338 Home heritage history 20th century childrens literature
#                GEO2125 Fieldwork at Home
#                        Number of matches :  4
#
#                PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer>
#
#
#
# Example 2 -->
#
#    when the user given pattern is matching with the texts in the text file.(withoutcase sensitivity)
#
#
#                PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer> cd "e:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer"
#                PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer> python -u "e:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer\answer.py"
#
#                        Enter the Pattern : home
#
#
#                APL3002 A Home for all  housing vulnerable populations
#                TCP2005 Houses and Homes
#                SEL3338 Home heritage history 20th century childrens literature
#                GEO2125 Fieldwork at Home
#                        Number of matches :  4
#
#                PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer>
#
#
#
# Example 3 -->
#
#    when the user given pattern dpoes not matching with the texts in the text file.
#
#
#               PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer> cd "e:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer"
#                PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer> python -u "e:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer\answer.py"
#
#                        Enter the Pattern : circuits
#
#                circuits pattern is not found in the file
#
#                PS E:\Chirasi Amaya\2nd year\SCS-2201\Assignment1\Assignment Answer>

