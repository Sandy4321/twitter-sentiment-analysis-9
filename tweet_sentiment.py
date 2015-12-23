import sys

def count_lines(f):
    print str(len(f.readlines()))

def main():
    sentiments_file = open(sys.argv[1])
    tweets_file = open(sys.argv[2])
    count_lines(sentiments_file)
    count_lines(tweets_file)

if __name__ == '__main__':
    main()
