import os
import time
#It must allow a user to easily select a candidate but also have a running log so poll workers can see what is happening without seeing who was voted for.

     
def process_file():     
    counter = dict()
    try:
        with open('voting_results.txt') as votes:
            for line, vote in enumerate(votes, start = 0):                
                if line % 2 == 0:
                    count_votes(vote, counter)                        #vote is the name of the candidates

        print('These are the number of votes per candidate: ')
        for name in counter:
            print(str(name) + ': ' + str(counter[name]) + ' votes')
        
        #names are keys and the frequency is the value
    except FileNotFoundError:
        print('No Votes have been thus far. Begin voting and then enter tally mode.')
        open('voting_results.txt', 'a')
        
        
    
def count_votes(vote, counter):
    vote = vote.strip()
    counter[vote] = counter.get(vote, 0) + 1
    
    #return counter      #for unittest                 
    

def menu(candidates):   
    print('Vote for one of the candidates below.')
    for k in candidates:
        print( str(k + 1) + ')' + str(candidates[k]))     
    vote_choice = False
    while vote_choice == False:
        try:
            vote = int(input('Enter the value of your choice: '))
            vote = vote - 1   
            vote = candidates[vote]
            vote_choice = True
        except (KeyError, ValueError):
            print('You have entered a value not within the range of choices.')
            vote_choice = False

    seconds = time.mktime(time.gmtime())
    with open('voting_results.txt', 'a', newline= '') as votes_file:   
        votes_file.write(vote + '\n')
        votes_file.write(str(seconds) + '\n')


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    print('A vote has been made.')

def list_to_dict(candidates):
    each_candidate = dict()
    for index in range(len(candidates)):
        each_candidate[index] = candidates[index]
    return each_candidate

        
def password_vote_shutdown(written_password_to_vote_shutdown_tally): 
    print('A poll worker must enter the password to get back into voting mode or to shut the machine down.')
    password = input('Enter password here: ')
 
    while password != written_password_to_vote_shutdown_tally[0] and password != written_password_to_vote_shutdown_tally[1]:
           print('You have entered the wrong password. Try again')
           password = input('Enter here: ')
    while password == written_password_to_vote_shutdown_tally[0]: 
        #send values to main so that main calls other functions  
        return True
    if password == written_password_to_vote_shutdown_tally[1]:             
        return False


def read_candidates():
    candidates = []
    try:
        with open('candidates.txt', 'r') as candidate_choice:
            for line in candidate_choice:
                candidate = line.strip()
                candidates.append(candidate)

        return candidates #list of candidates
    except FileNotFoundError:
        with open('candidates.txt', 'a') as candidate_choice:
            candidate_choice.write('Write one name per line for each candidate. Erase this line.')
        print('Please have an administrator set the candidates.')
        return candidates

        
