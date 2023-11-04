from typing import List

confirm = "cues2023"

# A1. Age in Days

from datetime import date
def age_days_assert(Y, M, D):
    d0 = date.today()
    d1 = date(Y, M, D)
    delta = d0 - d1
    if delta.days >= 0:
        return delta.days

def assert_A1(age_days):
    try:
        # assert(round(age_days(1970,1,1),-3)==19000)
        assert(int(age_days(1970,1,1))==int(age_days_assert(1970,1,1)))
        print("A1. Age in Days: Passed ✓")
    except:
        print("A1. Age in Days: Failed ×")

# A2. Recursive Sum

def assert_A2(recursive_sum):
    try:
        expected_output = 55
        output = recursive_sum(10)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        expected_output = 465
        output = recursive_sum(30)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        print("A2. Recursive Sum: Passed ✓")
    except AssertionError as e:
        print("A2. Recursive Sum: Failed ×\n Reason: ", e)
    except:
        print("A2. Recursive Sum: Failed ×")

# A3. Duplicates Only

def assert_A3(duplicates_only):
    try:
        n = [1, 3, 1, 4, 3, 7, -2, 0, 7, -2, -2, 1]
        expected_output = [3, 7]
        output = duplicates_only(n)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"

        n = [1, 2, 3, 4]
        expected_output = []
        output = duplicates_only(n)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"

        n = [1, 2, 3, 3, 4, 4, 4, 3, 2, 1]
        expected_output = [1, 2]
        output = duplicates_only(n)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        print("A3. Duplicates Only: Passed ✓")
    except AssertionError as e:
        print("A3. Duplicates Only: Failed ×\n Reason: ", e)
    except:
        print("A3. Duplicates Only: Failed ×")

# A4. Even Numbers

def assert_A4(even_numbers):
    try:
        n = [3, 7, 9, 2, 5, 5, 8, 5, 6, 3, 4, 7, 3, 1]
        expected_output = [2, 8, 6, 4]
        output = even_numbers(n)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        n = [3, 32, 9, 2, 21, 12, 8, 5, 6, 3, 14, 7, 13, 11, 16]
        expected_output = [32, 2, 12, 8, 6, 14, 16]
        output = even_numbers(n)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        n = []
        expected_output = []
        output = even_numbers(n)
        assert output == expected_output, f"Test case 3 failed: Expected {expected_output}, but got {output}"
        print("A4. Even Numbers: Passed ✓")
    except AssertionError as e:
        print("A4. Even Numbers: Failed ×\n Reason: ", e)
    except:
        print("A4. Even Numbers: Failed ×")

# A5. Remove Pairs

def assert_A5(remove_pairs):
    try:
        n = [3, 7, 9, 2, 5, 5, 8, 5, 6, 3, 4, 7, 3, 1]
        expected_output = [3, 7, 5, 5, 4, 7]
        output = remove_pairs(n)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        n = [3, 7, 9, 2, 5, 5, 8, 5, 6, 3, 4, 7, 3, 1, 3]
        expected_output = [3, 7, 5, 5, 4, 7]
        output = remove_pairs(n)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        n = []
        expected_output = []
        output = remove_pairs(n)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        print("A5. Remove Pairs: Passed ✓")
    except AssertionError as e:
        print("A5. Remove Pairs: Failed ×\n Reason: ", e)
    except:
        print("A5. Remove Pairs: Failed ×")

# A6. Binary to Decimal

def assert_A6(bin2dec):
    try:
        n = 100
        expected_output = 4
        output = bin2dec(n)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"

        n = 1000
        expected_output = 8
        output = bin2dec(n)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"

        n = 1011
        expected_output = 11
        output = bin2dec(n)
        assert output == expected_output, f"Test case 3 failed: Expected {expected_output}, but got {output}"

        n = 110110
        expected_output = 54
        output = bin2dec(n)
        assert output == expected_output, f"Test case 4 failed: Expected {expected_output}, but got {output}"

        n = 0
        expected_output = 0
        output = bin2dec(n)
        assert output == expected_output, f"Test case 5 failed: Expected {expected_output}, but got {output}"
        print("A6. Binary to Decimal: Passed ✓")
    except AssertionError as e:
        print("A6. Binary to Decimal: Failed ×\n Reason: ", e)
    except:
        print("A6. Binary to Decimal: Failed ×")

# A7. Can Make Sum

