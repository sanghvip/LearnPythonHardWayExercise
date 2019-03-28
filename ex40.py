class Song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		print("Total lines %d"%len(self.lyrics))
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Happy birthday to you","I dont want to get sued","So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family","With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

print("-"*10)

sautarah = ["Sau tarah ke rrog le lo","ishq ka maarz kya hai","tu kahe to jaan de du","Kehne me haarrz kya hai"]
dishoom = Song(sautarah)
dishoom.sing_me_a_song()