from colorthief import ColorThief
import glob

def classify(t_color):
    correct = 0
    all = 0
    for img in glob.glob(".\cones_images/"+t_color+"*.png"):
        all += 1
        color_thief = ColorThief(img)
        # get the dominant color
        #dominant_color = color_thief.get_color(quality=1)
        palette = color_thief.get_palette(color_count=4)
        p_color = "yellow"
        bcount = 0
        for color in palette:
            r, g, b = color
            if(r<=100 and g<=100 and b<=100):
                #black
                continue
            elif(r<=140 and g<=140 and b>=140):
                p_color = "blue"
        if(p_color==t_color):
            correct+=1
    print("got %d correct out of %d for color %s" % (correct, all, t_color))

if __name__ == '__main__':
    classify("blue")
    classify("yellow")

   

