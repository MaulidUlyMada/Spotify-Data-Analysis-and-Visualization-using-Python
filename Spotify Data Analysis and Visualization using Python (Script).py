# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qw_mlnDMMy5zm3kczkt1BfCZmttCBP2D
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_tracks = pd.read_csv("/content/drive/My Drive/Dataset/tracks.csv")
df_tracks.head()

# null values

pd.isnull(df_tracks).sum()

df_tracks.info()

sorted_df = df_tracks.sort_values('popularity', ascending = True).head(10)
sorted_df

df_tracks.describe().transpose()

most_popular = df_tracks.query("popularity>90", inplace = False).sort_values("popularity", ascending = False)
most_popular[:10]

df_tracks.set_index("release_date", inplace = True)
df_tracks.index = pd.to_datetime(df_tracks.index)
df_tracks.head()

df_tracks[["artists"]].iloc[18]

df_tracks["duration"] = df_tracks["duration_ms"].apply(lambda x: round(x/1000))
df_tracks.drop("duration_ms", inplace = True, axis = 1)

df_tracks.duration.head()

corr_df = df_tracks.drop(["key", "mode", "explicit"], axis = 1).corr(method = "pearson")
plt.figure(figsize = (14,6))
heatmap = sns.heatmap(corr_df, annot = True, fmt = ".1g", vmin = 1, vmax = 1, center = 0, cmap = "Spectral", linewidths = 1, linecolor = "Black")
heatmap.set_title("Correlation HeatMap Between Variable")
heatmap.set_xticklabels(heatmap.get_xticklabels(), rotation = 90)

sample_df = df_tracks.sample(int(0.004*len(df_tracks)))

print(len(sample_df))

plt.figure(figsize = (10,6))
sns.regplot(data = sample_df, y = "loudness", x = "energy", color = "red").set(title = "Loudness vs Energy Correlation")

plt.figure(figsize = (10,6))
sns.regplot(data = sample_df, y = "popularity", x = "acousticness", color = "blue").set(title = "Popularity vs Acousticness Correlation")

df_tracks["dates"] = df_tracks.index.get_level_values("release_date")
df_tracks.dates = pd.to_datetime(df_tracks.dates)
years = df_tracks.dates.dt.year

#pip install --user seaborn==0.11.0

sns.displot(years, discrete = True, aspect = 2, height = 5, kind = "hist").set(title = "Number of songs per year")

total_dr = df_tracks.duration
fig_dims = (18,7)
fig, ax = plt.subplots(figsize = fig_dims)
fig = sns.barplot(x = years, y = total_dr, ax = ax, errwidth = False).set(title = "Year vs Duration")
plt.xticks(rotation = 90)

df_genre = pd.read_csv("/content/drive/My Drive/Dataset/SpotifyFeatures.csv")

df_genre.head(10)

plt.title("Duration of the songs in Different Genres")
sns.color_palette("rocket", as_cmap = True)
sns.barplot(y = "genre", x = "duration_ms", data = df_genre)
plt.xlabel("Duration in mili seconds")
plt.ylabel("Genres")

sns.set_style(style = "darkgrid")
plt.figure(figsize = (10,5))
famous_genre = df_genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y = "genre", x = "popularity", data = famous_genre).set(title = "Top 5 Genres by Popularity")

sns.set_style(style = "darkgrid")
plt.figure(figsize = (10,5))
famous_artist = df_genre.sort_values("popularity", ascending = False).head(10)
sns.barplot(y = "artist_name", x = "popularity", data = famous_artist).set(title = "Top 5 Artists by Popularity")

df_artist = pd.read_csv("/content/drive/My Drive/Dataset/artists.csv")

df_artist.head(10)

plt.figure(figsize = (15,6))
sns.lineplot(data = df_artist, y = "followers", x = "popularity", color = "red").set(title = "Followers vs Popularity Correlation")