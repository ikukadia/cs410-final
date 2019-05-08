import changes
import mentioned
import poll
import react
import time
import uniqueWords
import words


def main():
    print("the following lists the amount of times people have modified nicknames")
    changes.main()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("the following lists how often a person has been mentioned in a message")
    mentioned.main()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("the following lists how many people have created polls before")
    poll.main()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("the following lists which reactions a person receives the most")
    react.main()
    #time.init()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("the following lists how strong a person's vocabulary is")
    uniqueWords.main()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("the following lists how often a person uses slang/mispells words")
    words.main()

if __name__ == '__main__':
    main()