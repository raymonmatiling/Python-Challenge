# Python-Challenge | Assignment - PyBank and PyPoll

## Background

It's time to put away the Excel sheet and join the big leagues. Welcome to the world of programming with Python. In this homework assignment, you'll be using the concepts you've learned to complete **2** Python Challenges, PyBank and PyPoll.
Both of these challenges encompasses a real-world situation where your newfound Python scripting skills can come in handy. These challenges are far from easy so expect some hard work ahead!

### Before You Begin

1. Create a new GitHub repo called `python-challenge`. Then, clone it to your computer.
2. Inside your local git repository, create a directory for both of the  Python Challenges. Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.
3. Inside of each folder that you just created, add a new file called `main.py`. This will be the main script to run for each analysis.
4. Push the above changes to GitHub.

## PyBank Instructions

In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following:
  * The total number of months included in the dataset
  * The total net amount of "Profit/Losses" over the entire period
  * The average change in "Profit/Losses" between months over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period

As an example, your analysis should look similar to the one below:
```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $-8311.11
  Greatest Increase in Profits: Aug-16 ($1862002)
  Greatest Decrease in Profits: Feb-14 ($-1825558)
```
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll Instructions

In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote

Your analysis should align with the following results:
```text
   Election Results
   -------------------------
   Total Votes: 369711
   -------------------------
   Charles Casper Stockham: 23.049% (85213)
   Diana DeGette: 73.812% (272892)
   Raymon Anthony Doane: 3.139% (11606)
   -------------------------
   Winner: Diana DeGette
   -------------------------
```
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

## Hints and Considerations
  * Consider what you've learned so far. You've learned how to import modules like csv. You’ve learned how to read and write files in various formats. You’ve learned how to store content in variables, lists, and   dictionaries. You’ve learned how to iterate through basic data structures. And you’ve learned how to debug along the way. Using all that you've learned, try to break down your tasks into discrete mini-objectives.
  * The datasets for these Challenges are quite large. This was done purposefully to showcase one of the limits of Excel-based analysis. As data analysts, our first instinct is often to go straight to Excel, but creating scripts in Python can provide us with more powerful options for handling big data.
  * Write one script for each of the provided datasets. Run each script separately to make sure that the code works for its respective dataset.
  * Always commit your work and back it up with pushes to GitHub or GitLab. You don't want to lose hours of your hard work! Also make sure that your repo has a detailed README.md file.

## Copyright

by edX Boot Camps LLC, and is intended for educational purposes only.
