--[[

Programmed by Anurag
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code SCOR_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            SCOR_LUA.lua
*  Created:             07/10/2020
*  Last Modified:       07/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
]]--
 
-- getTheTopper function finds the student name who scored max, i.e. Topper's name from the scorelist created by readScoreList function
function tablelength(T)
  local count = 0
  for _ in pairs(T) do count = count + 1 end
  return count
end
function getTheTopper(score_list)
    --Bubble sorting
    for i=2,tablelength(score_list),2 do
        for j=2,tablelength(score_list)-i,2 do
            if score_list[j] < score_list[j+2] then
                
                temp_name = score_list[j-1]
                temp_score = score_list[j]

                score_list[j-1] = score_list[j+1]
                score_list[j] = score_list[j+2]

                score_list[j+1] = temp_name
                score_list[j+2] =temp_score
            end
        end
    end

    --Showing result of the toppers
    local topper_name = {}
    topper_name[1] = score_list[1]

    for i=2,tablelength(score_list),2 do
    	if score_list[i] == score_list[i+2] then
    		table.insert(topper_name,score_list[i+1])
    	end
    	
        if score_list[i] > score_list[i+2] then
            break
        end
        
    end

    table.sort(topper_name)

    for i=1,tablelength(topper_name),1 do
    	print(topper_name[i])
    end
 
end
 
-- readScoreList function creates the scorelist table from input
function readScoreList(N)
    local scorelist={}
    
    for i=1,N
    do
    	str=io.read()
      
    	for word in string.gmatch(str,"%S+") do
    		table.insert(scorelist, word)
    	end
    end

    for i=2,tablelength(scorelist),2 do
        scorelist[i] = tonumber(scorelist[i])
    end
 
    return scorelist
end
 
-- for each case, call the readScoreList and getTheTopper functions to get the scores of students and then find the student name who scored max, i.e. Topper's name
tc = tonumber(io.read())
for i=1,tc
do
    local N=tonumber(io.read())
    score_list=readScoreList(N);
    getTheTopper(score_list)
    score_list ={}
end