{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "da3d9bad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<_csv.reader object at 0x000001BF2C1B0A00>\n",
      "CSV Header: ['Ballot ID', 'County', 'Candidate']\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import csv\n",
    "import pandas as pd\n",
    "\n",
    "# Variables\n",
    "total_votes = 0\n",
    "Charles = 0\n",
    "Diana = 0\n",
    "Raymon = 0\n",
    "\n",
    "csvpath = os.path.join('.', 'Resources', 'election_data.csv')\n",
    "\n",
    "with open(csvpath) as csvfile:\n",
    "\n",
    "    # CSV reader specifies delimiter and variable that holds contents\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "\n",
    "    print(csvreader)\n",
    "    \n",
    "    csv_header = next(csvreader)\n",
    "    print(f\"CSV Header: {csv_header}\")\n",
    "\n",
    "    # Read each row of data after the header\n",
    "    for row in csvreader:\n",
    "        total_votes = total_votes + 1\n",
    "        if row[2] == 'Charles Casper Stockham':\n",
    "            Charles = Charles + 1\n",
    "        elif row[2] == 'Diana DeGette':\n",
    "            Diana = Diana + 1\n",
    "        elif row[2] == 'Raymon Anthony Doane':\n",
    "            Raymon = Raymon + 1\n",
    "#The percentage of votes \n",
    "Charles_percent = round(Charles * 100/ total_votes,3)\n",
    "Diana_percent = round(Diana * 100/ total_votes,3)\n",
    "Raymon_percent = round(Raymon * 100/ total_votes,3)\n",
    "\n",
    "#Create DataFrame and sort by descending to determine the winner\n",
    "data ={'Candidates': ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane'],\n",
    "       'Votes': [Charles, Diana, Raymon]}\n",
    "df = pd.DataFrame(data)\n",
    "winner = df.sort_values(by='Votes', ignore_index=True, ascending=False)\n",
    "winner = winner['Candidates'][0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "522a817d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Total Votes: 369711\n",
      "-------------------------\n",
      "Charles Casper Stockham: 23.049 (85213)\n",
      "Diana DeGette: 73.812 (272892)\n",
      "Raymon Anthony Doane: 3.139 (11606\n",
      "-------------------------\n",
      "Winner: Diana DeGette\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "# Print the outcome\n",
    "\n",
    "print(\"Election Results\")\n",
    "print(\"-------------------------\")\n",
    "print(f'Total Votes: {total_votes}')\n",
    "print(\"-------------------------\")\n",
    "print(f'Charles Casper Stockham: {Charles_percent} ({Charles})')\n",
    "print(f'Diana DeGette: {Diana_percent} ({Diana})')\n",
    "print(f'Raymon Anthony Doane: {Raymon_percent} ({Raymon}')\n",
    "print(\"-------------------------\")\n",
    "print(f\"Winner: {winner}\")\n",
    "print(\"-------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "0dbac875",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Record csv file\n",
    "output_path = os.path.join(\".\", \"PyPoll_results.csv\")\n",
    "with open(output_path, 'w') as csvfile:\n",
    "\n",
    "    csvwriter = csv.writer(csvfile, delimiter=',')\n",
    "    csvwriter.writerow(['Election Results'])\n",
    "    csvwriter.writerow(['Total Votes:', total_votes])\n",
    "    csvwriter.writerow(['Charles Casper Stockham:', Charles_percent, Charles])\n",
    "    csvwriter.writerow(['Diana DeGette:', Diana_percent, Diana])\n",
    "    csvwriter.writerow(['Raymon Anthony Doane:', Raymon_percent, Raymon])\n",
    "    csvwriter.writerow(['Winner:', winner])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f273268",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
