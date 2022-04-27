from readfile_and_process import readFile_and_process

### READ AUTOMATON (The test files must be in the root folder)###
#DFA = readFile("test2.jff")
#print(DFA)
#DFA.show_table()
## Testing string acceptance in test1.txt ##

inputString=input("Introduce a string to verify if is accepted: ")
readFile_and_process("test2.jff",inputString)

print ("-----------------------------------------------------------------------------------")

