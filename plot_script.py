#!/usr/bin/python3

#################################
###Project RNA folding problem###
########by Kamély Lumière########
##########M2 GENIOMHE############
###########20190541##############
#################################


###plot_script.py###

import sys
import matplotlib.pyplot as plt

def build_plot(folder_input_path):
    di_nt = ["AA", "AU", "AC", "AG", "UU", "UC", "UG", "CC", "CG", "GG"]
    
    for dnt in di_nt:
        input_file = f"{folder_input_path}/{dnt}.txt"
        output_file = f"{folder_input_path}/{dnt}_plot.png" 
        x_axis = list(range(20)) #create the graduation from 0 to 10
        y_axis = []

        with open(input_file, "r") as fichierlecture: #for each file of dint
            lines = fichierlecture.readlines() #it reads the lines that contains the lines

            for line in lines:
                score = float(line.strip()) #convert the score into float
                y_axis.append(score)  #add the score in the y axis= score axis
                
            plt.figure()
            plt.plot(x_axis, y_axis, label=f'{dnt}') #plot the curve with x and y values
            plt.xlabel('Distance Interval in Å') #name of the xaxis and y axis
            plt.ylabel('Score')
            plt.title(f'Plot of interaction profile for {dnt} with score=f(distance interval)') #title 
            plt.legend()
            
            
            plt.xticks(range(0, 21, 1)) # add the 20 in the x axis
            plt.savefig(output_file)  # Sauvegarde du graphique dans un fichier
            #plt.show()
            plt.clf()
            
            
        print(f'The plot of interaction profile for {dnt} has been successfully saved in the folder {folder_input_path} as a .png file. \n ')


###
build_plot(sys.argv[1])
#build_plot("/home/lumiere/RNA_fold/PLOT/")
            
###end of the script plot_script.py###         
            
