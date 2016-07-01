# Word frequency
A helper script to scrub txt documents into statistics based om domains and their keywords.

# Domains
Domains and their keywords can be stored into a \*.txt file where the filename is the name of the domain. The txt file should contain keywords or partial sentences on every line. These domains are initially stored in the indexes folder

# Documents
Documents should be stored in txt files and stored under the documents folder. The script will scrub all unicode from the files. Be aware that unicode in the domain keywords is not tested or supported.

# Output
The default output is stdout and formatted in JSON. Uncommenting the lines of code beneath the CSV printing comment will replace JSON with CSV.