def assert_A7(can_make_sum):
    try:
        n = [3, 7, 9, 2, 5, 5, 8]
        expected_output = True
        output = can_make_sum(n, 25)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        n = [3, 7, 9, 5]
        expected_output = False
        output = can_make_sum(n, 18)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        n = [2, 5, 6, 2, 3, 5]
        expected_output = True
        output = can_make_sum(n, 23)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        print("A7. Can Make Sum: Passed ✓")
    except AssertionError as e:
        print("A7. Can Make Sum: Failed ×\n Reason: ", e)
    except:
        print("A7. Can Make Sum: Failed ×")

# A8. Pow

def assert_A8(my_pow):
    try: 
        # Test case 1
        x = 2.00000
        n = 10
        expected_output = 1024.0
        output = my_pow(x, n)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"

        # Test case 2
        x = 3
        n = 4
        expected_output = 81.0
        output = my_pow(x, n)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"

        # Test case 3
        x = 1.5
        n = 3
        expected_output = 3.375
        output = my_pow(x, n)
        assert output == expected_output, f"Test case 3 failed: Expected {expected_output}, but got {output}"

        # Test case 4
        x = 2.00000
        n = -2
        expected_output = 0.25
        output = my_pow(x, n)
        assert output == expected_output, f"Test case 4 failed: Expected {expected_output}, but got {output}"
        print("A8. Pow: Passed ✓")
    except AssertionError as e:
        print("A8. Pow: Failed ×\n Reason: ", e)
    except:
        print("A8. Pow: Failed ×")

# A9. Rotate Image

def assert_A9(rotate):
    try:
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        rotate(matrix)
        expected_output = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        assert matrix == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {matrix}"
        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        rotate(matrix)
        expected_output = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
        assert matrix == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {matrix}"
        matrix = [[1]]
        rotate(matrix)
        expected_output = [[1]]
        assert matrix == expected_output, f"Test case 3 failed: Expected {expected_output}, but got {matrix}"
        print("A9. Rotate Image: Passed ✓")
    except AssertionError as e:
        print("A9. Rotate Image: Failed ×\n Reason: ", e)
    except:
        print("A9. Rotate Image: Failed ×")

# A10. Merge Sort

def assert_A10(merge_sort):
    try:
        arr = [2, 1, 5, 3, 4]
        output = merge_sort(arr)
        expected_output = [1, 2, 3, 4, 5]
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        arr = [3]
        output = merge_sort(arr)
        expected_output = [3]
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        arr = [0, 1, 5, 2, 6, 2, 7, 4, 5]
        output = merge_sort(arr)
        expected_output = [0, 1, 2, 2, 4, 5, 5, 6, 7]
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        print("A10. Merge Sort: Passed ✓")
    except AssertionError as e:
        print("A10. Merge Sort: Failed ×\n Reason: ", e)
    except:
        print("A10. Merge Sort: Failed ×")

# A11. Longest Common Subsequence

def assert_A11(longest_common_subsequence_length):
    try:
        str1 = "AGGTAB"
        str2 = "GXTXAYB"
        output = longest_common_subsequence_length(str1, str2)
        expected_output = 4
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        str1 = "AGG"
        str2 = "XTXY"
        output = longest_common_subsequence_length(str1, str2)
        expected_output = 0
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        str1 = "AGAB"
        str2 = "AXGXTXBAY"
        output = longest_common_subsequence_length(str1, str2)
        expected_output = 3
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        print("A11. Longest Common Subsequence: Passed ✓")
    except AssertionError as e:
        print("A11. Longest Common Subsequence: Failed ×\n Reason: ", e)
    except:
        print("A11. Longest Common Subsequence: Failed ×")

# A12: Pascal's Triangle

def assert_A12(pascals_triangle):
    try:
        ret = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1], [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1], [1, 12, 66, 220, 495, 792, 924, 792, 495, 220, 66, 12, 1], [1, 13, 78, 286, 715, 1287, 1716, 1716, 1287, 715, 286, 78, 13, 1], [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1], [1, 15, 105, 455, 1365, 3003, 5005, 6435, 6435, 5005, 3003, 1365, 455, 105, 15, 1]]
        prod = 1329227995784915872903807060280344576
        assert(pascals_triangle(16)==(ret,prod))
        print("A12. Pascal's Triangle: Passed ✓")
    except:
        print("A12. Pascal's Triangle: Failed ×")

# A13. Roman Numeral Converter

def assert_A13(roman_numeral):
    try:
        assert [roman_numeral(i) for i in range(1,51)] == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL', 'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX','L']
        print("A13. Roman Numeral Converter: Passed ✓")
    except:
        print("A13. Roman Numeral Converter: Failed ×")

# A14. Not Wordle

