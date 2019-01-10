"""
The main program should use functions from music_reports and display modules
"""
import display

def delete_album_by_artist_and_album_name(albums, artist, album_name):
    """
    Deletes album of given name by given artist from list and updates data file

    :param list albums: currently existing albums
    :param str artist: artist who recorded the album
    :param str album_name: name of album to be deleted

    :returns: updated albums' list
    :rtype: list
    """


def main():
    
    """
    Calls all interaction between user and program, handles program menu
    and user inputs. It should repeat displaying menu and asking for
    input until that moment.

    You should create new functions and call them from main whenever it can
    make the code cleaner
    """

    display.print_program_menu(["get album by genere",
                                "get genre stats",
                                "get longest album",
                                "get last oldest",
                                "get last oldest of genre",
                                "get total albums length"])


    user_choice = input_handling(0,7)

    if user_choice == 0:
        pass
    elif user_choice == 1:  
        pass
    elif user_choice == 2:
        pass
    elif user_choice == 3:
        pass
    elif user_choice == 4:
        pass
    elif user_choice == 5:
        pass
    elif user_choice == 6:
        pass
    elif user_choice == 7:                              
        pass
if __name__ == '__main__':
    main()
