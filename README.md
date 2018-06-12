# player-rate

How does one determine how much a player contributes to his team?
You can clone this repository and get the code that gets data.  

This repo contains:
 - A way to gather data
 - Some data
 - Stored Keras models
 - CoreML models for iOS use cases
 - A way to train models
 - A way to run models

You must have nba_py, Keras, bs4(beautifulSoup), lxml, numpy, matplotlib, and tensorflow for everything to work. 

The current code is set up to train for point predictions. You can change this by changing the `statistic_wanted` variable. 
It will save to the file set in the code.

The data-gathering can be achieved by running `python playerstats.py start_player_id file_to_save.json`

The `start_player_id` will be `0` unless it was interupted during running of the program. Then, the last id printed to the console should be here. The file name should be the file you want to save to. Afterwards, move this file to the `data_json_files` directory

To do list

- [x] Gather Data
- [x] Create Neural Network
- [ ] Create Statistic
- [ ] Automatically Generate Trade Requests That Will Benefit Your Team
