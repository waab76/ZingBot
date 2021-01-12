'''
Created on Jan 12, 2021

@author: rcurtis
'''
import logging
import threading

from praw.models.reddit import comment
from praw.models.reddit import submission
from praw.models.util import stream_generator

from handlers import handle_comment, handle_submission
from util import subreddit

def monitor_submissions():
    print('Monitoring submissions')
    while True:
        submission_stream = subreddit.stream.submissions()
        try:
            for submission in submission_stream:
                handle_submission(submission)
        except:
            print('Error in submission monitoring')

def monitor_comments():
    print('Monitoring comments')
    while True:
        comment_stream = subreddit.stream.comments()
        try:
            for comment in comment_stream:
                handle_comment(comment)
        except:
            print('Error in comment monitoring')
        
def monitor_edits():
    print('Monitoring edits')
    while True:
        logging.info('Monitoring [r/%s] submission and comment edits', subreddit.display_name)
        edited_stream = stream_generator(subreddit.mod.edited, pause_after=0)
        try:
            for item in edited_stream:
                if isinstance(item, comment.Comment):
                    handle_comment(item)
                elif isinstance(item, submission.Submission):
                    handle_submission(item)
                elif item is not None:
                    pass
        except:
            print('Error in edit monitoring')

logging.debug('Starting child threads')
threading.Thread(target=monitor_submissions, name='submissions').start()
threading.Thread(target=monitor_comments, name='comments').start()
threading.Thread(target=monitor_edits, name='edits').start()
