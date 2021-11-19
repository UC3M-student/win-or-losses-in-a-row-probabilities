
import pandas as pd
import numpy as np
import glob
from pathlib import Path

database_ = []
excl_list = []

def nba_teams_prob_excell(path_to_all_excels):
    file_list = glob.glob(path_to_all_excels + "/*xls")
    for i in file_list:
            df = pd.read_excel(i)
            matrix = np.array([[0,0],[0,0]])
            size = len(df)
            results = df.iloc[0:size,7]
            n = 0
            
            try:
                while n < size: 
                    n += 1
                    t = n - 1
                    if results[n] == "W" and results[t] == "L":
                        a = np.array([[0,1],[0,0]])
                        matrix = matrix + a
                    elif results[n] == "L" and results[t] == "W":
                        b = np.array([[0,0],[1,0]])
                        matrix = matrix + b
                    elif results[n] == results[t] == "W":
                        c = np.array([[1,0],[0,0]])
                        matrix = matrix + c
                    elif results[n] == results[t] == "L":
                        d = np.array([[0,0],[0,1]])
                        matrix = matrix + d
                    else:
                        continue 
            except KeyError:
                print("")
                
            first0_0 = matrix[0,0]/(matrix[0,0] + matrix[0,1]) 
            first0_1 = matrix[0,1]/(matrix[0,0] + matrix[0,1])
            first1_0 = matrix[1,0]/(matrix[1,0] + matrix[1,1])
            first1_1 = matrix[1,1]/(matrix[1,0] + matrix[1,1])
            matrix_probailities = np.array([[first0_0,first0_1],[first1_0,first1_1]]) #1º done
            
            df = pd.read_excel(i)
            results = df.iloc[(len(df)-1):len(df),7] #2º done
            
            global database_
            
            for a in results:
                a
            if a == "W" : 
                two_wins_in_a_row = matrix_probailities[0,0] #win the next game
                three_wins_in_a_row = matrix_probailities[0,0]**2 #win the nexr 2 games
                four_wins_in_a_row = matrix_probailities[0,0]**3
                five_wins_in_a_row = matrix_probailities[0,0]**4
                six_wins_in_a_row = matrix_probailities[0,0]**5
                seven_wins_in_a_row = matrix_probailities[0,0]**6
                eight_wins_in_a_row = matrix_probailities[0,0]**7
                nine_wins_in_a_row = matrix_probailities[0,0]**8
                ten_wins_in_a_row = matrix_probailities[0,0]**9
                
                database_ =pd.DataFrame({ "2" : [two_wins_in_a_row ],
                                        "3" : [three_wins_in_a_row],
                                        "4": [four_wins_in_a_row],
                                        "5" : [ five_wins_in_a_row],
                                        "6": [ six_wins_in_a_row],
                                        "7": [seven_wins_in_a_row],
                                        "8": [eight_wins_in_a_row],
                                        "9": [nine_wins_in_a_row],
                                        "10": [ten_wins_in_a_row]})
                
            elif a == "L":   
                two_lose_in_a_row = matrix_probailities[1,0] #win the next game
                three_lose_in_a_row = matrix_probailities[1,0]**2 #win the next two games 
                four_lose_in_a_row = matrix_probailities[1,0]**3
                five_lose_in_a_row = matrix_probailities[1,0]**4
                six_lose_in_a_row = matrix_probailities[1,0]**5
                seven_lose_in_a_row = matrix_probailities[1,0]**6
                eight_lose_in_a_row = matrix_probailities[1,0]**7
                nine_lose_in_a_row = matrix_probailities[1,0]**8
                ten_lose_in_a_row = matrix_probailities[1,0]**9
                
                database_ = pd.DataFrame({ "2" : [two_lose_in_a_row ],
                                        "3" : [three_lose_in_a_row],
                                        "4": [four_lose_in_a_row],
                                        "5" : [ five_lose_in_a_row],
                                        "6": [ six_lose_in_a_row],
                                        "7": [seven_lose_in_a_row],
                                        "8": [eight_lose_in_a_row],
                                        "9": [nine_lose_in_a_row],
                                        "10": [ten_lose_in_a_row]})
                
            
            else:
                print("error in the probability matrix")
                pass 
            
            #print(database_)
            
            v = Path(i)
            path_parts = v.parts # file path in parts
            name_of_the_team = path_parts[3]
            team_name = name_of_the_team.replace(".xls", "") #name of the team
            
            database_.index = [team_name]
            
            df = pd.DataFrame(database_)
            df.to_excel("yesir.xls")
            excl_list.append(pd.read_excel("yesir.xls"))
            excl_merged = pd.concat(excl_list,ignore_index= True)
            excl_merged.to_excel("sssss.xls", index= False) #all_data_merged
             
           
            
            
            
    
    return  
        


    
nba_teams_prob_excell(r"D:\VSCODE projects\NBA")

