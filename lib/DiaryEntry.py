from datetime import datetime

class DiaryEntry():
    def __init__(self, title:str, content:str) -> None:
        '''
        Params:
            title: str - representing title of the diary entry
            contents: str of contents of the diary entry

        Side effects:
            Sets the title and content properties
        '''

        if type(title) != str or type(content) != str:
            raise TypeError("Invalid entry type.")
        
        self.title = title
        self.date_obj = datetime.now() #entry date as a datetime object
        self.date_formatted = datetime.strftime(self.date_obj,'%d/%m/%Y, %I:%M%p') #entry date formatted for print
        self.content = content
        self.words_left_to_read = self.word_list() #will store the words left to read if reading in chunks

    def word_list(self) -> None:
        '''
        Params: None
        Returns: self.contents as a list of words or an empty list if self.contents is an empty string.
        Side effects: None
        '''
        if self.content == "":
            return []
        else:
            return self.content.split(" ")

    def word_count(self) -> int:
        '''
        Params: None
        Returns: an integer representing the word count of self.contents
        Side effects: None
        '''
        return len(self.word_list())
    

    def reading_time(self, wpm:int) -> int:
        '''
        Parameters:
            wpm: an integer representing the number of words the user can read
            per minute
        Returns:
            An integer representing an estimate of the reading time in minutes
            for the contents at the given wpm.
        '''
        #1) find unrounded reading time in minutes:
        unrounded_reading_time = self.word_count()/wpm

        #2) return reading time in minutes rounded to the nearest integer
        return round(unrounded_reading_time)
    

    def reading_chunk(self, wpm, min) -> str:
        '''
        Params:
            wpm: an integer representing the number of words the user can read per minute
            minutes: an integer representing the number of minutes the user has to read

        Returns: Chunk of reading according to how much time you have to read
            If called again, `reading_chunk` should return the next chunk,
            skipping what has already been read, until the contents is fully read.
            The next call after that it should restart from the beginning.

        Side effects: changes self.words_left_to_read to reflect how much has been read.
        '''

        #5) After the last chunk and all contents have been read, restart from the beginning:
        if self.words_left_to_read == []:
            self.start_over_reading() #refresh words_left_to_read to start from the beginning

        #1) find number of words in this reading chunk:
        words_per_chunk = wpm * min

        #2) find the first {words_per_chunk} in self.word_list as a string.
        current_chunk_list = self.words_left_to_read[:words_per_chunk]
        current_chunk = " ".join(current_chunk_list)

        #3) update self.word_list to be the remaining unread words as a list:
        self.words_left_to_read = self.words_left_to_read[words_per_chunk:]


        #4) return the current_chunk
        return current_chunk
    
    def start_over_reading(self) -> None:
        '''
        Params: None
        Returns: None
        Side effects: resets words_left_to_read to the start of content
        '''
        self.words_left_to_read = self.word_list()

    def format_for_diary(self) -> str:
        '''
        Params: None
        Returns: a formatted string to be used in Diary for displaying each diary entry
        Side effects: None
        '''
        return f'''{self.title}
{self.date_formatted}
Word Count: {self.word_count()}'''