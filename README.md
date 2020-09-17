# DVPtask
Task1 has been completed while task2 needs a little bit of work.

I have tried 2 methods for Task1:
  1) Utilizes the colorthief library for getting dominant colors (14/15 blue correct, 13/14 yellow correct)
  2) Uses HSV values and range of blue colors to get mask. (13/15 blue correct, 12/14 yellow correct)
  
To run 
``` 
python KTHFSDV_perception_task1_1.py for 1st method of task1
python KTHFSDV_perception_task1_2.py for 2nd method of task1
```

For Task2:

I have used yolov4 to train a trafficcone detector. It detects with a high mAP score of 96-98% but does not classify cone color.
I tried to use this model to train an newer model based on self labelled blue cones and yellow cones (basically tried transfer learning) but it gave very poor results.
  
  
