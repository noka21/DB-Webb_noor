#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Some various ways of saying Hello World in Python.
"""

# Print out Hello World
print("Just saying Hello World")

# Assign the string Hello World to a variable and print it out
str1 = "Hello World in a variable"
print(str1)

# Combine two strings and print them out
str2 = "Hello World!"
str3 = "Its a nice day today!"
print(str2 + " " + str3)

# Combine string and values
a = 40
b = 2
c = a + b
str4 = "Summan är " + str(c) + "."
print(str2 + " " + str4)

# Print out my name
name = "Noor"
print("Mitt namn är " + name)

# Print out ASCII art
# Use prefix r for a raw string avoiding validation
noor = r"""

                         ______                     
 _________        .---"""      r"""---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  Little Error: | |             
|:______B:|      | |                | |             
|:______B:|      | | dbwebb course  | |             
|         |      | |                | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
    fsc        .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:


                   Art by Marcin Glanskis
"""

print(noor)

noor1 = r"""

           ,.         ,·´'; '         , ·. ,.-·~·.,   ‘           , ·. ,.-·~·.,   ‘         ,. -  .,              
      ;'´*´ ,'\       ,'  ';'\°       /  ·'´,.-·-.,   `,'‚          /  ·'´,.-·-.,   `,'‚       ,' ,. -  .,  `' ·,       
      ;    ';::\      ;  ;::'\      /  .'´\:::::::'\   '\ °       /  .'´\:::::::'\   '\ °     '; '·~;:::::'`,   ';\    
     ;      '\;'      ;  ;:::;   ,·'  ,'::::\:;:-·-:';  ';\‚    ,·'  ,'::::\:;:-·-:';  ';\‚      ;   ,':\::;:´  .·´::\'  
    ,'  ,'`\   \      ;  ;:::;  ;.   ';:::;´       ,'  ,':'\‚  ;.   ';:::;´       ,'  ,':'\‚     ;  ·'-·'´,.-·'´:::::::'; 
    ;  ;::;'\  '\    ;  ;:::;    ';   ;::;       ,'´ .'´\::';‚  ';   ;::;       ,'´ .'´\::';‚  ;´    ':,´:::::::::::·´'  
   ;  ;:::;  '\  '\ ,'  ;:::;'    ';   ':;:   ,.·´,.·´::::\;'°  ';   ':;:   ,.·´,.·´::::\;'°   ';  ,    `·:;:-·'´       
  ,' ,'::;'     '\   ¨ ,'\::;'      \·,   `*´,.·'´::::::;·´      \·,   `*´,.·'´::::::;·´      ; ,':\'`:·.,  ` ·.,      
  ;.'\::;        \`*´\::\; °      \\:¯::\:::::::;:·´          \\:¯::\:::::::;:·´         \·-;::\:::::'`:·-.,';    
  \:::\'          '\:::\:' '         `\:::::\;::·'´  °            `\:::::\;::·'´  °           \::\:;'` ·:;:::::\::\'  
    \:'             `*´'‚               ¯                           ¯                       '·-·'       `' · -':::'' 
                                        ‘                            ‘                                             
"""
print(noor1)
