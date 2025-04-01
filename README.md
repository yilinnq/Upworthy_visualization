# final_project
Final Project for Harvard Business School (HBS)'s Data Visualization for Analysis and Communication class.


## Dataset
I use the [Upworthy Research Archive](https://upworthy.natematias.com/) dataset, which contains results related to 32,487 online A/B tests conducted on Upworthy.com. 
The archive is structured into exploratory, confirmatory, holdout, and undeployed datasets. This project utilizes the Exploratory Data containing 4,873 of the A/B test results.

### Javascript Dataset access
The data files included in this project are parsed from their original `.csv` counterparts. They are now publically accessible at the following address:
- `2013.01.01-2015.04.30-aggregate-country-data.js`
    - Original source link: https://osf.io/jd64p/files/osfstorage
    - JS version public link: https://raw.githubusercontent.com/yilinnq/Upworthy_visualization/refs/heads/main/data/parsed/2013.01.01-2015.04.30-aggregate-country-data.js
- `2013.01.01-2015.04.30-daily-pageviews.js`
    - Original source link: https://osf.io/jd64p/files/osfstorage
    - JS version public link: https://raw.githubusercontent.com/yilinnq/Upworthy_visualization/refs/heads/main/data/parsed/2013.01.01-2015.04.30-daily-pageviews.js
- `2013.01.01-2015.04.30-daily-users-info.js`
    - Original source link: https://osf.io/jd64p/files/osfstorage
    - JS version public link: https://raw.githubusercontent.com/yilinnq/Upworthy_visualization/refs/heads/main/data/parsed/2013.01.01-2015.04.30-daily-users-info.js
- `2013.01.01-2015.04.30-aggregate-country-data.js`
    - Original source link: https://osf.io/3vqmp
    - JS version public link: https://raw.githubusercontent.com/yilinnq/Upworthy_visualization/refs/heads/main/data/parsed/upworthy-archive-exploratory-packages-03.12.2020.js


### Data Fields
**User-Related Fields**
From the [README](https://osf.io/a8ke6) of the user-level dataset:
- The `daily-users-info` file contains user-level information by day. For each day between Jan 1 2013 and Apr 30 2015, this csv contains data about the number of `users`, `new users`, `sessions per user`, `sessions`, `average session duration`, `bounce rate`, `pageviews`, `pages/session`.
- The `daily-pageviews` file contains pageview information by day. For each day between Jan 1 2013 and Apr 30 2015, this csv contains data about the number of pageviews.
- The `aggregate-country-data` file contains an aggregate view of the countries from which users were accessing upworthy.com between Jan 1 2013 and Apr 30 2015. For each country, this csv contains data about the number of `users`, `new users`, `sessions`, `bounce rate`, `average session duration`, `pages/session`.


**Experiments-Related Fields**
From the [About the Archive](https://upworthy.natematias.com/about-the-archive) page:
- Time-related columns:
    - `created_at`: time the package was created (timezone unknown)
    - `test_week`: week the package was created, a variable constructed by the archive creators for stratified random sampling
- Experiment-related columns:
    - `clickability_test_id`: the test ID. Viewers were randomly assigned to packages with the same test ID
    - `problem (0/1)`: set to 1 if the researchers believe the randomization for a given test was likely to have a randomization problem (see this page for more details). This value is set to 1 for all tests between June 25, 2013 and January 10, 2014.
    - `impressions`: the number of viewers who were assigned to this package. The total number of participants for a given test is the sum of impressions for all packages that share the same clickability_test_id.
- Stimuli shown to viewers:
    - `headline`: the headline being tested
    - `eyecatcher_id`: image ID. Image files are not available. Packages that shared the same image have the same eyecatcher_id
- Outcomes:
    -  `clicks`: the number of viewers (impressions) that clicked on the package. The click-rate for a given package is the number of clicks divided by the number of impressions.
Other fields were not shown to viewers or contain computation logic that are not recoverable.


### For More Information on the Dataset
- Nature article: https://www.nature.com/articles/s41597-021-00934-7
- Data Fields explanation: https://upworthy.natematias.com/about-the-archive
- Slides view of dataset: https://upworthy.natematias.com/resources/lecture-15-asking-questions-of-the-upworthy-archive.pdf
- User level data description: https://osf.io/a8ke6 