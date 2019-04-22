# WEBBL_Analyzer
### Feature Extractor/Future home for the decision algorithm

**Description:** Extracts feature data from both mouse and keystroke raw data, and saves in separate files

**Future Description:** Also analyzes feature data and classifies data as legitimate or not. If legitimate, add to training data.

**Currently Requires:** Python 3.7

**Possible Future Recommended Requirements:** Tensorflow (separate installation process if have access to graphics card)

**Inputs:** “data.csv”

**Outputs:** “key_features.csv”, “mouse_features.csv”

**Future Outputs:** Classifier Decision

**Installation: **
  1.  Clone repository to local directory (https://github.com/letaylo/WEBBL_Analyzer.git)


**Overview:**

Currently, only “feature_extract.py” is functioning. When this program is run, it will search for “data.csv” within the top level of the repository’s directory, and begin extracting the data into several lists: xpos, ypos, timestamp, events, and keys. Since each line of “data.csv” corresponds to a different entry, and each entry will have data for each value, each of these lists will have the same length and order, meaning they can be iterated through for extraction.

Keystroke feature extraction relies on using two dictionary classes, DwellDict and FlightDict, each providing a means to store data on the Dwell and Flight features. These classes are shown in Figure 1.

![alt text](https://raw.githubusercontent.com/letaylo/WEBBL_Analyzer/master/README/keyfeature_dict.PNG?token=AG5EVQPG4K37ZWTG4GCEZLK4XXRIC)

_Figure 1_

This data is stored by calling the Flight and Dwell Classes. These classes take basic keyAction data as inputs, and stores the key(s) as well as the start and end times of the action. For each key combination and action type, the mean, standard deviation, max, and min are stored as CSV for future analysis.

Mouse feature extraction is a bit more complicated, as there are various action types (mouse movement, mousemove to click, etc.), as well as a set of 9 main types of features. In order to determine the type of action, the script iterates through the basic events, concatenating them together as long as they occur relatively recently to another. Each time a silence occurs or there is a new action, the type and start location of the action is stored. Then, using the mouse coordinates and timestamp, the features are calculated, as well as the min, max, mean, and standard deviation of each of those features during that action. This data is all written into CSV as well.

_NOTE:_ feature_compare.py is only used as a proof of concept to visualize differences between users. Not to be used for actual analysis.
