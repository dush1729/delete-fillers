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

print("Enter filler list in form 23 - 26, 34, 121 - 140")
fillers_raw = input()
for s in fillers_raw.split(", "):
	l, r = 0, 0
	if("-" in s):
		idx = s.index("-")
		l, r = int(s[:idx]), int(s[idx + 1:])
	else:
		l, r = int(s), int(s)

	for filler_no in range(l, r + 1):
		filler = str(filler_no) + ".mkv"
		if(os.path.isfile(filler)):
			os.remove(filler)

print("fillers successfully removed!")