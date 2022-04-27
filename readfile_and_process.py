from bs4 import BeautifulSoup
from Automaton import Automaton
states=[]
alphabet=[]
final=[]
from_to_state=[]
input_symbol=[]

def addEntry(table, state, symbol, result):
    #"" This function inserts an entry (result) to the transition table given the row (state) and the column (symbol).
       # state is a string, indicating the starting state in transition table
        ##  result is a string, indicating the state after having processed the symbol."""
    table[state][symbol] = result

def empty_table(states, alphabet):
    """Given a list of states and an alphabet,
        this function creates and returns an empty dictionary of the type: {state: {character: newState}}
        Such dictionary represents the transition table"""
    table = {}
    for s in states:
        table[s] = {}
        for char in alphabet:
            table[s][char] = 'null'     # initialize with null values

    return table

def readFile_and_process(filename,inputString):
# Reading the data inside the xml file to a variable under the name  data
   with open(filename, 'r') as f:
         data = f.read()
# Passing the stored data inside the beautifulsoup parser
   bs_data = BeautifulSoup(data, 'xml')

# Finding all instances of tag
   s1 = bs_data.find('structure',{'type':'state_set'}).find_all('name')
   for i in s1:
      states.append(i.get_text())
   #print(states)
   a1= bs_data.find_all('symbol')
   for i in a1:
       alphabet.append(i.get_text())
       #print(alphabet)
   i1 = bs_data.find('structure',{'type':'start_state'}).find('name')
   initial=i1.get_text()
#print(initial)
   f1= bs_data.find('structure',{'type':'final_states'}).find_all('name')
   for i in f1:
       final.append(i.get_text())
#print(final)

# initialize an empty transition table
   table = empty_table(states, alphabet)
#parse the transitions and populate the table
   fts= bs_data.find('structure',{'type':'transition_set'}).find_all('name')
   for i in fts:
       from_to_state.append(i.get_text())

    #print(from_to_state)

   input_s=bs_data.find('structure',{'type':'transition_set'}).find_all('input')
   for i in input_s:
       input_symbol.append(i.get_text())

   #print(input_symbol)
   for i in range(0,len(from_to_state),2):
       addEntry(table,from_to_state[i],input_symbol[(2*i+1)//4], from_to_state[i+1])


   current_state = initial
   for char in inputString:
       current_state = table[current_state][char]
    # DFA.process(inputString)
       if current_state == 'null':
           a="No"
           break
       else:
        # When entire string is parsed, check whether the final state is an accepted state
           if (current_state in final):
               a="Yes"
           else:
               a="No"

   print(a)
   #f.close()
   #return Automaton(states, alphabet, table, initial, final)
