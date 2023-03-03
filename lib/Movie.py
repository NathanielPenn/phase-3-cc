class Movie:
    all = []
    
    def __init__(self, title):
        self.title = title

        # self.reviewed_movies = []
        self.reviews = []
        self.reviewers = []
        pass

    @property
    def title(self):
        return self._title
        pass
    
    @title.setter
    def title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception("Title must be a string of at least 1 character")

        

    def average_rating(self):
        sum = 0 
        for review in self.reviews:
            sum += review.rating
        average = sum / len(self.reviews)
        return average
        
        pass

    @classmethod
    def highest_rated(cls):
        return max(cls.all)
        pass
