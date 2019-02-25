# Scripts for StudySmart's backend

## libraryscraper.js

To run the file successfully: 

```node.js
npm install puppeteer --save
node libraryscraper.js
```

This file returns an array of JSON objects corresponding to available study rooms in Powell and YRL. 

Each JSON object has the following structure:

```JSON
{
    "Building Name": "Powell Library",
    "Room Number": "Group Study Room F",
    "Capacity": 6,
    "Date": "February 5, 2019",
    "Day": "Tuesday",
    "Start Time": "1:00PM"
}
```

## reslifescraper.js

To run the file successfully:

```node.js
npm install puppeteer --save
node libraryscraper.js
```

This file returns an array of JSON objects corresponding to all the available study rooms on the hill at UCLA within the next 7 days. 

Each JSON object has the following structure:

```JSON
{
  "Room Details": "Sproul Study Room 110E (max 4 people)",
  "Time": "11:00pm-midnight on Sun, Mar 03",
  "Link": "https://www.orl.ucla.edu/reserve?type=sproulstudy&duration=60&date=2019-03-03&roomid=3584&start=1551682800&stop=1551686400"
}
```


