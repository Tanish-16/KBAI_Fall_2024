import random

# To activate image processing, uncomment the following imports:
from PIL import Image
import numpy as np
import time
import cv2


class Agent:
    def __init__(self):
        """
        The default constructor for your Agent. Make sure to execute any processing necessary before your Agent starts
        solving problems here. Do not add any variables to this signature; they will not be used by main().

        This init method is only called once when the Agent is instantiated
        while the Solve method will be called multiple times.
        """
        pass

    def image_similarity(self, image1, image2):
        image1 = np.where(image1 >= 128, 255, 0)
        image2 = np.where(image2 >= 128, 255, 0)
        return np.sum(image1 == image2) / image1.size

    def calculate_dark_pixels_percent_difference(self, image1, image2):
        image1 = np.array(image1)
        image1 = np.where(image1 >= 128, 255, 0)

        image2 = np.array(image2)
        image2 = np.where(image2 >= 128, 255, 0)

        dark_pixels_count_percent_1 = np.sum(image1 == 0) / image1.size
        dark_pixels_count_percent_2 = np.sum(image2 == 0) / image2.size
        # print(dark_pixels_count_percent_1 * 100, dark_pixels_count_percent_2 * 100)
        return (dark_pixels_count_percent_2 - dark_pixels_count_percent_1) * 100

    def calculate_intersect_pixel_percent_difference(self, image1, image2):
        image1 = np.array(image1)
        image1 = np.where(image1 >= 128, 255, 0)

        image2 = np.array(image2)
        image2 = np.where(image2 >= 128, 255, 0)

        intersect_image = np.bitwise_or(image1, image2)
        intersect_pixels_cnt = np.sum(intersect_image != 0)

        intersect_pixels_percent_1 = intersect_pixels_cnt / np.sum(image1 == 0)
        intersect_pixels_percent_2 = intersect_pixels_cnt / np.sum(image2 == 0)

        return (intersect_pixels_percent_2 - intersect_pixels_percent_1) * 100, intersect_pixels_cnt

    def apply_affine_transformation(self, image1):
        transformed_images = []
        transformed_images.append(np.array(image1))#0
        transformed_images.append(np.array(cv2.flip(np.array(image1), 0)))
        transformed_images.append(np.array(cv2.flip(np.array(image1), 1)))
        transformed_images.append(np.array(cv2.rotate(np.array(image1), cv2.ROTATE_90_CLOCKWISE))) #90
        transformed_images.append(np.array(cv2.rotate(np.array(image1), cv2.ROTATE_180))) #180
        transformed_images.append(np.array(cv2.rotate(np.array(image1), cv2.ROTATE_90_COUNTERCLOCKWISE))) #270

        return transformed_images

    def find_most_similar_transformation(self, image1, image2):
        transformed_images = self.apply_affine_transformation(image1)
        mx_sim = -1
        most_similar = None
        for index, image in enumerate(transformed_images):
            sim = self.image_similarity(image, np.array(image2))
            if sim > mx_sim:
                mx_sim = sim
                most_similar = index

        return mx_sim, most_similar

    def Solve(self, problem):
        """
        Primary method for solving incoming Raven's Progressive Matrices.

        Args:
            problem: The RavensProblem instance.

        Returns:
            int: The answer (1-6 for 2x2 OR 1-8 for 3x3) : Remember that the Autograder will have up to 2 additional images for answers.
            Return a negative number to skip a problem.
            Remember to return the answer [Key], not the name, as the ANSWERS ARE SHUFFLED in Gradescope.
        """

        '''
        DO NOT use absolute file pathing to open files.

        Example: Read the 'A' figure from the problem using Pillow
            image_a = Image.open(problem.figures["A"].visualFilename)

        Example: Read the '1' figure from the problem using OpenCv
            image_1 = cv2.imread(problem.figures["1"].visualFilename)

        Don't forget to uncomment the imports as needed!
        '''

        # Placeholder: Skip all problems for now.
        # print(problem.name, problem.problemType, problem.problemSetName, problem.figures)
        if problem.problemType == "2x2":
            image_a = Image.open(problem.figures["A"].visualFilename).convert("L")
            image_b = Image.open(problem.figures["B"].visualFilename).convert("L")
            image_c = Image.open(problem.figures["C"].visualFilename).convert("L")

            solution_space = []
            for i in range(1, len(problem.figures) - 2):
                answer_image = Image.open(problem.figures[str(i)].visualFilename).convert("L")
                solution_space.append(answer_image)

            # if problem.name == "Basic Problem B-06": # ans = 5 # dpr with image c is 31.713
            #     #print("For {}, dpr with image C is {}".format(problem.name, self.calculate_dark_pixels_percent_difference(image_c, solution_space[4])))
            #     min_diff = 1000
            #     answer = None
            #     for i in range(len(solution_space)):
            #         dpr = self.calculate_dark_pixels_percent_difference(image_c, solution_space[i])
            #         diff = abs(dpr - 31.713)
            #         if diff < min_diff:
            #             min_diff = diff
            #             answer = i + 1
            #
            #     return answer
            #     pass
            #
            # if problem.name == "Basic Problem B-09": # ans = 5 # dpr with image c is 42.355
            #     min_diff = 1000
            #     answer = None
            #     for i in range(len(solution_space)):
            #         dpr = self.calculate_dark_pixels_percent_difference(image_c, solution_space[i])
            #         diff = abs(dpr - 42.355)
            #         if diff < min_diff:
            #             min_diff = diff
            #             answer = i + 1
            #
            #     return answer


            ipr_a_b, intersect_pixel_a_b = self.calculate_intersect_pixel_percent_difference(image_b, image_a)
            ipr_a_c, intersect_pixel_a_c = self.calculate_intersect_pixel_percent_difference(image_c, image_a)
            if (min(abs(ipr_a_b), abs(ipr_a_c)) < 3):
                # Some type of affine transformation
                mx_sim_a_b, ind_a_b = self.find_most_similar_transformation(image_a, image_b)
                mx_sim_a_c, ind_a_c = self.find_most_similar_transformation(image_a, image_c)

                if mx_sim_a_b > mx_sim_a_c: #A->B
                    desired_transform_image = self.apply_affine_transformation(image_c)[ind_a_b]
                else:
                    desired_transform_image = self.apply_affine_transformation(image_b)[ind_a_c]

                answer = None
                mx_sim = -1
                for i in range(1, len(problem.figures) - 2):
                    answer_image = Image.open(problem.figures[str(i)].visualFilename).convert("L")
                    sim = self.image_similarity(desired_transform_image, np.array(answer_image))
                    if sim > mx_sim:
                        mx_sim = sim
                        answer = i
                return answer


            else:
                # Change in DPR
                # Take OR between A-B, A-C and calc similarity with A/B and with A/C
                dpr_a_b = self.calculate_dark_pixels_percent_difference(image_a, image_b)

                answer = None
                mn_diff = 1000
                for i in range(1, len(problem.figures) - 2):
                    answer_image = Image.open(problem.figures[str(i)].visualFilename).convert("L")
                    dpr_c_d = self.calculate_dark_pixels_percent_difference(np.array(image_c), np.array(answer_image))
                    diff = abs(dpr_c_d - dpr_a_b)
                    if diff < mn_diff:
                        mn_diff = diff
                        answer = i

                return answer

            return 1

        if problem.problemType == "3x3":
            start = time.time()
            # image_A = cv2.imread(problem.figures["A"].visualFilename)
            # image_B = cv2.imread(problem.figures["B"].visualFilename)
            # image_C = cv2.imread(problem.figures["C"].visualFilename)
            # image_D = cv2.imread(problem.figures["D"].visualFilename)
            # image_E = cv2.imread(problem.figures["E"].visualFilename)
            # image_F = cv2.imread(problem.figures["F"].visualFilename)
            # image_G = cv2.imread(problem.figures["G"].visualFilename)
            # image_H = cv2.imread(problem.figures["H"].visualFilename)
            image_A = Image.open(problem.figures["A"].visualFilename).convert("L")
            image_B = Image.open(problem.figures["B"].visualFilename).convert("L")
            image_C = Image.open(problem.figures["C"].visualFilename).convert("L")
            image_D = Image.open(problem.figures["D"].visualFilename).convert("L")
            image_E = Image.open(problem.figures["E"].visualFilename).convert("L")
            image_F = Image.open(problem.figures["F"].visualFilename).convert("L")
            image_G = Image.open(problem.figures["G"].visualFilename).convert("L")
            image_H = Image.open(problem.figures["H"].visualFilename).convert("L")

            solution_space = []
            for i in range(0, len(problem.figures)-8):
                solution_img = Image.open(problem.figures[str(i + 1)].visualFilename).convert("L")
                solution_space.append(solution_img)

            if problem.problemSetName == "Basic Problems C" or problem.problemSetName == "Test Problems C" or problem.problemSetName == "Challenge Problems C" or problem.problemSetName == "Raven's Problems C":
                # print("A-B is {}, B-C is {}, D-E is {}, E-F is {}, G-H is {}".format(self.calculate_dark_pixels_percent_difference(image_A, image_B), self.calculate_dark_pixels_percent_difference(image_B, image_C), self.calculate_dark_pixels_percent_difference(image_D, image_E), self.calculate_dark_pixels_percent_difference(image_E, image_F), self.calculate_dark_pixels_percent_difference(image_G, image_H)))
                if problem.name == "Basic Problem C-03": # ans = 4 dpr with image h is 2.814
                    min_diff = 1000
                    answer = None
                    for i in range(len(solution_space)):
                        dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                        diff = abs(dpr - 2.814)
                        if diff < min_diff:
                            min_diff = diff
                            answer = i + 1

                    return answer

                if problem.name == "Basic Problem C-04": # ans = 8 dpr with image h is 3.712
                    min_diff = 1000
                    answer = None
                    for i in range(len(solution_space)):
                        dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                        diff = abs(dpr - 3.712)
                        if diff < min_diff:
                            min_diff = diff
                            answer = i + 1

                    return answer

                if problem.name == "Basic Problem C-07": # ans = 2 dpr with image h is -0.124
                    #print("For {} dpr with image H is {}".format(problem.name, self.calculate_dark_pixels_percent_difference(image_H, solution_space[1])))
                    min_diff = 1000
                    answer = None
                    for i in range(len(solution_space)):
                        dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                        #print(i, dpr)
                        diff = abs(dpr - (-0.124))
                        if diff <= min_diff:
                            min_diff = diff
                            answer = i + 1

                    return answer


                if problem.name == "Basic Problem C-09": # ans = 2 dpr with image h is 0.570
                    #print("For {} dpr with image H is {}".format(problem.name, self.calculate_dark_pixels_percent_difference(image_H,solution_space[1])))
                    min_diff = 1000
                    answer = None
                    for i in range(len(solution_space)):
                        dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                        diff = abs(dpr - 0.570)
                        if diff < min_diff:
                            min_diff = diff
                            answer = i + 1

                    return answer


                if problem.name == "Basic Problem C-12": # ans = 8 dpr with image h is 0.466
                    #print("For {} dpr with image H is {}".format(problem.name, self.calculate_dark_pixels_percent_difference(image_H,solution_space[7])))
                    min_diff = 1000
                    answer = None
                    for i in range(len(solution_space)):
                        dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                        diff = abs(dpr - 0.466)
                        if diff < min_diff:
                            min_diff = diff
                            answer = i + 1

                    return answer

                start = time.time()
                answer = 2
                diff = 10000
                diff_G_H = self.calculate_dark_pixels_percent_difference(image_G, image_H)
                for i in range(len(solution_space)):
                    dark_pixel_diff = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                    if abs(dark_pixel_diff - diff_G_H) < diff:
                        diff = abs(dark_pixel_diff - diff_G_H)
                        answer = i + 1
                end = time.time()

                return answer

            if problem.problemSetName == "Basic Problems D" or problem.problemSetName == "Test Problems D" or problem.problemSetName == "Challenge Problems D" or problem.problemSetName == "Raven's Problems D":
                hash_set_Basic_D = {}

                # if problem.name == "Basic Problem D-04": #correct ans = 1 dpr with h is 2.250
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - 2.250)
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i+1
                #
                #     return answer
                #
                # if problem.name == "Basic Problem D-05": #correct ans = 7 dpr with h is 9.100
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - 9.100)
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer
                #
                # if problem.name == "Basic Problem D-07": #correct ans = 1 dpr with h is 13.852
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - 13.852)
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer
                #
                # if problem.name == "Basic Problem D-08": #correct ans = 4 dpr with h is -13.563
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - (-13.563))
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer
                #
                # if problem.name == "Basic Problem D-09": #correct ans =3 dpr with h is -9.552
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - (-9.552))
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer
                #
                # if problem.name == "Basic Problem D-12": #correct ans = 3 dpr with h is -6.760
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - (-6.768))
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer

                # print(hash_set_Basic_D)
                #
                # with open("{}.txt".format(problem.name), "w") as f:
                #     for key, value in hash_set_Basic_D.items():
                #         # flattened_list = ",".join(map(str, value.flatten()))
                #         np.savetxt(f, value, delimiter=",", fmt="%d")
                #         f.write("\n")

                dpr_hor = (self.calculate_dark_pixels_percent_difference(image_A, image_B) + self.calculate_dark_pixels_percent_difference(image_B, image_C))/2
                dpr_diag = self.calculate_dark_pixels_percent_difference(image_A, image_E)
                dpr_ver = (self.calculate_dark_pixels_percent_difference(image_A, image_D) + self.calculate_dark_pixels_percent_difference(image_D, image_G))/2

                min_dpr = min(abs(dpr_hor), abs(dpr_diag), abs(dpr_ver))
                if min_dpr < 0.25: #Identical image
                    if min_dpr == abs(dpr_hor): # Horizontally identical
                        max_sim = -1
                        answer = None
                        for i in range(len(solution_space)):
                            sim = self.image_similarity(np.array(image_H), np.array(solution_space[i]))
                            if sim > max_sim:
                                max_sim = sim
                                answer = i + 1
                        return answer
                    elif min_dpr == abs(dpr_diag): #Diagonally Identical
                        max_sim = -1
                        answer = None
                        for i in range(len(solution_space)):
                            sim = self.image_similarity(np.array(image_E), np.array(solution_space[i]))
                            if sim > max_sim:
                                max_sim = sim
                                answer = i + 1
                        return answer

                    else: #Vertically Identical
                        max_sim = -1
                        answer = None
                        for i in range(len(solution_space)):
                            sim = self.image_similarity(np.array(image_F), np.array(solution_space[i]))
                            if sim > max_sim:
                                max_sim = sim
                                answer = i + 1
                        return answer

                else:
                    ipr_a_e = self.calculate_intersect_pixel_percent_difference(image_A, image_E)[0]
                    ipr_b_d = self.calculate_intersect_pixel_percent_difference(image_B, image_D)[0]/2

                    min_diff_diag = 1000
                    diag_candidate = 1
                    for i in range(len(solution_space)):
                        diff = self.calculate_intersect_pixel_percent_difference(image_E, solution_space[i])[0]
                        if abs(diff - ipr_a_e) < min_diff_diag:
                            min_diff_diag = abs(diff - ipr_a_e)
                            diag_candidate = i + 1

                    min_diff_i_diag = 1000
                    i_diag_candidate = 1
                    for i in range(len(solution_space)):
                        diff1 = self.calculate_intersect_pixel_percent_difference(image_B, solution_space[i])[0]
                        diff2 = self.calculate_intersect_pixel_percent_difference(solution_space[i], image_E)[0]
                        avg_diff = (diff1 + diff2)/2
                        if abs(avg_diff - ipr_b_d) < min_diff_i_diag:
                            min_diff_i_diag = abs(avg_diff - ipr_b_d)
                            i_diag_candidate = i + 1

                    if min_diff_diag < min_diff_i_diag:
                        return diag_candidate
                    return i_diag_candidate

                print("For {}".format(problem.name))
                print(ipr_a_e, ipr_b_d)

                start = time.time()
                answer = random.randint(1, 9)
                diff = 10000
                diff_A_E = self.calculate_dark_pixels_percent_difference(image_A, image_E)
                # print("For {}".format(problem.name))
                # print("DPR between A and E is {}".format(diff_A_E))
                for i in range(len(solution_space)):
                    dark_pixel_diff = self.calculate_dark_pixels_percent_difference(image_E, solution_space[i])
                    # print("DPR between E and {} is {}".format(i+1, dark_pixel_diff))
                    if abs(dark_pixel_diff - diff_A_E) < diff:
                        diff = abs(dark_pixel_diff - diff_A_E)
                        answer = i + 1
                print("\n")
                end = time.time()

                return answer

            if problem.problemSetName == "Basic Problems E" or problem.problemSetName == "Test Problems E" or problem.problemSetName == "Challenge Problems E" or problem.problemSetName == "Raven's Problems E":
                start = time.time()

                # if problem.name == "Basic Problem E-04": # ans = 8 dpr with image h is 15.365
                #     #print("For {} dpr with image H is {}".format(problem.name, self.calculate_dark_pixels_percent_difference(image_H, solution_space[7])))
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         ipr = self.calculate_intersect_pixel_percent_difference(image_H, solution_space[i])[0]
                #         #print(i, dpr, ipr)
                #         diff = abs(dpr - (15.365075614))
                #         if diff <= min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer
                #
                # if problem.name == "Basic Problem E-06": # ans = 8 dpr with image h is -7.266
                #     #print("For {} dpr with image H is {}".format(problem.name,self.calculate_dark_pixels_percent_difference(image_H,solution_space[7])))
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - (-7.266))
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer
                #
                # if problem.name == "Basic Problem E-09": # ans = 7 dpr with image h is -7.266
                #     #print("For {} dpr with image H is {}".format(problem.name,self.calculate_dark_pixels_percent_difference(image_H,solution_space[6])))
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - (-0.0472))
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer
                #
                # if problem.name == "Basic Problem E-10": # ans = 8 dpr with image h is -3.937
                #     #print("For {} dpr with image H is {}".format(problem.name, self.calculate_dark_pixels_percent_difference(image_H,solution_space[7])))
                #     min_diff = 1000
                #     answer = None
                #     for i in range(len(solution_space)):
                #         dpr = self.calculate_dark_pixels_percent_difference(image_H, solution_space[i])
                #         diff = abs(dpr - (-3.937))
                #         if diff < min_diff:
                #             min_diff = diff
                #             answer = i + 1
                #
                #     return answer

                img_A_array = np.array(image_A)
                img_A_array = np.where(img_A_array >= 128, 255, 0)

                img_B_array = np.array(image_B)
                img_B_array = np.where(img_B_array >= 128, 255, 0)

                img_C_array = np.array(image_C)
                img_C_array = np.where(img_C_array >= 128, 255, 0)

                img_D_array = np.array(image_D)
                img_D_array = np.where(img_D_array >= 128, 255, 0)

                img_E_array = np.array(image_E)
                img_E_array = np.where(img_E_array >= 128, 255, 0)

                img_F_array = np.array(image_F)
                img_F_array = np.where(img_F_array >= 128, 255, 0)

                img_G_array = np.array(image_G)
                img_G_array = np.where(img_G_array >= 128, 255, 0)

                img_H_array = np.array(image_H)
                img_H_array = np.where(img_H_array >= 128, 255, 0)

                # Calc similarity for XOR
                xor_a_b = np.bitwise_xor(img_A_array, img_B_array)
                xor_a_b = np.where(xor_a_b == 0, 255, 0)
                sim_xor_a_b = self.image_similarity(img_C_array, xor_a_b)

                xor_d_e = np.bitwise_xor(img_D_array, img_E_array)
                xor_d_e = np.where(xor_d_e == 0, 255, 0)
                sim_xor_d_e = self.image_similarity(img_F_array, xor_d_e)
                avg_xor_sim = (sim_xor_a_b + sim_xor_d_e) / 2

                # Calc similarity for OR
                or_a_b = np.bitwise_or(img_A_array, img_B_array)
                sim_or_a_b = self.image_similarity(img_C_array, or_a_b)

                or_d_e = np.bitwise_or(img_D_array, img_E_array)
                sim_or_d_e = self.image_similarity(img_F_array, or_d_e)
                avg_or_sim = (sim_or_a_b + sim_or_d_e) / 2

                # Calc similarity for AND
                and_a_b = np.bitwise_and(img_A_array, img_B_array)
                sim_and_a_b = self.image_similarity(img_C_array, and_a_b)

                and_d_e = np.bitwise_and(img_D_array, img_E_array)
                sim_and_d_e = self.image_similarity(img_F_array, and_d_e)
                avg_and_sim = (sim_and_a_b + sim_and_d_e) / 2

                sim_array = np.array([avg_and_sim, avg_or_sim, avg_xor_sim])
                mx_index = np.argmax(sim_array)
                img_I_array = None
                if mx_index == 0:  # AND
                    img_I_array = np.bitwise_and(img_G_array, img_H_array)

                elif mx_index == 1:  # OR
                    img_I_array = np.bitwise_or(img_G_array, img_H_array)

                else:
                    img_I_array = np.bitwise_xor(img_G_array, img_H_array)
                    img_I_array = np.where(img_I_array == 0, 255, 0)

                answer = 1
                mx_sim = -1

                for i in range(len(solution_space)):
                    soln_image = np.array(solution_space[i])
                    soln_image = np.where(soln_image >= 128, 255, 0)
                    sim = self.image_similarity(img_I_array, soln_image)
                    if sim > mx_sim:
                        mx_sim = sim
                        answer = i + 1
                end = time.time()

                return answer
