import vm_aids

def main():   
    written_password_to_vote_shutdown_tally = []  
    try:
        with open('passwords.txt', 'r') as password_file:
            for line, password_s in enumerate(password_file, start = 1):
                if line % 2 == 0:
                    written_password_to_vote_shutdown_tally.append(password_s.strip())
            
    except FileNotFoundError:
        print('No passwords have been set for the machine. Please have an administrator set the passwords.')
        open('passwords.txt', 'a')
        return

    #return written_password_to_vote_shutdown_tally   #used for unittest 
    ask_for_tally_mode_again = True
    tally_mode_password_wrong = True
    while ask_for_tally_mode_again == True:   
        print('Would you like to count the number of votes?')
        if_enter_tally_mode =  input('Enter yes or no here: ' )
        if_enter_tally_mode = if_enter_tally_mode.upper()
        
        if if_enter_tally_mode == 'YES':        #if the tally mode password is wrong, need another loop to correct that

            while tally_mode_password_wrong == True:
                tally_mode_password = input('Enter the password to enter tally mode here: ')

                if tally_mode_password == written_password_to_vote_shutdown_tally[2]:  

                    vm_aids.process_file()
                    ask_for_tally_mode_again = False
                    tally_mode_password_wrong = False 

                if tally_mode_password != written_password_to_vote_shutdown_tally[2]:
                    print('You have entered the wrong password.')
                    tally_mode_password_wrong = True
                    #ask_for_tally_mode_again = True  #fix this
                     

        if if_enter_tally_mode == 'NO':               
            candidates = vm_aids.read_candidates()  #list of candidates
            if len(candidates) == 0: 
                print('Please have the administrator set up the candidates in the text file.')
                return   #check this -- when for read_candidates

            input_password_to_vote_shutdown = vm_aids.password_vote_shutdown(written_password_to_vote_shutdown_tally)  
            ask_for_tally_mode_again = False 
            dict_of_candidates = vm_aids.list_to_dict(candidates)  #moved it out of the while loop line-52

            #True-to enter voting mode, False- to shut machine down -- returned from password_vote_shutdown()
            while input_password_to_vote_shutdown == True:

                vm_aids.menu(dict_of_candidates)  
                vm_aids.clear_screen()     
                input_password_to_vote_shutdown = vm_aids.password_vote_shutdown(written_password_to_vote_shutdown_tally)   
                
            if input_password_to_vote_shutdown == False:
                print('The machine will shut down now.')

        elif if_enter_tally_mode != 'YES' and if_enter_tally_mode != 'NO':
            print('Enter yes or no.')
            ask_for_tally_mode_again = True


if __name__ == '__main__':
    main()

