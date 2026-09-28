# =============================================================================
# Exercise 4 - Boolean Grade Assignment
# =============================================================================
#
# At the University of CPA, we use the standard university grading scheme:
#
#     Grade      Classification
#     -----      --------------
#     70+        First
#     60-69      2.1
#     50-59      2.2
#     40-49      3rd
#     under 40   Fail
#
# The "grade" used to calculate your classification is a weighted average of
# the marks for the two assignments - the first worth 20% and the second worth
# 80%.
#
# Write some code that uses Boolean expressions to determine the following
# students' overall classification:
#
#     Student   Assignment 1   Assignment 2
#     -------   ------------   ------------
#     Martin    100            35
#     Arthur    40             65
#     Hemma     25             80
#     Josh      60             45
# =============================================================================

# Example: Martin
a1 = 100
a2 = 35

assessment1_weight = 0.2
assessment2_weight = 0.8
average = (a1 * assessment1_weight) + (a2 * assessment2_weight)

# Only one of these expressions should be true.
is_first = average >= 70
is_2_1   = average < 70 and average >= 60
is_2_2   = average < 60 and average >= 50
is_third = average < 50 and average >= 40
is_fail  = average < 40

print("Martin: ", is_first, is_2_1, is_2_2, is_third, is_fail)

#Arthur
a1 = 40
a2 = 65

assessment1_weight = 0.2
assessment2_weight = 0.8
average = (a1 * assessment1_weight) + (a2 * assessment2_weight)

# Only one of these expressions should be true.
is_first = average >= 70
is_2_1   = average < 70 and average >= 60
is_2_2   = average < 60 and average >= 50
is_third = average < 50 and average >= 40
is_fail  = average < 40

print("Arthur: ", is_first, is_2_1, is_2_2, is_third, is_fail)

# Hemma
a1 = 25
a2 = 80

assessment1_weight = 0.2
assessment2_weight = 0.8
average = (a1 * assessment1_weight) + (a2 * assessment2_weight)

# Only one of these expressions should be true.
is_first = average >= 70
is_2_1   = average < 70 and average >= 60
is_2_2   = average < 60 and average >= 50
is_third = average < 50 and average >= 40
is_fail  = average < 40

print("Hemma: ", is_first, is_2_1, is_2_2, is_third, is_fail)

# Example: Josh
a1 = 60
a2 = 45

assessment1_weight = 0.2
assessment2_weight = 0.8
average = (a1 * assessment1_weight) + (a2 * assessment2_weight)

# Only one of these expressions should be true.
is_first = average >= 70
is_2_1   = average < 70 and average >= 60
is_2_2   = average < 60 and average >= 50
is_third = average < 50 and average >= 40
is_fail  = average < 40

print("Josh: ", is_first, is_2_1, is_2_2, is_third, is_fail)