def assert_A14(get_hint):
    try:
        assert(get_hint("1123", "0111") == "1G1Y")
        print("A14. Not Wordle: Passed ✓")
    except:
        print("A14. Not Wordle: Failed ×")

# A15. Strange Caps

def assert_A15(strange_caps):
    try:
        assert(strange_caps("Cambridge University Engineering Society") == "CaMbRiDgE uNiVeRsItY eNgInEeRiNg SoCiEtY")
        print("A15. Strange Caps: Passed ✓")
    except:
        print("A15. Strange Caps: Failed ×")

# A16. Valid Parantheses

def assert_A16(valid_parentheses):
    try:
        assert(valid_parentheses("()") == True)
        assert(valid_parentheses("()[]{}") == True)
        assert(valid_parentheses("(]") == False)
        assert(valid_parentheses("()[()]{}") == True)
        assert(valid_parentheses("()[(]){}") == False)
        print("A16. Valid Parantheses: Passed ✓")
    except:
        print("A16. Valid Parantheses: Failed ×")

# B1. Different Dice

def assert_B1(dice):
    try:
        print("B1. Different Dice: Manual Check Required")
        pw = input("Marker code: ")
        if pw == confirm:
            print("Marker note: nested for loops also acceptable. Ensure no white vertical bars in the histogram and that increasing the number of bins by 1 adds a white vertical bar in histogram.")
            print("Generating...")
            import matplotlib.pyplot as plt
            total = []
            def different_dice(idx, so_far):
                if idx == len(dice):
                    try:
                        total.append(so_far)
                    except:
                        print(so_far)
                    return
                for i in range(dice[idx]):
                    so_far += i + 1
                    different_dice(idx + 1, so_far)
                    so_far -= i + 1
            different_dice(0, 0)
            plt.hist(total, bins=sum(dice) - 5)
            plt.show()
            ans1 = input("Does their histogram look similar? (y/n) ")
            ans2 = input("Did they use for loop/nested loops? (y/n) ")
            if ans1 == "y" and ans2 == "y":
                print("B1. Different Dice: Passed ✓")
            else:
                print("B1. Different Dice: Failed ×")
        else:
            print("B1. Different Dice: Failed ×")
    except:
        print("B1. Different Dice: Failed ×")

# B2. Determining Static Equilibrium

def assert_B2(static_equilibrium):
    try:
        M, R = static_equilibrium()
        assert(round(abs(M[0]), 2) == 8.32)
        assert(round(abs(R[0]), 2) == 4.16)
        assert(round(abs(R[1]), 2) == 2.77)
        print("B2. Determining Static Equilibrium: Passed ✓")
    except:
        print("B2. Determining Static Equilibrium: Failed ×")

# B3. Traffic Sensor

def assert_B3(traffic_sensor):
    try:
        assert(traffic_sensor()[0] == [15.455555555555556, 8.222222222222221, 4.633333333333334, 4.844444444444444, 8.0, 14.355555555555556, 44.13333333333333, 86.74444444444444, 107.43333333333334, 98.6, 87.02222222222223, 94.0111111111111, 95.08888888888889, 93.1, 96.03333333333333, 101.68888888888888, 111.21111111111111, 119.03333333333333, 115.3, 96.18888888888888, 68.11111111111111, 62.733333333333334, 49.27777777777778, 28.433333333333334])
        assert(traffic_sensor()[1] == [1.5333333333333334, 0.8222222222222222, 0.5333333333333333, 0.6666666666666666, 1.0333333333333334, 1.3111111111111111, 5.544444444444444, 14.655555555555555, 29.677777777777777, 19.933333333333334, 15.21111111111111, 15.577777777777778, 17.61111111111111, 17.333333333333332, 14.833333333333334, 16.966666666666665, 19.72222222222222, 20.988888888888887, 19.055555555555557, 15.088888888888889, 9.666666666666666, 8.744444444444444, 4.644444444444445, 2.466666666666667])
        print("B3. Traffic Sensor: Passed ✓")
    except:
        print("B3. Traffic Sensor: Failed ×")

# B4. Scatter Plot

def assert_B4(gen_input_data):
    try:
        print("B4. Scatter Plot: Manual Check Required")
        pw = input("Marker code: ")
        if pw == confirm:
            print("Generating...")
            import matplotlib.pyplot as plt
            points = gen_input_data()
            x = [point[0] for point in points]
            y = [point[1] for point in points]
            c = [point[2] for point in points]
            plt.scatter(x, y, c=c)
            plt.show()
            ans = input("Does their scatter plot look similar? (y/n) ")
            if ans == "y":
                print("B4. Scatter Plot: Passed ✓")
            else:
                print("B4. Scatter Plot: Failed ×")
        else:
            print("B4. Scatter Plot: Failed ×")
    except:
        print("B4. Scatter Plot: Failed ×")

