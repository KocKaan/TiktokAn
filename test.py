from TikTokApi import TikTokApi
import csv
from collections import defaultdict

hashList =["householdgoods","householdproducts","householditems","foryou","fyp","homeproduct","goodstuff"]
#Cookie — Today at 1:06 AM
#"fashion","streetwearstyle","drippy","jordan1","aestheticoutfits","outfitideas","howtostyle","fashiontiktok"
#"amazonmusthaves","tiktokmademebuyit","tiktokmademedoit","amazonfinds", "thatgirl", "decor", "home", "ItsGreatOutdoors","amazonfinds", "amazonmusthave"
#"householdgoods","householdproducts","householditems","lifehacks","foryou","fyp","homeproduct","goodstuff"
#ornek data: {1314: ['mahmut', 34242, 25535]}
results= defaultdict(list)
resultsList=[]
yavuzsDatabase = {}

with TikTokApi() as api:
    for hashtag in hashList:
        print("The hashtag is: "+hashtag)

        tag = api.hashtag(name=hashtag)

        #print(tag.info())

        for video in tag.videos():
            #print(video.info())

            hashMap = video.info()
            listOfHashtags = []

            for i in hashMap["textExtra"]:
                listOfHashtags.append(i["hashtagName"])

            yavuzsDatabase[hashMap["id"]] = listOfHashtags


            if hashMap['stats']['playCount']> 100000 and hashMap['stats']['diggCount']> 10000:
                print("kk")
                #print(video.id,hashMap['stats']['playCount'] )
                #results.append([video.id, video.author.username])
                results[video.id].append(video.author.username)
                results[video.id].append(hashMap['stats']['playCount'])
                results[video.id].append(hashMap['stats']['diggCount'])
                resultsList.append([video.id,video.author.username,hashMap['stats']['playCount'],hashMap['stats']['diggCount']])
        #print(yavuzsDatabase)
#print(results)
#print(resultsList)
read= defaultdict(list)

with open('./book.csv', mode ='r')as file:
  # reading the CSV file
  csvFile = csv.reader(file)

  for lines in csvFile:
      if lines[0].isdigit():
          continue
      print(lines)
      #listVideo= lines[0].split(';')
      read[lines[0]].append(lines[1])
      read[lines[0]].append(lines[2])
      read[lines[0]].append(lines[3])
#print(read)
#['6987531218678041862', 'honeybobabear', '61100000', '9400000']

for key, val in results.items():
    newRes= val[1]
    print(newRes)

    #takes the difference between new and old
    if read[key] and (newRes- int(read[key][1]))> 100:
        print("THIS PRODUCT IS HOOOOOT")


print(resultsList)
fields = ['videoId', 'Author', 'View', 'Like']
#Write the file
with open('./book.csv', 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)

    # writing the data rows
    csvwriter.writerows(resultsList)

def takeView(elem):
    return elem[2]

resultsList.sort(key= takeView, reverse= True)

links= []
for result in resultsList:
    print(result[:2])
    for i in result[:2]:
        link = "https://www.tiktok.com/@{name}/video/{id}?is_copy_url=1&is_from_webapp=v1".format(name= result[1], id=result[0])
        links.append(link)

print(links)
