from lib.DiaryEntry import DiaryEntry

class Diary():
    def __init__(self) -> None:
        self.all_diary_entries = [] #list of all diary entry objects
        self.currently_reading = None #DiaryEntry object that is currently being read


    #ADDING/DELETING:
    def add(self, entry: DiaryEntry) -> None:
        '''
        Params: entry - a DiaryEntry object
        Returns: None
        Effects: adds entry to self.all_diary_entries
        '''
        if isinstance(entry, DiaryEntry) != True:
            raise Exception("Invalid entry")
        self.all_diary_entries.append(entry)

    def delete(self, entry: DiaryEntry) -> None:
        '''
        Params: entry - a DiaryEntry object
        Returns: None
        Effects: removes an entry from self.all_diary_entries
        '''
        if entry not in self.all_diary_entries:
            raise Exception("Invalid entry")
        self.all_diary_entries.remove(entry)
        

    def delete_all(self) -> None:
        '''
        Params: None
        Returns: None
        Effects: removes all entries from self.all_diary_entries
        '''
        self.all_diary_entries = []
    
    
    #DISPLAY ALL ENTRIES
    def display_all_diary_entries(self, by_word_count = False) -> str:
        '''
        Params: 
            by_word_count: boolean, if set to True, the entries are listed by highest to lowest word_count 
        Returns: A formatted string to display all entries by title, date and word count in the terminal
        Effects:
        '''
        # if by_word_count is true, sort by highest to lowest word_count
        if by_word_count == True:
            lst = sorted(self.all_diary_entries, key = lambda x: x.word_count(), reverse=True)
        
        else: # else, default is sorted by added
            lst = self.all_diary_entries
        
        formatted_strings_list = [entry.format_for_diary() for entry in lst]
        
        # join with two spaces added in between for readablility
        return '\n\n'.join(formatted_strings_list)


    #SELECT BY TITLE:
    def select_by_title(self, title:str) -> DiaryEntry:
        '''
        Params: None
        Result: DiaryEntry object for which entry.title == title
        Effects: None'''
        result = next((obj for obj in self.all_diary_entries if obj.title == title), None)
        if result == None:
            raise Exception("Invalid entry name.")
        else:
            return result


    def word_count_all(self) -> int:
        '''
        Params: None
        Returns: Integer representing the total word count of all entries
        Effects: None
        '''
        return sum([entry.word_count() for entry in self.all_diary_entries])


    def read_whole_entry(self, entry:DiaryEntry) -> str:
        '''
        Params: entry - DiaryEntry object
        Returns: entry.content
        Effects: None
        '''
        if entry not in self.all_diary_entries:
            raise Exception("Invalid entry")
        return entry.content
        

    def read_partial(self, wpm:int, min:int, entry=None) -> str:
        '''
        Params: entry - DiaryEntry object, or None by default. If it is None, 
        we will read the last diary entry that was called for read_partial
        Returns: the next portion of the entry
        Side effects: changes self.currently_reading to entry
        '''
        if entry == None:
            if self.currently_reading != None:
                entry = self.currently_reading
            else:
                raise Exception("No entry currently being read. Please choose an entry.")
        elif entry not in self.all_diary_entries:
            raise Exception("Invalid entry")
        
        else:
            self.currently_reading = entry #set currently reading to the chosen entry
            for obj in self.all_diary_entries: #reset all other entries to be read from the beginning.
                if obj != entry:
                    obj.start_over_reading()
        return entry.reading_chunk(wpm, min) #can repeatedly call this method to get the next reading chunk of currently_reading
        

    def start_over_reading_current(self):
        '''
        Params: None
        Return: None
        Side effects: restarts self.currently_reading to the start
        '''
        if self.currently_reading == None:
            raise Exception("No entry currently being read. Please choose an entry.")
        self.currently_reading.start_over_reading()


    def find_best_entry_for_reading_time(self, wpm:int, min:int) -> DiaryEntry:
        '''
        Params:
            wpm: integer representing the number of words the user can read per minute
            min: integer representing the numbe of minutes a user has to read
        Returns: the first DiaryEntry object for with the contents are closest to, but not over,
        the length that the user could read in the minutes they have available at their reading speed.
        '''
        if self.all_diary_entries == []:
            raise Exception("No diary entries available.")
        
        words_readable = wpm * min
        longest_entry_length = 0
        longest_entry = None

        #loop through all_diary_entries to find the longest entry that is not over the words_readable
        for entry in self.all_diary_entries:
            if words_readable >= entry.word_count() > longest_entry_length:
                longest_entry = entry

        #if longest_entry is still None, no entry was short enough to be read in the timeframe
        if longest_entry == None:
            raise Exception("Reading time too short to read any entry entirely.")

        return entry



    #EXTRACTING PHONE NUMBERS:
    def extract_phone_numbers(self) -> list:
        '''
        Params: None
        Returns: a list of all phone numbers in all diary contents
        Side effects: none
        '''
        result = []
        for entry in self.all_diary_entries:
            for string in entry.word_list():
                if string.isnumeric() and len(string) == 11 and string not in result:
                    result.append(string)
        return result

    def display_all_phone_numbers(self) -> str:
        '''
        Params: None
        Returns: a formatted string to print out all phone numbers
        Side effects: none
        '''
        return "\n".join(self.extract_phone_numbers())
    