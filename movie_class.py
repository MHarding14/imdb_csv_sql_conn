class Movie:

    movie_instances = []

    def __init__(self, titletype, primarytitle, originaltitle, isadult, startyear, endyear, runtimeminutes, genres):
        Movie.movie_instances.append(self)
        self.titletype = titletype
        self.primarytitle = primarytitle
        self.originaltitle = originaltitle
        self.isadult = isadult
        self.startyear = startyear
        self.endyear = endyear
        self.runtimeminutes = runtimeminutes
        self.genres = genres