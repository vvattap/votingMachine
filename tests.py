import unittest
import vm_aids  
import main
import unittest.mock

 #call the actual function
#from unittest import mock

class TestMain(unittest.TestCase):

    def test_read_candidates(self): 
        candidates = vm_aids.read_candidates()
        compare_candidates = [ 'Jack', 'Ryan', 'Asi', 'Amala', 'Arusa', 'Safura', 'Janki']
        self.assertListEqual(compare_candidates, candidates)

    def test_list_to_dict(self):
        compare_dict_of_candidates = {0:'Arusa', 1: 'Safura', 2: 'Janki', 3 :'Amala'}
        list_of_candidates = ['Arusa', 'Safura', 'Janki', 'Amala']

        returned_dict_candidates = vm_aids.list_to_dict(list_of_candidates)
        self.assertEqual(compare_dict_of_candidates, returned_dict_candidates)

    def test_main(self): #--line 16 --take # off  (main)
        check_passwords_list = ['4772ym','CFKA1845','QUOITENPED']   
        passwords_list = main.main()
        self.assertListEqual(check_passwords_list, passwords_list)

    def test_password_vote_shutdown(self):
        all_passwords_list = ['4772ym','CFKA1845','QUOITENPED']
        with unittest.mock.patch('builtins.input', return_value = '4772ym'):
            voting_mode_password_checker = vm_aids.password_vote_shutdown(all_passwords_list)
        self.assertEqual(True, voting_mode_password_checker)

    def test_password_vote_shutdown_two(self):
        all_passwords_list = ['4772ym','CFKA1845','QUOITENPED']
        with unittest.mock.patch('builtins.input', return_value = 'CFKA1845'):
            voting_mode_password_checker = vm_aids.password_vote_shutdown(all_passwords_list)
        self.assertEqual(False, voting_mode_password_checker)

    
    def test_count_votes(self):  #line 29  (vm_aids)
        vote = 'Janki'
        counter = dict()
        dict_of_votes = vm_aids.count_votes(vote,counter)
        expected_result = {'Janki': 1}
        self.assertDictEqual(expected_result, dict_of_votes)
        
        








if __name__ == '__main__':
    unittest.main()