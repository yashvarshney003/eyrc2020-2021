--[[
*****************************************************************************************
*
*
*  This script is code stub for CodeChef problem code INV_LUA
*  under contest PYLT20TS in Task 0 of Nirikshak Bot (NB) Theme (eYRC 2020-21).
*
*  Filename:            INV_LUA.lua
*  Created:             07/10/2020
*  Last Modified:       07/10/2020
*  Author:              e-Yantra Team
*
*****************************************************************************************
]]--
 
-- manageInventory function to add, update / delete items to / from the Inventory
function manageInventory()
    -- reading total Items N
    N = tonumber(io.read())
    local L = {} --list of items

    for i=1,N,1 do
        str = io.read()

        local temp = {}
        for word in string.gmatch(str,"%S+") do
            table.insert(temp,word)
        end

        item_name = temp[1]
        item_quantity = tonumber(temp[2])

        table.insert(L,item_name)
        table.insert(L,item_quantity)

        --[[BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
        for item_name in string.gmatch(str,"%a+") do
            table.insert(L,item_name)
        end

        for item_quantity in string.gmatch(str,"%d+") do
            item_quantity = tonumber(item_quantity)
            table.insert(L, item_quantity)
        end
        BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB]]--
    end
 
 
    -- reading total M operations to perform
    M = tonumber(io.read())
    for i=1,M,1 do
        str = io.read()
        temp = {} --temp table to store the data to make program small

        for word in string.gmatch(str,"%S+") do
            table.insert(temp, word)
        end

        operation_name = temp[1]
        item_name = temp[2]
        item_quantity = tonumber(temp[3])

        flag_notfound = 1

        for i=1,#L,2 do
            if L[i] == item_name then

                flag_notfound = 0
                
                if operation_name == "ADD" then
                L[i+1] = L[i+1] + item_quantity
                print("UPDATED Item "..item_name)
                end

                if operation_name == "DELETE" then
                    if L[i+1] < item_quantity then
                        print("Item "..item_name.." could not be DELETED")
                    else
                        L[i+1] = L[i+1] - item_quantity
                        print("DELETED item "..item_name)
                    end
                end
            end
        end
        -- add and delete condition also here
        if flag_notfound == 1 then
            i = #L
            if operation_name == "ADD" then
                L[i+1] = item_name
                L[i+2] = item_quantity
                print("ADDED Item "..item_name)
            end
            if operation_name == "DELETE" then
                print("Item "..item_name.." does not exist")
            end

        end

            
    end
 
    --[[printing table
    for i=1,#L,1 do
        print(i.." >>item>> "..L[i])
    end]]--

    -- calculate the sum of items
    local sum = 0
    for i=2,#L,2 do
        sum = sum + L[i]
        --print(i.."-->Sum-->"..sum)
    end 
 
    print(sum)

end
 
-- for each case, call the manageInventory function to add, update / delete items to / from the Inventory

tc = tonumber(io.read())
i = 0
while i < tc do
    manageInventory()
    i = i + 1
end