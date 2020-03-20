# Phase 1 : Scraper
> `phase1/scraper.py`

## Goal
- In Phase 1 we implemented our web scraper for gathering YouTube video HTML information from a initial queue of video links.
  The scraper takes in a queue of links, gets the HTML for that YouTube video, and parses the HTML to gather the following 
  information for each video:
  - Title
  - Link
  - Channel
  - Channel Link
  - Channel Subscriber count
  - Video Category
  - Video ID
  - Video Views count
  - Video Likes count
  - Video Dislikes count
  - Related Video Links
- The Related video links are then placed into the queue to be parsed after the current video is done.

## Current Progress
- Our web scraper is able to begin with a list of starting videos, gather all relevant video information, and append the data to a csv file
- Our scraper also gathers all related videos per URL and appends them to the queue to continue scraping
- Our web scraper is complete :smiley:

# Phase 2 : Exploratory Data Analysis (EDA)
> `phase2/phase2_jerry.ipynb` | `phase2/phase2_cam.ipynb` | `phase2/phase2_garret.ipynb`
## Goal
- In Phase 2, we implemented three different versions of EDA in order to better braodly understand the data. Garret mostly focused on the Tags correlation with other features, Jerry focused on Likes/Dislikes/Views distributions throughout different regions, and Cameron analyzed the time components of the videos. All EDA's can be found in the respective file mentioned above.

# Phase 3 : Machine Learning Model
> `regression.ipynb` | `kmeans.ipynb`
## Goal
- In Phase 3, we implemented a couple of different machine learning models on our dataset. We had originally planned on making a KNN classifier to predict whether a video is trending/non-trending, however there was much difficulty in classifiying non-trending videos while scraping YouTube. Instead, we created a linear regression model to predict the number of views a video will receive based on the number of likes/dislikes/comments. We also implemented a K-Means cluster on the unique words in the video "tags" in order to see if there were any distinct clusters that showed any correlation between tags and likes/dislikes/comments/views.
  
# Project Contributions
- Garret, Jerry, and Cameron all contributed equally during each phase of the project. 
  - In Phases 1 and 3, all three partners worked
    together on the same files and did pair-programming in order to implement the scraper and machine learning models.
  - In Phase 2,
    each partner made their own EDA file with a pre-discussed topic to dive deeper into and analyze.
