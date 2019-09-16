#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 15:40:04 2019

Course: CS 2302 - Data Structures
Author: Brian Perez
Assignment: Lab 1 
Instructor: Diego Aguirre 
D.O.L.M.: 9/16/19 (to write this)


"""
import hashlib
 
def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig

def read_file(): 
    file = open('password_file.txt', 'r')       # opens password text file 
    users = []                                   
    for element in file.read().split('\n'):     # for loop that for each element in the file split by new line...
       users.append(element.split(','))         # appends it to the users list to create a list of lists, organized by the ','
    
    return users                                #returns the users list for later password_check function

       
     
def generator (string_list, length):    # **** Unused iteration of recursive password generation *****
    if length == -1:                    # The idea was to pass an empty list and through each generation of password digit, decrease length till finish 
        print("hi")                     #making it each combination of numbers one digit at a time till desired length 
        return string_list              # Base case, length used up and triggers end of recursive calls 
    for i in range(length):             # length times ...
        print("Length", length)
        for x in range (10):            # 0-9 would be used to place into digits 
            string_list[i]+=(str(x))    # appending number to string list 
            print ("List", string_list) # trace checks 
            string_list[i]= string_list[i][:-1] # removing the last digit to be replaced later 
    return generator(string_list, length-1)     #returns method, passing list, and length minus 1

def password_check (passwords, records):                    # passes 2 paramters, passwords list and users list (now records)
    for x in passwords :                                    # each password
        for y in range(len(records)):                       # and the length of the records so as to know how many users to check through 
            test_pass = x + (records[y][1])                         # makes z a version of the password with the salt value attached 
            if (hash_with_sha256(test_pass)) == (records[y][2]):    # hashes salted value and checks password correctness 
                print("Password found: ", x, "for", records [y][0])                # done 
    
# =============================================================================
# def gen(string_list, length):          ## Unused iteration of recursive password generation 
#     if length < 0:
#         return
#     for i in range(10):
#         gen(string_list[ln]+=str(i)), length-1)
# =============================================================================
        
        
    
        


def main():
    records = read_file() #reads file, and organizes into list of lists 
#    print(records[0][1])
    #print(generator([""], 3))
    
    #Sample passwords that would have been generated
    #*"0000" & "1000" to show not all entries are displayed, only true passwords after check 
    passwords = ["1000", "6140", "00000", "942", "6682", "2419445", "0000"]  
    password_check(passwords, records) #Checks and prints passwords 
    

main()