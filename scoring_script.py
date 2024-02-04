#!/usr/bin/python3

#################################
###Project RNA folding problem###
########by Kamély Lumière########
##########M2 GENIOMHE############
###########20190541##############
#################################


###scoring_script.py###

#script to comptute the Gibbs free energy of ONE input pdb file by summing all the score calculated from the previous score obtain of each dint from train.py script.

import sys
from training_script import download_list_pdb, interatomic_distance #to avoid to copy paste the function download_list_pdb...


#path to the list_test_pdb with the uniqu pdb file for this part
#list_pdb_file = "/home/lumiere/RNA_fold/SCORING/list_test_pdb.txt" #here the list has only one id of pdb...

#path where the pdb file downloaded will be stored
#folder_path = "/home/lumiere/RNA_fold/SCORING/"



def scoring (path_to_file_pdb_dist, path_to_files_scores_dint):

    with open (f'{path_to_file_pdb_dist[:-4]}_dist.txt', "r") as fichierlecture: #open the file with the IAD coputed for the pdb
    
        col1=[] #dinucleotide
        col2=[] #IAD
        
        #create 2 list: one for dint and the second one to store the IAD
        for line in fichierlecture:
            all_lines=line.split("\t")
            col1.append(all_lines[0]) #col1 : list of AA, AU...
            col2.append(float(all_lines[1])) #col2: list of IAD float
            
        score_new_pdb=[] #list of the score of the pdb file according to the dint .txt files
        list_score_pdb=[]   
        di_nt=["AA","AU","AC","AG","UU","UC","UG","CC","CG","GG"] #10 name of the score for the dint
         
        for i in range(len(col1)):
            DT=col1[i].strip() # otherwise it reverse all the time..
           
            if (DT not in di_nt): #if the dint is not in the same "order" that in the list it will reverse to find the corresponding file
                col1[i]= DT[::-1].strip()
         
            else:
                col1[i]=DT
          
            with open (f'{path_to_files_scores_dint}{col1[i]}.txt', "r") as fichierlecture: #it opens the file with the score for the dint corresponding
            
                
                score_dint=[]
                
                for line in fichierlecture:
                    all_lines=line.split("\n")
                    score_dint.append(all_lines[0]) # the score of each ligne is appended to the list
                 
                #assign a score to the IAD according the the dint file.txt
                if (col2[i]<1):
                    score_new_pdb.append(score_dint[0])
                    
                elif (col2[i]>=1 and col2[i] <2):
                    score_new_pdb.append(score_dint[1])
                    
                elif (col2[i]>=2 and col2[i]<3):
                    score_new_pdb.append(score_dint[2])
                    
                elif (col2[i]>=3 and col2[i]<4):
                    score_new_pdb.append(score_dint[3])
                    
                elif (col2[i]>=4 and col2[i]<5):
                    score_new_pdb.append(score_dint[4])
                    
                elif (col2[i]>=5 and col2[i]<6):
                    score_new_pdb.append(score_dint[5])
                   
                elif(col2[i]>=6 and col2[i] <7):
                    score_new_pdb.append(score_dint[6])
                    
                elif (col2[i]>=7 and col2[i]<8):
                    score_new_pdb.append(score_dint[7])
                    
                elif (col2[i]>=8 and col2[i]<9):
                    score_new_pdb.append(score_dint[8])
                    
                elif (col2[i]>=9 and col2[i]<10):
                    score_new_pdb.append(score_dint[9])
                    
                elif (col2[i]>=10 and col2[i]<11):
                    score_new_pdb.append(score_dint[10])
                    
                elif (col2[i]>=11 and col2[i]<12):
                    score_new_pdb.append(score_dint[11])
                 
                elif (col2[i]>=12 and col2[i]<13):
                    score_new_pdb.append(score_dint[12])
                    
                elif (col2[i]>=13 and col2[i]<14):
                    score_new_pdb.append(score_dint[13])
                    
                elif (col2[i]>=14 and col2[i]<15):
                    score_new_pdb.append(score_dint[14])
                    
                elif (col2[i]>=15 and col2[i]<16):
                    score_new_pdb.append(score_dint[15])
                    
                elif (col2[i]>=16 and col2[i]<17):
                    score_new_pdb.append(score_dint[16]) 
                    
                elif (col2[i]>=17 and col2[i]<18):
                    score_new_pdb.append(score_dint[17])
                    
                elif (col2[i]>=18 and col2[i]<19):
                    score_new_pdb.append(score_dint[18]) 
                    
                else:
                    score_new_pdb.append(score_dint[19]) 
                    
                
              
            with open("score_without_interpolation_for_plot.txt", "w") as fichierecriture: #file with the score associated to the IAD and based on the score for AA.txt, AU.txt ...
                for i in range (len(score_new_pdb)):
                    #print(i)
                    fichierecriture.write(str(col2[i])+"\t"+score_new_pdb[i]+"\n")
                    
                
                
                    
            with open("score_without_interpolation.txt", "w") as fichierecriture: #file with the score associated to the IAD and based on the score for AA.txt, AU.txt ...
                for i in range (len(score_new_pdb)):
                    #print(i)
                    fichierecriture.write(score_new_pdb[i]+"\n")
          
### with interpolation

#def scoring_with_interpolation (path_to_file_pdb_dist, path_to_files_scores_dint):

  ##no time##
  
  
  

#function to calculate the estimated Gibbs free energy by summing all the score                  
def calculation_GFE_estimation (input_file_score_pdb): 

    gibbs_estimation=0 # estimated Gibbs free energy initialize to 0
    
    
    with open (f'{input_file_score_pdb}', "r") as fichierlecture:
    
        for line in fichierlecture :
            score=float(line.strip())
            
            gibbs_estimation+=score
            
        print(f'The estimated Gibbs free energy for the pdb file is {gibbs_estimation}.') #print the result
    

###        
#1/ Download the pdb file form a list that have on pdb id            
download_list_pdb(sys.argv[1], sys.argv[2]) #we downloaded the pdb file 2O3Y.pdb

#2/ Compute the IAD
interatomic_distance (sys.argv[2]) #compute the IAD for this pdb
#print(len(sys.argv))  

# 3/ Calculate the scoring without interpolation       
scoring(sys.argv[3], sys.argv[4])

#4/ Estimate the Gibbs free energy
calculation_GFE_estimation(sys.argv[5])

###end of the script###

