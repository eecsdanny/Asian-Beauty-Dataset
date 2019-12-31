# Asian-Beauty-Dataset (ABD)
Asian Beauty Dataset that contains more than 100000 instances !!

## Dataset discription
ABD is a dataset with lots of Asian beauties regardless of nationality.
ABD is created using web-crawler on a Taiwan forum which have people posting beauty pics everyday.
For now, ABD contains more than 100000 instances, it's probably the biggest Asian beauty dataset you can find.
The dataset will update regularly and grow larger.
If you need more instances, try to check this repo and update!!

## Things to know on ABD
### standard
The dataset is scraped down by the following standard
1. push(thumbs up) on the post is above 5
2. posts with title \[正妹\](beauty)
3. posts that must have imgur link inside to exclude some news or other link posts that must handle case by case.
### Cons
1. some of the data may come from a concern troll post.

## Usage
The dataset will be provided as image url links since there's copyright and provicy problems.
You can easily download and process it with simple python script.

### Example
1. download [], [] and [] to your host device
2. 
3. (optional)use [] to crop the faces down, so that the dataset only contains faces.
