from lib.DiaryEntry import DiaryEntry
import pytest
from datetime import datetime

lorem_ipsum_100_words = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ut erat nunc. Vivamus facilisis libero nunc, et ullamcorper nunc finibus non. Pellentesque facilisis nisi dolor, vitae volutpat mi fermentum in. Maecenas risus risus, lacinia eu risus non, mollis sagittis enim. Proin augue felis, mattis non est vel, cursus dictum nisl. Sed quis tempor elit. Maecenas ac nulla interdum, feugiat nunc eu, sodales libero. Vivamus sit amet placerat massa. In justo leo, tristique sit amet est eu, suscipit pharetra ex. Sed enim libero, maximus sed nisl eu, sagittis laoreet est. Mauris sed ultricies neque. Mauris vel nunc ac velit pulvinar efficitur."
lorem_ipsum_1000_words = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed suscipit, ipsum ut porta maximus, libero enim feugiat orci, ac blandit enim sem placerat magna. Mauris luctus aliquet purus id placerat. Proin consectetur eros ut justo pretium, sed auctor elit elementum. Vestibulum viverra consequat mattis. Phasellus quis lacus fringilla, gravida ipsum eget, euismod neque. Maecenas dictum ullamcorper magna quis mollis. Curabitur pulvinar dignissim dolor sit amet pretium. Donec quis congue sapien.
Morbi interdum euismod nisl id aliquet. Donec in dignissim ipsum. Vestibulum diam ante, euismod ut leo a, varius luctus erat. Curabitur cursus dolor sit amet justo consequat blandit. Aenean imperdiet metus felis, eget varius dolor ullamcorper sed. Donec mi justo, cursus nec metus quis, accumsan finibus metus. Pellentesque dolor libero, posuere sed nulla non, euismod vulputate magna. Pellentesque dapibus, ipsum vitae convallis pharetra, sem est aliquam nunc, in commodo ligula urna eu dolor. Integer facilisis leo in leo mattis, non pharetra arcu semper. Aenean eget odio gravida, posuere nisl id, dictum leo.
Sed commodo sem condimentum leo eleifend porta. Proin arcu metus, imperdiet vel rutrum sed, pharetra sit amet nulla. Morbi vel faucibus felis. Pellentesque id magna pulvinar, viverra sapien congue, mattis mauris. Aliquam vel pellentesque arcu. Ut sollicitudin blandit eros, a malesuada felis pretium ut. Vivamus eu turpis nunc. Interdum et malesuada fames ac ante ipsum primis in faucibus. Duis ultricies rutrum arcu.
Fusce sollicitudin risus augue, mollis suscipit sapien elementum in. Donec sed elementum sem. Nulla ante nunc, convallis et placerat vel, aliquet sit amet velit. Proin euismod eleifend enim. Suspendisse potenti. Mauris scelerisque ipsum diam, at tempus magna vulputate ac. Praesent ac varius nisi.
Pellentesque finibus neque erat, vel porta dui venenatis vel. Vestibulum interdum in nunc in luctus. Integer aliquet commodo diam et placerat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Suspendisse accumsan ligula ut erat pulvinar vulputate. Pellentesque dictum sodales elementum. Nulla varius, quam at imperdiet finibus, lacus metus tincidunt nulla, id tincidunt tellus dui nec purus. Mauris ac sagittis massa. Praesent dictum elementum libero. Morbi dapibus sem sit amet leo auctor dapibus id vitae nulla. Duis mattis elementum tempor. Maecenas ut elementum urna. Duis scelerisque id arcu ut ultrices. Integer elementum, turpis et scelerisque imperdiet, lacus erat egestas neque, sit amet varius tortor eros vitae nulla. Fusce ut tortor pulvinar, fermentum purus suscipit, bibendum tortor.
Donec porta mi ac elit convallis congue. Donec egestas neque vel dolor posuere tempus. Proin at orci magna. Donec convallis ornare quam. Nulla vitae accumsan felis. Vestibulum pellentesque dui et mauris sagittis sollicitudin. Maecenas mollis augue commodo, mollis ante faucibus, mollis sapien. Fusce commodo volutpat metus vitae lacinia. Praesent feugiat cursus arcu, ac ultricies justo commodo et. Sed tristique bibendum lacus, ut vehicula neque dignissim non. Phasellus posuere laoreet lacinia. Nunc nec imperdiet diam. Maecenas molestie maximus mauris sed egestas. Donec sed metus faucibus tellus luctus posuere.
Vestibulum efficitur lectus a turpis pulvinar, at fringilla mi sollicitudin. Aenean faucibus, odio et venenatis gravida, sem arcu sollicitudin velit, quis elementum velit leo nec sapien. Etiam malesuada sed mi vel aliquet. Quisque molestie iaculis dolor ac tincidunt. Pellentesque mattis, orci eu condimentum consectetur, nibh sem convallis mauris, et consequat ipsum nisl id eros. Pellentesque vitae nisl sit amet dolor scelerisque semper ac varius ligula. Sed semper venenatis lacus, in congue nibh pretium nec. Sed eget posuere felis, sed rhoncus ex.
Nunc ultrices dui ut purus consequat lobortis. Phasellus lectus mi, placerat sed pulvinar eget, suscipit cursus erat. Vivamus porttitor dolor et urna tempus maximus. Donec pellentesque egestas augue eget pellentesque. Curabitur a diam tellus. Nullam non ante odio. Duis dapibus urna lacinia, commodo nibh quis, tincidunt mi. In bibendum tincidunt lacus vel volutpat. Duis nisl justo, sollicitudin ac purus eu, condimentum maximus felis. Pellentesque fermentum augue sed arcu luctus, ut congue felis dapibus. Vivamus in lacus porta, euismod metus at, commodo lectus. Nulla in tempus ligula. Phasellus egestas diam id purus interdum aliquam.
Phasellus ligula magna, luctus sed mauris non, feugiat tempor nisl. Nam volutpat lacus augue, sed dictum dolor facilisis a. Cras posuere, erat quis tempor pretium, dolor nulla venenatis neque, quis dictum turpis lacus vel nulla. Sed eu magna sapien. Aenean posuere, nisl a porttitor aliquet, ante odio molestie nisi, eu sagittis lectus libero at quam. Quisque ornare bibendum maximus. Maecenas sollicitudin lectus eget dui laoreet, euismod cursus nibh varius. Aliquam sit amet augue egestas lectus mattis dictum non quis nibh.
Suspendisse potenti. Phasellus vestibulum est non dolor lacinia bibendum. Nam ornare ac orci eu viverra. Nulla faucibus placerat placerat. Nunc quis risus turpis. Proin imperdiet iaculis orci, id ornare leo laoreet quis. Maecenas semper diam arcu, id accumsan elit scelerisque at. Aliquam erat volutpat. Vivamus ullamcorper mauris nec malesuada porta. Ut id enim urna.
Morbi sed rhoncus mi, ut venenatis purus. Quisque efficitur cursus quam quis efficitur. Pellentesque blandit sodales ultricies. Vestibulum laoreet, augue et cursus ornare, sapien ex aliquet magna, eu consequat neque orci a ligula. Nunc iaculis lacus nec diam tempor, vitae ullamcorper enim consequat. Nullam gravida ante blandit porttitor iaculis. Sed placerat eros leo, nec efficitur sem blandit in. Fusce nec quam nec arcu consequat eleifend. Aenean in dolor ullamcorper, pulvinar lacus vel, mollis eros. Etiam velit magna, hendrerit a ipsum vel, gravida pellentesque ante. Aenean egestas turpis sed mattis molestie. Nullam gravida convallis erat sit amet aliquet. Maecenas blandit arcu sem, eu venenatis lorem ultrices vitae. Sed facilisis, nisl et semper viverra, nunc sapien laoreet massa, et semper leo massa sit amet nulla. Mauris sit amet velit tellus. Etiam dapibus orci eu ex mollis imperdiet.
Nunc mollis tellus et eleifend ullamcorper. Sed accumsan ante sodales justo ultrices suscipit. Nullam vestibulum nibh ac nisi sodales, vel auctor metus mollis. Nam efficitur vehicula pharetra. Sed et venenatis massa, ut malesuada nunc. Quisque vitae tincidunt dui. Sed sit amet tortor vel urna aliquet dapibus eu id lorem. Suspendisse quis ultricies risus, a iaculis neque. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean lorem sem, interdum quis dignissim eget, elementum nec ante. Aliquam id nulla ac.'''


def test_init_diary_entry():
    diary_entry = DiaryEntry(title="Title of entry", content="Here's the entry of my diary")
    assert diary_entry.title == "Title of entry"
    assert diary_entry.content == "Here's the entry of my diary"

def test_error_diary_entry():
    with pytest.raises(TypeError) as e:
        diary_entry = DiaryEntry(title="Title of entry", content=9)
    assert str(e.value) == "Invalid entry type."

def test_empty_string_diary_entry():
    diary_entry = DiaryEntry(title="", content="")
    assert diary_entry.word_count() == 0
    assert diary_entry.word_list() == []

def test_word_list():
    diary_entry = DiaryEntry(title="Title of entry", content="Here's the entry of my diary")
    assert diary_entry.word_list() == ["Here's", "the", "entry", "of", "my", "diary"]

def test_word_count():
    diary = DiaryEntry(title="My Title", content=lorem_ipsum_100_words)
    assert diary.word_count() == 100

def test_reading_time():
    diary = DiaryEntry(title="My Title", content=lorem_ipsum_1000_words)
    reading_speed = 23 #words per minute
    assert diary.reading_time(wpm=reading_speed) == 43 #rounded to nearest integer?

def test_reading_chunk():
    diary = DiaryEntry(title="My Title", content=lorem_ipsum_100_words)
    reading_speed = 23 #words per minute
    reading_time = 1
    assert diary.reading_chunk(wpm=reading_speed, min=reading_time) == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ut erat nunc. Vivamus facilisis libero nunc, et ullamcorper nunc finibus non. Pellentesque facilisis"
    assert diary.reading_chunk(wpm=reading_speed, min=reading_time) == "nisi dolor, vitae volutpat mi fermentum in. Maecenas risus risus, lacinia eu risus non, mollis sagittis enim. Proin augue felis, mattis non est"
    assert diary.reading_chunk(wpm=reading_speed, min=reading_time) == "vel, cursus dictum nisl. Sed quis tempor elit. Maecenas ac nulla interdum, feugiat nunc eu, sodales libero. Vivamus sit amet placerat massa. In"
    assert diary.reading_chunk(wpm=reading_speed, min=reading_time) == "justo leo, tristique sit amet est eu, suscipit pharetra ex. Sed enim libero, maximus sed nisl eu, sagittis laoreet est. Mauris sed ultricies"
    assert diary.reading_chunk(wpm=reading_speed, min=reading_time) == "neque. Mauris vel nunc ac velit pulvinar efficitur."
    assert diary.reading_chunk(wpm=reading_speed, min=reading_time) == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ut erat nunc. Vivamus facilisis libero nunc, et ullamcorper nunc finibus non. Pellentesque facilisis"


def test_empty_reading_chunk():
    diary = DiaryEntry(title="My Title", content="")
    reading_speed = 23 #words per minute
    reading_time = 1
    assert diary.reading_chunk(wpm=reading_speed, min=reading_time) == ""


def test_format():
    diary = DiaryEntry(title="My Title", content=lorem_ipsum_100_words)
    assert diary.format_for_diary() == f"My Title\n{datetime.strftime(datetime.now(),'%d/%m/%Y, %I:%M%p')}\nWord Count: 100"