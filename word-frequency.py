import codecs
import os
import os.path
import re
import json

collection = {}


def finddocs(documents_dir):
    files = []
    for dirname, subdirlist, filelist in os.walk(documents_dir, topdown=False):
        for f in filelist:
            if f.endswith('.txt'):
                files.append(os.path.join(dirname, f))
    return files


def getkeywords(keyword_files):
    keywords = {}
    for kf in keyword_files:
        keywords[kf] = {} 
        words = []
        with open(kf, 'r') as fh:
            for k in fh:
                words.append(k[:-1])
            keywords[kf] = words
    return keywords


def indexfiles(files, keywords, collection):
#    print("Start with indexing files:")
    for f in files:
        with codecs.open(f, 'r', 'utf-8') as fh:
            collection[f] = {}
            for k,v in keywords.iteritems():
                k = os.path.basename(os.path.splitext(k)[0])
                collection[f][k] = {}
                for word in v:
#                    print("\tIndexing {} ; domain {} ; keyword {}").format(f, k, word)
                    createindex(fh, word, k, collection)


def createindex(filehandle, keyword, k, collection):
    filehandle.seek(0)
    text = filehandle.read().lower().encode('utf-8')
    data = text.decode('unicode_escape').encode('ascii', 'ignore')
    occurrence = re.findall(keyword, data)
#    for i in occurrence:
#        print(i)
    s = len(occurrence)
    if s!=0:
        collection[filehandle.name][k][keyword] = s


def main():
    documents_dir = './documents/'
    keyword_dir = './indexes/'
    keyword_files = finddocs(keyword_dir)
    keywords = getkeywords(keyword_files)
    indexfiles(finddocs(documents_dir), keywords, collection)
    ## print json
    print(json.dumps(collection, indent=4, sort_keys=True))
    ## print csv
    #print("article;date;domain;keyword;count")
    #for k,v in collection.iteritems():
    #    kdate = os.path.basename(k).split('_', 1)[0]
    #    for a,b in v.iteritems():
    #        for c,d in b.iteritems():
    #            print("{};{};{};{};{}").format(k,kdate,a,c,d)


if __name__ == "__main__":
    main()
