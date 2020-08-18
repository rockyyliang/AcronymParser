# AcronymParser

Used to count acronyms in your thesis paper if you want to list them in order of frequency.  
Call the count script with paths to your .tex or .txt as command line arguments. It will count up acronyms in all given files as one since larger latex documents are often split into multiple .tex files.  
Example:  

```bash
python count.py testfiles/test1.txt testfiles/test2.txt
```

Or:

```bash
#Count all files with a .tex extension in the testfiles directory
python count.py $(ls ./testfiles | egrep .tex)
```

Results will be printed to the terminal :)


