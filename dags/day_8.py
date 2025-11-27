from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 8th")
def day_8():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-08":
            print("It is December 8th! Let me open the window!")
        elif today > "2025-12-08":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def its_beginning_to_look_a_lot_like_christmas_1():
        print("It's beginning to look a lot like Christmas")
        
    @task
    def its_beginning_to_look_a_lot_like_christmas_2():
        print("Everywhere you go")
        
    @task
    def its_beginning_to_look_a_lot_like_christmas_3():
        print("Take a look in the five-and-ten")
        
    @task
    def its_beginning_to_look_a_lot_like_christmas_4():
        print("Glistening once again")
        
    @task
    def your_song_for_today():
        print("Today's song is It's Beginning to Look a Lot Like Christmas by Perry Como!")
        print("Listen here: https://www.youtube.com/watch?v=KmddeUJJEuU")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _ibtlallc_1 = its_beginning_to_look_a_lot_like_christmas_1()
    _ibtlallc_2 = its_beginning_to_look_a_lot_like_christmas_2()
    _ibtlallc_3 = its_beginning_to_look_a_lot_like_christmas_3()
    _ibtlallc_4 = its_beginning_to_look_a_lot_like_christmas_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _ibtlallc_1, _ibtlallc_2, _ibtlallc_3, _ibtlallc_4, _your_song_for_today, _opening_the_window)


day_8()
