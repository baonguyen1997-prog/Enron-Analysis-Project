import re
import argparse
import sys


class Server:
'''This class stores the data for all emails found in the dataset.'''

emails = []  #Create a list of emails
def __init__(self, path):
    
    self.path = path
   

    file = re.compile(r'.txt')
    open(file, path)
    emails.append(file.Email)




class Email:
'''This class stores the data related to individual email messages.'''
def __init__(self, message_id, date, subject, sender, receiver, body):
    self.message_id = message_id #The id message of each email message
    self.date = date   # The  date  associated  with  each  email  message. 
    self.subject = subject #The subject of each email message
    self.sender = sender # The sender of each email message. 
    self.receiver = receiver #The receiver of each email message. 
    self.body = body # The body message of each email message

def main(path):
'''Create an instance of server-class using the path that was passed in and save that to a variable.'''
S = Server(path)
return len(S.emails)

def parse_args(args_list[]):
'''Creates an instance of ArgumentParser class
and save that to a variable. Add the path to add_argument method passed from command line arguments'''
ArgumentP = argparse.ArgumentParser()
ArgumentP.add_argument(sys.argv[1])

return ArgumentP


if __name__ == "__main__":
cmd_line_args = parse_args(sys.argv[1:])
main(cmd_line_args[1])