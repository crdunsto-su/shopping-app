{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Now You Code 2: IP Addresses\n",
    "\n",
    "For this Now You Code, you will complete a very common task in data analytics: converting an IP address https://en.wikipedia.org/wiki/IP_address to an approximate location.\n",
    "\n",
    "Write a program to read the IP Addresses from the File `NYC2-IP-Addresses.txt` and for each IP address determine the approximate location (City and State) for the origin of that IP Address. This is usually done as part of analytics to determine the origins of website visitors. \n",
    "\n",
    "To perform the lookups, use the http://freegeoip.net API. **You'll have to read through the API documentation first and understand how to use the API before you write the program. **\n",
    "\n",
    "Once again, problem simplification is key here.  Just get the  IP lookup working, writing it as a function, and then try to read from the file and perform the lookups for each IP address in the file.\n",
    "\n",
    "Here's a sample of a geoip lookup of the IP Address `'128.230.182.217'`\n",
    "\n",
    "```\n",
    "{'city': 'Syracuse',\n",
    " 'country_code': 'US',\n",
    " 'country_name': 'United States',\n",
    " 'ip': '128.230.182.217',\n",
    " 'latitude': 43.0377,\n",
    " 'longitude': -76.1396,\n",
    " 'metro_code': 555,\n",
    " 'region_code': 'NY',\n",
    " 'region_name': 'New York',\n",
    " 'time_zone': 'America/New_York',\n",
    " 'zip_code': '13244'}\n",
    "```\n",
    "\n",
    "In this example the city and state would be `Syracuse, NY`\n",
    "\n",
    "\n",
    "Final Program Output will read all the addresses from the file.:\n",
    "\n",
    "```\n",
    "IP: 128.122.140.238 LOCATION: New York,NY\n",
    "IP: 23.112.232.160 LOCATION: Green Bay,WI\n",
    "IP: 23.192.215.44 LOCATION: Cambridge,MA\n",
    "IP: 23.224.160.4 LOCATION: Cheyenne,WY\n",
    "IP: 23.230.12.5 LOCATION: San Jose,CA\n",
    "IP: 23.80.125.101 LOCATION: Phoenix,AZ\n",
    "IP: 23.83.132.200 LOCATION: Phoenix,AZ\n",
    "IP: 23.88.15.5 LOCATION: Los Angeles,CA\n",
    "IP: 24.0.14.56 LOCATION: Iselin,NJ\n",
    "IP: 24.1.25.140 LOCATION: Chicago,IL\n",
    "IP: 24.11.125.10 LOCATION: Orem,UT\n",
    "IP: 24.38.114.105 LOCATION: Matawan,NJ\n",
    "IP: 24.38.224.161 LOCATION: Darien,CT\n",
    "IP: 56.216.127.219 LOCATION: Raleigh,NC\n",
    "IP: 68.199.40.156 LOCATION: Elmont,NY\n",
    "IP: 74.111.18.59 LOCATION: Auburn,NY\n",
    "IP: 74.111.6.173 LOCATION: Liverpool,NY\n",
    "IP: 98.29.25.44 LOCATION: Dayton,OH\n",
    "```\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Step 1: Problem Analysis for `geoiplookup` function\n",
    "\n",
    "Inputs: IP address\n",
    "\n",
    "Outputs: Dictionary of Geographic information for that IP Address\n",
    "\n",
    "Algorithm (Steps in Program):\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Step 2: write the user defined function `geoiplookup`\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3: Problem Analysis for entire program\n",
    "\n",
    "Inputs: \n",
    "\n",
    "Outputs: \n",
    "\n",
    "Algorithm (Steps in Program):\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Step 4: write main program here\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5: Questions\n",
    "\n",
    "1. Place your laptop in Airplane mode and run the program. How can this program be modified so that it will not error in the event of a network outage? \n",
    "2. In what other ways can this program be modified to be more useful?\n",
    "3. What is the advantage of reading the IP Addresses from a file as opposed to entering them in ar run time?\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reminder of Evaluation Criteria\n",
    "\n",
    "1. What the problem attempted (analysis, code, and answered questions) ?\n",
    "2. What the problem analysis thought out? (does the program match the plan?)\n",
    "3. Does the code execute without syntax error?\n",
    "4. Does the code solve the intended problem?\n",
    "5. Is the code well written? (easy to understand, modular, and self-documenting, handles errors)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python [default]",
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
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