# C1. Invert Order of String

def assert_C1(invert_string):
    try:
        test_string = "qwertyuiopasdfghjklzxcvbnm"
        assert(invert_string(test_string) == "mnbvcxzlkjhgfdsapoiuytrewq")
        print("C1. Invert Order of String: Passed ✓")
    except:
        print("C1. Invert Order of String: Failed ×")

# C2. Can Jump

def assert_C2(can_jump):
    try:
        nums = [2, 3, 1, 1, 4]
        expected_output = True
        output = can_jump(nums)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        nums = [3, 2, 1, 0, 4]
        expected_output = False
        output = can_jump(nums)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        nums = [2, 0, 0, 0, 0]
        expected_output = False
        output = can_jump(nums)
        assert output == expected_output, f"Test case 3 failed: Expected {expected_output}, but got {output}"
        nums = [1, 1, 1, 1, 1, 1]
        expected_output = True
        output = can_jump(nums)
        assert output == expected_output, f"Test case 4 failed: Expected {expected_output}, but got {output}"
        print("C2. Can Jump: Passed ✓")
    except AssertionError as e:
        print("C2. Can Jump: Failed ×\n Reason: ", e)
    except:
        print("C2. Can Jump: Failed ×")

# C3. Climbing Stairs

def assert_C3(climb_stairs):
    try:
        N = 1
        expected_output = 1
        output = climb_stairs(N)
        assert output == expected_output, f"Test case 1 failed: Expected {expected_output}, but got {output}"
        N = 4
        expected_output = 5
        output = climb_stairs(N)
        assert output == expected_output, f"Test case 2 failed: Expected {expected_output}, but got {output}"
        N = 8
        expected_output = 34
        output = climb_stairs(N)
        assert output == expected_output, f"Test case 3 failed: Expected {expected_output}, but got {output}"
        N = 12
        expected_output = 233
        output = climb_stairs(N)
        assert output == expected_output, f"Test case 4 failed: Expected {expected_output}, but got {output}"
        print("C3. Climbing Stairs: Passed ✓")
    except AssertionError as e:
        print("C3. Climbing Stairs: Failed ×\n Reason: ", e)
    except:
        print("C3. Climbing Stairs: Failed ×")

# C4. Remove Duplicate Letters

def assert_C4(remove_duplicate):
    try:
        s1 = "bcabc"
        expected_output1 = "abc"
        output1 = remove_duplicate(s1)
        assert output1 == expected_output1, f"Test case 1 failed: Expected '{expected_output1}', but got '{output1}'"
        s2 = "cbacdcbc"
        expected_output2 = "acdb"
        output2 = remove_duplicate(s2)
        assert output2 == expected_output2, f"Test case 2 failed: Expected '{expected_output2}', but got '{output2}'"
        s4 = "abcdef"
        expected_output4 = "abcdef"
        output4 = remove_duplicate(s4)
        assert output4 == expected_output4, f"Test case 3 failed: Expected '{expected_output4}', but got '{output4}'"
        s5 = "aaaaa"
        expected_output5 = "a"
        output5 = remove_duplicate(s5)
        assert output5 == expected_output5, f"Test case 4 failed: Expected '{expected_output5}', but got '{output5}'"
        s6 = "b"
        expected_output6 = "b"
        output6 = remove_duplicate(s6)
        assert output6 == expected_output6, f"Test case 5 failed: Expected '{expected_output6}', but got '{output6}'"
        s7 = "abcdefghijklmnopqrstuvwxyz"
        expected_output7 = "abcdefghijklmnopqrstuvwxyz"
        output7 = remove_duplicate(s7)
        assert output7 == expected_output7, f"Test case 6 failed: Expected '{expected_output7}', but got '{output7}'"
        print("C4. Remove Duplicate Letters: Passed ✓")
    except AssertionError as e:
        print("C4. Remove Duplicate Letters: Failed ×\n Reason: ", e)
    except:
        print("C4. Remove Duplicate Letters: Failed ×")

# C5. Find Duplicate Number

