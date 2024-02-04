#!/usr/bin/python3

#################################
###Project RNA folding problem###
########by Kamély Lumière########
##########M2 GENIOMHE############
###########20190541##############
#################################


###training_script.py###


#librairies

import sys
import requests
import os
import math #for the formula with sqrt,abs
from math import log #for the logarithm in the formula of the score

'''function to download PDB files from a list containing RNA identifiers 
from the RCSB database and store them directly in a folder to have the training set input/
list_pdb_path is the path where you have your list of id of pdb file and folder_pdb_path 
is the path where you want to store all your pdb file once its downloaded'''

def download_list_pdb(list_pdb_path,folder_pdb_path):

    with open (list_pdb_path,"r") as fichierlecture: #read the train_pdb_list.txt file: each line is an id of a pdf file

        id_pdb=[ligne.strip() for ligne in fichierlecture] #put all the ids in a list id_pdb
    
    for id in id_pdb:
    
        url = f"https://files.rcsb.org/download/{id}.pdb"
        os.system(f"wget {url}") #download the pdb file of the corresponding id
    
        pdb_downloaded = f"{id}.pdb" #name of the file downloaded
        destination_path = os.path.join(folder_pdb_path, f"{id}.pdb") 
        os.rename(pdb_downloaded, destination_path)  #move the pdb downloaded to the right folder
        print(f"Downloaded {id}.pdb and moved to {folder_pdb_path}")
        
    print(f"All the pdb files for the trainset are downloaded in the folder {folder_pdb_path} \n")


#function to compute the IAD (interatomic dist) between two residus that are separated by at least 4 nt and are in the same chain in the pdb file downloaded and stored int the file training_pdb_files
def interatomic_distance(folder_pdb):

    list_pdb_files = [f for f in os.listdir(folder_pdb) if f.endswith(".pdb")]  #store all the pdb file in a list
    
    for pdb_file in list_pdb_files:
        pdb_file_path=os.path.join(folder_pdb,pdb_file)
        pdb_file_output=f"{folder_pdb}{pdb_file[:-4]}.txt" #outputs will be named {pdb_id}.txt= file with only lines with ATOM and C3'
        pdb_file_output_dist=f"{folder_pdb}{pdb_file[:-4]}_dist.txt" #output with the dist computed will be names {pdb_id}_dist.txt
        
        with open(pdb_file_path, "r") as fichierlecture:
        
            lines=fichierlecture.readlines()
            
            all_lines=[]
            
            for line in lines:
                if (line[0:4]=="ATOM" and line[13:16]=="C3'"): #select only line with ATOM and C3'
                    one_line=[
                    line[0:4].strip(), #col1 with "ATOM"
                    line[7:11].strip(), #col2 with the number of the atom
                    line[13:16].strip(), #col3 with the name of the atom=> here it will be C3' for all lines
                    line[19:20].strip(), #col4 with the nucleotide of which the atome belongs to
                    line[21:22].strip(), #col5 with the name of the polypeptidique chain
                    line[23:26].strip(), #col6 with the number of the nucleotide in the rna (no need)
                    line[31:38].strip(), #col7 with the coordinate x of the atom
                    line[39:46].strip(), #col8 with the coordinate y of the atom
                    line[47:54].strip(), #col9 with the coordinate z of the atom
                    line[55:60].strip(), #col10 with the occupancy factor (no need)
                    line[61:66].strip(), #col11 with the temperature factor (no need)
                    line[77:78].strip(), #col12 with the chemical element of the atom (no need)
                    ]
                    all_lines.append(one_line)
                    
                    
            #to convert col2 cols 2,6,7,8,9,10,11 into int or float
            for i in range(len(all_lines)):
                for j in range(len(all_lines[i])):
                    all_lines[i][1]=int(all_lines[i][1])
                    all_lines[i][5]=int(all_lines[i][5])
                    all_lines[i][6]=float(all_lines[i][6])
                    all_lines[i][7]=float(all_lines[i][7])
                    all_lines[i][8]=float(all_lines[i][8])
                    all_lines[i][9]=float(all_lines[i][9])
                    all_lines[i][10]=float(all_lines[i][10])
                    
                
            with open (pdb_file_output,"w") as fichierecriture: #stores the line ATOM, C3' in a file (optionnal)->we don't care but to make sure that it filter correctly
                for line in all_lines:
                    line = map(str, line) #pour avoir str a la place de int
                    fichierecriture.write('\t'.join(line)+ "\n")
                
                with open (pdb_file_output_dist,"w") as fichierecriture: #stores the computed interatomic distance in a file
                    #fichierecriture.write("dinucleotide"+"\t"+"IAD" +"\n")
                    for i in range(len(all_lines)):
         
                        for j in range(i+1,len(all_lines)): #i+1 to avoid the repetition
                        
                        #Check if the two residu are in the same chain and there are at least 4 residus seprarating them     
                            if(( all_lines[i][4]==all_lines[j][4] and abs(all_lines[i][5] - all_lines[j][5])>=4)): 
                                
                                
                                #Definition of the coordinates: xa, xb, ya, yb, za, zb
                                xa = all_lines[i][6]
                                xb = all_lines[j][6]
                                ya = all_lines[i][7]
                                yb = all_lines[j][7]
                                za = all_lines[i][8]
                                zb = all_lines[j][8]
 
                                #Formula of the interatomic distance
                                inter_atom_dist = math.sqrt((xa - xb)**2 + (ya - yb)**2 + (za - zb)**2)
                            
                                #Print only if the IAD <=20: threshold for the distance
                                if (inter_atom_dist <=20):
                                    fichierecriture.write(
                                ##test to display the nt and IAD
                                ##f"{all_lines[i][3]}/{all_lines[j][3]}|{all_lines[i][4]} => IAD: {inter_atom_dist:.1f}\n") # a decommenter
                                #f"{all_lines[i][5]}/{all_lines[j][5]}|{all_lines[i][4]}:{all_lines[j][4]} => IAD: {inter_atom_dist:.1f}\n") #useful to test
                                    f"{all_lines[i][3]}{all_lines[j][3]} \t {inter_atom_dist:.1f}\n") #useful to test
                                ##test to display the posititon of the residu and IAD
                                #f"{all_lines[i][3]}:{all_lines[j][3]}|{all_lines[i][4]} => IAD: {inter_atom_dist}\n")
                                #f"{all_lines[i][3]}{all_lines[j][3]} \t {inter_atom_dist:.1f}\n")

    print(f"All the IAD for each pdb has been computed in  the folder {folder_pdb} in a _dist.txt file \n")

