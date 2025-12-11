# import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
#load the data set
data=pd.read_csv('netflix_titles.csv')
print(data.head())
#clean the data
df=data.dropna(subset=['type','director','cast','country','date_added','rating','duration','listed_in','description','release_year'])

# visualize the data
type_count=df['type'].value_counts()
plt.figure(figsize=(8,5)) #it tells the size of the plot
plt.bar(type_count.index,type_count.values,color=['skyblue','coral'],width=0.5,label=['Movie','TV Show'])#save the plot
plt.title('Number  of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count') 
plt.legend()
plt.tight_layout()
plt.savefig('movies_vs_tvshows_bar.png')
plt.show()


#
rating_count=df['rating'].value_counts().head(6)
plt.figure(figsize=(10,6))
plt.pie(rating_count,labels=rating_count.index,autopct='%1.1f%%',colors=['pink','blue','green','yellow','purple','orange'],startangle=140)
plt.title('Percentage of Content by Rating')
plt.tight_layout()
plt.savefig('rating_distribution_pie.png')
plt.show()


#
movie_df=df[df['type']=='Movie'].copy()
movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(10,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black',label="Movie Duration")
plt.title('Distribution of Movies  duration on Netflix')
plt.xlabel('Duration (min)')
plt.ylabel('Number of Movies')
plt.legend()
plt.tight_layout()
plt.savefig('movie_duration_hist.png')
plt.show()

#
release_counts=df['release_year'].value_counts().sort_index().head(10)
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red',marker='o',linestyle='--',label='Release Year')
plt.title('Release Year vs Number of shows')
plt.xlabel('Year')
plt.ylabel('Count')
plt.grid(color="green")
plt.legend()  
plt.tight_layout()
plt.savefig('release_year_shows_scatter.png')
plt.show()

#
coutry_counts=df['country'].value_counts().head(10)
plt.figure(figsize=(10,6))
plt.barh(coutry_counts.index,coutry_counts.values,color='teal',edgecolor='black',label='Country')
plt.title('Top 10 Countries with Most Movies and TV Shows on Netflix')
plt.xlabel('number of shows')
plt.ylabel('country')
plt.legend()
plt.tight_layout()
plt.savefig('top10_countries_barh.png')
plt.show()

#group the data
content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(20,10))
#first sub plot movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue',label='Movie')
ax[0].set_title('Movies release per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('number of movies')
ax[0].legend()


#second sub plot tv shows
ax[0].plot(content_by_year.index,content_by_year['TV Show'],color='red',label='TV Show')
ax[0].set_title('TV Shows by Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of TV Shows')
ax[0].legend()


fig.suptitle('Comparison of Movies and TV Shows by Year')
plt.tight_layout()
plt.savefig('movies_vs_tvshows_by_year.png')
plt.show()