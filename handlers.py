'''
Created on Jan 12, 2021

@author: rcurtis
'''

from util import reddit, trigger

def handle_comment(comment):
    print('Handling comment [%s]' % comment.id)
    if trigger in comment.body.lower():
        print('Comment contains %s' % trigger)
        message_zingari('Comment containing %s' % trigger, 'http://reddit.com' + comment.permalink)
    
def handle_submission(submission):
    print('Handling submission [%s]' % submission.id)
    if submission.is_self and trigger in submission.selftext.lower():
        print('Submission contains %s' % trigger)
        message_zingari('Post containing %s' % trigger, submission.url)

def message_zingari(topic, body):
    print('Sending message: %s - %s' % (topic, body))
    reddit.redditor('Zingariman').message(topic, body)