#function to concatenate all the file dis.txt in order to have only one file with all the dint int he fist column and the IAD in the second column
def concatene_trainset(fold_path, name_output_file):

    #path of the output file where all the IAD computed in each pdf file will be stored
    all_dist_file = f"{fold_path}{name_output_file}.txt"

    #write in the output file
    with open(all_dist_file, "w") as fichierecriture:
    
        #iterate throught all the file in the folder
        for file in os.listdir(fold_path):
        
            #check if the file end with "dist.txt"
            if file.endswith("dist.txt"):
                
                #read the file and wrote it in the output
                with open(os.path.join(fold_path, file), "r") as fichierlecture:
                    
                    fichierecriture.write(fichierlecture.read())   
                    
    print(f'All the IAD are stored in the unique file in the folder {all_dist_file} \n')                    
#function to compute the score using the observed proba and the ref freq                    
def frequencies_and_scores(trainset_dist_path, score_output_path):
    
    
    
    ##for the observed probability##
    
    nij_r={} #dictionnary of all the counters that take account the dint and the dist
    nij={} #dictionnary with all the counters that take account only the dint= Nij in the formula  
    
    with open(f'{trainset_dist_path}trainset_dist.txt',"r") as fichierlecture:
    
    
        lines=fichierlecture.readlines()
        all_lines=[]
        
        ##to create the 200 counters
        dist=[i for i in range (0,20)] #20 distances (0 à20)
        di_nt=["AA","AU","AC","AG","UU","UC","UG","CC","CG","GG"] #10 possibilities of di-nucleotides
        
        ## ce dictionnaire as des clées qui correspondent à AA_0,AA_1, AA_2,..,AA_20, GG_19   et des valeurs correspondant au nb de fois qu'on retrouve ce dint à la distance r = les Nij(r)
        
        for d in dist:
            for nt in di_nt:
                cpt_name=f'{nt}_{d}'.strip() #name the counter with the di_nt and the dist
                nij_r[cpt_name]=0 #initialize them to 0
        
        #nij_r['reste_a_10']=0  a supprimer       
        for nt in di_nt:
            cpt_name=f'{nt}'
            nij[cpt_name]=0 #initialize them to 0
                    
        
        tot_iad=0 #count the total nb of interatomic dist for the calculation of ref freq
        
        for line in lines:
            
            all_lines=line.strip().split("\t")
            DT=all_lines[0].strip() #the first element of the line is the dint
            D=float(all_lines[1]) #the 2nd element of the line is the IAD (interatomic dist) , I removed the header because issu when concatenate | convert into a float to compare to value for different intervals
            
          
            if (DT not in nij): # if the dint is not in the dico (it means that the dint is reverse AG/GA) so we have to reverse it to incremente the value of the dico key
                
                DT=DT[::-1] #reverse it
            
            else:
                DT=DT #do nothing
            tot_iad+=1    
          
            nij[DT]+=1 #for each line in the file with all de IAD, we increases the corresponding Nij
            
            ## different interval of distance from 1 to 20, for 0 cf last else
            if(D>=1 and D<2): #2nd line of the output file with the 20 score: 1rst line interval of IAD such as IAD<1 
                nij_r[f'{DT}_1']+=1 #the counter withe the dint and the given dist is incremented to 1= 2nd line
                    
            elif(D>=2 and D<3):#3rd line
                nij_r[f'{DT}_2']+=1
                    
            elif(D>=3 and D<4):#4rth line
                nij_r[f'{DT}_3']+=1 
                
            elif(D>=4 and D<5): #5th line
                nij_r[f'{DT}_4']+=1
                    
            elif(D>=5 and D<6): #6th line
                nij_r[f'{DT}_5']+=1
                    
            elif(D>=6 and D<7): #7th line 
                nij_r[f'{DT}_6']+=1
                    
            elif(D>=7 and D<8): #8th line
                nij_r[f'{DT}_7']+=1
                    
            elif(D>=8 and D<9): #9th line
                nij_r[f'{DT}_8']+=1  
                       
            elif(D>=9 and D<10): #10th line
                nij_r[f'{DT}_9']+=1
                    
            elif(D>=10 and D<11): #11th line
                nij_r[f'{DT}_10']+=1
                    
            elif(D>=11 and D<12): #12th line
                nij_r[f'{DT}_11']+=1
                    
            elif(D>=12 and D<13): #13th line
                nij_r[f'{DT}_12']+=1
                    
            elif(D>=13 and D<14): #13th line
                nij_r[f'{DT}_13']+=1
                    
            elif(D>=14 and D<15): #14th line
                nij_r[f'{DT}_14']+=1
                    
            elif(D>=15 and D<16): #15th line
                nij_r[f'{DT}_15']+=1
                    
            elif(D>=16 and D<17): #16th line
                nij_r[f'{DT}_16']+=1
                    
            elif(D>=17 and D<18): #18th line
                nij_r[f'{DT}_17']+=1
                    
            elif(D>=18 and D<19): #19th line
                nij_r[f'{DT}_18']+=1
                    
            elif(D>=19 and D<=20): #20th line
                nij_r[f'{DT}_19']+=1
           
            else:
            
                nij_r[f'{DT}_0']=nij_r[f'{DT}_0'] #lines that have a dist to 0 Angström or dont' have a dist in the above intervals wil be set to 0 but then il all the cases the score will be 0 for these cases = 1rst line of the score file
    
   
    ###to compute the reference frequencies: dint are indistinct###  
   
        nxx_r={} #dico that contains all the nxx_1, nxx_2, nx_21
        for d in dist:
            cpt_name=f'nxx_{d}'  
            nxx_r[cpt_name]=0
            
      
        for key, value in nij_r.items():
            for d in dist:
                if key.endswith(f'_{d}'):
                    nxx_r[f'nxx_{d}']+=value
     
        nxx=tot_iad # the nb of the total interatomic dist in the concatenated file= nxx
    
        #store the 20 score ina file for each dint
        for dnt in di_nt:
        
            score_output=f"{score_output_path}{dnt}.txt" # 10 output (10 dint) with the the 20 scores
            
            with open(score_output,"w") as fichierecriture:
            
            
                scores={}
                scores[f'scores_0']=10
                for i in range(1,20):
            
                    line=f'scores_{i}'
                
                    
                    ##note: Instead of calculate separatelely the obs freq, the ref freq using other loops etc : I directly calculate the score because of the nb of dictionaries used and the time....
                    
                    #check if one of the term in the formula is not egal to 0 because log(0) forbidden
                    
                    if (nxx_r[f'nxx_{i}'] !=0 and nij_r[f'{dnt}_{i}'] and nij[f'{dnt}']) : #nxx !=0
                        scores[line]= -log( (nij_r[f'{dnt}_{i}'] / nij[f'{dnt}']) / (nxx_r[f'nxx_{i}'] / nxx) )
                    
                    else:
                
                        scores[line]=10 # if the dint is not observed at the dist i or the dist =0, the score willbe arbitrarily set to 10
                
                
                for key, value in scores.items():
                    fichierecriture.write(f"{value}\n")
                
    print(f"All the scores were stored in a unique file in the folder {score_output[:-6]} in .txt file \n")
    
###    
      
#1/ Download the pdb file from the train_pdb_list.txt from the RCSB db           

download_list_pdb(sys.argv[1],sys.argv[2])
##download_list_pdb("/home/lumiere/RNA_fold/TRAIN/train_pdb_list.txt","/home/lumiere/RNA_fold/TRAIN/training_pdb_files/")

#2/ Extract the lines needed to compute the IAD in all the pdb file and store in the same folder  
  
interatomic_distance(sys.argv[2])
##interatomic_distance("/home/lumiere/RNA_fold/TRAIN/training_pdb_files/")

#3/ Concatenate all the file dist.txt to have all the IAD in the same file and store it in the same folder to use it after..
if (len(sys.argv)<=5):
    concatene_trainset(sys.argv[2], sys.argv[4])
#concatene_trainset("/home/lumiere/RNA_fold/TRAIN/training_pdb_files")

#4/ Calculation of the score for each di nucleotide (AA, AU,.., GG) and store it the the folder PLOT/

    frequencies_and_scores(sys.argv[2], sys.argv[3])
#frequencies_and_scores("/home/lumiere/RNA_fold/TRAIN/training_pdb_files/trainset_dist.txt")

#print("LEN sys argv:",len(sys.argv))

###end of the script train_script.py###
