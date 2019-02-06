# Validation Mini Project

In this mini-project, you’ll start from scratch in making a training-testing split in the data. This will be the first step toward your final project, of building a POI identifier.

Note:
From Python 3.3 forward, a change to the order in which dictionary keys are processed was made such that the orders are randomized each time the code is run. This will cause some compatibility problems with the graders and project code, which were run under Python 2.7. To correct for this, add the following argument to the `featureFormat` call on line 25 of `validate_poi.py`:

`sort_keys = '../tools/python2_lesson13_keys.pkl'`

This will open up a file in the `tools` folder with the Python 2 key order.

Note: If you are not getting the results expected by the grader, then you may want to check the file `tools/feature_format.py`. Due to changes in the final project, some file changes have affected the numbers output on this assignment as written. Check that you have the most recent version of the file from the repository, such that the `featureFormat` has a default parameter for `sort_keys = False` and that `keys = dictionary.keys()` results.