def assert_C5(find_duplicate):
    try:
        A = [1, 2, 3, 4, 4, 5, 6]
        expected_output = 4
        output = find_duplicate(A)
        assert output == expected_output, f"Test case 1 failed: Expected '{expected_output}', but got '{output}'"
        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12]
        expected_output = 9
        output = find_duplicate(A)
        assert output == expected_output, f"Test case 2 failed: Expected '{expected_output}', but got '{output}'"
        print("C5. Find Duplicate Number: Passed ✓")
    except AssertionError as e:
        print("C5. Find Duplicate Number: Failed ×\n Reason: ", e)
    except:
        print("C5. Find Duplicate Number: Failed ×")

# C6. Sum Odd Subarrays

def assert_C6(sum_odd_subarrays):
    try:
        INPUTS = [
        [1, 4, 2],
        [1, 3],
        [1, 4, 2, 5, 3],
        [5, 2, 0, 8, 8, 5, 2, 2, 4, 1, 4, 6, 1, 1, 6, 5, 3, 6, 4, 2],
        [3, 19, 41, 16,  3, 23, 32,  6, 18, 43,  1,  3,  1, 44, 41, 27, 45, 3, 11, 40, 45, 22, 37, 37, 21, 45, 18, 18,  2,  7, 46, 23, 21,  3]
        ]
        EXP_OUTPUTS = [
        14,
        4,
        58,
        2853,
        86304,
        ]
        assert(sum_odd_subarrays(INPUTS[0]) == EXP_OUTPUTS[0])
        assert(sum_odd_subarrays(INPUTS[1]) == EXP_OUTPUTS[1])
        assert(sum_odd_subarrays(INPUTS[2]) == EXP_OUTPUTS[2])
        assert(sum_odd_subarrays(INPUTS[3]) == EXP_OUTPUTS[3])
        assert(sum_odd_subarrays(INPUTS[4]) == EXP_OUTPUTS[4])
        print("C6. Sum Odd Subarrays: Passed ✓")
    except:
        print("C6. Sum Odd Subarrays: Failed ×")

# C7. Largest Island

def assert_C7(largest_island):
    try:
        INPUTS = [
        [[1, 0, 0, 1], [1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 1, 0]],
        [[1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1, 1], [0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 0, 0, 0]]
        ]
        EXP_OUTPUTS = [
            9,
            24
        ]
        assert(largest_island(INPUTS[0]) == EXP_OUTPUTS[0])
        assert(largest_island(INPUTS[1]) == EXP_OUTPUTS[1])
        print("C7. Largest Island: Passed ✓")
    except:
        print("C7. Largest Island: Failed ×")

# C8. Overlapping Shapes

def assert_C8(do_overlap):
    try:
        INPUTS = [
        ([(0.0, 0.0), (0.0, 2.0), (4.0, 2.0), (4.0, 0.0)], [(1.0, 0.0), (1.0, 2.0), (5.0, 2.0), (5.0, 0.0)]),
        ([(0.0, 0.0), (0.0, 2.0), (4.0, 2.0), (4.0, 0.0)], [(-4.0, 0.0), (0.5, 3.0), (-5.0, 2.0)]),
        ([(0.0, 0.0), (1.0, 1.0), (0.0, 2.0)], [(0.55, 0.5), (1.5, 0.5), (0.55, 0.0), (1.5, 0.0)]),
        ([(0.0, -1.0), (1.0, 1.0), (0.0, 2.0)], [(0.55, 0.5), (1.5, 0.5), (0.55, 0.0), (1.5, 0.0)]),
        ([(1.0, 0.3), (0.8, 0.1), (1.4, 0.2)], [(0.55, 0.5), (1.5, 0.5), (0.55, 0.0)]),
        ([(0.55, 0.5), (1.5, 0.5),(0.55, 0.0), (2, 0.0), (1.0, -1.0)], [(1, 0), (1.1, 0), (1.1, 0.1)])
        ]
        EXP_OUTPUTS = [
            True,
            False,
            False,
            True,
            True,
            True,
        ]
        assert(do_overlap(INPUTS[0][0], INPUTS[0][1]) == EXP_OUTPUTS[0])
        assert(do_overlap(INPUTS[1][0], INPUTS[1][1]) == EXP_OUTPUTS[1])
        assert(do_overlap(INPUTS[2][0], INPUTS[2][1]) == EXP_OUTPUTS[2])
        assert(do_overlap(INPUTS[3][0], INPUTS[3][1]) == EXP_OUTPUTS[3])
        assert(do_overlap(INPUTS[4][0], INPUTS[4][1]) == EXP_OUTPUTS[4])
        assert(do_overlap(INPUTS[5][0], INPUTS[5][1]) == EXP_OUTPUTS[5])
        print("C8. Overlapping Shapes: Passed ✓")
    except:
        print("C8. Overlapping Shapes: Failed ×")
        