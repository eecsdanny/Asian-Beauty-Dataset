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
2. The dataset may contain some faces that are'nt Asian but most of the data are Asian, so don't worry.
## Usage
The dataset will be provided as image url links since there's copyright and provicy problems.
You can easily download and process it with simple python script.

### Example
1. download [download_image.py](/download_image.py), [img_url_history.csv](/img_url_history.csv) and [face_crop.py](/face_crop.py) to your host device
2. put 3 files in the same folder and run [download_image.py](/download_image.py)
3. (optional)use [face_crop.py](/face_crop.py) to crop the faces down, so that the dataset only contains faces.
