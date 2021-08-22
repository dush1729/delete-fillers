import os

print("Enter common file prefix to remove everything before episode number")
print("example [AnimeKaizoku] One Piece - : ")
file_prefix = input()

# move all files in single folder and file name cleanup
seasons = [name for name in os.listdir(".") if os.path.isdir(name)]
for season in seasons:
	os.chdir(season)

	episodes = os.listdir(".")
	for episode in episodes:
		episode_prefix_deleted = episode.replace(file_prefix, "")
		episode_no = ""
		for c in episode_prefix_deleted:
			if c.isdigit():
				episode_no += c
			else:
				break
		os.rename(episode, "../" + episode_no + ".mkv")

	os.chdir("..")
	os.rmdir(season)