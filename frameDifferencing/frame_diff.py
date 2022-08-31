import cv2

# compute difference in frames
def frame_diff(prev_frame, cur_frame, next_frame):
    # difference between current and previous frame
    diff_frames_1 = cv2.absdiff(next_frame, cur_frame)

    # difference between the current frame and prev
    diff_frames_2 = cv2.absdiff(cur_frame, prev_frame)
    return cv2.bitwise_and(diff_frames_1, diff_frames_2)

# define function to get current frame from cam
def get_frame(cap, scaling_factor):
    #read current frame from vid
    _, frame = cap.read()

    #resize the image
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    return gray

if __name__=='__main__':
    #defin the vid vaptured 
    cap = cv2.VideoCapture(0)

    #define scaling
    scaling_factor = 0.5
    
    #define the current frame
    prev_frame = get_frame(cap, scaling_factor)

    #grab the next frame
    cur_frame = get_frame(cap, scaling_factor)

    ##grab the frame after
    next_frame = get_frame(cap, scaling_factor)

    # keep reading frames until user hits 'esc'
    while True:
        cv2.imshow('Object Movement', frame_diff(prev_frame, cur_frame, next_frame))

        prev_frame = cur_frame
        cur_frame = next_frame

        next_frame = get_frame(cap, scaling_factor)

        key = cv2.waitKey(10)
        if key == 27:
            break

    cv2.destroyAllWindows()
