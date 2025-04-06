# Vote Calculator
A set of simple Python scripts that turn the raw Google Sheets results of GhostLand's elections into something useful.
## Project Structure
* `vote-calculator/[name]/` -> Folder associated with a given election. Currently, only one election is available: `gl7-worldgen`.
* `vote-calculator/[name]/example-datadump.tsv` -> An example Google Sheets export that a given's election scripts can read.
* `vote-calculator/[name]/[script]` -> Some script realted to a given election. For example, `gl7-worldgen` only has a single script (`calc.py`) that just calculates everything it can, given a particualr TSV file.
* `datadumps/` -> There's a `.gitignore`d folder called Datadumps present. It's recommended to put all your downloaded TSVs files either there, or outside the repo completley - so that they don't accidentially get commited into the repo, risking a data leak.
## How to use?
These instructions only concern the ongoing or most recent elections: `gl7-worldgen`. Please use Git history if you want to see an older version of this document *(Well, such a version doesn't exist yet becasue `gl7-worldgen` are the 1st elections where this repo is/was used, but that'll (hopefully) change soon)*, related to some older elections. [Polish usage instructions here.](https://github.com/Team-GhostLand/vote-calculator/blob/master/INSTRUKCJE.md)
### Step 1: Install Python
...If you don't have it yet.
### Step 2: Clone this repo.
Use command `git clone https://github.com/Team-GhostLand/vote-calculator.git`, its equivalent via GitHub or download it as a ZIP if you don't have the Git CLI installed.
### Step 3: Procure a spec-compliant TSV file.
* You can see an example TSV file inside `vote-calculator/gl7-worldgen/example-datadump.tsv`. It's good for testing.
* If you're a part of the election commission, you may download a TSV from a Google Sheet linked to our Google Form (File > Download > TSV). It is **highly reccomended** that you store your downloaded file inside `datadumps/`. Create this folder first, of course, as - because it's `.gitignore`d - it doesn't exist by default (which is precisely why it's a good place to store downloaded TSVs - you don't risk accidentially commiting them).
* Because we allow anwsers to be viewed after completing a form, you can - if you're not a part of the comitiee, but want to see how the poll's going - try recreating the results based on `vote-calculator/gl7-worldgen/example-datadump.tsv`. Just... Look at the elections results there on Google Sheets and try compiling them into a file. 
### Step 4: Almost there!
Open a terminal inside `vote-calculator/gl7-worldgen`. On Windows, you can do so by navigating there and then doing `Shift+RClick` > Open CMD here (or something similar to that - I dunno, I don't use Windows). On Linux, you already know.
### Step 5: Execution
In the just-opened terminal, run `python calc.py ../../datadumps/[name].tsv` to run whatever TSV you want (just replace `[name]` with the actual filename) or do `python calc.py example-datadump.tsv` to run our example TSV.
## Why Python?
It was a **huge, huge mistake**. I was supposed to explain here why - and also why I even chose it in the first place. Unfortunatley, I don't have time right now. Consider it `TODO!`.