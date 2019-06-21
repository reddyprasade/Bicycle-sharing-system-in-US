# Packages Leading
import time
import pandas as pd
import numpy as np


# Q1: Data Lading In Dict
CITY_DATA = { 'Chicago': 'chicago.csv',

              'New York City': 'new_york_city.csv',

              'Washington': 'washington.csv' }



# Filtering Data According to User Input funcation such as City, Month,Day

def get_filters():

    """

    Asks user to specify a city, month, and day to analyze.

    Returns:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """

    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # Q2: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:

      city = input("\nWhich city would you like to filter by? New York City, Chicago or Washington?\n")

      if city not in ('New York City', 'Chicago', 'Washington'):

        print("Sorry, I didn't catch that. Try again.")

        continue

      else:

        break



    # Q3 : get user input for month (all, january, february, ... , june)



    while True:

      month = input("\nWhich month would you like to filter by? January, February, March, April, May, June or type 'all' if you do not have any preference?\n")

      if month not in ('January', 'February', 'March', 'April', 'May', 'June', 'all'):

        print("Sorry, I didn't catch that. Try again.")

        continue

      else:

        break



    # Q4: get user input for day of week (all, monday, tuesday, ... sunday)



    while True:
      day = input("\nAre you looking for a particular day? If so, kindly enter the day as follows: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all' if you do not have any preference.\n")

      if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all'):

        print("Sorry, I didn't catch that. Try again.")

        continue

      else:

        break

    print('@'*40)

    return city, month, day




# Q5:Loads data for the specified city and filters by month and day if applicable. 
def load_data(city, month, day):



    """

    Loads data for the specified city and filters by month and day if applicable.



    Args:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:

        df - Pandas DataFrame containing city data filtered by month and day

    """

    #Q6: load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])



    #Q7: convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])



    # Q8: Extract month and day of week from Start Time to create new columns



    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name



    #Q9: filter by month if applicable

    if month != 'all':

   	 	# use the index of the months list to get the corresponding int

        months = ['January', 'February', 'March', 'April', 'May', 'June']

        month = months.index(month) + 1



    	# filter by month to create the new dataframe

        df = df[df['month'] == month]



        # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]



    return df


# Q10: Displays statistics on the most frequent times of travel.
def time_stats(df):

    """Displays statistics on the most frequent times of travel."""



    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()



    # Q10.1: display the most common month



    popular_month = df['month'].mode()[0]

    print('Most Common Month:', popular_month)





    # Q10.2: display the most common day of week



    popular_day = df['day_of_week'].mode()[0]

    print('Most Common day:', popular_day)







    # Q10.3 display the most common start hour



    df['hour'] = df['Start Time'].dt.hour

    popular_hour = df['hour'].mode()[0]

    print('Most Common Hour:', popular_hour)





    print("\nThis took %s seconds." % (time.time() - start_time))

    print('#'*80)





def station_stats(df):

    """Displays statistics on the most popular stations and trip."""



    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()



    # Q11:Display most commonly used start station



    Start_Station = df['Start Station'].value_counts().idxmax()

    print('Most Commonly used start station:', Start_Station)





    # Q12: display most commonly used end station



    End_Station = df['End Station'].value_counts().idxmax()

    print('\nMost Commonly used end station:', End_Station)





    # Q13 display most frequent combination of start station and end station trip



    Combination_Station = df.groupby(['Start Station', 'End Station']).count()

    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)





    print("\nThis took %s seconds." % (time.time() - start_time))

    print('$'*80)



# Q14: Displays statistics on the total and average trip duration.
def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""



    print('\nCalculating Trip Duration...\n')

    start_time = time.time()



    # Q 14.1: display total travel time




    Total_Travel_Time = sum(df['Trip Duration'])

    print('Total travel time:', Total_Travel_Time/86400, " Days")





    # Q14.2: display mean travel time



    Mean_Travel_Time = df['Trip Duration'].mean()

    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")





    print("\nThis took %s seconds." % (time.time() - start_time))

    print('@'*80)




#Q15: Displays statistics on bikeshare users
def user_stats(df):

    """Displays statistics on bikeshare users."""



    print('\nCalculating User Stats...\n')

    start_time = time.time()



    # Q15.1 Display counts of user types



    user_types = df['User Type'].value_counts()

    #print(user_types)

    print('User Types:\n', user_types)



    # Q15.2 Display counts of gender



    try:

      gender_types = df['Gender'].value_counts()

      print('\nGender Types:\n', gender_types)

    except KeyError:

      print("\nGender Types:\nNo data available for this month.")



    # Q15.3 Display earliest, most recent, and most common year of birth



    try:

      Earliest_Year = df['Birth Year'].min()

      print('\nEarliest Year:', Earliest_Year)

    except KeyError:

      print("\nEarliest Year:\nNo data available for this month.")



    try:

      Most_Recent_Year = df['Birth Year'].max()

      print('\nMost Recent Year:', Most_Recent_Year)

    except KeyError:

      print("\nMost Recent Year:\nNo data available for this month.")



    try:

      Most_Common_Year = df['Birth Year'].value_counts().idxmax()

      print('\nMost Common Year:', Most_Common_Year)

    except KeyError:

      print("\nMost Common Year:\nNo data available for this month.")



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-.-'*80)





def main():

    while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)



        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break





if __name__ == "__main__":

	main()
