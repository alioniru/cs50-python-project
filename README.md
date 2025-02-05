# cs50-python-project
# SPORTS DATA ANALYSIS
    #### Video Demo:  https://youtu.be/qmWhQXSVZGE
    #### Description:
    I chose this project because I hope to analyse American Football game data. project.py analyses the game data from a chosen dataset based on the metric chosen by the user. The modules used include pandas and matplotlib.

    main takes input for the spreadsheet file from the user. it loops in case the user makes a typo. read_file checks the filetype, then converts to csv. A loop in the main function allows for user error in input. if it is not an accepted file type, it returns to the user. The user can input again. It loops until user inputs correct file name. clean_data updates some metrics specific to american football and returns to the dataframe. The main function prints the metrics to the user to choose a metric they want to plot.

    clean_data adds extra metrics for American Football data to round out the metrics. It adds the metrics to the dataframe. visualise_data plots the user's chosen metric and returns as a png file. It uses matplotlib to create a plot with an easy-to-read design. I chose this design because it best suits simple chronological data analysis over the number of games.

    test_project tests read_file to check that it is not accepting incorrect file types and nonexistant files, and that it is correctly accepting existant correct filetypes. test_clean_data_TYG tests that clean_data is correctly creating the Total Yards Gained metric. test_clean_data_YPP tests that clean_data is correctly creating the Yards Per Play metric. test_visualise_data tests that visualise_data is not accepting nonexistant metrics from the user. test_visualise_data_png tests that visualise_data is correctly outputting a png file with the correct file name. all the pytests return as passed.

    It was outside the scope of this project, but I would expand it to not be so strict as to the metrics used by clean_data. Possibly this code could be used for any data analysis, but I focued primarily on American Football statistics. Another way to do it could be show the user the metrics, ask if the user wants to modify any metrics to create a new column. This way the code could be more versatile. However, for my current purposes, this code is sufficient.
