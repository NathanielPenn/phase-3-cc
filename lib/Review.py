class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        # self.add_movie_to_viewer()
        self.add_viewer_to_movie()
        self.add_review_to_movie()
        self.add_review_to_viewer()

        pass
    
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if type(rating) is int and rating > 0 and rating < 6:
            self._rating = rating
        else:
            raise Exception("Rating must be between 1 and 5")
        pass

    @property
    def viewer(self):
        return self._viewer

    @viewer.setter
    def viewer(self, viewer):
        from viewer import Viewer
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else: 
            raise Exception("Viewer must be an instance of Viewer")
        pass

    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        from movie import Movie
        if isinstance(movie, Movie):
            self._movie = movie
        else: 
            raise Exception("Movie must be an instance of Movie")
        pass

    def add_viewer_to_movie(self):
        if self._viewer not in self._movie.reviewers:
            self._movie.reviewers.append(self._viewer)
        pass
    def add_movie_to_viewer(self):
        if self._movie not in self._viewer.movies:
            self._viewer.movies.append(self._movie)
        pass
    def add_review_to_movie(self):
        self._movie.reviews.append(self)
        pass
    def add_review_to_viewer(self):
        self._viewer.reviews.append(self)
        pass